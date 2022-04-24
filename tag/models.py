from django.db import models

# Create your models here.

class Tag(models.Model):
  name = models.CharField(max_length=32, verbose_name='테그명')
  registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

  def __str__(self):            # 객체를 리스트로 받았을 때의 이름을 보여주는 함수
    return self.name

  class Meta:
    db_table = 'fastcampus_tag'
    verbose_name = '패스트캠퍼스 테그'
    verbose_name_plural = '패스트캠퍼스 테그'
