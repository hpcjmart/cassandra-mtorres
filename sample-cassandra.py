from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cluster = Cluster(['localhost'], port=9042)

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(auth_provider=auth_provider)

session = cluster.connect()

row = session.execute("SELECT release_version FROM system.local").one()
if row:
    print(row[0])
