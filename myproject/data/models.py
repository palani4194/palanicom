from django.db import models

# Create your models here.

class SampleData(models.Model):
	firstname = models.CharField(max_length=10)
	age = models.IntegerField( default=0)
	phone = models.CharField(max_length=10)
	def __str__(self):
		return self.firstname


class AdultData(models.Model):
	# firstname = models.CharField(max_length=10)
	age = models.IntegerField( default=0)
	WORK_CLASS =(
    ('PR', 'Private'), ('SE', 'Self-emp-not-inc'), ('SEI', 'Self-emp-inc'), ('FG','Federal-gov'), ('LG','Local-gov'), ('SG', 'State-gov'), ('WP', 'Without-pay'), ('NW','Never-worked'),
    )
	workclass = models.CharField(max_length=50,default='--select--', choices=WORK_CLASS)
	fnl_wgt = models.IntegerField( default=0)
	EDUCATION_DETAILS =(
    ('BA','Bachelors'), ('SC','Some-college'), ('EL','11th'), ('HSC','HS-grad'), ('PS','Prof-school'),('AA','Assoc-acdm'), ('AV','Assoc-voc'), ('NI','9th'), ('STE','7th-8th'), ('TWE','12th'),
    ('MS','Masters'), ('FTF','1st-4th'), ('SSLC','10th'), ('DR','Doctorate'), ('FTS','5th-6th'), ('PS','Preschool'),
    )
	education = models.CharField(max_length=50, default='--select--', choices=EDUCATION_DETAILS)
	education_num = models.IntegerField( default=0)
	MARITAL_STATUS =(
     ('MC','Married-civ-spouse'), ('DV','Divorced'), ('NM','Never-married'), ('SE','Separated'),('WD','Widowed'), ('MSA','Married-spouse-absent'), ('MAS','Married-AF-spouse'),
     )
	maritalstatus = models.CharField(max_length=50,default='--select--', choices=MARITAL_STATUS)
	OCCUPATION_DETAILS = (
    ('TS','Tech-support'), ('CR','Craft-repair'), ('OS','Other-service'), ('SA','Sales'),
    ('EM','Exec-managerial'), ('PS','Prof-specialty'), ('HC','Handlers-cleaners'), ('MOP','Machine-op-inspct'),
    ( 'AC','Adm-clerical'), ('FF','Farming-fishing'), ('TM','Transport-moving'), ('PHS','Priv-house-serv'), ('PS','Protective-serv'), ('AF','Armed-Forces'),
    )
	occupation = models.CharField(default='--select--',max_length=50,choices=OCCUPATION_DETAILS)
	RELATIONSHIP_DETAILS =(
    ('Wife', 'Wife'), ('Own-child','Own-child'), ('Husband','Husband'), ('Not-in-family','Not-in-family'), ('Other-relative','Other-relative'), ('Unmarried','Unmarried'),

    )
	relationship = models.CharField(default='--select--',max_length=50, choices=RELATIONSHIP_DETAILS)
	RACE_DETAILS =(
    ('WH','White'), ('API','Asian-Pac-Islander'), ('AIE','Amer-Indian-Eskimo'), ('OT','Other'), ('BL','Black'),
    )
	race = models.CharField(default='--select--',max_length=50, choices=RACE_DETAILS)
	SEX_DETAILS = (('Female','Female'),('Male', 'Male'))
	sex = models.CharField(default='--select--',max_length=50,choices=SEX_DETAILS)
	capital_gain = models.IntegerField(default=0)
	capital_loss = models.IntegerField(default=0)
	hours_per_week = models.IntegerField( default=0)
	NATIVE_COUNTRY = (
    ('US', 'United-States'), ('CAM','Cambodia'), ('UK','England'),
    ('PR','Puerto-Rico'), ('CA','Canada'), ('GER','Germany'), ('OUS','Outlying-US(Guam-USVI-etc)'), ('IND','India'),
    ('JAP',' Japan'), ('GRE','Greece'), ('SO','South'), ('CHI','China'), ('CU','Cuba'), ('IR','Iran'), ('HO','Honduras'), ('PH','Philippines'), ('IT','Italy'),
    ('PL','Poland'), ('JAM','Jamaica'),('VI','Vietnam'), ('MX','Mexico'), ('PO','Portugal'), ('IR','Ireland'), ('FR','France'), ('DR','Dominican-Republic'),('LA','Laos'),
    ('ECU','Ecuador'), ('TAI','Taiwan'), ('HAI','Haiti'), ('COL','Columbia'),('HUN','Hungary'), ('GUA','Guatemala'),
    ('NIC','Nicaragua'), ('SCO','Scotland'), ('THA','Thailand'), ('YUG','Yugoslavia'), ('EIS','El-Salvador'), ('TRI','Trinadad&Tobago'),
    ('PER','Peru'), ('HO','Hong'), ('HN','Holand-Netherlands'),
    )
	native_country = models.CharField(default='--select--',max_length=50,choices=NATIVE_COUNTRY)


	def __str__(self):
		return self.workclass
