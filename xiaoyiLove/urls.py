from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('get_token/', views.getToken),

    # 获取文章列表
    path('get_article_list', views.getArticleList),

    # 获取所有分类、标签
    path('get_all_category/', views.getAllCategory),
    path('get_all_tag/', views.getAllTag),

    # 创建文章
    path('create_article/', views.createArticle),

    # 删除文章
    path('delete_article/<int:articleId>', views.deleteArticle),

]
