from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django import forms

from .models import Article, Tag, Scope




# вот тут я не очень поняла, как проверять. как достучаться отсюда до scope.is_main
class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        data_ismain = 0
        tag = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                data_ismain += 1
            if form.cleaned_data['tag']:
                tag += 1
        if tag == 0:
            raise ValidationError('Укажите хотя бы один раздел')
        if data_ismain == 0:
            raise ValidationError('Укажите основной раздел')
        if data_ismain != 1:
            raise ValidationError('Основным может быть только один раздел')


        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    #как в эту таблицу вытащить теги статей - тоже не поняла. мы же задавали related_name, и я думала, этого достаточно, чтобы дописать сюда 'tag'?..
    inlines = [ScopeInline, ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopeInline,]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag', 'is_main']

