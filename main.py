import sqlite3

 

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

 

    # Esta consulta es insegura y susceptible a inyección de SQL
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

 

    return user

 

# Ejemplo de uso del código inseguro
if __name__ == "__main__":
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

 

    user = login(username, password)

 

    if user:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
