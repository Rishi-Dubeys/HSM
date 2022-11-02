"""
Routes and views for the flask application.
"""
import mysql.connector
from datetime import datetime
#from flask import render_template
from flask import Flask, render_template, request, redirect, url_for
from HMSWeb import app
#mysql.connector datavase connection
msqldb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password1234",
  database="hms"
)
sqlcursor = msqldb.cursor()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year
    )


@app.route('/patientscreen')
def patientscreen():
    """Renders the about page."""
    return render_template(
        'patientscreen.html',
        title='Patient',
        year=datetime.now().year,
        message='Your application description page.'
    )




@app.route('/billing')
def billing():
    """Renders the about page."""
    return render_template(
        'billing.html',
        title='Payment',
        year=datetime.now().year,
        message='Your application description page.'
    )


# @app.route('/Search')
# def Search():
#     """Renders the about page."""
#     return render_template(
#         'Search.html',
#         title='Payment',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )


# @app.route('/Appointment')
# def Appointment():
#     """Renders the about page."""
#     return render_template(
#         'Appointment.html',
#         title='Appointment',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )

@app.route('/medicines')
def medicines():
    """Renders the about page."""
    return render_template(
        'medicines.html',
        title='medicines',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/search_patient')
def search_patient():
    """Renders the about page."""
    return render_template(
        'search_patient.html',
        title='SearchP',
        year=datetime.now().year,
        message='Your application description page.'
    )



# @app.route('/lab')
# def lab():
#     """Renders the about page."""
#     return render_template(
#         'lab.html',
#         title='lab',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )

# #Staff registration page
# @app.route('/staff_registration', methods=['GET', 'POST'])
# def staff_registration():
#     if request.method == 'POST':
#         Staff_number = request.form['Staff_number']
#         Staff_firstname = request.form['Staff_firstname']
#         Staff_lastname = request.form['Staff_lastname']
#         DOJ = request.form['DOJ']
#         Designation = request.form['Designation']
#         mobile = request.form['mobile']
#         Address = request.form['Address']
#         sql = "INSERT INTO Staff (Staff_number, Staff_firstname, Staff_lastname, DOJ, Designation, mobile, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         val = (Staff_number, Staff_firstname, Staff_lastname, DOJ, Designation, mobile, Address)
#         sqlcursor.execute(sql, val)
#         msqldb.commit()
#         return redirect(url_for('staff_registration'))
#     return render_template('home.html')


#flask route for registration page
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         PatientID = request.form['PatientID']
#         Appointmentdate = request.form['Appointmentdate']
#         FirstName = request.form['FirstName']
#         LastName = request.form['LastName']
#         MobileNumber = request.form['MobileNumber']
#         city = request.form['city']
#         address = request.form['address']
#         state = request.form['state']
#         sql = "INSERT INTO patient (PatientID, AppoinmentDate, FirstName, LastName, MobileNumber, city, address, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         val = (PatientID, Appointmentdate, FirstName, LastName, MobileNumber, city, address, state)
#         sqlcursor.execute(sql, val)
#         msqldb.commit()
#         return redirect(url_for('register'))
#     return render_template('home.html')



@app.route('/generatebill', methods=['GET', 'POST'])
def generatebill():
    if request.method == 'POST':
        ReceptionNo = request.form['ReceptionNo']
        PatientID = request.form['PatientID']
        PaymentDate = request.form['PaymentDate']
        PaymentWith = request.form['PaymentWith']
        Amount = request.form['Amount']
        sql = "INSERT INTO Payment(ReceptionNo,PatientID,PaymentDate,PaymentWith,Amount) VALUES (%s, %s, %s, %s, %s)"
        val = (ReceptionNo,PatientID,PaymentDate,PaymentWith,Amount)
        sqlcursor.execute(sql, val)
        msqldb.commit()

       # cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO Payment(ReceptionNo,PatientID,PaymentDate,PaymentWith,Amount) VALUES (%s, %s, %s, %s, %s)", (ReceptionNo,PatientID,PaymentDate,PaymentWith,Amount))
        #mysql.connection.commit()
      
        return redirect(url_for('generatebill'))
    return render_template('home.html')





# @app.route('/appointment', methods=['GET', 'POST'])
# def appointment():
#     if request.method == 'POST':
#         AppointmentID = request.form['AppointmentID']
#         Appointmentdate = request.form['Appointmentdate']
#         Appointmenttime = request.form['Appointmenttime']
#         DoctorID = request.form['DoctorID']
#         Visit = request.form['Visit']
#         Status = request.form['Status']
        
#         sql ="INSERT INTO appointment(AppointmentID,Appointmentdate,Appointmenttime,DoctorID,Visit,Status) VALUES (%s, %s, %s, %s, %s, %s)"
#         val = (AppointmentID, Appointmentdate, Appointmenttime, DoctorID, Visit, Status)
#         sqlcursor.execute(sql, val)
#         msqldb.commit()

#         return redirect(url_for('appointment'))
#     return render_template('home.html')


# @app.route('/patientmedicinreg', methods=['GET', 'POST'])
# def patientmedicinreg():
#     if request.method == 'POST':
#         ID = request.form['ID']
#         DoctorID = request.form['DoctorID']
#         PatientID = request.form['PatientID']
#         MedicinDetail = request.form['MedicinDetail']
#         NextVisit = request.form['NextVisit']
        
#         sql="INSERT INTO patientmedicin(ID, DoctorID, PatientID, MedicinDetail, NextVisit) VALUES (%s, %s, %s, %s, %s)"
#         val=(ID, DoctorID, PatientID, MedicinDetail, NextVisit)
#         sqlcursor.execute(sql, val)
#         msqldb.commit()

#         return render_template('home.html')
#     return render_template('home.html')

@app.route('/create_patient', methods=['GET', 'POST'])
def create_patient():
    if request.method == 'POST':
        ID = request.form['ID']
        DoctorID = request.form['DoctorID']
        PatientID = request.form['PatientID']
        MedicinDetail = request.form['MedicinDetail']
        NextVisit = request.form['NextVisit']
        
        sql="INSERT INTO patientmedicin(ID, DoctorID, PatientID, MedicinDetail, NextVisit) VALUES (%s, %s, %s, %s, %s)"
        val=(ID, DoctorID, PatientID, MedicinDetail, NextVisit)
        sqlcursor.execute(sql, val)
        msqldb.commit()

        return render_template('create_patient.html')
    return render_template('home.html')

    
@app.route('/staff_registration', methods=['GET', 'POST'])
def staff_registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        country = request.form['country']
        cursor = msqldb.cursor()
        cursor.execute("INSERT INTO registration(username, password, email, phone, address, city, state, zip, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (username, password, email, phone, address, city, state, zip, country))
        msqldb.commit()
        cursor.close()
        return redirect(url_for('staff_registration'))
    return render_template('staff_registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        cursor = msqldb.cursor()
        msql="SELECT * FROM registration WHERE username = '" + user +  "' and password= '" + password + "'"  
        cursor.execute(msql)
        account = cursor.fetchone()
        if account:
            msg = 'Logged in successfully !'
            return render_template('Home.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html')


@app.route('/labreg', methods=['GET', 'POST'])
def labreg():
    if request.method == 'POST':
        ID = request.form['ID']
        PatientID = request.form['PatientID']
        DoctorID = request.form['DoctorID']
        Test = request.form['Test']
        BillAmount = request.form['BillAmount']
        Billdate = request.form['Billdate']
        if ID and PatientID and DoctorID and Test and BillAmount and Billdate:
             
            sql="INSERT INTO lab(ID,PatientID,DoctorID,Test,BillAmount,Billdate) VALUES(%s, %s, %s, %s, %s, %s)"
            val=(ID, PatientID, DoctorID, Test, BillAmount, Billdate)
            sqlcursor.execute(sql, val)
            msqldb.commit()
            
            return render_template('home.html')
        else:
            return 'Error while inserting'


# @app.route('/searchDoctor', methods=['POST', 'GET'])
# def searchDoctor():
#     if request.method == 'POST':
#         Doctor_number = request.form['Doctor_number']
#         msqldb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           passwd="root",
#           database="hms"
#         )
#         sqlcursor = msqldb.cursor()
#         #cur = conn.cursor
#         sql="SELECT * FROM Doctor WHERE Doctor_number = " + Doctor_number
#         sqlcursor.execute(sql)
#         data = sqlcursor.fetchall()
#         return render_template("searchDoctor.html", data=data)
#     return render_template("searchDoctor.html")


@app.route('/search_Patient', methods=['POST', 'GET'])
def search_Patient():
    if request.method == 'POST':
        PatientID = request.form['PatientID']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        msqldb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="root",
          database="hms"
        )
        sqlcursor = msqldb.cursor()
       
        sql="SELECT * FROM patient WHERE PatientID = " + PatientID +  " or FirstName= '" + FirstName + "' or LastName= '" + LastName + "'"
        sqlcursor.execute(sql)
        data = sqlcursor.fetchall()
        return render_template("search_patient.html", data=data)