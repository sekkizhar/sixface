from django.conf.urls import patterns, include, url
from sixfaceapp import views
from django.conf import settings
#from django.conf import static
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
     # url(r'^$', 'sixfaceapp.views.firstpage'),
     url(r'^home/$', 'sixfaceapp.views.employee_details'),
     url(r'^$', 'sixfaceapp.views.student_details'),
     url(r'^sixfaceview/$', 'sixfaceapp.views.sixfaceview',name='sixfaceview'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    )
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
