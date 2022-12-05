import datetime
import unittest

from signature_xades.sri.Bill import Init, VERSION_110


class TestBill(unittest.TestCase):
    def test_version_100(self):
        # Version 1.0.0
        bill = Init()
        bill.set_info_tributaria(
            ambiente='1', tipo_emision='1', razon_social='razonSocial0', ruc='0000000000001',
            clave_acceso='0000000000000000000000000000000000000000000000000', estab='000', pto_emi='000',
            secuencial='000000000', dir_matriz='dirMatriz0'
        )
        bill.info_tributaria.set_nombre_comercial('nombreComercial0')
        bill.info_tributaria.set_agente_retention('0')
        bill.info_tributaria.set_contribuyente_rimpe(True)

        info_factura = bill.set_info_factura(fecha_emision=datetime.date.today(), tipo_identificacion_comprador='04',
                                             razon_social_comprador='razonSocialComprador0',
                                             identificacion_comprador='identificacionCompra', total_sin_impuestos=50,
                                             total_descuento=0, importe_total=50)
        info_factura.set_dir_establecimiento('dirEstablecimiento0')
        info_factura.set_contribuyente_especial('contribuyente')
        info_factura.set_obligado_contabilidad(True)
        info_factura.set_comercio_exterior(True)
        info_factura.set_inco_term_factura("A")
        info_factura.set_lugar_inco_term("lugarIncoTerm0")
        info_factura.set_pais_origen("000")
        info_factura.set_puerto_embarque("puertoEmbarque0")
        info_factura.set_puerto_destino("puertoDestino0")
        info_factura.set_pais_destino("000")
        info_factura.set_pais_adquisicion("000")
        info_factura.set_guia_remision("000-000-000000000")
        info_factura.set_direccion_comprador("direccionComprador0")
        info_factura.set_total_subsidio(50)
        info_factura.set_inco_term_total_sin_impuestos("A")
        info_factura.set_cod_doc_reembolso("00")
        info_factura.set_total_comprobantes_reembolso(50)
        info_factura.set_total_base_imponible_reembolso(50)
        info_factura.set_total_impuesto_reembolso(50)

        total_impuesto = info_factura.add_total_con_impuestos(codigo='2', codigo_porcentaje='0', base_imponible=50,
                                                              valor=50)
        total_impuesto.set_descuento_adicional(0)
        total_impuesto.set_tarifa(49.50)
        total_impuesto.set_valor_devolution_iva(50)

        total_impuesto = info_factura.add_total_con_impuestos(codigo='2', codigo_porcentaje='0', base_imponible=500,
                                                              valor=500)
        total_impuesto.set_descuento_adicional(0)
        total_impuesto.set_tarifa(499.50)
        total_impuesto.set_valor_devolution_iva(500)

        info_factura.add_compensation(codigo='1', tarifa=49.5, valor=50)
        info_factura.add_compensation(codigo='1', tarifa=499.5, valor=500)

        info_factura.set_propina(50)
        info_factura.set_flete_internacional(50)
        info_factura.set_seguro_internacional(50)
        info_factura.set_gastos_aduaneros(50)
        info_factura.set_gastos_transporte_otros(50)
        info_factura.set_moneda("moneda0")
        info_factura.set_placa("placa0")

        _pago = info_factura.add_pago(forma_pago='01', total=50, plazo=50, unidad_tiempo='unidadTiem')
        _pago = info_factura.add_pago(forma_pago='01', total=500, plazo=500, unidad_tiempo='unidadTiem2')

        info_factura.set_valor_ret_iva(50)
        info_factura.set_valor_ret_renta(50)

        detalle = bill.add_detalle(descripcion='descripcion0', cantidad=50, precio_unitario=50, descuento=50,
                                   precio_total_sin_impuesto=50)
        detalle.set_code_principal('codigoPrincipal0')
        detalle.set_code_auxiliar('codigoAuxiliar0')
        detalle.set_unidad_medida('unidadMedida0')
        detalle.set_precio_sin_subsidio(50)
        # Agregando detalles adicionales
        detalle.add_det_adicional('nombre0', 'valor0')
        detalle.add_det_adicional('nombre1', 'valor1')

        # Agregando impuestos
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=50, valor=50)
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=501, valor=501)

        detalle = bill.add_detalle(descripcion='descripcion1', cantidad=50, precio_unitario=50, descuento=50,
                                   precio_total_sin_impuesto=50)
        detalle.set_code_principal('codigoPrincipal1')
        detalle.set_code_auxiliar('codigoAuxiliar1')
        detalle.set_unidad_medida('unidadMedida1')
        detalle.set_precio_sin_subsidio(50)
        # Agregando detalles adicionales
        detalle.add_det_adicional('nombre2', 'valor2')
        detalle.add_det_adicional('nombre3', 'valor3')

        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=50, valor=50)
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=50, valor=50)

        # Agregando reembolsos
        reembolso = bill.add_reembolsos(
            tipo_identificacion_proveedor_reembolso='04', identificacion_proveedor_reembolso='identificacionProvee',
            tipo_proveedor_reembolso='01', cod_doc_reembolso='00', estab_doc_reembolso='000',
            pto_emi_doc_reembolso='000', secuencial_doc_reembolso='000000000',
            fecha_emision_doc_reembolso=datetime.date.today(), numero_autorizacion_doc_reemb='0000000000'
        )
        reembolso.set_cod_pais_pago_proveedor_reembolso('000')
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)

        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)
        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)

        reembolso = bill.add_reembolsos(
            tipo_identificacion_proveedor_reembolso='04', identificacion_proveedor_reembolso='identificacionProvee',
            tipo_proveedor_reembolso='01', cod_doc_reembolso='00', estab_doc_reembolso='000',
            pto_emi_doc_reembolso='000', secuencial_doc_reembolso='000000000',
            fecha_emision_doc_reembolso=datetime.date.today(), numero_autorizacion_doc_reemb='0000000000'
        )
        reembolso.set_cod_pais_pago_proveedor_reembolso('000')
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)

        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)
        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)

        bill.set_tipo_negociable(correo="correo0")

        bill.set_maquina_fiscal(marca="marca0", modelo="modelo0", serie="serie0")

        bill.add_info_adicional(name="nombre4", text="campoAdicional0")
        bill.add_info_adicional(name="nombre5", text="campoAdicional1")

        is_valid = bill.is_valid()
        print('is valid:', is_valid)
        print(bill.xml_str())
        if not is_valid:
            print(bill.validate())
        self.assertTrue(is_valid)

    def test_version_110(self):
        # Version 1.1.0
        bill = Init(version=VERSION_110)
        bill.set_info_tributaria(
            ambiente='1', tipo_emision='1', razon_social='razonSocial0', ruc='0000000000001',
            clave_acceso='0000000000000000000000000000000000000000000000000', estab='000', pto_emi='000',
            secuencial='000000000', dir_matriz='dirMatriz0'
        )
        bill.info_tributaria.set_nombre_comercial('nombreComercial0')
        bill.info_tributaria.set_agente_retention('0')
        bill.info_tributaria.set_contribuyente_rimpe(True)

        info_factura = bill.set_info_factura(
            fecha_emision=datetime.date.today(), tipo_identificacion_comprador='04',
            razon_social_comprador='razonSocialComprador0', identificacion_comprador='identificacionCompra',
            total_sin_impuestos=50, total_descuento=0, importe_total=50
        )
        info_factura.set_dir_establecimiento('dirEstablecimiento0')
        info_factura.set_contribuyente_especial('contribuyente')
        info_factura.set_obligado_contabilidad(True)
        info_factura.set_comercio_exterior(True)
        info_factura.set_inco_term_factura("A")
        info_factura.set_lugar_inco_term("lugarIncoTerm0")
        info_factura.set_pais_origen("000")
        info_factura.set_puerto_embarque("puertoEmbarque0")
        info_factura.set_puerto_destino("puertoDestino0")
        info_factura.set_pais_destino("000")
        info_factura.set_pais_adquisicion("000")
        info_factura.set_guia_remision("000-000-000000000")
        info_factura.set_direccion_comprador("direccionComprador0")
        info_factura.set_total_subsidio(50)
        info_factura.set_inco_term_total_sin_impuestos("A")
        info_factura.set_cod_doc_reembolso("00")
        info_factura.set_total_comprobantes_reembolso(50)
        info_factura.set_total_base_imponible_reembolso(50)
        info_factura.set_total_impuesto_reembolso(50)

        total_impuesto = info_factura.add_total_con_impuestos(codigo='2', codigo_porcentaje='0', base_imponible=50,
                                                              valor=50)
        total_impuesto.set_descuento_adicional(10)
        total_impuesto.set_tarifa(49.50)
        total_impuesto.set_valor_devolution_iva(50)

        total_impuesto = info_factura.add_total_con_impuestos(codigo='2', codigo_porcentaje='0', base_imponible=500,
                                                              valor=500)
        total_impuesto.set_descuento_adicional(20)
        total_impuesto.set_tarifa(499.50)
        total_impuesto.set_valor_devolution_iva(500)

        info_factura.add_compensation(codigo='1', tarifa=49.5, valor=50)
        info_factura.add_compensation(codigo='1', tarifa=499.5, valor=500)

        info_factura.set_propina(50)
        info_factura.set_flete_internacional(50)
        info_factura.set_seguro_internacional(50)
        info_factura.set_gastos_aduaneros(50)
        info_factura.set_gastos_transporte_otros(50)
        info_factura.set_moneda("moneda0")
        info_factura.set_placa("placa0")

        _pago = info_factura.add_pago(forma_pago='01', total=50, plazo=50, unidad_tiempo='unidadTiem')
        _pago = info_factura.add_pago(forma_pago='01', total=500, plazo=500, unidad_tiempo='unidadTiem2')

        info_factura.set_valor_ret_iva(50)
        info_factura.set_valor_ret_renta(50)

        detalle = bill.add_detalle(descripcion='descripcion0', cantidad=50, precio_unitario=50, descuento=50,
                                   precio_total_sin_impuesto=50)
        detalle.set_code_principal('codigoPrincipal0')
        detalle.set_code_auxiliar('codigoAuxiliar0')
        detalle.set_unidad_medida('unidadMedida0')
        detalle.set_precio_sin_subsidio(50)
        # Agregando detalles adicionales
        detalle.add_det_adicional('nombre0', 'valor0')
        detalle.add_det_adicional('nombre1', 'valor1')

        # Agregando impuestos
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=50, valor=50)
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=501, valor=501)

        detalle = bill.add_detalle(descripcion='descripcion1', cantidad=50, precio_unitario=50, descuento=50,
                                   precio_total_sin_impuesto=50)
        detalle.set_code_principal('codigoPrincipal1')
        detalle.set_code_auxiliar('codigoAuxiliar1')
        detalle.set_unidad_medida('unidadMedida1')
        detalle.set_precio_sin_subsidio(50)
        # Agregando detalles adicionales
        detalle.add_det_adicional('nombre2', 'valor2')
        detalle.add_det_adicional('nombre3', 'valor3')

        # Agregando impuestos
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=50, valor=50)
        detalle.add_impuesto(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible=501, valor=501)

        # Agregando reembolsos
        reembolso = bill.add_reembolsos(
            tipo_identificacion_proveedor_reembolso='04', identificacion_proveedor_reembolso='identificacionProvee',
            tipo_proveedor_reembolso='01', cod_doc_reembolso='00', estab_doc_reembolso='000',
            pto_emi_doc_reembolso='000', secuencial_doc_reembolso='000000000',
            fecha_emision_doc_reembolso=datetime.date.today(), numero_autorizacion_doc_reemb='0000000000'
        )
        reembolso.set_cod_pais_pago_proveedor_reembolso('000')
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)

        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)
        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)

        reembolso = bill.add_reembolsos(
            tipo_identificacion_proveedor_reembolso='04', identificacion_proveedor_reembolso='identificacionProvee',
            tipo_proveedor_reembolso='01', cod_doc_reembolso='00', estab_doc_reembolso='000',
            pto_emi_doc_reembolso='000', secuencial_doc_reembolso='000000000',
            fecha_emision_doc_reembolso=datetime.date.today(), numero_autorizacion_doc_reemb='0000000000'
        )
        reembolso.set_cod_pais_pago_proveedor_reembolso('000')
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)
        reembolso.add_detalle_impuestos(codigo='2', codigo_porcentaje='0', tarifa=49.5, base_imponible_reembolso=50,
                                        impuesto_reembolso=50)

        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)
        reembolso.add_compensation_reembolso(codigo='1', tarifa=49.5, valor=50)

        bill.set_tipo_negociable(correo="correo0")

        bill.set_maquina_fiscal(marca="marca0", modelo="modelo0", serie="serie0")

        bill.add_info_adicional(name="nombre4", text="campoAdicional0")
        bill.add_info_adicional(name="nombre5", text="campoAdicional1")

        bill.add_retention(codigo='4', codigo_porcentaje='0', tarifa=499.50, valor=50)
        bill.add_retention(codigo='4', codigo_porcentaje='0', tarifa=499.50, valor=50)

        is_valid = bill.is_valid()
        print('is valid:', is_valid)
        print(bill.xml_str())
        if not is_valid:
            print(bill.validate())
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()
