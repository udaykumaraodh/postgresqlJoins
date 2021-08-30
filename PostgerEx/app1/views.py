
from django.db.backends.utils import CursorDebugWrapper
from django.shortcuts import render, HttpResponse
from django.db import connection

# Create your views here.

def curd_op_c(request):
    print(connection.cursor())
    with connection.cursor() as cursor:
        cursor.execute('''INSERT INTO app1_CollegeModel  VALUES (%s,%s)''',("BBCIT","kachiguda"))
        connection.commit()

        #data  = cursor.fetchone()
        #print(data)
    return HttpResponse('craeted')


def departmentTable(request):
    with connection.cursor() as cursor:
        #cursor.execute(''' INSERT INTO app1_DepartmentModel (d_no,dep_name,clg_id) values(3,'ECE','BBCIT'),(4,'MECH','BBCIT')''')
        #connection.commit()

        cursor.execute('''Select * from app1_DepartmentModel''')
        al=cursor.fetchall()
        print(al)

    return HttpResponse(al)


def lectTable(request):
    with connection.cursor() as cursor:
        cursor.execute(''' Insert into app1_LecturerModel (lecturer_id,l_name,subject,clg_id) values (104,'harish','Mathematics','BBCIT')''')
        connection.commit()
        cursor.execute('''Select * from app1_LecturerModel ''')
        #data=cursor.fetchone()

        # cursor.execute('''Insert into app1_lecturermodel_depname(LecturerModel_id,DepartmentModel_id) values (102,1)''')
        # connection.commit()
        # cursor.execute('''Select * from app1_lecturermodel_depname''')

        # ld=cursor.fetchall()

        #cursor.execute('''select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,l2.departmentmodel_id as Department from app1_lecturermodel as l1 left join  app1_lecturermodel_depname as l2  on  l1.lecturer_id=l2.lecturermodel_id''')

        ld=cursor.fetchall()



    return HttpResponse(ld)


def studentTable(request):
    with connection.cursor() as cursor:
        cursor.execute(''' Insert into app1_StudentModel (rollno,dep_id,lname_id,s_name,email,clg_id) values(10002,3,102,'priya ','priya124@gmail.com','BBCIT'),(10003,3,102,'kiran ','kiran12@gmail.com','BBCIT'),(10004,2,101,'likith ','likith12@gmail.com','BBCIT')''')
        connection.commit()
        cursor.execute(''' select * from app1_studentmodel''')
        ds=cursor.fetchall()

        # cursor.execute(''' update app1_StudentModel set email ='priya24@gmail.com' where rollno=10002      ''')
        # connection.commit()
        # cursor.execute(''' select * from app1_studentmodel''')
        # ds=cursor.fetchall()

        # cursor.execute(''' delete from app1_StudentModel where rollno=10002      ''')
        # connection.commit()
        # cursor.execute(''' select * from app1_studentmodel''')
        # ds=cursor.fetchall()


        
    
    return HttpResponse(ds)

def joinTable(request):
    #inner join
    with connection.cursor() as cursor:
        #cursor.execute(''' select distinct l.clg_id ,l.lecturer_id ,l.l_name,l.subject,d.dep_name from app1_lecturermodel l inner join app1_departmentmodel d on l.clg_id= d.clg_id''')
        #cursor.execute(''' select distinct l.clg_id ,l.lecturer_id ,l.l_name,l.subject,d.dep_name from app1_lecturermodel l inner join app1_departmentmodel d using(clg_id)''')
        #cursor.execute(''' select Distinct s.rollno,s.s_name,s.email,s.lname_id,l.l_name,l.subject,d.dep_name from app1_studentmodel s inner join app1_lecturermodel l using (clg_id) inner join app1_departmentmodel d on l.clg_id = d.clg_id  order by s.rollno''')
#         cursor.execute('''select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,l2.departmentmodel_id as Department ,
# d.dep_name as depname from  app1_lecturermodel l1 inner join  
# app1_lecturermodel_depname l2  on lecturer_id=l2.lecturermodel_id inner join 
# app1_departmentmodel d on l2.departmentmodel_id=d.d_no  ''')

        cursor.execute('''select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,l2.departmentmodel_id as Department ,
d.dep_name as depname from  app1_lecturermodel l1 inner join  
app1_lecturermodel_depname l2  on lecturer_id=l2.lecturermodel_id inner join 
app1_departmentmodel d on l2.departmentmodel_id=d.d_no and d.dep_name='CSE' ''')



        ds=cursor.fetchall()
    return HttpResponse(ds)

def leftJTable(request):
    with connection.cursor() as cursor:
        cursor.execute(''' select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,l2.departmentmodel_id as Department,d.d_no,d.dep_name from app1_lecturermodel as l1 left join  app1_lecturermodel_depname as l2  on  l1.lecturer_id=l2.lecturermodel_id left join app1_departmentmodel d on l2.departmentmodel_id= d.d_no 
 ''')
        ds=cursor.fetchall()
    return HttpResponse(ds)


def rightJTable(request):
    with connection.cursor() as cursor:
        cursor.execute('''select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,d.d_no,d.dep_name from app1_lecturermodel as l1 right join 
app1_lecturermodel_depname as l2  on  l1.lecturer_id=l2.lecturermodel_id right join app1_departmentmodel d on l2.departmentmodel_id= d.d_no 
''')
        ds=cursor.fetchall()
    return HttpResponse(ds)


def fullJTable(request):
    with connection.cursor() as cursor:
        cursor.execute(''' select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,l2.departmentmodel_id as Department,d.d_no,d.dep_name from app1_lecturermodel as l1 full join  app1_lecturermodel_depname as l2  on  l1.lecturer_id=l2.lecturermodel_id full join app1_departmentmodel d on l2.departmentmodel_id= d.d_no ''')
        ds=cursor.fetchall()
    return HttpResponse(ds)



def crossJTable(request):
    with connection.cursor() as cursor:
        cursor.execute(''' select l1.l_name as Name,l1.subject as subject ,l1.clg_id ,d.dep_name from app1_lecturermodel as l1 cross join  app1_departmentmodel d ''')
        ds=cursor.fetchall()
    return HttpResponse(ds)






    


 
