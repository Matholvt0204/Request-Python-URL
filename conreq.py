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
#query = "SELECT * FROM channel;"
#cur.execute(query)

#for cha in cur:
#    print(cha)

#Test Request
url = "http://ela.oglobo.globo.com"
resp = requests.get(url)

print(resp.url)

def func(acc):

    query = "SELECT chaId, chaurl FROM channel WHERE accId = " + str(acc) + ";"
    cur.execute(query)
    for fetch in cur:
        print(fetch)

#acc = input("Passe o id da conta: ") 
#func(acc)
func(input("Passe o id da conta: "))


#Close the Connection 
cur.close()
con.close()

