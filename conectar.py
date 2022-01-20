import psycopg2
class bd():
    conectar=psycopg2.connect(
    database="aula",
    user="aula",
    password="aula",
    host="200.18.128.54",
    port="5432")
    ab=conectar.cursor()
    conectar.close()