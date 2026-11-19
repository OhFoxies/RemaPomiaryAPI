from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, String, Boolean
from models.user import  User
from datetime import datetime
from core.database import Base
class License(Base):
    __tablename__ = "licenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    expiry_date: Mapped[datetime] = mapped_column(DateTime)
    is_activated: Mapped[bool] = mapped_column(Boolean)
    device: Mapped[str] = mapped_column(String(255))
    license_code: Mapped[str] = mapped_column(String(255))
    user: Mapped["User"] = relationship(
        back_populates="licenses"
    )