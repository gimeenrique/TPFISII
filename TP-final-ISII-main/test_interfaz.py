import unittest
from InterfazParaAWS import InterfazParaAWS

class TestInterfazParaAWS(unittest.TestCase):

    def setUp(self):
        self.aws_interface = InterfazParaAWS()
        # Establecer los valores directamente si no hay setter
        self.aws_interface._CorporateData = {"id": 1, "name": "Empresa XYZ", "balance": 1000.75}
        self.aws_interface._CUIT = "20-12345678-9"
        self.aws_interface._SeqID = "SEQ123456"

    def test_getCUIT_success(self):
        # Verificar que el CUIT se obtiene correctamente
        self.assertEqual(self.aws_interface.getCUIT(), "20-12345678-9")

    def test_getCUIT_missing_argument(self):
        # Verificar que se maneja el caso de CUIT no establecido (usando el valor por defecto)
        self.aws_interface._CUIT = None
        self.assertIsNone(self.aws_interface.getCUIT())

    def test_getSeqID_success(self):
        # Verificar que el SeqID se obtiene correctamente
        self.assertEqual(self.aws_interface.getSeqID(), "SEQ123456")

    def test_getSeqID_empty_argument(self):
        # Verificar el comportamiento si SeqID no se establece (vacío)
        self.aws_interface._SeqID = ""
        self.assertEqual(self.aws_interface.getSeqID(), "")

    def test_getCorporateData_success(self):
        # Verificar que los datos corporativos se obtienen correctamente
        self.assertEqual(self.aws_interface.getCorporateData(), {"id": 1, "name": "Empresa XYZ", "balance": 1000.75})

    def test_getCorporateData_missing_data(self):
        # Verificar que se maneja el caso de datos no establecidos
        self.aws_interface._CorporateData = None
        self.assertIsNone(self.aws_interface.getCorporateData())

if __name__ == "__main__":
    unittest.main()
