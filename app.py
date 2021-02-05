from flask import Flask , render_template, request,redirect, flash , url_for
import smtplib, ssl

app = Flask(__name__)
app.config['SECRET_KEY']= 'e4c1df590ecea9fd104c33bc39d52412'

@app.route('/')
def home():
    return render_template('Assoc_web_home.html')

@app.route('/about')
def about():
    return render_template('Assoc_web_about.html')

@app.route('/contact')
def contact():
    return render_template('Assoc_web_contact.html')

@app.route('/join')
def join(): 
    return render_template('Assoc_web_join.html')

@app.route('/join/join-status',methods = ['POST', 'GET'])
def joinstatus(): 
    # if request.method == 'POST':
    #     formdetails =request.form
    #     port = 465  # For SSL
    #     smtp_server = "smtp.gmail.com"
    #     sender_email = "mathsfirstperson@gmail.com"  # Enter your address
    #     receiver_email = "mathssecondperson@gmail.com"  # Enter receiver address
    #     password = "maths1234"
    #     message = """\
    #     Subject: Joining details Mathematics Association, BITS Pilani

    #     Name : {name}
    #     BITS ID : {id}
    #     Contact No : {no}
    #     BITS Email : {mail}""".format(name=formdetails["Name"],id=formdetails["BITS ID"],no=formdetails["Contact Number"],mail=formdetails["BITS Email"])
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message)
    return render_template("Join-status.html")
        
        
if __name__ =='__main__':
    app.run(debug=True)





