"""document_verification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from docapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url('^reg/$', views.reg, name='reg'),
    url('^reg_view/$', views.reg_view, name='reg_view'),
    url('^reg_del/(?P<pk>\d+)/$', views.reg_del, name='reg_del'),
    url('^reg_update/(?P<pk>\d+)/$', views.reg_update, name='reg_update'),
    url('^reg_db/$', views.reg_db, name='reg_db'),

    url('^login/$', views.login, name='login'),

    url('^simple_upload/$', views.simple_upload, name='simple_upload'),
    url('^simple_upload_view/$', views.simple_upload_view, name='simple_upload_view'),

    url('^StaffInfo/$', views.StaffInfo, name='StaffInfo'),
    url('^AddStaff_view/$', views.AddStaff_view, name='AddStaff_view'),
    url('^AddStaff_del/(?P<pk>\d+)/$', views.AddStaff_del, name='AddStaff_del'),
    url('^AddStaff_update/(?P<pk>\d+)/$', views.AddStaff_update, name='AddStaff_update'),
    url('^AddStaff_db/$',views.AddStaff_db,name='AddStaff_db'),


    url('^ComplaintDetails/$', views.ComplaintDetails, name='ComplaintDetails'),
    url('^ComplaintInfo_view/$', views.ComplaintInfo_view, name='ComplaintInfo_view'),
    url('^ComplaintInfo_view_c/$', views.ComplaintInfo_view_c, name='ComplaintInfo_view_c'),
    url('^ComplaintInfo_del/(?P<pk>\d+)/$', views.ComplaintInfo_del, name='ComplaintInfo_del'),
    url('^ComplaintInfo_update/(?P<pk>\d+)/$', views.ComplaintInfo_update, name='ComplaintInfo_update'),
    url('^ComplaintInfo_db/$', views.ComplaintInfo_db, name='ComplaintInfo_db'),

    url('^ComplaintStatus/(?P<pk>\d+)/$', views.ComplaintStatus, name='ComplaintStatus'),
    url('^ComplaintStatus_view/$', views.ComplaintStatus_view, name='ComplaintStatus_view'),
    url('^ComplaintStatus_view_c/(?P<pk>\d+)/$', views.ComplaintStatus_view_c, name='ComplaintStatus_view_c'),
    url('^ComplaintStatus_del/(?P<pk>\d+)$', views.ComplaintStatus_del, name='ComplaintStatus_del'),
    url('^ComplaintStatus_update/(?P<pk>\d+)$', views.ComplaintStatus_update, name='ComplaintStatus_update'),
    url('^ComplaintStatus_db/$', views.ComplaintStatus_db, name='ComplaintStatus_db'),

    url('^DocumentResult/$', views.DocumentResult, name='DocumentResult'),
    url('^DocumentResult_view/$', views.DocumentResult_view, name='DocumentResult_view'),
    url('^DocumentResult_view_2/$', views.DocumentResult_view_2, name='DocumentResult_view_2'),
    url('^doc_status_view_c/$', views.doc_status_view_c, name='doc_status_view_c'),
    url('^DocumentResult_del/(?P<pk>\d+)$', views.DocumentResult_del, name='DocumentResult_del'),
    url('^DocumentResult_update/(?P<pk>\d+)$', views.DocumentResult_update, name='DocumentResult_update'),
    url('^DocumentResult_update_v/(?P<pk>\d+)$', views.DocumentResult_update_v, name='DocumentResult_update_v'),
    url('^DocumentResult_update_a/(?P<pk>\d+)$', views.DocumentResult_update_a, name='DocumentResult_update_a'),
    url('^DocumentResult_update_r/(?P<pk>\d+)$', views.DocumentResult_update_r, name='DocumentResult_update_r'),
    url('^DocumentResult_db/$', views.DocumentResult_db, name='DocumentResult_db'),


    url('^DownloadDocs/$', views.DownloadDocs, name='DownloadDocs'),
    url('^DownloadDocs_view/$', views.DownloadDocs_view, name='DownloadDocs_view'),
    url('^DownloadDocs_del/(?P<pk>\d+)$', views.DownloadDocs_del, name='DownloadDocs_del'),
    url('^DownloadDocs_update/(?P<pk>\d+)$', views.DownloadDocs_update, name='DownloadDocs_update'),
    url('^DownloadDocs_db/$', views.DownloadDocs_db, name='DownloadDocs_db'),
    url('^download/$', views.download, name='download'),


    url('^ForwordComplaints/$', views.ForwordComplaints, name='ForwordComplaints'),
    url('^ForwordComplaints_view/$', views.ForwordComplaints_view, name='ForwordComplaints_view'),
    url('^ForwordComplaints_del/(?P<pk>\d+)$', views.ForwordComplaints_del, name='ForwordComplaints_del'),
    url('^ForwordComplaints_update/(?P<pk>\d+)$', views.ForwordComplaints_update, name='ForwordComplaints_update'),
    url('^ForwordComplaints_db/$', views.ForwordComplaints_db, name='ForwordComplaints_db'),

    url('^ForwordComplaintsworkes/$', views.ForwordComplaintsworkes, name='ForwordComplaintsworkes'),
    url('^ForwordComplaintsworkes_view/$', views.ForwordComplaintsworkes_view, name='ForwordComplaintsworkes_view'),
    url('^ForwordComplaintsworkes_del/(?P<pk>\d+)$', views.ForwordComplaintsworkes_del, name='ForwordComplaintsworkes_del'),
    url('^ForwordComplaintsworkes_update/(?P<pk>\d+)$', views.ForwordComplaintsworkes_update,name='ForwordComplaintsworkes_update'),
    url('^ForwordComplaintsworkes_db/$', views.ForwordComplaintsworkes_db, name='ForwordComplaintsworkes_db'),


    url('^UserRegistration1/$', views.UserRegistration1,name='UserRegistration1'),
    url('^UserRegistration1_view/$', views.UserRegistration1_view,name='UserRegistration1_view'),
    url('^UserRegistration1_del/(?P<pk>\d+)$', views.UserRegistration1_del,name='UserRegistration1_del'),
    url('^UserRegistration1_update/(?P<pk>\d+)$', views.UserRegistration1_update,name='UserRegistration1_update'),
    url('^UserRegistration1_db/$', views.UserRegistration1_db,name='UserRegistration1_db'),

    url('^SecurityKey/(?P<pk>\d+)/$',views.SecurityKey, name='SecurityKey'),
    url('^SecurityKey_view/$', views.SecurityKey_view, name='SecurityKey_view'),
    url('^SecurityKey_del/(?P<pk>\d+)$', views.SecurityKey_del, name='SecurityKey_del'),
    url('^SecurityKey_update/(?P<pk>\d+)$', views.SecurityKey_update, name='SecurityKey_update'),
    url('^SecurityKey_db/$', views.SecurityKey_db, name='SecurityKey_db'),

    url('^UploadDocs/(?P<pk>\d+)/$', views.UploadDocs, name='UploadDocs'),
    url('^UploadDocs_view/$', views.UploadDocs_view, name='UploadDocs_view'),
    url('^UploadDocs_del/(?P<pk>\d+)$', views.UploadDocs_del, name='UploadDocs_del'),
    url('^UploadDocs_update/(?P<pk>\d+)$', views.UploadDocs_update, name='UploadDocs_update'),
    url('^UploadDocs_db/$', views.UploadDocs_db, name='UploadDocs_db'),


    url('^send_email/$', views.send_email, name='send_email'),
    url('^changepass/$', views.changepass, name='changepass'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)