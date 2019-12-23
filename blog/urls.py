"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from storm import views
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from storm.sitemaps import ArticleSitemap, CategorySitemap, TagSitemap
from django.views import static
from django.views.static import serve

# 网站地图
sitemaps = {
    'articles': ArticleSitemap,
    'tags': TagSitemap,
    'categories': CategorySitemap
}
urlpatterns = [
	# 后台管理应用，django自带
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')), #添加DjangoUeditor的URL
    # 用户
    path('accounts/', include('user.urls')),
    # storm 应用
    path('', include('storm.urls')),
    # 评论
    url('comment/', include('comment.urls')),  # comment
    # 网站地图
    url('sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url('static/(?P<path>.*)$', serve,
      {'document_root': settings.STATIC_ROOT}),
    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
]
