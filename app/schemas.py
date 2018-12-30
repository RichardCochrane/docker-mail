from marshmallow import Schema, fields


class MessageSchema(Schema):
    """Schema representing contractual presentation/validation of ExerciseSummary data."""

    id = fields.Int(dump_only=True)
    recipient_address = fields.Str()
    sender_address = fields.Str()
    subject = fields.Str()
    body = fields.Str()
    sent = fields.DateTime()
