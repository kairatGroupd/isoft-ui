# from django.urls import path, include
# from django.contrib.auth.views import LogoutView
# from rest_framework import routers

# from .views import (
#     dashboard,
#     profile,
#     profile_edit,
#     messages,
#     messages_api,
#     projects,
#     projects_api,
#     LoginView,
#     EducationView,
#     )
# router = routers.DefaultRouter()
# # router.register('product', views.ProductViewSet, basename='product')
# router.register('profile', )

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# app_name = 'api'
# # urlpatterns = [

# #     path('', dashboard, name='dashboard'),

# #     path('profile/', profile, name='profile'),
# #     path('profile/edit/', profile_edit, name='profile_edit'),

# #     path('messages', messages, name='messages'),
# #     path('messages/api/', messages_api, name='messages_api'),

# #     path('projects', projects, name='projects'),
# #     path('projects/api/', projects_api, name='projects_api'),

# #     path('education/', EducationView.as_view(), name='education'),
# #     # path('education/', EducationView.as_view(), name='one_education'),

# #     path('login/', LoginView.as_view(), name='login'),
# #     path('logout/', LogoutView.as_view(), name='logout'),
# # ]
