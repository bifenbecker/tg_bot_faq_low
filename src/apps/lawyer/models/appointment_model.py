import sqlalchemy as sa

from src.core.orm import Base


class AppointmentModel(Base):
    __tablename__ = "appointments"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    question = sa.Column(sa.String)
    time = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
