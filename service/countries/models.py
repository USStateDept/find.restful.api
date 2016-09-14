from django.db import models

class Country(models.Model):
    country_id = models.AutoField(db_column='Country_ID', primary_key=True)  # Field name made lowercase.
    country_name = models.CharField(db_column='Country_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dod_group = models.CharField(db_column='DOD_Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dos_group = models.CharField(db_column='DOS_Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usaid_group = models.CharField(db_column='USAID_Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    income_group = models.CharField(db_column='INCOME_Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # country_geography = models.TextField(db_column='Country_Geography', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iso = models.CharField(db_column='ISO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Countries'