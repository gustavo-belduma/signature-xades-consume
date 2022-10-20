# -*- coding: utf-8 -*-
import base64
import logging
import os
from pathlib import Path
from urllib.error import URLError

from suds import Client

from signature_xades.xades import Xades, CheckDigit

logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent
URL_RECEPTION = "https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl"
URL_AUTHORIZATION = "https://celcer.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl"


def sign_xml_file():
    """
    Ejemplo básico de como firmar un archivo .xml y posteriormente validar comprobante contra el wsdl del SRI
    """
    try:
        path_xml = os.path.join(os.path.dirname(__file__), 'xml_comprobantes/factura_V1.0.0.xml')

        # Reading the data inside the xml file to a variable under the name  data
        with open(path_xml, 'r') as f:
            xml_document = f.read()
        f.close()

        file_pk12 = '/home/gbelduma/PycharmProjects/signature-xades-consume/res/sign.pfx'
        password = 'Amoniojairo15'

        xades = Xades(signature_path=file_pk12, password=password)
        errors = xades.validate()
        if errors:
            logger.error("Corrija los siguientes errores:\n%s" % "\n - ".join(errors))
        else:
            # firmar documento
            res = xades.sign(xml_document)
            # Mostrar resultado del documento firmado
            logger.warning(msg=res.decode('utf-8'))

            base64_binary_xml = base64.b64encode(res).decode('utf-8')
            sri_client = Client(URL_RECEPTION)

            # consumo de ws
            response_suds = sri_client.service.validarComprobante(base64_binary_xml)
            # imprimir respuesta de ws
            logger.warning(response_suds)

    except Exception as e:
        logger.error("Error al firmar documento: %s" % str(e))


def check_digit(text):
    """
    Permite invocar a función que obtiene el dígito verificar aplicando módulo 11.
    :param text: clave de acceso de 48 dígitos de longitud.
    :return: dígito verificar de tipo entero.
    """
    check = CheckDigit()
    return check.compute_mod11(text)


def authorization():
    try:
        sri_client = Client(URL_AUTHORIZATION)
        # consumo de ws
        response_suds = sri_client.service.autorizacionComprobante("0000000000000000000000000000000000000000000000000")
        # imprimir respuesta de ws
        logger.warning(response_suds)
    except URLError as e:
        logger.error('authorization. URLError. %s' % str(e))
    except Exception as e:
        logger.error('authorization. Exception. %s' % str(e))


if __name__ == '__main__':
    """Obtener dígito verificador"""
    text = '310820220109900057370012001001180575405010801151'
    check_digit_temp = check_digit(text)
    print("Dígito verificador de '{}' es: {}".format(text, check_digit_temp))

    """Firmar electrónicamente archivo (xml)"""
    sign_xml_file()
    authorization()
