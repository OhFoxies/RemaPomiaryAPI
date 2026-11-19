from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, String, Boolean, Integer, Text

from models.license_product import LicenseProduct
from models.order import Order
from datetime import datetime
from core.database import Base


class OrderItems(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id")
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("licenses_products.id")
    )

    quantity: Mapped[int] = mapped_column(Integer)
    unit_price: Mapped[int] = mapped_column(Integer)

    order: Mapped["Order"] = relationship(
        back_populates="order_items"
    )

    products: Mapped["LicenseProduct"] = relationship()