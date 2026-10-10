from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from datetime import date


class Base(DeclarativeBase):
  pass
class customer(Base):
  __tablename__ = "customer"
  customer_id : Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50))
  city: Mapped[str] = mapped_column(String(50)) 
  orders: Mapped[list["order"]] = relationship(back_populates="customer")
  
class agent(Base):
  __tablename__ = "agent"
  agent_id : Mapped[int] = mapped_column(primary_key =True)
  name: Mapped[str] = mapped_column(String(50))
  city: Mapped[str] = mapped_column(String(50))
  orders: Mapped[list["order"]] = relationship(back_populates="agent")
  
class order(Base):
  __tablename__ = "orders"
  order_id : Mapped[int] = mapped_column(primary_key = True)
  customer_id : Mapped[int] = mapped_column(ForeignKey("customer.customer_id"))
  agent_id : Mapped[int] = mapped_column(ForeignKey("agent.agent_id"))
  order_date: Mapped[date]
  delivery_date: Mapped[date | None]
  status: Mapped[str]
  delivery_time: Mapped[int | None]
  amount: Mapped[int]
  customer: Mapped["customer"] = relationship(
        back_populates="orders"
    )

  agent: Mapped["agent"] = relationship(
        back_populates="orders"
    )
