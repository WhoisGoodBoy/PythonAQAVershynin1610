import psycopg2


connection = psycopg2.connect(user='postgres',
                              password='d2z76ctb',
                              host='localhost',
                              port='5432',
                              database='postgres')

cursor = connection.cursor()
#cursor.execute('CREATE TABLE userstable1 (id varchar(8) primary key, first_name varchar(25), last_name varchar(25), email varchar(25));COMMIT;')
cursor.execute("INSERT INTO userstable1 (id, first_name, last_name, email) VALUES ('AAAAAAAA', 'Jack','Whatt','jackwhatt@gmail.com'),('BBBBBBBB','Angelina','Stewart','angelinatewart@ff.com');COMMIT;")
cursor.execute('SELECT * from userstable1;')
connection.commit()
for row in cursor.fetchall():
    print(row)
    print(type(row))
cursor.close()
if connection:
    connection.close()


