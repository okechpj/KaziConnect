from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('supper-admin/', admin.site.urls),
    path('account/', include('account.urls')),
]

"""
>>>> Models


>>>> Models

>>>>> admin

>>>>> admin

"""