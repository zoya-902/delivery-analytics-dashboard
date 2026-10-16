from sqlalchemy import create_engine, text
from models import Base, agent,customer,order
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from schemas import customerResponse, agentResponse, orderResponse, customerCreate, agentCreate,orderCreate, orderUpdate
from datetime import date
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500",
                   "https://delivery-analytics-frontend.onrender.com", 
                   ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg2://",
        1
    )

engine = create_engine(DATABASE_URL)
print("database_connected")

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind = engine)
def get_db():
  db  = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/customer", response_model= customerResponse)
def create_customer(data: customerCreate, db: Session = Depends(get_db)):
  cust = customer(**data.model_dump())
  db.add(cust)
  db.commit()
  db.refresh(cust)
  return cust

@app.post("/agent", response_model= agentResponse)
def create_agent(data: agentCreate, db: Session = Depends(get_db)):
  ag = agent(**data.model_dump())
  db.add(ag)
  db.commit()
  db.refresh(ag)
  return ag

@app.post("/order", response_model=orderResponse)
def create_order(data : orderCreate, db:Session = Depends(get_db)):
  ord = order(**data.model_dump())
  db.add(ord)
  try:
    db.commit()
  except IntegrityError:
    db.rollback()
    raise HTTPException(
      status_code=409,
      detail="Order violates a database constraint"
    )
  db.refresh(ord)
  return ord

@app.get("/customer/{id}", response_model= customerResponse)
def get_customer(id:int, db: Session = Depends(get_db)):
  customer_obj = db.query(customer).filter(
    customer.customer_id == id
  ).first()
  
  if customer_obj is None:
    raise HTTPException(
      status_code=404,
      detail= "Not Found"
    )
  return customer_obj

@app.get("/agent/{agent_id}", response_model=agentResponse)
def get_agent(agent_id: int, db: Session = Depends(get_db)):
  agent_obj = db.query(agent).filter(
    agent.agent_id == agent_id
  ).first()
  if agent_obj is None:
    raise HTTPException(
      status_code = 404,
      detail = "Not found"
    )
  return agent_obj


@app.get("/order/{order_id}", response_model= orderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
  order_obj = db.query(order).filter(
    order.order_id == order_id
  ).first()
  if order_obj is None:
    raise HTTPException(
      status_code= 404,
      detail="Not Found"
    )
  return order_obj

@app.get("/order", response_model= list[orderResponse])
def get_Allorder(db: Session = Depends(get_db)):
  return db.query(order).all()

@app.get("/customer", response_model= list[customerResponse])
def get_Allcustomer(db: Session = Depends(get_db)):
  return db.query(customer).all()

@app.get("/agent", response_model= list[agentResponse])
def get_Allagent(db: Session = Depends(get_db)):
  return db.query(agent).all()
  

@app.put("/customer/{customer_id}", response_model=customerResponse)
def update_customer(customer_id: int, name: str, city:str, db: Session = Depends(get_db)):
  c_find = db.query(customer).filter(
    customer.customer_id == customer_id
  ).first()
  if c_find is None:
    raise HTTPException(
      status_code=404,
      detail="Not Found"
    )
  c_find.name = name
  c_find.city = city
  db.commit()
  db.refresh(c_find)
  return c_find
  
@app.put("/agent/{agent_id}", response_model=agentResponse)
def update_agent(
    agent_id: int,
    name: str,
    city: str,
    db: Session = Depends(get_db)
):
    a_find = db.query(agent).filter(
        agent.agent_id == agent_id
    ).first()
    if a_find is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    a_find.name = name
    a_find.city = city
    db.commit()
    db.refresh(a_find)
    return a_find
  
@app.patch("/order/{order_id}", response_model=orderResponse)
def update_order(
    order_id: int,
    data: orderUpdate,
    db: Session = Depends(get_db)
):
    o_find = db.query(order).filter(
        order.order_id == order_id
    ).first()
    if o_find is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    if data.delivery_date is not None:
        o_find.delivery_date = data.delivery_date
    if data.status is not None:
        o_find.status = data.status
    if data.delivery_time is not None:
        o_find.delivery_time = data.delivery_time
    if data.amount is not None:
        o_find.amount = data.amount
    db.commit()
    db.refresh(o_find)
    return o_find

@app.delete("/order/{order_id}", response_model=orderResponse)
def del_order(order_id: int, db: Session = Depends(get_db)):
  o_d = db.query(order).filter(
    order.order_id == order_id
  ).first()
  if o_d is None:
    raise HTTPException(
      status_code=404,
      detail="Not Found"
    )
  db.delete(o_d)
  db.commit()
  return o_d

@app.delete("/customer/{customer_id}", response_model=customerResponse)
def del_customer(customer_id: int, db: Session = Depends(get_db)):
    c_d = db.query(customer).filter(
        customer.customer_id == customer_id
    ).first()

    if c_d is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    db.delete(c_d)
    try:
      db.commit()
    except IntegrityError:
      db.rollback()
      raise HTTPException(
        status_code=409,
        detail="Customer has existing order and can't be deleted"
      )
    return c_d

@app.delete("/agent/{agent_id}", response_model=agentResponse)
def del_agent(agent_id: int, db: Session = Depends(get_db)):
    a_d = db.query(agent).filter(
        agent.agent_id == agent_id
    ).first()
    if a_d is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    db.delete(a_d)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Agent has existing orders and can't be deleted"
        )
    return a_d


@app.get("/customer/{customer_id}/orders")
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    c_find = db.query(customer).filter(
        customer.customer_id == customer_id
    ).first()
    if c_find is None:
        raise HTTPException(
            status_code=404,
            detail="Customer Not Found"
        )

    return c_find.orders
  
@app.get("/agent/{agent_id}/orders")
def get_agent_orders(
    agent_id: int,
    db: Session = Depends(get_db)
):
    a_find = db.query(agent).filter(
        agent.agent_id == agent_id
    ).first()
    if a_find is None:
        raise HTTPException(
            status_code=404,
            detail="Agent Not Found"
        )
    return a_find.orders
  
@app.get("/analytics/summary")
def analytics_summary(db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT COUNT(order_id) FROM orders")
    )
    result_revenue = db.execute(
    text("SELECT SUM(amount) FROM orders")
    )
    result_avg = db.execute(
    text("""
        SELECT AVG(delivery_time)
        FROM orders
        WHERE delivery_time IS NOT NULL
    """)
)
    total_revenue = result_revenue.scalar()
    total_orders = result.scalar()
    average_delivery_time = result_avg.scalar()
    return {
        "total_orders": total_orders,
        "total_revenue":total_revenue,
        "average_delivery_time": average_delivery_time
    }


@app.get("/analytics/status")
def analytics_status(db: Session = Depends(get_db)):
    result = db.execute(
        text("""
            SELECT status, COUNT(*) AS total_orders
            FROM orders
            GROUP BY status
            ORDER BY total_orders DESC
        """)
    )
    rows = result.fetchall()
    return [
        {
            "status": row.status,
            "total_orders": row.total_orders
        }
        for row in rows
    ]
    
@app.get("/analytics/cities")
def analytics_cities(db: Session = Depends(get_db)):

    result = db.execute(
        text("""
            SELECT c.city, COUNT(o.order_id) AS total_orders
            FROM customer c
            JOIN orders o
                ON c.customer_id = o.customer_id
            GROUP BY c.city
            ORDER BY total_orders DESC
        """)
    )

    rows = result.fetchall()

    return [
        {
            "city": row.city,
            "total_orders": row.total_orders
        }
        for row in rows
    ]
    
@app.get("/analytics/city-revenue")
def analytics_city_revenue(db: Session = Depends(get_db)):
  result = db.execute(
    text("""
         SELECT c.city, SUM(o.amount) AS total_revenue
          FROM customer c
          JOIN orders o
          ON c.customer_id = o.customer_id
          GROUP BY c.city
          ORDER BY total_revenue DESC
         """)
  )
  rows = result.fetchall()
  
  return[
    {
      "city": row.city,
      "total_revenue": row.total_revenue
    }
    for row in rows
  ]
  
  
  
@app.get("/analytics/agents")
def analytics_agents(db: Session = Depends(get_db)):

    result = db.execute(
        text("""
            SELECT
            a.agent_id,
            a.name,
            COUNT(o.order_id) AS total_orders,
            AVG(o.delivery_time) AS avg_delivery_time
            FROM agent a
            JOIN orders o
            ON a.agent_id = o.agent_id
            GROUP BY a.agent_id, a.name
            ORDER BY total_orders DESC
        """)
    )

    rows = result.fetchall()

    return [
        {
            "agent_id": row.agent_id,
            "name": row.name,
            "total_orders": row.total_orders,
            "avg_delivery_time": row.avg_delivery_time
        }
        for row in rows
    ]
    
@app.get("/analytics/monthly-revenue")
def analytics_monthly_revenue(db: Session = Depends(get_db)):

    result = db.execute(
        text("""
            SELECT
            TO_CHAR(order_date, 'YYYY-MM') AS month,
            SUM(amount) AS total_revenue
            FROM orders
            GROUP BY TO_CHAR(order_date, 'YYYY-MM')
            ORDER BY month
        """)
    )

    rows = result.fetchall()

    return [
        {
            "month": row.month,
            "total_revenue": row.total_revenue
        }
        for row in rows
    ]