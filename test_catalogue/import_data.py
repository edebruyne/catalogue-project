import os, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_catalogue.settings")
import django
django.setup()
from catalogue.models import *

fname = "data.csv"
file = open(fname, "rb")

try:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "Product":
            brand, created = Brand.objects.get_or_create(name=row[2])
            categ, created = Category.objects.get_or_create(name=row[3])
            prd, created = Product.objects.get_or_create(name=row[1], brand=brand, category=categ, price=int(row[4]))
        elif row[0] == "Category":
            categ, created = Category.objects.get_or_create(name=row[2])
        elif row[0] == "User":
            brand, created = Brand.objects.get_or_create(name=row[3])
            user, created = User.objects.get_or_create(username=row[1], is_staff=row[4])
            user.set_password(row[2])
            user.save()
            cusUser, created = CustomUser.objects.get_or_create(user=user, brand=brand)
        elif row[0] == "Brand":
            brand, created = Brand.objects.get_or_create(name=row[1])
finally:
    file.close()