from django.db import models


class ArticleModel(models):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=256)
    # category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CategoryModel(models):
    class Meta:
        db_table = "category"


    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)