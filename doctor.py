from flask import Flask, render_template, request

import pymysql
app = Flask(__name__)
# Database connection
conn = pymysql.connect(host='localhost', user='root', password='root', db='hms')
a = conn.cursor()
# Staff registration page
@app.route('/Staff_registration', methods=['POST', 'GET'])
def Staff_registration():
    if request.method == 'POST':
        try:
            Staff_number = request.form['Staff_number']
            Staff_firstname = request.form['Staff_firstname']
            Staff_lastname = request.form['Staff_lastname']
            DOJ = request.form['DOJ']
            Designation = request.form['Designation']
            mobile = request.form['mobile']
            Address = request.form['Address']
            a.execute("INSERT INTO Staff (Staff_number, Staff_firstname, Staff_lastname, DOJ, Designation, mobile, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Staff_number, Staff_firstname, Staff_lastname, DOJ, Designation, mobile, Address))
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("staff_registration.html", msg=msg)
            
conn.close()