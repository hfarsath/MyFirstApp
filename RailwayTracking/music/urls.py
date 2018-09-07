from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='music'
urlpatterns = [
    
    path('',views.index,name='index'),
    path('<album_id>/',views.detail,name='detail'),
     path('<album_id>/favorite/',views.favorite,name='favorite'),


]