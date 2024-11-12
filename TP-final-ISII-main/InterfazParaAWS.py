from CorporateData import CorporateData
from CorporateLog import CorporateLog

class InterfazParaAWS:
    def __init__(self):
        self.corporate_data = CorporateData()  # Instancia de CorporateData
        self.corporate_log = CorporateLog()    # Instancia de CorporateLog

    def saveCorporateData(self):
        """Guardar los datos de la empresa en DynamoDB usando CorporateData."""
        response = self.corporate_data.save()
        return response

    def logData(self):
        """Registrar un log con los datos de CorporateData usando CorporateLog."""
        self.corporate_log.log()

    def getCorporateData(self):
        """Obtener los datos completos de la empresa desde CorporateData."""
        return self.corporate_data.getData()

    def getCUIT(self):
        """Obtener el CUIT de la empresa desde CorporateData."""
        return self.corporate_data.getCUIT()

    def getSeqID(self):
        """Obtener el ID de secuencia desde CorporateData."""
        return self.corporate_data.getSeqID()
