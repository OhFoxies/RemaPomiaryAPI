from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime

from datetime import datetime
from core.database import Base
from models.license import License
from models.companies import Company
from models.order import Order


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))
    role: Mapped[str] = mapped_column()

    licenses: Mapped[list["License"]] = relationship(back_populates="user")

    company: Mapped["Company"] = relationship(back_populates="users")

    orders: Mapped[list['Order']] = relationship(back_populates="user")