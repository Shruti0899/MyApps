from django.urls import path
from . import views

urlpatterns=[
    path("/first/",views.first,name="first"),
    path("/form/",views.form,name="form"),
    path("/log_in/",views.log,name="log"),
    path("/db_abc/", views.show_form, name = "show_form"),
    path("/analysis/",views.data_analysis,name="data_analysis"),
    path("/table_data/", views.table_view, name = "table_view"),
    path("/tables", views.table_analysis, name = "table_analysis"),
    ]