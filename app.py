from flask import Flask , render_template, request,redirect, flash , url_for
import smtplib, ssl

app = Flask(__name__)
app.config['SECRET_KEY']= 'e4c1df590ecea9fd104c33bc39d52412'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def members():
    return render_template('web-members.html')

@app.route('/event')
def event():
    return render_template('web-events.html')

@app.route('/apogee')
def apogee():
    return render_template('apogee.html')

@app.route('/amo')
def amo():
    return render_template('amo.html')

@app.route('/b4mo')
def b4mo():
    return render_template('b4mo.html')

@app.route('/symposium')
def symposium():
    return render_template('symposium.html')

@app.route('/teachersday')
def teachersday():
    return render_template('teachersday.html')

@app.route('/volleyball')
def volleyball():
    return render_template('volleyball.html')

@app.route('/contact')
def contact():
    return render_template('web-contactus.html')

@app.route('/join')
def join(): 
    return render_template('web-joinus.html')

@app.route('/contact/contact-status',methods = ['POST', 'GET'])
def contactstatus(): 
    if request.method == 'POST':
        formdetails =request.form
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "mathsfirstperson@gmail.com"  # Enter your address
        receiver_email = "mathssecondperson@gmail.com"  # Enter receiver address
        password = "maths1234"
        message = """\
        Subject: Contact details Mathematics Association, BITS Pilani

        Name : {name}
        Mail : {mail}
        Contact No : {no}
        Message : {message}""".format(name=formdetails["name"],mail=formdetails["mail"],no=formdetails["mobile"],message=formdetails["message"])
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    return redirect(url_for("home"))

@app.route('/join/join-status',methods = ['POST', 'GET'])
def joinstatus(): 
    if request.method == 'POST':
        formdetails =request.form
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "mathsfirstperson@gmail.com"  # Enter your address
        receiver_email = "mathssecondperson@gmail.com"  # Enter receiver address
        password = "maths1234"
        message = """\
        Subject: Joining details Mathematics Association, BITS Pilani

        Name : {name}
        BITS ID : {id}
        Contact No : {no}
        BITS Email : {mail}""".format(name=formdetails["name"],id=formdetails["BITS ID"],no=formdetails["mobile"],mail=formdetails["mail"])
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    return redirect(url_for("home"))
        
        
if __name__ =='__main__':
    app.run(debug=True)





