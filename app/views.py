import json

from flask import jsonify, request

from app import app
from app.db import db_session
from app.models import Message
from app.schemas import MessageSchema
from marshmallow import ValidationError


def return_non_success_json(status_code, data):
    return app.response_class(
        response=json.dumps(data),
        status=status_code,
        mimetype='application/json'
    )


@app.route('/api/create')
def create_view():
    json_data = request.get_json()
    if not json_data:
        return return_non_success_json(400, {'message': 'No input data provided'})

    # Validate and deserialize input
    message_schema = MessageSchema(only=('recipient_address', 'sender_address', 'subject', 'body'))
    try:
        data = message_schema.load(json_data)
    except ValidationError as err:
        return return_non_success_json(422, err.messages)

    message = Message(**data.data)
    db_session.add(message)
    db_session.flush()
    db_session.commit()

    return jsonify({'messages': 'ok'})
