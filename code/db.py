import cql
host = 'localhost'
port = 9160
keyspace = 'duke'
connection = cql.connect(host, port, keyspace, cql_version='3.0.0')
cursor = connection.cursor()
cursor.execute("SELECT * FROM safety_dance WHERE url=:url;", {'url':'http://curtis.lassam.net'} )
for row in cursor:
    print row

cursor.close()
connection.close()


