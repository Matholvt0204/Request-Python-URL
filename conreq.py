import mysql.connector
import requests

#Starting the connection
con = mysql.connector.connect(
        host="localhost",
        database="channeltest",
        user="matheus",
        passwd=""
)

#Starting the cursor
cur = con.cursor()

#Testing the connection
if not con:
    print("Connected")
else:
    print("Not_Connected")

#Testing Cursor
query = "SELECT * FROM channel;"
cur.execute(query)

for cha in cur:
    print(cha)

#Test Request
url = "http://ela.oglobo.globo.com"
resp = requests.get(url)

print(resp.url)

#Close the Connection 
cur.close()
con.close()

