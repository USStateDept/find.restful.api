from django.db import models

# class Data(models.Model):
#     data_id = models.AutoField(db_column='Data_ID', primary_key=True)  # Field name made lowercase.
#     date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
#     value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     indicator = models.ForeignKey('Indicators', models.DO_NOTHING, db_column='Indicator_ID', blank=True, null=True)  # Field name made lowercase.
#     country = models.ForeignKey('Countries', models.DO_NOTHING, db_column='Country_ID', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         # managed = False
#         db_table = 'Data'