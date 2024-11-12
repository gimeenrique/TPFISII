# CorporateData.py

import boto3
import uuid
from decimal import Decimal
from singleton import SingletonMeta

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CorporateData')

class CorporateData(metaclass=SingletonMeta):
    def __init__(self):
        # Solo inicializa si no ha sido inicializado antes
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = {
                'id': str(uuid.uuid4()),  # Añadir un id único
                'Sede': "FCyT",
                'Domicilio': "25 de Mayo 385",
                'Localidad': "Concepción del Uruguay",
                'CodigoPostal': "3260",
                'Provincia': "Entre Rios",
                'CUIT': "30-70925411-8",
                'idSeq': Decimal('123'),
                'idReq': Decimal('83'),
                'Telefono': "03442 43-1442",
                'ID': "UADER-FCyT-IS2",
                'Web': "http://www.uader.edu.ar"
            }

    def save(self):
        response = table.put_item(
            Item=self.data
        )
        return response

    def getCUIT(self):
        return self.data.get('CUIT')

    def getSeqID(self):
        return self.data.get('idSeq')

    def getData(self):
        return self.data
