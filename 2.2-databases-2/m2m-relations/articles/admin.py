from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

# вот тут я не очень поняла, как проверять. как достучаться отсюда до scope.is_main
# class ScopeInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             form.cleaned_data = form.dict()
#             if form.cleaned_data.is_main == 0:
#                 raise ValidationError('Укажите основной раздел')
#             if form.cleaned_data.is_main > 1:
#                 raise ValidationError('Основным может быть только один раздел')
#             # for key, value in form.items():
#             #     if form.is_main:
#             #         raise ValidationError('Укажите основной раздел')
#             #     if value > 1:
#             #         raise ValidationError('Основным может быть только один раздел')
#
#         #     # В form.cleaned_data будет словарь с данными
#         #     # каждой отдельной формы, которые вы можете проверить
#         #     form.cleaned_data
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             # raise ValidationError('Основным может быть только один раздел')
#             # raise ValidationError('Укажите основной раздел')
#         return super().clean()  # вызываем базовый код переопределяемого метода



class ScopeInline(admin.TabularInline):
    model = Scope
    # formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    #как в эту таблицу вытащить теги статей - тоже не поняла
    inlines = [ScopeInline, ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopeInline,]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag', 'is_main']

