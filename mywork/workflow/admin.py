from django.contrib import admin
from .models import Work,Worktype

# Register your models here.
class BookInfo(admin.ModelAdmin):
	list_display = ('Number','Title','Target','Steps','Work_type','Ordered','Finisher','Startime','Endtime')
	search_fields = ('Types','Title','Target','Finisher')
	Work.objects.extra(
			select={'Number':'CAST(Number as INTEGER)'}).order_by("Number")
	list_per_page = 5

admin.site.register(Worktype)
admin.site.register(Work,BookInfo)
