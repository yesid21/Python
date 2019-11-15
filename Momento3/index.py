import sqlite3
conexion = sqlite3.connect('estudiantes.db')
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE estudiantes (id INT PRIMARY KEY , nombre VARCHAR(100), apellido VARCHAR(100), cedula INT(200), telefono INT(100))")
#cursor.execute("INSERT INTO estudiantes VALUES (12, 'Yesid', 'Cadavid', 124846526, 8456445)")
#cursor.execute("SELECT * FROM estudiantes")
#estudiantes = cursor.fetchone()
#print(estudiantes[1])
#estudiantes = [
    #(1, 'Pedro', 'Carvajal', 48512, 485615),
    #(2, 'Jorman', 'Cadavid', 111111, 8461),
    #(3, 'Manuel', 'Perez', 2221515, 564513),
#]
#cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?,?)", estudiantes)
#cursor.execute("SELECT * FROM estudiantes")
#estudiantes = cursor.fetchall()
#for estudiantes in estudiantes:
 #   print(estudiantes)
#cursor.execute("UPDATE estudiantes SET  nombre = 'camilo' WHERE id=45")

#cursor.execute("DELETE FROM estudiantes")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()

