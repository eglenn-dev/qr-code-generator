from flask import Flask, render_template, redirect, request
from qr_codes import make_qr_code

app = Flask(__name__, static_url_path='/static', static_folder='static')
qr_code_filepath = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/qr')
def qr():
    return render_template('qr.html')

@app.route('/qr-img', methods=['POST'])
def qr_img():
    try:
        qr_code_filepath = make_qr_code(url=request.form['urlInput'], scale=request.form['scale'], background=request.form['backgroundColor'], code_color=request.form['codeColor'], border_color=request.form['borderColor'])
        return render_template('qr-img.html', qr_code_img_path=qr_code_filepath)
    except:
        return render_template('error.html')

@app.route('/<short_url>')
def page_not_found(short_url):
    return render_template('404.html', short_url=short_url)

if __name__ == '__main__':
    # Runs the app on default port and on broadcasts on all channels.
    # This is done for the live deployment versions of the app. 
    app.run(port=5000, host='0.0.0.0')

    # Runs the app on the local server 127.0.0.1:5001
    # app.run(port=5001, debug=True)

    # Also for debugging purposes. Will run on 127.0.0.1:5000 if available.
    # app.run(debug=True)