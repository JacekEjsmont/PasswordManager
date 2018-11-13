from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('entries/', views.EntryList.as_view(), name='entries'),
    path('details/<int:pk>', views.EntryDetail.as_view(), name='details'),
    path('add_entry/', views.EntryCreate.as_view(), name='add_entry'),
    path('edit_entry/<int:pk>', views.EntryEdit.as_view(), name='edit_entry'),
    path('delete_entry/<int:pk>', views.EntryDelete.as_view(), name='delete_entry'),

    path('register/', views.UserFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='password_manager:entries'), name='logout'),
]
