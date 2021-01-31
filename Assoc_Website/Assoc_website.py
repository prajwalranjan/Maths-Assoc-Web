from flask import Flask , render_template
app = Flask(__name__)

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

if __name__ =='__main__':
    app.run(debug=True)





