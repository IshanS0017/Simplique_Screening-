import mysql.connector
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Remind-me-Later", description="API endpoint to save data into db")
db = mysql.connector.connect(
    host='localhost',
    user='Symplique',
    password='PASSKEY',
    database='db'
    )
cursor = db.cursor()

@app.get("/api/save_data_to_db")
def save_data_to_db(date, time, message='Reminder'):
    try:
        sql = "INSERT INTO dbtable (date, time, message) VALUES (%s,%s,%s)"
        val = (date, time, message)
        cursor.execute(sql,val)
        db.commit()
        print("Record Updated")
    except:
        print("Exception: save_data_tp_db")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=11000)
