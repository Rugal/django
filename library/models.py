from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.

class Libuser(User):
    PROVINCE_CHOICES = (
    ('AB','Alberta'), # The first value is actually stored in db, the second is descriptive
    ('MB', 'Manitoba'),
    ('ON', 'Ontario'),
    ('QC', 'Quebec'),
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    phone = models.IntegerField(null=True)
    postalcode = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Libitem(models.Model):
    TYPE_CHOICES = (
    ('Book', 'Book'),
    ('DVD','DVD'),
    ('Other', 'Other'),
    )
    title = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Book')
    checked_out=models.BooleanField(default=False)
    user=models.ForeignKey(Libuser, default=None, null=True, blank=True)
    duedate=models.DateField(default=None, null=True, blank=True)
    last_chkout = models.DateField(default=None, null=True, blank=True)
    date_acquired = models.DateField(default=datetime.today())
    pubyr = models.IntegerField()

    def overdue(self):
        return 'Yes' if self.checked_out == True and self.duedate < datetime.today().date() else 'No'


    def __str__(self):
        return self.title


class Book(Libitem):
    CATEGORY_CHOICES = (
    (1, 'Fiction'),
    (2, 'Biography'),
    (3, 'Self Help'),
    (4, 'Education'),
    (5, 'Children'),
    (6, 'Teen'),
    (7, 'Other'),
    )
    author = models.CharField(max_length=100)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)

    def __str__(self):
        return self.title + ' by ' + self.author


class Dvd(Libitem):
    CATEGORY_CHOICES = (
    (1, 'G'),
    (2, 'PG'),
    (3, 'PG-13'),
    (4, '14A'),
    (5, 'R'),
    (6, 'NR'),
    )
    maker = models.CharField(max_length=100)
    duration = models.IntegerField(default=1)
    rating = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    instructor = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.title + ' by ' + self.maker
