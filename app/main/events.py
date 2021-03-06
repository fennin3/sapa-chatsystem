from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import  requests


@socketio.on('joined', namespace='/chat')
def joined(message):
    print(message)
    receiver = message['receiver']
    sender = message['sender']
    room = message['room']
    session['room'] = room

    
    # setting messages to read once the receiver join the websocket...
    # data = requests.post(f"http://127.0.0.1:8000/general/set-unread-messages-to-read/{receiver}/{sender}/")
    # print(data.status_code)
    
    # room = session.get('room')
    join_room(room)
    # emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):


    # # Saving sent message back to SAPA main Database
    # data = requests.post("http://127.0.0.1:8000/chatsystem/message/", message)


    # print(data.status_code)
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    # emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

