from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


from user import views

app_name = 'user'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserListView.as_view(), name='user-list'),
    path('add_user/', views.AddUserView.as_view(template_name="user.html")),
    path('get_user/<int:user_id>', views.UserDetailView.as_view()),
    path('edit_user/<int:user_id>', views.EditUserView.as_view()),
    path('delete_user/<int:user_id>', views.DeleteUserView.as_view()),
]