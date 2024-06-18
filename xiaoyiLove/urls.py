from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('get_token/', views.getToken),

    # 从api获取相关信息
    path('api/weather/', views.fetchWeather),
    path('api/quotes/', views.fetchQuotes),

    # 获取文章列表
    path('get_articles_list/', views.getArticlesList),
    # 获取首页文章篇
    path('get_home_articles_list/', views.getHomeArticlesList),

    # 获取所有分类、标签
    path('get_all_category/', views.getAllCategory),
    path('get_all_tag/', views.getAllTag),

    # 创建文章
    path('create_article/', views.createArticle),

    # 删除文章
    path('delete_article/<int:articleId>/', views.deleteArticle),

    # 获取指定文章
    path('fetch_article/<int:articleId>/', views.fetchArticle),

    # 修改文章
    path('revise_article/', views.reviseArticle),

    # 筛选文章
    path('filter_article/', views.filterArticle),

]
