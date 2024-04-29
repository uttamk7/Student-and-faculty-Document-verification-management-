from django.shortcuts import render,redirect
from django.urls import reverse
from docapp.models import UserRegistration
from docapp.models import UserLogin
from docapp.models import AddStaff
from docapp.models import ComplaintInfo
from docapp.models import Complaint_Status
from docapp.models import Document_Result
from docapp.models import Download_Docs
from docapp.models import Forword_Complaints
from docapp.models import Forword_complaints_workes
from docapp.models import User_Registration1
from docapp.models import Security_Key
from docapp.models import Upload_Docs
import smtplib
from docapp.models import UploadImage
from django.core.files.storage import FileSystemStorage
import os
from document_verification.settings import BASE_DIR
import datetime
import random

def index(request):

    return render(request,'index.html')
def index1(request):

    return render(request,'index1.html')

def reg(request):
    if request.method=="POST":
        name=request.POST.get('t1','')
        city=request.POST.get('t2','')
        address=request.POST.get('t3','')
        email=request.POST.get('t4','')
        contact=request.POST.get('t5','')
        UserRegistration.objects.create(name=name,city=city,address=address,email=email,contact=contact)
        UserLogin.objects.create(username=email,password=contact,utype='student')
        return render(request,'index.html')
    return render(request,'reg.html')

def login(request):

    if request.method=="POST":
        username=request.POST.get('t1','')
        request.session['username']=username
        password1=request.POST.get('t2','')
        request.session['password'] = password1
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck>=1:
            udata=UserLogin.objects.get(username=username)
            password=udata.password
            utype=udata.utype
            if password1==password:
                if utype=="admin":
                    return render(request,'admin_home.html')
                if utype=="student":
                    return render(request,'user_home.html')

                if utype=="staff":
                    return render(request,'worker_home.html')
            else:
                return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request, 'login.html',{'msg':'invalid username'})
    return render(request, 'login.html')

def reg_view(request):
    userdict=UserRegistration.objects.all()
    return render(request,'reg_view.html',{'userdict':userdict})

def reg_del(request,pk):
    rid=UserRegistration.objects.get(id=pk)
    rid.delete()
    userdict=UserRegistration.objects.all()
    return render(request,'reg_view.html',{'userdict':userdict})

def reg_update(request,pk):
    userdict=UserRegistration.objects.filter(id=pk).values()
    return render(request,'reg_edit.html',{'userdict': userdict})

def reg_db(request):
    if request.method=="POST":
        id=request.POST.get('id')
        name = request.POST.get('t1', '')
        city = request.POST.get('t2', '')
        address = request.POST.get('t3', '')
        email = request.POST.get('t4', '')
        contact = request.POST.get('t5', '')
        UserRegistration.objects.filter(id=id).update(name=name, city=city, address=address, email=email, contact=contact)
        userdict=UserRegistration.objects.all()
        return render(request,'reg_view.html',{'userdict': userdict})



def StaffInfo(request):
    if request.method=="POST":
        dept=request.POST.get('t1','')
        staff_name=request.POST.get('t2','')
        designation=request.POST.get('t3','')
        email=request.POST.get('t4','')
        contact=request.POST.get('t5','')
        AddStaff.objects.create(dept=dept,staff_name=staff_name, designation=designation, email=email,contact=contact)
    return render(request,'staffinfo.html')

def  AddStaff_view(request):
    userdict= AddStaff.objects.all()
    return render(request,'StaffInfo_view.html',{'userdict':userdict})

def AddStaff_del(request,pk):
    rid=AddStaff.objects.get(id=pk)
    rid.delete()
    userdict=AddStaff.objects.all()
    return render(request,'StaffInfo_view.html',{'userdict':userdict})

def AddStaff_update(request,pk):
    userdict=AddStaff.objects.filter(id=pk).values()
    return render(request,'StaffInfo_edit.html',{'userdict': userdict})

def AddStaff_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        dept = request.POST.get('t1','')
        staff_name = request.POST.get('t2','')
        designation = request.POST.get('t3','')
        email = request.POST.get('t4','')
        contact = request.POST.get('t5','')
        AddStaff.objects.filter(id=id).update(dept=dept, staff_name=staff_name, designation=designation, email=email, contact=contact)
        userdict = AddStaff.objects.all()
        return render(request, 'StaffInfo_view.html', {'userdict': userdict})

def ComplaintDetails(request):
    username=request.session['username']
    if request.method=="POST" and request.FILES['myfile']:
        userid=request.POST.get('t1','')
        complaint_type=request.POST.get('t2','')
        complaint_name=request.POST.get('t3','')
        location=request.POST.get('t4','')
        myfile=request.FILES['myfile']
        cmp_id=random.randint(1,7000)
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        pat=os.path.join(BASE_DIR,'/media/'+filename)
        ComplaintInfo.objects.create(userid=userid,complaint_type=complaint_type,complaint_name=complaint_name,location=location,photo=myfile,cmp_id=cmp_id)
        Complaint_Status.objects.create(cmp_id=cmp_id,photo=myfile,status='pending')
        return render(request,'ComplaintInfo.html',{'msg':'Complaint has registered successfully '})
    return  render(request,'ComplaintInfo.html',{'username':username})

def  ComplaintInfo_view(request):
    userdict=ComplaintInfo.objects.all()
    return render(request,'ComplaintInfo_view.html',{'userdict':userdict})

def  ComplaintInfo_view_c(request):
    username=request.session['username']
    userdict=ComplaintInfo.objects.filter(userid=username).values()
    return render(request,'ComplaintInfo_view_c.html',{'userdict':userdict})

def ComplaintInfo_del(request,pk):
    rid=ComplaintInfo.objects.get(id=pk)
    rid.delete()
    userdict=ComplaintInfo.objects.all()
    return render(request,'ComplaintInfo_view.html',{'userdict':userdict})

def ComplaintInfo_update(request,pk):
    userdict=ComplaintInfo.objects.filter(id=pk).values()
    return render(request,'ComplaintInfo_edit.html',{'userdict':userdict})

def ComplaintInfo_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        userid = request.POST.get('t1','')
        complaint_type = request.POST.get('t2','')
        complaint_name = request.POST.get('t3','')
        location = request.POST.get('t4','')
        photo = request.POST.get('t5','')
        cmp_id = request.POST.get('t5','')
        ComplaintInfo.objects.filter(id=id).update(userid=userid, complaint_type=complaint_type, complaint_name=complaint_name,location=location, photo=photo,cmp_id=cmp_id)
        userdict =ComplaintInfo.objects.all()
        return render(request, 'ComplaintInfo_view.html',{'userdict': userdict})





def ComplaintStatus(request,pk):
    udata=ComplaintInfo.objects.get(id=pk)
    cmp_id=udata.cmp_id
    if request.method=="POST" and request.FILES['myfile']:
        cmp_id= request.POST.get('t1','')
        myfile = request.FILES['myfile']
        status=request.POST.get('t3','')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/'+filename)
        Complaint_Status.objects.create(cmp_id=cmp_id,photo=myfile,status=status)
        return render(request,'worker_home.html')
    return render(request,'ComplaintStatus.html',{'cmp_id':cmp_id})


def download(request):
    if request.method=="POST":
        request_id=request.POST.get('t1')
        security_key=request.POST.get('t2')
        udata=Document_Result.objects.get(request_id=request_id)
        regno=udata.regno
        doc_name=udata.doc_name
        now=datetime.datetime.now()
        download_date=now.strftime("%Y-%m-%d")
        download_time=now.strftime("%X")
        ucheck=Security_Key.objects.filter(user_id=request_id).filter(security_key=security_key).count()
        if ucheck >=1:
            userdict=Upload_Docs.objects.filter(reg_id=request_id).values()
            Download_Docs.objects.create(regno=regno, doc_name=doc_name, download_date=download_date,download_time=download_time)

            return render(request,'upload_docs_view_c.html',{'userdict':userdict})
        else:
            Download_Docs.objects.create(regno=regno,doc_name=doc_name,download_date=download_date,download_time=download_time)
            return render(request,'download.html',{'msg':'invalid security key or request id'})
    return render(request,'download.html')

def  ComplaintStatus_view(request):

    userdict= Complaint_Status.objects.all()
    return render(request,'ComplaintStatus_view.html',{'userdict':userdict})

def  ComplaintStatus_view_c(request,pk):
    udata = ComplaintInfo.objects.get(id=pk)
    cmpid = udata.cmp_id
    userdict= Complaint_Status.objects.filter(cmp_id=cmpid).values()
    return render(request,'ComplaintStatus_view_c.html',{'userdict':userdict})

def ComplaintStatus_del(request,pk):
    rid= Complaint_Status.objects.get(id=pk)
    rid.delete()
    userdict= Complaint_Status.objects.all()
    return render(request,'ComplaintStatus_view.html',{'userdict':userdict})

def ComplaintStatus_update(request,pk):
    userdict=Complaint_Status.objects.filter(id=pk).values()
    return render(request,'ComplaintStatus_edit.html',{'userdict':userdict})

def ComplaintStatus_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        cmp_id = request.POST.get('t1','')
        photo = request.POST.get('t2','')
        status = request.POST.get('t3','')
        Complaint_Status.objects.filter(id=id).update(cmp_id=cmp_id,photo=photo,status=status)
        userdict = Complaint_Status.objects.all()
        return render(request,'ComplaintStatus_view.html',{'userdict': userdict})


def DocumentResult(request):
    username=request.session['username']
    regno=request.session['password']
    now=datetime.datetime.now()
    request_date=now.strftime("%Y-%m-%d")
    if request.method=="POST":
        request_id=random.randint(1,7000)
        regno=request.POST.get('t2', '')
        doc_name=request.POST.get('t3', '')
        Document_Result.objects.create(request_id=request_id, regno=regno, doc_name=doc_name,request_date=request_date,user_id=username, verify_status='pending', acceptance_status='pending',uploaded_status='pending')
        return render(request,'DocumentResult.html',{'msg':'Request has been sent successfully'})
    return  render(request,'DocumentResult.html',{'regno':regno})

def DocumentResult_view(request):
    userdict=Document_Result.objects.all()
    return render(request,'DocumentResult_view.html',{'userdict':userdict})


def DocumentResult_view_2(request):
    userdict=Document_Result.objects.filter(verify_status='Verified').filter(acceptance_status='Accepted').values()
    return render(request,'DocumentResult_view_2.html',{'userdict':userdict})

def doc_status_view_c(request):
    regno=request.session['password']
    userdict=Document_Result.objects.filter(regno=regno).values()
    return render(request,'DocumentResult_view_c.html',{'userdict':userdict})


def DocumentResult_del(request,pk):
    rid=Document_Result.objects.get(id=pk)
    rid.delete()
    userdict=Document_Result.objects.all()
    return render(request,'DocumentResult_view.html',{'userdict':userdict})

def DocumentResult_update(request,pk):
    userdict=Document_Result.objects.filter(id=pk).values()
    return render(request,'DocumentResult_edit.html',{'userdict':userdict})

def DocumentResult_update_a(request,pk):
    Document_Result.objects.filter(id=pk).update(acceptance_status='Accepted')
    userdict=Document_Result.objects.filter(id=pk).values()
    return render(request,'DocumentResult_view.html',{'userdict':userdict})

def DocumentResult_update_v(request,pk):
    Document_Result.objects.filter(id=pk).update(verify_status='Verified')
    userdict=Document_Result.objects.filter(id=pk).values()
    return render(request,'DocumentResult_view.html',{'userdict':userdict})

def DocumentResult_update_r(request,pk):
    Document_Result.objects.filter(id=pk).update(acceptance_status='Rejected')
    userdict=Document_Result.objects.filter(id=pk).values()
    return render(request,'DocumentResult_view.html',{'userdict':userdict})

def DocumentResult_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        request_id=request.POST.get('t1','')
        regno=request.POST.get('t2','')
        doc_name=request.POST.get('t3','')
        request_date=request.POST.get('t4','')
        user_id=request.POST.get('t5','')
        verify_status=request.POST.get('t6','')
        acceptance_status=request.POST.get('t7','')
        Document_Result.objects.filter(id=id).update(request_id=request_id, regno=regno, doc_name=doc_name,request_date=request_date,user_id=user_id, verify_status=verify_status, acceptance_status=acceptance_status)
        userdict=Document_Result.objects.all()
        return render(request, 'DocumentResult_view.html',{'userdict': userdict})

def DownloadDocs(request):
    if request.method=="POST":
        regno=request.POST.get('t1','')
        doc_name=request.POST.get('t2','')
        download_date=request.POST.get('t3','')
        download_time=request.POST.get('t4','')
        Download_Docs.objects.create(regno=regno,doc_name=doc_name,download_date=download_date,download_time=download_time)
    return  render(request,'DownloadDocs.html')

def DownloadDocs_view(request):
    userdict=Download_Docs.objects.all()
    return render(request,'DownloadDocs_view.html',{'userdict':userdict})

def DownloadDocs_del(request,pk):
    rid= Download_Docs.objects.get(id=pk)
    rid.delete()
    userdict=Download_Docs.objects.all()
    return render(request,'DownloadDocs_view.html',{'userdict':userdict})

def DownloadDocs_update(request,pk):
    userdict=Download_Docs.objects.filter(id=pk).values()
    return render(request,'DownloadDocs_edit.html',{'userdict':userdict})

def DownloadDocs_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        regno = request.POST.get('t1', '')
        doc_name = request.POST.get('t2', '')
        download_date = request.POST.get('t3', '')
        download_time = request.POST.get('t4', '')
        Download_Docs.objects.filter(id=id).update(regno=regno, doc_name=doc_name, download_date=download_date,download_time=download_time)
        userdict = Download_Docs.objects.all()
        return render(request,'DownloadDocs_view.html',{'userdict': userdict})


def ForwordComplaints(request):
    if request.method=="POST":
        cmp_id=request.POST.get('t1','')
        staff_name=request.POST.get('t2','')
        dept=request.POST.get('t3','')
        forword_date=request.POST.get('t4','')
        status=request.POST.get('t5','')
        Forword_Complaints.objects.create(cmp_id=cmp_id, staff_name=staff_name, dept=dept, forword_date=forword_date, status=status)
    return  render(request,'ForwordComplaints.html')

def ForwordComplaints_view(request):
    userdict=Forword_Complaints.objects.all()
    return render(request,'ForwordComplaints_view.html',{'userdict':userdict})

def ForwordComplaints_del(request,pk):
    rid= Forword_Complaints.objects.get(id=pk)
    rid.delete()
    userdict=Forword_Complaints.objects.all()
    return render(request,'ForwordComplaints_view.html',{'userdict':userdict})

def ForwordComplaints_update(request,pk):
    userdict=Forword_Complaints.objects.filter(id=pk).values()
    return render(request,'ForwordComplaints_edit.html',{'userdict':userdict})

def ForwordComplaints_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        cmp_id = request.POST.get('t1','')
        staff_name = request.POST.get('t2','')
        dept = request.POST.get('t3','')
        forword_date = request.POST.get('t4','')
        status = request.POST.get('t5','')
        Forword_Complaints.objects.filter(id=id).update(cmp_id=cmp_id, staff_name=staff_name, dept=dept, forword_date=forword_date,status=status)
        userdict = Forword_Complaints.objects.all()
        return render(request,'ForwordComplaints_view.html',{'userdict': userdict})



def ForwordComplaintsworkes(request):
    if request.method=="POST":
        cmp_id=request.POST.get('t1','')
        forword_date=request.POST.get('t2','')
        status=request.POST.get('t3','')
        Forword_complaints_workes.objects.create(cmp_id=cmp_id,forword_date=forword_date, status=status)
    return  render(request,'Forword_Complaints_workes.html')

def ForwordComplaintsworkes_view(request):
    userdict=Forword_complaints_workes.objects.all()
    return render(request,'ForwordComplaintsworkes_view.html',{'userdict':userdict})

def ForwordComplaintsworkes_del(request,pk):
    rid= Forword_complaints_workes.objects.get(id=pk)
    rid.delete()
    userdict=Forword_complaints_workes.objects.all()
    return render(request,'ForwordComplaintsworkes_view.html',{'userdict':userdict})

def ForwordComplaintsworkes_update(request,pk):
    userdict=Forword_complaints_workes.objects.filter(id=pk).values()
    return render(request,'ForwordComplaintsworkes_edit.html',{'userdict':userdict})

def ForwordComplaintsworkes_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        cmp_id = request.POST.get('t1', '')
        forword_date = request.POST.get('t2', '')
        status = request.POST.get('t3','')
        Forword_complaints_workes.objects.filter(id=id).update(cmp_id=cmp_id, forword_date=forword_date,status=status)
        userdict = Forword_complaints_workes.objects.all()
        return render(request, 'ForwordComplaintsworkes_view.html', {'userdict': userdict})

def UserRegistration1(request):
    if request.method=="POST" and request.FILES['myfile']:
        regno=request.POST.get('t1','')
        name=request.POST.get('t2','')
        dept=request.POST.get('t3','')
        address=request.POST.get('t4','')
        contact=request.POST.get('t5','')
        email=request.POST.get('t6','')
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        upload_file_url=fs.url(filename)
        pat=os.path.join(BASE_DIR,'/media/'+filename)
        User_Registration1.objects.create(regno=regno,name=name,dept=dept,address=address,email=email,contact=contact,photo=myfile)
        UserLogin.objects.create(username=email,password=regno,utype='student')
    return render(request,'UserRegistration1.html')

def UserRegistration1_view(request):
    userdict=User_Registration1.objects.all()
    return render(request,'UserRegistration1_view.html',{'userdict':userdict})

def  UserRegistration1_del(request,pk):
    rid=User_Registration1.objects.get(id=pk)
    rid.delete()
    userdict=User_Registration1.objects.all()
    return render(request,'UserRegistration1_view.html',{'userdict':userdict})

def UserRegistration1_update(request,pk):
    userdict=User_Registration1.objects.filter(id=pk).values()
    return render(request,'UserRegistration1_edit.html',{'userdict':userdict})

def UserRegistration1_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        regno = request.POST.get('t1','')
        name = request.POST.get('t2','')
        dept = request.POST.get('t3','')
        address = request.POST.get('t4','')
        contact = request.POST.get('t5','')
        email = request.POST.get('t6','')
        photo = request.POST.get('t7','')
        User_Registration1.objects.filter(id=id).update(regno=regno,name=name,dept=dept,address=address,email=email,contact=contact, photo=photo)
        userdict = User_Registration1.objects.all()
        return render(request,'UserRegistration1_view.html',{'userdict': userdict})


def SecurityKey(request,pk):
    udata=Document_Result.objects.get(id=pk)
    request_id=udata.request_id
    user_id=udata.user_id
    security_key=random.randint(1,11000)
    key=str(security_key)
    content = "Your Security Key-"+key
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('studentfacultydevelopment@gmail.com', 'wzlpjhnduclqwppc')
    mail.sendmail('studentfacultydevelopment@gmail.com', user_id, content)
    mail.close()
    Security_Key.objects.create(user_id=request_id,security_key=key,status='active')
    userdict = Document_Result.objects.filter(verify_status='Verified').filter(acceptance_status='Accepted').values()
    return render(request,'DocumentResult_view_2.html',{'userdict':userdict,'msg':'security key has sent'})

def SecurityKey_view(request):
    userdict=Security_Key.objects.all()
    return render(request,'SecurityKey_view.html',{'userdict':userdict})

def SecurityKey_del(request,pk):
    rid= Security_Key.objects.get(id=pk)
    rid.delete()
    userdict=Security_Key.objects.all()
    return render(request,'SecurityKey_view.html',{'userdict':userdict})

def SecurityKey_update(request,pk):
    userdict=Security_Key.objects.filter(id=pk).values()
    return render(request,'SecurityKey_edit.html',{'userdict':userdict})

def SecurityKey_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        user_id = request.POST.get('t1', '')
        security_key = request.POST.get('t2', '')
        status = request.POST.get('t3', '')
        Security_Key.objects.filter(id=id).update(user_id=user_id, security_key=security_key, status=status)
        userdict = Security_Key.objects.all()
        return render(request,'SecurityKey_view.html',{'userdict': userdict})

def UploadDocs(request,pk):
    udata=Document_Result.objects.get(id=pk)
    regno=udata.regno
    reg_id=udata.request_id
    user_id=udata.user_id
    document_name=udata.doc_name
    now=datetime.datetime.now()
    upload_date=now.strftime("%Y-%m-%d")
    if request.method=="POST" and request.FILES['myfile']:
        reg_id= request.POST.get('t1','')
        user_id = request.POST.get('t2','')
        regno= request.POST.get('t3','')
        dept= request.POST.get('t4','')
        document_name = request.POST.get('t5','')
        myfile= request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)
        Upload_Docs.objects.create(reg_id=reg_id,user_id=user_id,regno=regno,dept=dept,document_name=document_name,upload_doc=myfile,upload_date=upload_date,status='Uploaded')
        Document_Result.objects.filter(request_id=reg_id).update(uploaded_status='Uploaded')
        userdict = Document_Result.objects.filter(verify_status='Verified').filter(acceptance_status='Accepted').values()
        return render(request,'DocumentResult_view_2.html',{'userdict':userdict})
    return  render(request,'UploadDocs.html',{'reg_id':reg_id,'user_id':user_id,'regno':regno,'doc_name':document_name})

def UploadDocs_view(request):
    userdict=Upload_Docs.objects.all()
    return render(request,'UploadDocs_view.html',{'userdict':userdict})

def UploadDocs_del(request,pk):
    rid= Upload_Docs.objects.get(id=pk)
    rid.delete()
    userdict=Upload_Docs.objects.all()
    return render(request,'UploadDocs_view.html',{'userdict':userdict})

def UploadDocs_update(request,pk):
    userdict=Upload_Docs.objects.filter(id=pk).values()
    return render(request,'UploadDocs_edit.html',{'userdict':userdict})

def UploadDocs_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        reg_id = request.POST.get('t1', '')
        user_id = request.POST.get('t2', '')
        regno = request.POST.get('t3', '')
        dept = request.POST.get('t4', '')
        document_name = request.POST.get('t5', '')
        upload_doc = request.POST.get('t6', '')
        upload_date=request.POST.get('t7', '')
        Upload_Docs.objects.filter(id=id).update(reg_id=reg_id, user_id=user_id, regno=regno, dept=dept, document_name=document_name,upload_doc=upload_doc, upload_date=upload_date)
        userdict = Upload_Docs.objects.all()
        return render(request, 'UploadDocs_view.html', {'userdict': userdict})

def simple_upload(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        name=request.POST.get('t1')
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        pat=os.path.join(BASE_DIR,'/media/'+filename)
        UploadImage.objects.create(name=name,image=myfile)
        return render(request,'index1.html')
    return render(request,'simple_upload.html')

def simple_upload_view(request):
    userdict= UploadImage.objects.all()
    return render(request,'simple_upload_view.html',{'userdict':userdict})

def send_email(request):
    content="testing email"
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('studentfacultydevelopment@gmail.com','wzlpjhnduclqwppc')
    mail.sendmail('studentfacultydevelopment@gmail.com','jainuttam1008@gmail.com',content)
    mail.close()
    return render(request,'send_email.html')




def changepass(request):
    uname=request.session['username']
    userdict={'msg':'one record inserted successfully'}
    if request.method == 'POST':

        currentpass=request.POST.get('t2','')
        newpass=request.POST.get('t3','')
        confirmpass=request.POST.get('t4','')

        ucheck=UserLogin.objects.filter(username=uname).values()
        for a in ucheck:
            u=a['username']
            p=a['password']
            if u==uname and currentpass==p:
                if newpass==confirmpass:
                    UserLogin.objects.filter(username=uname).update(password=newpass)
                    base_url=reverse('login')
                    return redirect(base_url)
                else:
                    return render(request,'changepass.html',context={'msg':'both theusername and password'})
            else:
                return render(request,'changepass.html',context={'msg':'invalid username'})
    return render(request,'changepass.html')