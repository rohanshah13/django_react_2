from django.conf.urls import url

from . import views

app_name = 'chat'
urlpatterns = [
	url(r'^',views.ReactAppView.as_view()),
]