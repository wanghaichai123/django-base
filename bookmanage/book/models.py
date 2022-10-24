from django.db import models

# Create your models here.
'''
MVT设计模式中Medel专门负责和数据库交互对应models.py
1、我们的模型类 需要继承自 models.Model
2、系统会自动为我们添加一个主键--id
3、字段  
      字段名=model.类型（选项）
      字段名就是数据表的字段名
       char(M）
       varchar(M)
       M就是选项
'''
#准备书籍列表信息的模型类
#定义模型类,继承models，书数据库需要两个字段：id和name书名称
class BookInfo(models.Model):
         #会自动生成id
         name=models.CharField(max_length=10)
         #重写str方法让admin来显示书籍名称
         def __str__(self):
             return self.name
         #当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据



#准备人物列表信息的模型类
class PeoleInfo(models.Model):
        #自动生成id
        #书籍人物名称
        name = models.CharField(max_length=10)
        #人物性别
        gender = models.BooleanField()
        #外键约束：人物属于哪本书
        book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
# 模型迁移（建表）：迁移由两步完成：
# 1、生成迁移文件：根据模型类型生成创建表的语句 python manage.py makemigrations
# 2、执行迁移：根据第一步生成的语句在数据库中创建表  python manage.py migrate
