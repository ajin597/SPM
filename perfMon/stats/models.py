# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Stats(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpu_percent = models.FloatField(db_column='CPU_percent', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    ram_percent = models.FloatField(db_column='RAM_percent', blank=True, null=True)  # Field name made lowercase.
    mysql_ram_percent = models.FloatField(db_column='MySQL_RAM_percent', blank=True, null=True)  # Field name made lowercase.
    load_average = models.FloatField(db_column='Load_Average', blank=True, null=True)  # Field name made lowercase.
    uptime_mysql = models.BigIntegerField(db_column='Uptime_mysql', blank=True, null=True)  # Field name made lowercase.
    uptime_linux = models.BigIntegerField(db_column='Uptime_Linux', blank=True, null=True)  # Field name made lowercase.
    packet_loss = models.IntegerField(db_column='Packet_Loss', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stats'
