from django.db import models

class UserRegistration(models.Model):
    name=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    contact=models.CharField(max_length=10)


class UserLogin(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)

class AddStaff(models.Model):
    dept=models.CharField(max_length=40,null=True,blank=True)
    staff_name=models.CharField(max_length=40,null=True,blank=True)
    designation=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=40,null=True,blank=True)
    contact=models.CharField(max_length=10,null=True,blank=True)

class ComplaintInfo(models.Model):
    userid=models.CharField(max_length=40,null=True,blank=True)
    complaint_type=models.CharField(max_length=100,null=True,blank=True)
    complaint_name=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    photo=models.FileField(upload_to='documents/',null=True,blank=True)
    cmp_id=models.CharField(max_length=40,null=True,blank=True)

class Complaint_Status(models.Model):
    cmp_id=models.CharField(max_length=40)
    photo=models.FileField(upload_to='documents/')
    status=models.CharField(max_length=100)

class Document_Result(models.Model):
    request_id=models.CharField(max_length=40)
    regno=models.CharField(max_length=40)
    doc_name=models.CharField(max_length=40)
    request_date=models.DateField()
    user_id=models.CharField(max_length=40)
    verify_status=models.CharField(max_length=100)
    acceptance_status=models.CharField(max_length=100)
    uploaded_status=models.CharField(max_length=40,null=True,blank=True)

class Download_Docs(models.Model):
    regno=models.CharField(max_length=40)
    doc_name=models.CharField(max_length=40)
    download_date=models.DateField()
    download_time=models.CharField(max_length=40)

class Forword_Complaints(models.Model):
    cmp_id=models.CharField(max_length=40)
    staff_name=models.CharField(max_length=40)
    dept=models.CharField(max_length=40)
    forword_date=models.CharField(max_length=40)
    status=models.CharField(max_length=40)

class Forword_complaints_workes(models.Model):
    cmp_id=models.CharField(max_length=40)
    forword_date=models.CharField(max_length=40)
    status=models.CharField(max_length=40)

class User_Registration1(models.Model):
    regno=models.CharField(max_length=40,null=True,blank=True)
    name=models.CharField(max_length=40)
    dept=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    photo=models.FileField(upload_to='documents/')

class Security_Key(models.Model):
    user_id=models.CharField(max_length=40)
    security_key=models.CharField(max_length=40)
    status=models.CharField(max_length=40)

class Upload_Docs(models.Model):
    reg_id=models.CharField(max_length=40)
    user_id=models.CharField(max_length=40)
    regno=models.CharField(max_length=40)
    dept=models.CharField(max_length=40)
    document_name=models.CharField(max_length=40)
    upload_doc=models.FileField(upload_to='documents/')
    upload_date=models.DateField()
    status=models.CharField(max_length=100,null=True,blank=True)

class UserLogin1(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    utype=models.CharField(max_length=40)


class UploadImage(models.Model):
    name=models.CharField(max_length=40)
    image=models.FileField(upload_to='documents/')

