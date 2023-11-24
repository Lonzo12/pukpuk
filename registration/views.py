
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect,JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import *
from .models import *
from .utils import *

def index(request):
    return render(request, 'registration/index.html')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/reg.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'registration/vhod.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')

def profile(request):
    return render(request, 'registration/profile.html')
        
def logout_user(request):
    logout(request)
    return redirect('login')

def product_list(request):
    products = Products.objects.all()
    return render(request, 'registration/bron.html', context)


def add_to_cart(request, product_id):
    product = Products.objects.get(pk=product_id)

    # Проверяем, есть ли у пользователя уже корзина
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # Если пользователь не аутентифицирован, можно использовать сессии для хранения корзины
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    # Проверяем, есть ли уже такой товар в корзине
    try:
        item = cart.items.get(product=product)
        if item.quantity < product.kol:
            item.quantity += 1
            item.save()
        else:
            # Обработка случая, когда количество товаров в корзине уже равно доступному количеству
            # Можно вывести сообщение об ошибке или выполнить другие действия
            pass
    except CartItem.DoesNotExist:
        if product.kol > 0:
            item = CartItem.objects.create(cart=cart, product=product)
            product.save()
        else:
            pass



    cart.update_total_price()
    return redirect('cart')

def cartview(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)

    context = {'cart': cart}
    return render(request, 'registration/cart.html', context)


def update_cart(request, item_id):
    item = CartItem.objects.get(pk=item_id)
    action = request.POST.get('action')

    if action == 'increment':
        item.quantity += 1
        item.cart.total_price = item.calculate_total_price()
        item.cart.save()
    elif action == 'decrement':
        item.quantity -= 1
        item.cart.total_price = item.calculate_total_price()
        item.cart.save()
    if item.quantity <= 0:
        item.delete()
        item.cart.update_total_price()

    else:
        item.save()

    return redirect('cart')

def sendmail(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    items = cart.items.all()
    subject = 'Ваши товары'
    body = ''
    for item in items:
        body += f'{item.product.name} x {item.quantity}: {item.calculate_total_price()}\n'
    body += f'Итого: {cart.total_price}'
    em = EmailMessage(subject=subject, body=body, to=[user.email])
    cart.items.all().delete()
    # Отправляем письмо
    em.send()
    return render(request,'registration/cart.html',{'notice':'Товары отправленны'})


def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form = form.save()
            return render(request, 'registration/profile.html')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'registration/profile.html', context)

def add_product(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CreateProduct()
    return render(request, 'registration/aprofile.html', {'form': form})


