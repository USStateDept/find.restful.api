from django.db import models

class RegionData(models.Model):
    region_data = models.AutoField(db_column='Region_Data', primary_key=True)  # Field name made lowercase.
    indicator_id = models.IntegerField(db_column='Indicator_ID', blank=True, null=True)  # Field name made lowercase.
    region_id = models.IntegerField(db_column='Region_ID', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(db_column='Avg', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    # dataviewdataviewid = models.ForeignKey(DataViews, models.DO_NOTHING, db_column='DataViewDataViewID', blank=True, null=True)  # Field name made lowercase.
    # regiondatumregiondata = models.ForeignKey('self', models.DO_NOTHING, db_column='RegionDatumRegionData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Region_Data'