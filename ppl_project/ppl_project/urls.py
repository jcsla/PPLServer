from django.conf.urls import patterns, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^insert_ppl_data$', insert_ppl_data),
    (r'^get_ppl_data$', get_ppl_data),
    (r'^modify_ppl_data$', modify_ppl_data),
)
