
from django.conf.urls.static import static
from django.urls import path,include
from bookstore import settings
from bookstore.settings import DEBUG,MEDIA_URL,MEDIA_ROOT
from book import views

urlpatterns = [
    path('',views.index,name='index'),
    path('upload/',views.upload_book,name='upload-book'),
    path('update/<int:book_id>',views.update,name='update_book'),
    path('delete/<int:book_id>',views.delete,name='delete_book'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
