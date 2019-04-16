import sqlite3


def student(mode)
     
  if (mode == 1):    
    conn = sqlite3.connect("C:\\Users\\Al\\Desktop\\Tutor\\done\\lib\\schoolDbase.db")
    curr = conn.cursor()
    sql = "select * from student"
    data = curr.execute(sql)

    configFile = open("C:\\Users\\Al\\Desktop\\Tutor\\done\\lib\\schoolFile.txt","a")
    
    for item in data:
    tempStr = item[1]
    configFile.write(tempStr + "\n")
      
    configFile.close()
    conn.close()

  
  if (mode == 2):
    configFile = open("C:\\Users\\Al\\Desktop\\Tutor\\done\\lib\\schoolFile.txt","w")
    conn = sqlite3.connect("C:\\Users\\Al\\Desktop\\Tutor\\done\\lib\\schoolDbase.db")
    lines = configFile.readlines()
    configFile.close()
    
    configFile = open("C:\\Users\\Al\\Desktop\\Tutor\\done\\lib\\schoolFile.txt","r")
    x = 1
    while (x <= len(lines)):
      data = configFile.readline()
      data = data.rstrip()
      curr = conn.cursor()
      sql = "Insert student(name) values('" + data + "')"
      data = curr.execute(sql)
      conn.commit()
      x +=1
    
      
    
