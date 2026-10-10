import random
import pandas as pd
from datetime import datetime ,timedelta 
Cities = ["Delhi", "Noida", "Ghaziabad", "Jaipur", "Lucknow", "Gurgaon"]
names = [
    "Sanjay","Sarah","Manu","Ali","Aney","Sam","Udit","Manha","John", "Zuh", "Namrah","Rasi", "Denark"
]
Name = ["sanjay", "meh", "Den", "sagar", "Agy", "Ballu"]
Statues = ["Pending", "Out for Delivery", "Delivered", "Cancelled", "Delayed"]

customer_data =[]
for i in range(1,101):
 customer_data.append(
    {
      "customer_id":i,
      "Name" : random.choice(names),
      "City": random.choice(Cities)
    }
  )
customer_df = pd.DataFrame(customer_data)
customer_df.to_csv("customer.csv", index = False)



agent_data =[]
for i in range(1,21):
  agent_data.append(
    {
      "agent_id":i,
      "Name" : random.choice(Name),
      "City": random.choice(Cities)
    }
  )
agent_df = pd.DataFrame(agent_data)
agent_df.to_csv("agent.csv", index = False)


start_date = datetime(2026,1,1)
order_data = []
for i in range(1,1001):
  
  order_date = start_date+timedelta(days = random.randint(1,270))
  status = random.choice(Statues)
  if status in ["Delayed", "Delivered"]:
    delivery_date = order_date + timedelta(days = random.randint(1,5))
    delivery_time = random.randint(20,180)
  else:
    delivery_date=None
    delivery_time= None
    
    
  order_data.append(
    {
      "order_id":i,
      "customer_id": random.randint(1,100),
      "agent_id":random.randint(1,20),
      "order_date":order_date.date(),
      "delivery_date":(
        delivery_date.date()
        if delivery_date
        else None
      ),
      "status":status,
      "delivery_time":delivery_time,
      "amount":random.randint(100,3000)
    }
  )
order_df = pd.DataFrame(order_data)
order_df["delivery_time"] = order_df["delivery_time"].astype("Int64")
order_df.to_csv("order.csv", index  = False)