import json
import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import get_token
from django.http import JsonResponse
from backend import models
from django.core import serializers


def getToken(request):
    csrf_token = get_token(request)
    response = {'csrf_token': csrf_token}
    print(response)
    return JsonResponse(response)


def getAllArticles(request):
    response = {
        'articles_data': []
    }

    allArticles = models.Article.objects.all()
    for article in allArticles:
        currentArticle = {
            'article_id': article.article_id,
            'title': article.title,
            'subtitle': article.subtitle,
            'is_display': article.is_display,
            'content_text': article.content_text,
            'content_html': article.content_html,

            'read_count': article.article_info.read_count,
            'comment_count': article.article_info.comment_count,
            'like_count': article.article_info.like_count,
            'reprinted_count': article.article_info.reprinted_count,
            'updated_date': article.article_info.updated_date,
            'created_date': article.article_info.created_date,

            'levelFirstCategory': article.sub_category.category.get_category_name_display(),
            'levelSecondCategory': article.sub_category.sub_category_name,

            'tags': []
        }
        for tag in article.tag.all():
            currentArticle['tags'].append(tag.tag_name)
        response['articles_data'].append(currentArticle)

    response['code'] = 1
    response['message'] = '获取文章列表成功'
    print(response)
    # return HttpResponse('1')
    return JsonResponse(response)


def getAllCategory(request):
    response = {
        'category_data': [],
        'subcategory_data': {}
    }

    allCategory = models.Category.objects.all()
    print(allCategory[0].get_category_name_display())
    print(allCategory[0].sub_category_set.all()[0].sub_category_name)

    for category in allCategory:
        response['category_data'].append(category.get_category_name_display())
        subList = []
        for sub in category.sub_category_set.all():
            subList.append(sub.sub_category_name)
        response['subcategory_data'][category.get_category_name_display()] = subList
    response['code'] = 1
    response['message'] = '获取文章列表成功'
    print(response)
    # return HttpResponse('1')
    return JsonResponse(response)
