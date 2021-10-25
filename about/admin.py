from django.contrib import admin
from django.db.models import fields
from django.db.models.expressions import Exists
from .models import Head, Info
# Register your models here.


class Edite(admin.ModelAdmin):
    fields = ['Who_We_are_URI',
              'What_Do_We_Care_about_Why_Did_URI_Stablish',
              'The_Goal_Of_Scientific_Research',
              'The_Goal_Of_Scientific_Research_2',
              'The_Goal_Of_Scientific_Research_3',
              'The_Goal_Of_Scientific_Research_4',
              'The_Goal_Of_Scientific_Research_5',
              'The_Goal_Of_Scientific_Research_6',
              'The_Goal_Of_Scientific_Research_7',
              'The_Goal_Of_Scientific_Research_8',
              'The_Goal_Of_Scientific_Research_9',
              'The_Goal_Of_Scientific_Research_10',
              'What_Will_You_Benefit_From_URI',
              'Beginning_Of_The_Story',
              ]


admin.site.register(Head)
admin.site.register(Info, Edite)
