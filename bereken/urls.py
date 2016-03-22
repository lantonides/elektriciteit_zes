from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.bereken, name='bereken'),
	url(r'^gasregios', views.gasregios, name='gasregios'),
	url(r'^tarieven', views.tarieven, name='tarieven'),
	url(r'^prijsontwikkeling', views.prijsontwikkeling, name='prijsontwikkeling'),
]

