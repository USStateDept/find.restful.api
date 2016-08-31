from django.db import models

class Indicator(models.Model):
    indicator_id = models.AutoField(db_column='Indicator_ID', primary_key=True)  # Field name made lowercase.
    indicator_name = models.CharField(db_column='Indicator_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indicator_url = models.CharField(db_column='Indicator_URL', max_length=520, blank=True, null=True)  # Field name made lowercase.
    indicator_data_url = models.CharField(db_column='Indicator_Data_URL', max_length=520, blank=True, null=True)  # Field name made lowercase.
    direct_indicator_source = models.CharField(db_column='Direct_Indicator_Source', max_length=255, blank=True, null=True)  # Field name made lowercase.
    original_indicator_source = models.CharField(db_column='Original_Indicator_Source', max_length=520, blank=True, null=True)  # Field name made lowercase.
    update_cycle = models.CharField(db_column='Update_Cycle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scope = models.CharField(db_column='Scope', max_length=255, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_source_update_ts = models.DateTimeField(db_column='Last_Source_Update_TS', blank=True, null=True)  # Field name made lowercase.
    when_to_update_ts = models.DateTimeField(db_column='When_To_Update_TS', blank=True, null=True)  # Field name made lowercase.
    indicator_definition = models.TextField(db_column='Indicator_Definition', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    avg_equal = models.NullBooleanField(db_column='AVG_EQUAL')  # Field name made lowercase.
    avg_population = models.NullBooleanField(db_column='AVG_POPULATION')  # Field name made lowercase.
    avg_gdp = models.NullBooleanField(db_column='AVG_GDP')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Indicators'