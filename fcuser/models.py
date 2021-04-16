from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    # auto_now_add = 자동으로 현재시간을 저장 
    regisrered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간') 

    def __str__(self):
        return self.username  #문자열로 username반환 

    class Meta:
        db_table = 'fastcampus_fcuser'  # 테이블명을 지정
        verbose_name = '패스트 캠퍼스 사용자'
        verbose_name_plural = '패스트 캠퍼스 사용자'