

# Register your models here.

from django.contrib import admin
from .models import Academic, Category,Question,Reference,Result

class CategoryAdmin(admin.ModelAdmin):
      list_display=('title', 'createdAt')



class QuestionAdmin(admin.ModelAdmin):
      list_display=('questionText',)

class ReferenceAdmin(admin.ModelAdmin):
      list_display=('categoryid','questionid','link',)

class ResultAdmin(admin.ModelAdmin):
      list_display=('user','category','got_marks')
      search_fields=('id',)
      list_filter=('category',)
      list_per_page=3


class AcademicAdmin(admin.ModelAdmin):
      list_display = ('sub_name', 'fac_name',)

# Register your models here.

admin.site.register(Result,ResultAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Reference,ReferenceAdmin)
admin.site.register(Academic,AcademicAdmin)