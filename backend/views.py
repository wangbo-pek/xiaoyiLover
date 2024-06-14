import json
import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import get_token
from django.http import JsonResponse
from backend import models
from django.core import serializers


def getToken(request):
    csrf_token = get_token(request)
    response = {
        'csrf_token': csrf_token,
        'code': 1,
        'message': '获取Token成功'}
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
    response['message'] = '获取文章成功'
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
    response['message'] = '获取文章分类成功'
    print(response)
    # return HttpResponse('1')
    return JsonResponse(response)


def getAllTag(request):
    response = {
        'tag_data': []
    }
    allTag = models.Tag.objects.all()

    for tag in allTag:
        response['tag_data'].append(tag.tag_name)
    response['code'] = 1
    response['message'] = '获取文章标签成功'
    # return HttpResponse('1')
    return JsonResponse(response)


def createArticle(request):
    data = json.loads(request.body)
    print(data)
    newAddedTage = []

    # 判断新创建文章的文章中是否有标签
    if data['selectedTag']:
        # 判断新创建文章中是否有新创建的标签
        if data['newAddedTag']:
            for newTag in data['newAddedTag']:
                new = models.Tag.objects.create(
                    tag_name=newTag,
                    created_date=datetime.datetime.now()
                )
                newAddedTage.append(new.tag_id)

        # 将新创建文章中的所有标签的id，保存在列表中(此时新标签已经存储到数据库中了)
        for tagName in data['selectedTag']:
            tag = models.Tag.objects.filter(tag_name=tagName).first()
            newAddedTage.append(tag)

    # 添加文章信息：Article_Info
    newArticleInfo = models.Article_Info.objects.create(
        read_count=0,
        comment_count=0,
        like_count=0,
        reprinted_count=0,
        updated_date=datetime.datetime.now(),
        created_date=datetime.datetime.now()
    )

    subCategoryObject = models.Sub_Category.objects.filter(sub_category_name=data['levelSecondCategory']).first()
    print(subCategoryObject)
    # 添加文章：Article
    newArticle = models.Article.objects.create(
        title=data['title'],
        subtitle=data['subtitle'],
        is_display=data['is_display'],
        content_text=data['content_text'],
        content_html=data['content_html'],
        article_info_id=newArticleInfo.article_info_id,
        sub_category=subCategoryObject
    )

    # 设置文章和标签的关系
    newArticle.tag.add(*newAddedTage)

    response = {
        'code': 1,
        'message': '创建文章成功'
    }
    # return HttpResponse('1')
    return JsonResponse(response)
