from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ProductList.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^brand/$', views.BrandList.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),

)
 
urlpatterns = format_suffix_patterns(urlpatterns)