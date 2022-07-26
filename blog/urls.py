from django.urls import path, include
from . import views
# from .views import PostEdit, PostNew, PostSearch, PostDelete, LogIn, SignUp, ChangePassword, PostDraft
# from .views import PostView
# from .views import PostDetail
from rest_framework.routers import DefaultRouter
import rest_framework
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail,name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
# ]

# urlpatterns = [
#     path('', PostView.as_view(), name='post_list'),
#     path('post/<int:pk>/', PostDetail.as_view(),name='post_detail'),
#     path('post/new/', PostNew.as_view(), name='post_new'),
#     path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
#     path('search', PostSearch.as_view(), name='post_search'),
#     path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
#     path('myposts/', PostDraft.as_view(), name='my_posts'),
#     path('signup/', SignUp.as_view(), name='sign_up'),
#     path('accounts/password_change/', ChangePassword.as_view(template_name='changepass.html', success_url='/'), name='change_password'),
#     path('accounts/password_change/done/', PostView.as_view(), name='pass_done')
# ]

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
# router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('dj_rest_auth.urls')), # new
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
]