import MySQLdb

basis_data = MySQLdb.connect(host="127.0.0.1", user="root")
arahan = basis_data.cursor()
while True:
    try:
        arahan.execute(input("MySQL Command: "))
        for output in arahan.fetchall():
          print(output)
    except KeyboardInterrupt:
        break
    except Exception as error:
        print(str(error))
basis_data.close()