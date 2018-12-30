from sqlalchemy import Column, DateTime, Integer, String, Text
from app.db import Base


class Message(Base):
    """Class representing a single message to be sent."""

    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    recipient_address = Column(String(80), nullable=False)
    sender_address = Column(String(80), nullable=False)
    subject = Column(String(80), nullable=False)
    body = Column(Text, nullable=False)
    sent = Column(DateTime, nullable=True)

    def __repr__(self):
        """Return a readable version of the message contents."""
        return 'Message: {} | {} --> {} | {}'.format(
            self.id, self.sender_address, self.recipient_address, self.subject)
