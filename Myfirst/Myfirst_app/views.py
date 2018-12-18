from django.shortcuts import render, redirect
from .models import Userform
import sqlite3 as sql
import pandas as pd
import xlrd


data_base_name = '';
# Create your views here.
def first(request):
    return render(request,"Myfirst_app/basic.html")


def form(request):
    return render(request,"Myfirst_app/form.html")

def log(request):
    name = request.POST['name'];
    psw = request.POST['psw'];
    email = request.POST['id'];
    print(name, psw, email)
    print('Request recieved...',request.POST)
    value=Userform.objects.create(name=name,email=email,psw=psw)
    value.save()
    return render(request,"Myfirst_app/loggedin.html")

def data_analysis(request):
    global data_base_name;
    data_base_name=request.POST['db'];
    print("data base",data_base_name)
    db = sql.connect(data_base_name);
    cur = db.cursor();
    table_init = cur.execute("select name from sqlite_master where type='table'");
    table_data = table_init.fetchall()
    #console.log(table_data)
    table = [i[0] for i in table_data];
    db.close()
    return render(request, 'Myfirst_app/table_names.html', {'table' : table})

def show_form(request):
    return render(request, 'Myfirst_app/my_page.html');

def table_view(request):
    return render(request, 'Myfirst_app/table_names.html')

def table_analysis(request):
    global data_base_name;
    print('table_values', request.POST['table_drop_down']);
    
    db = sql.connect(data_base_name);
    cur = db.cursor();
    data=request.POST['table_drop_down']
    
    table = cur.execute("select * from  {}".format(data));
    table_data=[list(i) for i in table.fetchall()]
    col_names=cur.execute("PRAGMA TABLE_INFO({})".format(data))
    col=col_names.fetchall();
    col=[i[1] for i in col]
    db.close()
    df=pd.DataFrame(table_data,columns=col)
    type_of_file=request.POST['file_menu']
    if type_of_file=='csv':
        df.to_csv("./Myfirst_app/static/media/{}.csv".format(data))
        data = data+'.csv'
    elif type_of_file=='xls':
        df.to_excel("./Myfirst_app/static/media/{}.xls".format(data))
        data = data+'.xls'
    else :
        df.to_excel("./Myfirst_app/static/media/{}.xlsx".format(data))
        data = data+'.xlsx'

    return render(request,'Myfirst_app/details.html', {'table_data' : table_data, 'data' : data});

