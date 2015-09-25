from flask import Flask, render_template, Response,send_file, request, session, redirect, url_for
import camera
import flask_httpauth
import config
import os
import io
import threading
import time
import hashlib
import logging
import datetime
import ssl

app = Flask(__name__)
conf = config.Configuration()
logging.basicConfig(filename='app.log',level=logging.DEBUG)
auth = flask_httpauth.HTTPBasicAuth()
app.secret_key = os.urandom(24)
user = None
online = None
cmra = camera.VideoCamera(conf)
import cloud
drop = cloud.DropObj(conf)
@auth.get_password
def get_pw(username):
    global user
    user = username
    return conf.get('User')[username]

@auth.hash_password
def hash_pw(password):
    return hashlib.sha224(password).hexdigest()

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    cloud = False
    auth = False
    error = ''
    if request.method == 'POST':
        key = request.form['code']
        drop.auth(key)
        dropbox = '#'
    else:
        dropbox = drop.get_website()
        if conf.get('Cloud')['token'] == 'none':
            error = "You need to register your dropbox account first, go to settings tab."
        if request.args.get('options') == 'record':
            if request.args.has_key('cloud'):
                cloud = True
            recording = threading.Thread(target=cmra.record,args=[cloud,drop] )
            recording.start()
            session['options'] = 'record'
            return '<IMG id="bg"  SRC="/video_feed_record" width="320" height="240" >'


    return render_template('index.html', online = online, dropbox = dropbox, error = error)

def gen(camera, save=False, vstart=False):
    while True:

        frame = camera.get_frame(False,save,vstart)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/audio', methods=['POST'])
@auth.login_required
def audio():
    file = request.files['edition[audio]']
    file.save("audio.wav")
    cmra.playAudio()
    return ('', 204)
@app.route('/video_feed')
@auth.login_required
def video_feed():
    if 'options' in session:
        if session['options'] == 'record':
            return Response(gen(cmra,False,True),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response(gen(cmra),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_record')
@auth.login_required
def video_feed2():
    return Response(gen(cmra,False,True),
                mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_frame')
@auth.login_required
def get_frame():
    frame = cmra.get_frame(False)
    if request.args.get('options') == 'save':
        timestr = time.strftime("%Y%m%d-%H%M%S")
        f = open(conf.get('File')['photos'] + 'image' + timestr +'.jpg', 'wb')
        f.write(frame)
        logging.info('Snapshot taken at  ' + str(datetime.datetime.now()))
        return ('', 204)
    return send_file(io.BytesIO(frame))
    
@app.route('/stopV')
@auth.login_required
def stopV():
    session.pop('options',None)
    cmra.endVideo()
    return '<IMG id="bg"  SRC="/video_feed" width="320" height="240" >'
    
@app.route('/toggle_online',methods=['POST'])
@auth.login_required
def toggle_online():
    global online
    if 'submit' in request.form:
        cmra.online = True
        return redirect(url_for('index'))
    sens = int(request.form['sensitive'])
    method = request.form['method']
    sound = True if 'chk-sound' in request.form else False
    mail = True if 'chk-mail' in request.form else False
    notify = True if 'chk-not' in request.form else False
    online = threading.Thread(target=cmra.start, args=[sens, method, mail, sound, notify])
    online.start()
    return redirect(url_for('index'))

if __name__ == "__main__":
    if conf.boolean('Connection','https'):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(conf.get('Connection')['certificate'], conf.get('Connection')['key'])
        app.run(threaded=True,host=conf.get('Connection')['ip'], port=int(conf.get('Connection')['port']) ,ssl_context=context)
    else:
        app.run(threaded=True,host=conf.get('Connection')['ip'], port=int(conf.get('Connection')['port']))
