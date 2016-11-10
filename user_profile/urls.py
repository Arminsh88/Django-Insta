from user_profile.views import profile
from django.conf.urls import url
from user_profile.views import followers
from user_profile.views import following

urlpatterns = [
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})', profile, name='username'),
    url(r'^[a-zA-Z0-9_.]{4,}/followers', followers, name='followers'),
    url(r'^[a-zA-Z0-9_.]{4,}/following', following, name='following'),
]

"""

pattern =>

(?P<username>pattern)


"""