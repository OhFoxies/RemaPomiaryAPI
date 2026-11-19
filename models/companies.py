from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime

from datetime import datetime
from core.database import Base
from models.user import User


class Company(Base):
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str] = mapped_column(String(255))
    nip: Mapped[str] = mapped_column(String(255))
    street: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(255))
    postal_code: Mapped[str] = mapped_column(String(255))

    users: Mapped[list["User"]] = relationship(back_populates="company")
