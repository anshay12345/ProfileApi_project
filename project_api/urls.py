from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
# as we register new routes using our router it generate a list of urls that are associated with our viewset
# it figures out the urls that are required for all of the functions that we add to our view set and then it
# generate this urls list which we pass in to using the path function and the include function to our url
# patterns
