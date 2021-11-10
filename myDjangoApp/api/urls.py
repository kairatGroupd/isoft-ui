from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='categoty')
router.register('information', InformationViews)
router.register('exiperiens', ExperienceViewSet)
router.register('competence', CompetenceViewSet)
router.register('project', ProjectViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('order/', OrderView.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog-author/', BlogAuthorViews.as_view()),
    path('blog-comment/', BlogCommentViews.as_view()),
    path('messege', MessegeViews.as_view()),
]

