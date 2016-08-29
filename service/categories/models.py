from django.db import models

class Category(models.Model):
    category_id = models.AutoField(db_column='Category_ID', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sub_category_name = models.CharField(db_column='Sub_Category_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        db_table = 'Categories'