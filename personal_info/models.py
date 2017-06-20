from django.db import models


class Resume(models.Model):
    company = models.CharField(u'公司', max_length=200, help_text='就职公司')
    position = models.CharField(u'职位', max_length=200)
    entry_time = models.DateField(u'入职时间')
    time_of_separation = models.DateField(u'离职时间', null=True, blank=True)
    verbose_for_work = models.TextField(u'工作描述', null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.company


class ContactInfo(models.Model):
    method = models.CharField(u'联系方式', max_length=200)
    detail = models.CharField(u'详情', max_length=512)

    def __unicode__(self):
        return self.method


class Aboutme(models.Model):
    item = models.CharField(u'社交', max_length=200)
    link = models.URLField(u'链接', max_length=512)

    def __unicode__(self):
        return self.item


class OpenSourceProject(models.Model):
    name = models.CharField(u'项目', max_length=200)
    link = models.URLField(u'链接', max_length=512)

    def __unicode__(self):
        return self.name


class ContributedProject(models.Model):
    name = models.CharField(u'项目', max_length=200)
    link = models.URLField(u'链接', max_length=512)

    def __unicode__(self):
        return self.name
