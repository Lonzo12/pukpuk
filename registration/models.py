from django.conf import settings
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/avatars/', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Numbers(models.Model):
    nomer = models.IntegerField('Номер')
    date_bron = models.DateField('Дата бронирования',default=date.today)
    date_zaezda = models.DateField('Дата заезда',default=date.today)
    date_viezda = models.DateField('Дата выезда',default=date.today)
    status = models.CharField('Статус', max_length=256)
    
    
    def __str__(self):
        return f"{self.nomer} - {'Дата бронирования: '}{self.date_bron} - {'Дата заезда: '}{self.date_zaezda} - {'Дата выезда: '}{self.date_viezda} - {'Статус: '}{self.status}"
    
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
       return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



class Products(models.Model):
    pict = models.ImageField(upload_to='static/', null=True, blank=True)
    name = models.CharField('Название', max_length=256)
    desc = models.TextField('Описание', max_length=256)
    kol = models.PositiveBigIntegerField(default = 0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
       return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Products', through='CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def update_total_price(self):
        # Обновляем общую стоимость корзины
        total = sum(item.calculate_total_price() for item in self.items.all())
        self.total_price = total
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        # Обновляем стоимость корзины при сохранении элемента корзины
        super().save(*args, **kwargs)
        self.cart.update_total_price()

