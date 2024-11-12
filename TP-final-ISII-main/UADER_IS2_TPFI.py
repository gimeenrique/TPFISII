from InterfazParaAWS import InterfazParaAWS

def main():
    # Crear la instancia de la interfaz
    aws_interface = InterfazParaAWS()
    
    # Guardar los datos de la empresa
    response = aws_interface.saveCorporateData()
    
    # Mostrar solo algunos campos específicos de los datos guardados
    if response:  # Asegúrate de que response no esté vacío
        # Supongamos que 'response' tiene un campo 'id' y 'CUIT' (ajusta según tu estructura)
        print("Datos guardados en DynamoDB:")
    
    # Registrar un log con los datos de la empresa
    aws_interface.logData()
    
    # Obtener datos específicos de la empresa
    print("CUIT:", aws_interface.getCUIT())
    print("SeqID:", aws_interface.getSeqID())
    print("Datos completos de la empresa:", aws_interface.getCorporateData())

if __name__ == "__main__":
    main()
