from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return "{0} {1} {2}".format(self, self.first_name, self.last_name)


class Books(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    member = models.ForeignKey(Member, related_name="books", null=True)

    def get_absolute_url(self):
        return reverse('library:detail_book', kwargs={'book_id': self.id})

    def __unicode__(self):
        return "%s %s" % (self, self.name, self.author)

    def __str__(self):
        return "{0} {1}".format(self.name, self.author)
