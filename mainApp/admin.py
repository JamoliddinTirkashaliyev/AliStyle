from django.contrib import admin
from  .models import *

admin.site.register([Country,City,Category,SubCategory])
