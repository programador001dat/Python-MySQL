import mysql.connector
import os

os.system("clear")
def __addContato__():

    try:

        conn = mysql.connector.connect(
            host="localhost",
            user="caio",
            password="ILoveYou",
            database="agenda_telefonica"
        )
        if conn.is_connected():
            print("Conexão com Sucesso ao MySql.")
            nome = str(input("=> Nome completo: "))
            email = str(input("=> E-mail: "))
            telefone = int(input("=> Telefone: "))

            cursor = conn.cursor()
            command = "INSERT INTO contatos(nome, email, telefone) VALUES (%s, %s, %s);"
            cursor.execute(command, (nome, email, telefone))
            conn.commit()

            cursor.close()
            conn.close()
            print("=> Salvo.")

    except Exception as Error:
        print("Erro ao conectar ao MySql", Error)

    finally:
        quit()

def __Views__():

    conn = mysql.connector.connect(
        host="localhost",
        user="caio",
        password="ILoveYou",
        database="agenda_telefonica"
    )
    if conn.is_connected():
        print("Conexão com Sucesso ao MySql.")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos")

        for i in cursor.fetchall():
            print(i)

        cursor.close()
        conn.close()

    else:
        print("Não foi possivél conectar ao MySql")
        quit()

def main():

    while True:

        print("[1] adicionar novo contato.")
        print("[2] visualizar contatos.")
        try:
            user = int(input("=> "))
            if user == 1:
                __addContato__()

            elif user == 2:
                __Views__()

        except Exception as Error:
            print("Error por argumento inválido\n", Error)

        finally:
            quit()

if __name__ == "__main__":
    main()