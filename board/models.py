from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')

    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE ,verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그') 
    # auto_now_add = 자동으로 현재시간을 저장 
    regisrered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간') 

    def __str__(self):
        return self.title  #문자열로 title반환 

    class Meta:
        db_table = 'fastcampus_board'  # 테이블명을 지정
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'