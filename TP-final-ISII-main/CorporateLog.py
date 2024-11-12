import boto3
import uuid
from datetime import datetime
from decimal import Decimal
from CorporateData import CorporateData
from singleton import SingletonMeta

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CorporateLog')

class CorporateLog(metaclass=SingletonMeta):
    def __init__(self):
        self.data = CorporateData()  # Instancia de CorporateData

    def log(self):
        uniqueID = str(uuid.uuid4())
        CPUid = str(uuid.getnode())
        sessionid = str(uuid.uuid4())
        ts = datetime.now().isoformat()  # Timestamp actual en formato ISO

        # Datos de CorporateData
        cuit = self.data.getCUIT()
        seqID = self.data.getSeqID()

        # Registrando el log
        response = table.put_item(
            Item={
                'id': uniqueID,
                'CPUid': CPUid,
                'sessionid': sessionid,
                'timestamp': ts,
                'CUIT': cuit,
                'SeqID': seqID
            }
        )

        print(f"id={uniqueID} CPU={CPUid} session={sessionid} time={ts} CUIT={cuit} SeqID={seqID}")
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        print("status code:", status_code)
