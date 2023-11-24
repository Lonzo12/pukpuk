from django.urls import path
from .views import *

urlpatterns = [
    path('case/', case, name='case'),
    path('case/open_case/<int:case_id>/', open_case, name='open_case'),
]
