from django.db import models

class Regions(models.Model):
    region_id = models.AutoField(db_column='Region_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Regions'