from django.db import models

# Create your models here.
class RatingTableOne(models.Model):

    Name = models.CharField(max_length=15,primary_key=True)
    rValue=[
        ('0','None'),('1','*'),('2','**'),('3','***'),('4','****'),('5','*****')
    ]
    No_1= models.CharField(max_length=2,default='0',choices=rValue,help_text='Synergic Calculator')
    No_2 = models.CharField(max_length=2,default='0',choices=rValue,help_text='ID Card Generator')
    No_3 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Inventory Management')
    No_4 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Food Chatbot')
    No_5 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Incident Reporter')
    No_6 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Online Banking System')
    No_7 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Online Voting System')
    No_8 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Bus Times')
    No_9 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Secret Code')
    No_10 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Health Dot')
    No_11 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Online Attendance using Face Recognition')
    No_12 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Heart Disease Prediction')
    No_13 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Exquisite Checks')
    No_14 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Facemask Detection System')
    No_15 = models.CharField(max_length=2,default='0',choices=rValue,help_text='OTP Verification')
    No_16 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Language Translator')
    No_17= models.CharField(max_length=2,default='0',choices=rValue,help_text='Matrix Calculator')
    No_18 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Project Info')
    No_19 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Housing Society Management System')
    No_20 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Hangman')
    No_21 = models.CharField(max_length=2,default='0',choices=rValue,help_text="Virtual Counselor")





class RatingTableTwo(models.Model):
    Name = models.CharField(max_length=15,primary_key=True)
    rValue=[
        ('0','None'),('1','*'),('2','**'),('3','***'),('4','****'),('5','*****')
    ]
    No_1= models.CharField(max_length=2,default='0',choices=rValue,help_text='Interview IQ:Aptitude&Interview Training Game')
    No_2 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Steganography')
    No_3 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Controlling Home Appliances using Voice Assistence')
    No_4 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Virtual AI Assistent')
    No_5 = models.CharField(max_length=2,default='0',choices=rValue,help_text='IV Bag Monitoring & Alert System')
    No_6 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Virtual Mouse')
    No_7 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Barrier Buster')
    No_8 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Object Detection')
    No_9 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Fraud Detection')
    No_10 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Gesture Control')
    No_11 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Plagiarism Checker')
    No_12 = models.CharField(max_length=2,default='0',choices=rValue,help_text='E-Cart Universe & AI Virtual Marker')
    No_13 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Word Game')
    No_14 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Song Recommendation using Face Reaction')
