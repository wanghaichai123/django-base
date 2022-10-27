from django.db import models

# Create your models here.

'''
1、模型类 需要继承models.Model
2、定义属性
      属性名=models.类型（选项）
      2.1 属性名 对应 就是字段名
          不要使用python，Mysql关键字
          不要使用连续的下划线（__）
      2.2 类型 MySQL的类型
      2.3选项 是否有默认值，是否唯一，是否为null
             CharField必须设置max_length
             verbose_name 主要是admin站点使用
3、改变表的名称
    默认表的名称是：子应用名称——类名 都是小写
    修改表的名字如下在class类中在写个class类
create table 'qq_user'(
   id int,
   name varchar(10) not null default ''
)
      
'''
class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True,verbose_name='名字')
    pub_data = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Mata:
        db_table = 'bookinfo' #修改表的名称
        verbose_name = '书籍管理02' #admin站点使用的（了解）