from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, String, Boolean, Integer, Text
from models.user import  User
from datetime import datetime
from core.database import Base
class LicenseProduct(Base):
    __tablename__ = "licenses_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    amount_of_licenses: Mapped[int] = mapped_column(Integer)