from flask import Blueprint, request, jsonify
from be.models.Notification import Notification,NotificationType
from be.models.User import User
from be.models import db
from flask_jwt_extended import jwt_required, current_user
from be.utils.socketio import socketio
from be.utils.jwt import role


notify_blu = Blueprint('notify',__name__)



@notify_blu.get('/activateUser')
@role('Admin')
def activateUser():
    user_id=request.args.get("id")
    user=User.query.filter_by(id=user_id).first()
    user.active=True
    notification=Notification.query.filter_by(belongToId=user.id,type=NotificationType.VerifyUser).first()
    notification_id=notification.id
    db.session.delete(notification)
    db.session.commit()
    socketio.emit('deleteNotification',[notification_id,])

    return "blahblah",200

@notify_blu.get('/studentApproval')
@role('Lecturer')
def studentApproval():
    student_id=request.args.get("id")
    student=User.query.filter_by(id=student_id).first()
    current_user.students.append(student)
    notification=Notification.query.filter_by(belongToId=student.id,type=NotificationType.VerifyStudent).first()
    notification_id=notification.id
    db.session.delete(notification)
    db.session.commit()
    socketio.emit('deleteNotification',[notification_id,])

    return "blahblah",200

@notify_blu.get('/dismiss')
@jwt_required()
def dismiss_notification():
    nft_id=request.args.get("id",type=int)
    notification=Notification.query.filter_by(id=nft_id).first()
    notification_id=notification.id
    db.session.delete(notification)
    db.session.commit()
    socketio.emit('deleteNotification',[notification_id,])

    return "blahblah",200


@notify_blu.get('/load-all')
@jwt_required()
def load_notifications():
    notifications=[n.to_json() for n in current_user.notifications]
    return jsonify(notifications),200   


