"""
Routes and views for the flask application.
"""
import mysql.connector
from datetime import datetime
#from flask import render_template
from HMSWeb import app
from flask import Flask, render_template, request
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import render_template
from HMSWeb import app
#mysql.connector datavase connection
msqldb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="hms"
)
sqlcursor = msqldb.cursor()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Patient')
def Patient():
    """Renders the about page."""
    return render_template(
        'Patient.html',
        title='Patient',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Staff')
def Staff():
    """Renders the about page."""
    return render_template(
        'Staff.html',
        title='Staff',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Payment')
def Payment():
    """Renders the about page."""
    return render_template(
        'Payment.html',
        title='Payment',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/Search')
def Search():
    """Renders the about page."""
    return render_template(
        'Search.html',
        title='Payment',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/Appointment')
def Appointment():
    """Renders the about page."""
    return render_template(
        'Appointment.html',
        title='Appointment',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/patientmedicin')
def patientmedicin():
    """Renders the about page."""
    return render_template(
        'patientmedicin.html',
        title='patientmedicin',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/SearchP')
def SearchP():
    """Renders the about page."""
    return render_template(
        'SearchP.html',
        title='SearchP',
        year=datetime.now().year,
        message='Your application description page.'
    )



@app.route('/lab')
def lab():
    """Renders the about page."""
    return render_template(
        'lab.html',
        title='lab',
        year=datetime.now().year,
        message='Your application description page.'
    )

#Staff registration page
@app.route('/Staff_registration', methods=['GET', 'POST'])
def Staff_registration():
    if request.method == 'POST':
        Staff_number = request.form['Staff_number']
        Staff_firstname = request.form['Staff_firstname']
        Staff_lastname = request.form['Staff_lastname']
        DOJ = request.form['DOJ']
        Designation = request.form['Designation']
        mobile = request.form['mobile']
        Address = request.form['Address']
        sql = "INSERT INTO Staff (Staff_number, Staff_firstname, Staff_lastname, DOJ, Designation, mobile, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (Staff_number, Staff_firstname, Staff_lastname, DOJ, Designation, mobile, Address)
        sqlcursor.execute(sql, val)
        msqldb.commit()
        return redirect(url_for('Staff_registration'))
    return render_template('index.html')


#flask route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        PatientID = request.form['PatientID']
        Appointmentdate = request.form['Appointmentdate']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        MobileNumber = request.form['MobileNumber']
        city = request.form['city']
        address = request.form['address']
        state = request.form['state']
        sql = "INSERT INTO patient (PatientID, AppoinmentDate, FirstName, LastName, MobileNumber, city, address, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (PatientID, Appointmentdate, FirstName, LastName, MobileNumber, city, address, state)
        sqlcursor.execute(sql, val)
        msqldb.commit()
        return redirect(url_for('register'))
    return render_template('index.html')



#Staff registration page
@app.route('/Paymentregister', methods=['GET', 'POST'])
def Paymentregister():
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
      
        return redirect(url_for('Paymentregister'))
    return render_template('index.html')





@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        AppointmentID = request.form['AppointmentID']
        Appointmentdate = request.form['Appointmentdate']
        Appointmenttime = request.form['Appointmenttime']
        DoctorID = request.form['DoctorID']
        Visit = request.form['Visit']
        Status = request.form['Status']
        
        sql ="INSERT INTO appointment(AppointmentID,Appointmentdate,Appointmenttime,DoctorID,Visit,Status) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (AppointmentID, Appointmentdate, Appointmenttime, DoctorID, Visit, Status)
        sqlcursor.execute(sql, val)
        msqldb.commit()

        return redirect(url_for('appointment'))
    return render_template('index.html')




@app.route('/patientmedicinreg', methods=['GET', 'POST'])
def patientmedicinreg():
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

        return render_template('index.html')
    return render_template('index.html')


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
            
            return render_template('index.html')
        else:
            return 'Error while inserting'


@app.route('/searchDoctor', methods=['POST', 'GET'])
def searchDoctor():
    if request.method == 'POST':
        Doctor_number = request.form['Doctor_number']
        msqldb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="root",
          database="hms"
        )
        sqlcursor = msqldb.cursor()
        #cur = conn.cursor
        sql="SELECT * FROM Doctor WHERE Doctor_number = " + Doctor_number
        sqlcursor.execute(sql)
        data = sqlcursor.fetchall()
        return render_template("searchDoctor.html", data=data)
    return render_template("searchDoctor.html")


@app.route('/searchPatient', methods=['POST', 'GET'])
def searchPatient():
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
        return render_template("SearchPatient.html", data=data)
    return render_template("searchDoctor.html")