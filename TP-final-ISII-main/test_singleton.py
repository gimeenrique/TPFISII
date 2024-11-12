import logging
from CorporateData import CorporateData
from CorporateLog import CorporateLog

# Configurar el logging para mostrar mensajes de debug
logging.basicConfig(level=logging.DEBUG)

def test_singleton(instance1, instance2, class_name):
    if instance1 is instance2:
        logging.debug(f"Test Passed: {class_name} is a Singleton.")
    else:
        logging.debug(f"Test Failed: {class_name} is not a Singleton.")

def test_corporate_data():
    corporate_data = CorporateData()
    logging.debug("CUIT: %s", corporate_data.getCUIT())
    logging.debug("SeqID: %s", corporate_data.getSeqID())
    logging.debug("Data: %s", corporate_data.getData())

def test_corporate_log():
    corporate_log1 = CorporateLog()
    corporate_log2 = CorporateLog()
    
    test_singleton(corporate_log1, corporate_log2, "CorporateLog")
    
    corporate_log1.log()  # Llama a log para registrar los datos

if __name__ == "__main__":
    logging.debug("Testing CorporateData...")
    test_corporate_data()
    
    logging.debug("\nTesting CorporateLog...")
    test_corporate_log()
    
    # Desactivar el logging si se desea
    logging.getLogger().setLevel(logging.WARNING)
