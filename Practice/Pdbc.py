import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CrowdStrike"
)
if con.is_connected():
    print("Connected")
    
st = con.cursor()

st.execute("CREATE DATABASE pydb")

st.execute("SHOW DATABASES")
for x in st:
    print(x)