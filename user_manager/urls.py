from django.conf.urls import url
from .views import login_view, register, forgot_pass
urlpatterns = [
    url(r'^login/$', login_view.as_view(), name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^login/forgot$', forgot_pass,name='forgot')
]