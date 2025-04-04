import mysql.connector
import json

with open('config.json', 'r') as file:
    config = json.load(file)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=config["DATABASE_PASS"],
  # database="discord_acc_price"
)
is_there_db = True
cur = db.cursor(buffered=True)



################# Connecting DB  ####################### 
cur.execute("SHOW DATABASES")
for t in cur.fetchall():
  if "discord_acc_price" in t:
    is_there_db = False
    cur.execute("USE discord_acc_price")
if is_there_db:
    cur.execute("CREATE DATABASE discord_acc_price")
    cur.execute("USE discord_acc_price")
    cur.execute("""CREATE TABLE acc_price (
  Account_Hex VARCHAR(255),
  Price INT,
  status INT)""")

db.commit()

################# Connecting DB ####################### 






