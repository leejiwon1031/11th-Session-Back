"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import blog.views       #blog 폴더의 views.py 파일을 가져와..

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home,name='home'),       
    #127.0.0.1:8000에 접속했을 때, views.py의 home 함수를 실행시키고, home.html 파일을 출력하라는 뜻!
    path('blog/<int:blog_id>/',blog.views.detail,name="detail"),
    path('new/',blog.views.new,name="new"),
    path('create/',blog.views.create,name="create"),
    path('delete/<int:blog_id>',blog.views.delete,name='delete'),
    path('update_page/<int:blog_id>',blog.views.update_page,name="update_page"),
    path('update/<int:blog_id>', blog.views.update,name="update2"),
    path('<int:blog_id>/comment',blog.views.add_comment,name="add_comment"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
