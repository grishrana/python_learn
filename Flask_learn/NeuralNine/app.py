from flask import Flask, render_template,redirect ,url_for

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    myvalue="Grish Rana"
    myresult = 399
    mylist = [10,20,30]
    return render_template('index.html',mylist=mylist)

@app.route('/otherpage')
def otherpage():
    some_text="Hello World"
    return render_template('otherpage.html',some_text=some_text)

@app.route('/redirectToOtherpage')
def redirectToOtherpage():
    return redirect(url_for('otherpage'))


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=2):
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i%2 == 0 else c.lower() for i,c in enumerate(s)])

if(__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5555, debug=True)
