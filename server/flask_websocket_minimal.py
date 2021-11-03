from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

@socketio.on('cliMsg')
def handle_rev_cli_msg(data):
    print('cliMsg')
    print(data)

@socketio.on('emitSrvMsg')
def handle_emit_srv_msg():
    print('emitSrvMsg')
    socketio.emit('srvMsg', "OK")



# if __name__ == '__main__':
    # socketio.run(app)