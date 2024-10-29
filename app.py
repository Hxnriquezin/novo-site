from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('site.html')
@app.route('/site')
def site():
    return render_template('site.html')
if __name__ =='__main__':
    app.run(debug=True)