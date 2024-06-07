from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

# вот тут я не очень поняла, что мы проверяем. что только один тег может быть главным?..
class ScopeInlineFormset(BaseInlineFormSet):
def clean(self):
    for form in self.forms:
        # В form.cleaned_data будет словарь с данными
        # каждой отдельной формы, которые вы можете проверить
        form.cleaned_data
        # вызовом исключения ValidationError можно указать админке о наличие ошибки
        # таким образом объект не будет сохранен,
        # а пользователю выведется соответствующее сообщение об ошибке
        raise ValidationError('Тут всегда ошибка')
    return super().clean()  # вызываем базовый код переопределяемого метода



class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 2


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopeInline,]