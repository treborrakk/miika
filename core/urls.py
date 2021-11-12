from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     UserPostListView
# )
from . import views

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),

    path('', views.home, name='core-home'),
    # path('', views.Home.as_view(), name='core-home'),
# Online Library
    path('class/subjects/', views.subject_list, name='subject_list'),
    path('subjects/<int:pk>/', views.delete_subject, name='delete_subject'),
    path('class/subjects/edit/<int:id>', views.edit_subject, name='edit_subject'),
    path('class/subjects/update/<int:id>', views.update_subject, name='update_subject'),
# Online Library view
    path('class/subjects/list', views.SubjectListView.as_view(), name='class_subject_list'),
    path('class/subjects/upload/', views.UploadSubjectView.as_view(), name='class_upload_subject'),
    # path('class/subjects/upload/', views.upload_book, name='class_upload_subject'),
# Online Lookup view
    path('api/lookup/', views.LookupAPIView.as_view()),
    path('error403/', views.error403, name='core-403'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)