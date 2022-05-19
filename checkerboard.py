from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def one():
    return render_template('checkerboard.html')

@app.route('/4')
def four():
    return render_template('checkerboard2.html')

@app.route('/4/<int:play1>/<int:play2>')
def five(play1, play2):
    return render_template('checkerboard3.html', nun1=play1, nun2=play2)

if __name__== "__main__":
    app.run(debug=True)