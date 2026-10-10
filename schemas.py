from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from typing import Literal

class customerResponse(BaseModel):
  customer_id:int
  name:str
  city:str
  model_config = ConfigDict(from_attributes = True)
  
class agentResponse(BaseModel):
  agent_id:int
  name:str
  city:str
  model_config = ConfigDict(from_attributes = True)
  
class orderResponse(BaseModel):
  order_id: int
  customer_id: int
  agent_id: int
  order_date: date 
  delivery_date: date | None
  status: str
  delivery_time: int | None
  amount:int
  model_config = ConfigDict(from_attributes= True)
  
class customerCreate(BaseModel):
  name : str
  city: str

class agentCreate(BaseModel):
  name: str
  city: str

class orderCreate(BaseModel):
  customer_id: int
  agent_id: int
  order_date: date 
  delivery_date: date | None = None
  status: Literal["Pending", "Out for Delivery", "Delivered", "Cancelled", "Delayed"]
  delivery_time: int | None = Field(gt =0)
  amount:int = Field(gt=0)
  
class orderUpdate(BaseModel):
    delivery_date: date | None = None
    status: Literal[
        "Pending",
        "Out for Delivery",
        "Delivered",
        "Cancelled",
        "Delayed"
    ] | None = None
    delivery_time: int | None = Field(default=None, gt=0)
    amount: int | None = Field(default=None, gt=0)