
import mysql.connector


config = {
    'user': 'root',
    'password': 'abc123',
    'host': '34.69.198.118',
    'use_pure':True,
    'database':'GLO_7027',
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}

cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()
print(cursor)
cursor.execute("SHOW TABLES")

for table in [tables[0] for tables in cursor.fetchall()]:
    print(table)

#create publications table
cursor.execute("CREATE TABLE publications ("
               "id INT AUTO_INCREMENT NOT NULL,"
               "type VARCHAR(100) NOT NULL,"
               "organizationKey VARCHAR(100) NOT NULL,"
               "editionId VARCHAR(100) NOT NULL,"
               "publicationsSectionId VARCHAR(100) NOT NULL,"
               "publicationsType VARCHAR(100) NOT NULL,"
               "publicationsSlug VARCHAR(100) NOT NULL,"
               "publicationsPublicationDate DATETIME NOT NULL,"
               "publicationsCanonical BOOLEAN NOT NULL,"
               "CONSTRAINT publication_PK PRIMARY KEY (id) ) ")

cursor.execute("SELECT COUNT(*) from publications")
out = cursor.fetchall()
out

cnxn.commit()