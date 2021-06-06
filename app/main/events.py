from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import  requests


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    # emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):

    dat = {
        "sender":"GH2117241972",
        "receiver":"GH1427453171",
        "message":"microservices trying here.",
        "attached_file":None,
    }
    data = requests.post("http://127.0.0.1:8000/chatsystem/message/", dat)
    print(data.status_code)
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    # emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

