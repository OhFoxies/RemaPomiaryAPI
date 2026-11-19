from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, String, Boolean, Integer, Text

from models.order_items import OrderItems
from models.user import User
from datetime import datetime
from core.database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    status: Mapped[str] = mapped_column(String(255))


    date: Mapped[datetime] = mapped_column(DateTime)
    order_total: Mapped[int] = mapped_column(Integer)

    user: Mapped["User"] = relationship(
        back_populates="orders"
    )

    order_items: Mapped[list[OrderItems]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
