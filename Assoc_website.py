from flask import Flask , render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('WebsiteF.html')

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
    if request.method == 'POST':
        result =request.form
        return render_template("join_data.html",result = result)
 
if __name__ =='__main__':
    app.run(debug=True)





