import mysql.connector
import os
import time
import glom
import json
import glob

config = {
    'user': 'root',
    'password': 'abc123',
    'host': '34.69.198.118',
    'use_pure': True,
    'database': 'GLO_7027',
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}

cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()

sql = "INSERT INTO publications " \
      "(type, organizationKey, editionId, " \
      "publicationsSectionId, publicationsType, " \
      "publicationsSlug, publicationsPublicationDate, " \
      "publicationsCanonical) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

path = 'test/'

# Ouvrir tout les fichiers publication-info
for filename in glob.glob(os.path.join(path, '*publication-info.json')):
    with open(os.path.join(os.getcwd(), filename), 'r') as jar:
        data = json.load(jar)

        # Boucle dans la prémiere niveau du json
        for d in data:

            # Variable
            type_ = d['type']
            organizationKey = d['organizationKey']
            editionId = d['editionId']

            # Boucle dans le niveau Publications
            for d2 in d['publications']:
                # Variables
                publicationsSectionId = d2['sectionId']
                publicationsType = d2['type']
                publicationsSlug = glom.glom(d2, 'slug.fr')
                publicationsCanonical = d2['canonical']

                print(type_, " ", organizationKey, " ", editionId, " ", publicationsSectionId, " ",
                        publicationsType, " ", publicationsSlug, " ", publicationsCanonical)

                val = (type_, organizationKey, editionId, publicationsSectionId, publicationsType, publicationsCanonical)
                cursor.execute(sql, val)
                cnxn.commit()

jar.close()
