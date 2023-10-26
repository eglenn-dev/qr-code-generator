from flask import Flask, render_template, redirect, request
from qr_codes import make_qr_code

app = Flask(__name__, static_url_path='/static', static_folder='static')
qr_code_filename = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/qr')
def qr():
    return render_template('qr.html')

@app.route('/qr-img', methods=['POST'])
def qr_img():
    qr_code_filename = make_qr_code(request.form['urlInput'], request.form['scale'], request.form['borderColor'], request.form['codeColor'], request.form['backgroundColor'])
    return render_template('qr-img.html', qr_code_img_path=qr_code_filename)

if __name__ == '__main__':
    # Runs the app on default port and on broadcasts on all channels.
    # This is done for the live deployment versions of the app. 
    app.run(port=5000, host='0.0.0.0')

    # Runs the app on the local server 127.0.0.1:5001
    # app.run(port=5001, debug=True)

    # Also for debugging purposes
    # app.run(debug=True)