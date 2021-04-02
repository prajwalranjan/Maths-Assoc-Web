from flask import Flask, render_template, request, redirect, flash, url_for
import smtplib
import ssl
from flask_mail import Mail, Message
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = Flask(__name__)
app.config.from_object('config.Config')
mail = Mail(app)


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


@app.route('/contact/contact-status', methods=['POST', 'GET'])
def contactstatus():
    if request.method == 'POST':
        formdetails = request.form

        message = Mail(
            from_email='mathsfirstperson@gmail.com',
            # to_emails='mathssecondperson@gmail.com',
            to_emails='maths.assoc@pilani.bits-pilani.ac.in',
            subject='Contact Details, MABP Website',
            plain_text_content="""\
                Name : {name}
                Mail : {mail}
                Contact No : {no}
                Message : {message}""".format(name=formdetails["name"], mail=formdetails["mail"], no=formdetails["mobile"], message=formdetails["message"]))
        try:
            sg = SendGridAPIClient(
                app.config["SENDGRID_API_KEY"])
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

        # # using python mailing
        # port = 465  # For SSL
        # smtp_server = "smtp.gmail.com"
        # sender_email = "mathsfirstperson@gmail.com"  # Enter your address
        # receiver_email = "maths.assoc@pilani.bits-pilani.ac.in"  # Enter receiver address
        # password = "maths1234"
        # message = """\
        # Subject: Contact details Mathematics Association, BITS Pilani

        # Name : {name}
        # Mail : {mail}
        # Contact No : {no}
        # Message : {message}""".format(name=formdetails["name"], mail=formdetails["mail"], no=formdetails["mobile"], message=formdetails["message"])
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #     server.login(sender_email, password)
        #     server.sendmail(sender_email, receiver_email, message)
    return redirect(url_for("home"))


@ app.route('/join/join-status', methods=['POST', 'GET'])
def joinstatus():
    if request.method == 'POST':
        formdetails = request.form

        message = Mail(
            from_email='mathsfirstperson@gmail.com',
            # to_emails='mathssecondperson@gmail.com',
            to_emails='maths.assoc@pilani.bits-pilani.ac.in',
            subject='Maths-Assoc Recruitment, MABP Website',
            plain_text_content="""\
                Name : {name}
                BITS ID : {id}
                Contact No : {no}
                BITS Email : {mail}""".format(name=formdetails["name"], id=formdetails["BITS ID"], no=formdetails["mobile"], mail=formdetails["mail"]))
        try:
            sg = SendGridAPIClient(
                app.config["SENDGRID_API_KEY"])
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

    return redirect(url_for("home"))

    # # Using Flask Mail
    # msg = Message('Joining details Mathematics Association, BITS Pilani',
    #               sender='mathsfirstperson@gmail.com', recipients=['mathssecondperson@gmail.com'])
    # msg.body = """\
    # Name : {name}
    # BITS ID : {id}
    # Contact No : {no}
    # BITS Email : {mail}""".format(name=formdetails["name"], id=formdetails["BITS ID"], no=formdetails["mobile"], mail=formdetails["mail"])
    # mail.send(msg)
    # return redirect(url_for("home"))

    # # Using python mailing
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
    #     BITS Email : {mail}""".format(name=formdetails["name"], id=formdetails["BITS ID"], no=formdetails["mobile"], mail=formdetails["mail"])
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message)
    # return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
