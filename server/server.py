from flask import Flask,request,render_template,url_for
app = Flask(__name__)
app.stacic_folder = 'static'

@app.route('/')
def re_route():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fever')
def fever_page():
    return render_template('temperature_trends.html')

@app.route('/ovulation')
def ovulation():
    return render_template('ovulation_trends.html')

if __name__ == '__main__':
  app.run(debug=True)
