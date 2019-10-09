import mysql.connector
import requests

con = mysql.connector.connect(
        host="localhost",
        database="channeltest",
        user="matheus",
        passwd=""
)

cur = con.cursor()

if not con:
    print("ruim")
else:
    print("boa")

if con.is_connected():
    print(con)

query = "SELECT * FROM channel;"
cur.execute(query)

#fetch = cur.fetchall()
#print(cur.rowcount)
for cha in cur:
    print(cha)

url = "http://ela.oglobo.globo.com"
resp = requests.get(url)

print(resp.url)

cur.close()
con.close()

