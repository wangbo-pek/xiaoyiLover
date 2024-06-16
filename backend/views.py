import json
import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import get_token
from django.http import JsonResponse
from backend import models
from django.core import serializers


# 获取token
def getToken(request):
    csrf_token = get_token(request)
    response = {
        'csrf_token': csrf_token,
        'code': 1,
        'message': '获取Token成功'}
    return JsonResponse(response)


# 获取所有文章列表
def getArticleList(request):
    response = {
        'articlesList_data': []
    }

    articlesList = models.Article.objects.all()
    for article in articlesList:
        currentArticle = {
            'article_id': article.article_id,
            'title': article.title,
            'subtitle': article.subtitle,
            'is_display': article.is_display,
            'updated_date': article.updated_date,
            'created_date': article.created_date,
            'subcategory': article.sub_category.sub_category_name,
            'category': article.sub_category.category.category_name,
            'tags': []
        }
        for tag in article.tag.all():
            currentArticle['tags'].append(tag.tag_name)
        response['articlesList_data'].append(currentArticle)
    response['code'] = 1
    response['message'] = '获取文章列表成功'
    return JsonResponse(response)
    # return HttpResponse('1')


# 获取文章分类
def getAllCategory(request):
    response = {
        'category_data': [],
        'subcategory_data': {}
    }

    allCategory = models.Category.objects.all()
    print(allCategory[0].category_name)
    print(allCategory[0].sub_category_set.all()[0].sub_category_name)

    for category in allCategory:
        response['category_data'].append(category.category_name)
        subList = []
        for sub in category.sub_category_set.all():
            subList.append(sub.sub_category_name)
        response['subcategory_data'][category.category_name] = subList
    response['code'] = 1
    response['message'] = '获取文章分类成功'
    print(response)
    return JsonResponse(response)


# 获取文章标签
def getAllTag(request):
    response = {
        'tag_data': []
    }
    allTag = models.Tag.objects.all()

    for tag in allTag:
        response['tag_data'].append(tag.tag_name)
    response['code'] = 1
    response['message'] = '获取文章标签成功'
    return JsonResponse(response)


# 创建文章
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
        content_text=data['content_text'],
        content_html=data['content_html'],
    )

    subCategoryObject = models.Sub_Category.objects.filter(sub_category_name=data['levelSecondCategory']).first()

    # 添加文章：Article
    newArticle = models.Article.objects.create(
        title=data['title'],
        subtitle=data['subtitle'],
        is_display=data['is_display'],
        updated_date=datetime.datetime.now(),
        article_info_id=newArticleInfo.article_info_id,
        sub_category=subCategoryObject
    )

    # 设置文章和标签的关系
    newArticle.tag.add(*newAddedTage)

    # 将新创建的文章返回给前端
    newCreatedArticle = {
        'article_id': newArticle.article_id,
        'title': newArticle.title,
        'subtitle': newArticle.subtitle,
        'is_display': newArticle.is_display,
        'updated_date': newArticle.updated_date,
        'created_date': newArticle.created_date,
        'subcategory': newArticle.sub_category.sub_category_name,
        'category': newArticle.sub_category.category.category_name,
        'tags': []
    }

    for tag in newArticle.tag.all():
        newCreatedArticle['tags'].append(tag.tag_name)

    response = {
        'newArticle_data': newCreatedArticle,
        'code': 1,
        'message': f'文章{newArticle.title}创建成功'
    }
    return JsonResponse(response)


def deleteArticle(request, articleId):
    # 清除文章与标签的对应关系
    toBeDeleteArticle = models.Article.objects.filter(article_id=articleId)[0]
    toBeDeleteArticle.tag.clear()
    toBeDeleteArticleTitle = toBeDeleteArticle.title

    # 获取到要删除的文章的model对象
    toBeDeleteArticleObject = models.Article.objects.filter(article_id=articleId).first()

    # 删除article_info
    models.Article_Info.objects.filter(article_info_id=toBeDeleteArticleObject.article_info.article_info_id).delete()
    # 删除article
    models.Article.objects.filter(article_id=articleId).delete()
    response = {
        'code': 1,
        'message': f'文章{toBeDeleteArticleTitle}删除成功'
    }
    return JsonResponse(response)


def fetchArticle(request, articleId):
    response = {}
    articleObject = models.Article.objects.filter(article_id=articleId).first()
    response['article_info'] = {
        'content_text': articleObject.article_info.content_text,
        'content_html': articleObject.article_info.content_html,
        'read_count': articleObject.article_info.read_count,
        'comment_count': articleObject.article_info.comment_count,
        'like_count': articleObject.article_info.like_count,
        'reprinted_count': articleObject.article_info.reprinted_count,
    }
    response['code'] = 1
    response['message'] = f'获取文章{articleObject.title}成功'
    return JsonResponse(response)
    # return HttpResponse('1')


def reviseArticle(request):
    toBeReviseArticleData = json.loads(request.body)
    print(toBeReviseArticleData)
    tagsIdList = []

    # 修改文章的标题、副标题、更新日期
    models.Article.objects.filter(article_id=toBeReviseArticleData['article_id']).update(
        title=toBeReviseArticleData['title'],
        subtitle=toBeReviseArticleData['subtitle'],
        is_display=toBeReviseArticleData['is_display'],
        updated_date=datetime.datetime.now(),
    )

    # 获取到已经修改后文章的model对象
    revisedArticleObject = models.Article.objects.filter(article_id=toBeReviseArticleData['article_id'])[0]
    # 获取到修改后文章的sub_category的model对象
    subcategoryObject = models.Sub_Category.objects.filter(
        sub_category_name=toBeReviseArticleData['subcategory']).first()
    # 修改sub_category
    revisedArticleObject.sub_category_id = subcategoryObject.sub_category_id

    # 修改文章的text和html
    models.Article_Info.objects.filter(article_info_id=revisedArticleObject.article_info_id).update(
        content_text=toBeReviseArticleData['content_text'],
        content_html=toBeReviseArticleData['content_html']
    )



    # 判断修改的文章中是否有标签
    if 'selectedTag' in toBeReviseArticleData:
        # 将修改的文章与标签的关系删除
        revisedArticleObject.tag.clear()

        # 文章中有标签，并判断是否有新创建的标签
        if 'newAddedTag' in toBeReviseArticleData:
            # 文章中有标签，且包含了新创建的标签
            # 将新创建的标签存储到数据库
            for newTagName in toBeReviseArticleData['newAddedTag']:
                models.Tag.objects.create(
                    tag_name=newTagName,
                    created_date=datetime.datetime.now()
                )

        # 将文章中的所有标签的id，保存在列表中(此时新标签已经存储到数据库中了)
        for tagName in toBeReviseArticleData['selectedTag']:
            tag = models.Tag.objects.filter(tag_name=tagName).first()
            tagsIdList.append(tag.tag_id)

    revisedArticleObject.tag.add(*tagsIdList)

    # 将编辑修改后的文章返回给前端
    revisedArticle = {
        'article_id': revisedArticleObject.article_id,
        'title': revisedArticleObject.title,
        'subtitle': revisedArticleObject.subtitle,
        'is_display': revisedArticleObject.is_display,
        'updated_date': revisedArticleObject.updated_date,
        'created_date': revisedArticleObject.created_date,
        'subcategory': revisedArticleObject.sub_category.sub_category_name,
        'category': revisedArticleObject.sub_category.category.category_name,
        'content_text': revisedArticleObject.article_info.content_text,
        'content_html': revisedArticleObject.article_info.content_html,
        'tags': []
    }

    for tag in revisedArticleObject.tag.all():
        revisedArticle['tags'].append(tag.tag_name)

    response = {
        'revisedArticle_data': revisedArticle,
        'code': 1,
        'message': f'文章{revisedArticleObject.title}修改成功'
    }

    return JsonResponse(response)
    # return HttpResponse('1')
