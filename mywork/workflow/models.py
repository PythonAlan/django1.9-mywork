

from django.db import models

# Create your models here.
class Worktype(models.Model):
	Name	= 	models.CharField('工作分类',max_length=30)
	def __str__(self):
		return self.Name
	class Meta:

		verbose_name = '工作分类'
		verbose_name_plural = '工作分类'



class Work(models.Model):

	Number	=	models.IntegerField('编号')
	Title	=	models.CharField('标题',max_length=200)
	Target	=	models.CharField('目的',max_length=100)
	Steps	=	models.TextField('方案',max_length=1024)
	Work_type =	models.ForeignKey(Worktype)
	Ordered	=	models.BooleanField(default=False)
	Finisher =  models.CharField('负责人',max_length=50)
	Startime = models.DateField('开始时间',blank=True,null=True)
	Endtime	= 	models.DateField('结束时间',blank=True,null=True)
	def __str__(self):
		return self.Title

	class Meta:

		verbose_name = '工作流'
		verbose_name_plural = '工作流'