import pypyodbc
import win32com.client
db_path = r'C:\Users\yuan\Desktop\201601.MDB'

def access_table(db_path):
    conn = pypyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb)};DBQ="+db_path+";" )
    cursor = conn.cursor()
    SQL = "Update WdSd set timeXP = '2018'+Right(timeXP,Len(timeXP)-4)"
    cursor.execute(SQL)
    cursor.commit()    
    cursor.close()
    conn.close()

if  __name__ == '__main__':
    access_table("C:\\Users\\yuan\\Desktop\\201601.mdb")