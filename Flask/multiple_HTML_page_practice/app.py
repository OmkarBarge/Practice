from flask import Flask ,render_template, request

app = Flask(__name__)


############################################

@app.route('/')
def index_function():
    return render_template('index.html')


@app.route('/thankyou', methods=['POST'])
def thanku_function():
    name = request.form['in_1']
    age = int(request.form['in_2'])
    return render_template('thankyou.html',name=name,age=age)

@app.route('/contact_us')
def contact_function():
    return render_template('contact.html')

@app.route('/about-us')
def about_function():
    return render_template('about.html')

#############################################


if __name__ == '__main__':
    app.run(debug=True)