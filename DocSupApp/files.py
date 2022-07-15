from .models import documento, properties
import time

def genera_archivo(id):
    doc = documento.objects.get(id = id)
    numRes = properties.objects.first()
    name_file = numRes.path_file + numRes.name_file + str(numRes.Num_resolution) + ".txt"

    f = open("%s"%name_file ,"w+")
    f.write("ENC,INVOIC,DIAN 2.1: documento soporte en adquisiciones efectuadas a no obligados a facturar.," + "%s"%numRes.prefijo_res + "%s"%numRes.Num_resolution  + "," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1," + "%s"%doc.payment_date + ",2,10,UBL 2.1\n")
    f.write("CUD,\n")
    f.write("EMI," + "%s"%doc.tipo_persona + ",," + "%s"%doc.city_id + "," +"%s"%doc.city_name.capitalize() + "," + "%s"%doc.city_id  + "," + "%s"%doc.name_est_fed_prov.capitalize() + "," + "%s"%doc.est_fed_prov + "," + "%s"%doc.address + "," + "%s"%doc.country + ",Colombia,," + "%s"%doc.name_supplier_vendor + "," + "%s"%doc.Nit + "," + "%s"%doc.dv  + ",31\n") # informacion del proveedor
    f.write("TAC,R-99-PN\n")
    f.write("GTE,ZZ,No aplica\n")   
    f.write("ADQ,1,,,,,,,,,,860070698,1,31,Black & Decker de Colombia S.A.S\n") 
    f.write("TCR,O-13\n")
    f.write("GTA,01,IVA\n") 
    f.write("TOT," + "%s"%doc.net_amount.replace('.','').replace(',','.') + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP,0.00,COP,0.00,COP,,,,\n")
    f.write("TIM,true,0.00,COP\n")
    f.write("IMP,01," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.tax_amount.replace('.','').replace(',','.') + ",COP,0.00\n")	
    f.write("TIM,true," + "%s"%doc.amount_RTE.replace('.','').replace(',','.') + ",COP\n")
    f.write("IMP,06," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.amount_RTE.replace('.','').replace(',','.') + ",COP," + "%s"%doc.percent_RTE.replace(',','.') + "\n")	
    f.write("DRF,"+ "%s"%numRes.autorization + "," + "%s"%numRes.start_date_res + "," + "%s"%numRes.end_date_res + "," + "%s"%numRes.prefijo_res + "," + "%s"%numRes.initial_range_res + "," + "%s"%numRes.end_range_res + "\n")
    f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")
    f.write("MEP,1,2," +  "%s"%doc.payment_date + "\n") ## VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
    f.write("ITE,1,1,94," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP,," + "%s"%doc.item_description + ",1," + "%s"%doc.zSupplierID  + ",1,94,1," + "%s"%doc.net_amount.replace('.','').replace(',','.') + ",COP,,,,\n") # validar codigo vendedor
    f.write("FCB," + "%s"%doc.date_Invoice + ",1,Por operación\n")
    f.write("TII," + "%s"%doc.tax_amount.replace('.','').replace(',','.') + ",COP,false\n")
    f.write("IIM,01," + "%s"%doc.tax_amount.replace('.','').replace(',','.') + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.') + ",COP,0.00\n")
    f.close()


def genera_archivo_usd(id):
    doc = documento.objects.get(id = id)
    numRes = properties.objects.first()
    name_file = numRes.path_file + numRes.name_file + str(numRes.Num_resolution) + "-prueba.txt"

    f = open("%s"%name_file ,"w+")
    f.write("ENC,INVOIC,DIAN 2.1: documento soporte en adquisiciones efectuadas a no obligados a facturar.," + "%s"%numRes.prefijo_res + "%s"%numRes.Num_resolution  + "," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,USD,1," + "%s"%doc.payment_date + ",2,11,UBL 2.1\n")
    f.write("EMI," + "%s"%doc.tipo_persona + ",,," + doc.name_est_fed_prov.capitalize() + ",,,,," + doc.country +",Argentina,,"  + "%s"%doc.name_supplier_vendor + "," + "%s"%doc.Nit + ",," + "%s"%doc.type_of_tax_number + "\n") # informacion del proveedorf.write("TAC,R-99-PN\n")
    f.write("TAC,R-99-PN\n")
    f.write("GTE,ZZ,No aplica\n")   
    f.write("ADQ,1,,,,,,,,,,860070698,1,31,Black & Decker de Colombia S.A.S\n") 
    f.write("TCR,O-13\n")
    f.write("GTA,01,IVA\n") 
    f.write("TOT," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','')  + ",USD," + "%s"%doc.gross_amount.replace('.','').replace(',','.').replace(' USD','')  + ",USD," + "%s"%doc.gross_amount.replace('.','').replace(',','.').replace(' USD','')  + ",USD,0.00,USD,0.00,USD,,,,\n")
    f.write("TIM,false," + "%s"%doc.tax_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD\n")
    f.write("IMP,01," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','')  + ",USD," + "%s"%doc.tax_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD,19.00\n")	
    f.write("TDC,USD,COP," + "4500," + "2022-07-14," + "1.00,1.00\n")
    f.write("DRF,"+ "%s"%numRes.autorization + "," + "%s"%numRes.start_date_res + "," + "%s"%numRes.end_date_res + "," + "%s"%numRes.prefijo_res + "," + "%s"%numRes.initial_range_res + "," + "%s"%numRes.end_range_res + "\n")
    f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")
    f.write("MEP,1,2," +  "%s"%doc.payment_date + "\n") ## VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
    f.write("ITE,1,1,94," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','')  + ",USD," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','')  + ",USD,," + "%s"%doc.item_description + ",1," + "%s"%doc.zSupplierID  + ",1,94,1," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD,,,,\n") # validar codigo vendedor
    f.write("FCB," + "%s"%doc.date_Invoice + ",1,Por operación\n")
    f.write("TII," + "%s"%doc.tax_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD,false\n")
    f.write("IIM,01," + "%s"%doc.tax_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD," + "%s"%doc.net_amount.replace('.','').replace(',','.').replace(' USD','') + ",USD,19.00\n")
    f.close()


def genera_nc(id):
    doc = documento.objects.get(id = id)
    numRes = properties.objects.first()
    name_file = numRes.path_file  + doc.num_documento + "-NC.txt"
    fecha_anulacion = str(doc.Date_process)

    f = open("%s"%name_file ,"w+")
    f.write("ENC,NC,DIAN 2.1: Nota de ajuste al documento soporte en adquisiciones efectuadas a sujetos no obligados a expedir factura o documento equivalente.," + "%s"%numRes.prefijo_res + "%s"%numRes.Num_resolution  + "," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "95,COP,1," + "%s"%doc.payment_date + ",2,10,UBL 2.1\n")
    f.write("CUD,\n")
    f.write("EMI," + "%s"%doc.tipo_persona + ",," + "%s"%doc.city_id + "," +"%s"%doc.city_name.capitalize() + "," + "%s"%doc.city_id  + "," + "%s"%doc.name_est_fed_prov.capitalize() + "," + "%s"%doc.est_fed_prov + "," + "%s"%doc.address + "," + "%s"%doc.country + ",Colombia,," + "%s"%doc.name_supplier_vendor + "," + "%s"%doc.Nit + "," + "%s"%doc.dv  + ",31\n") # informacion del proveedor
    f.write("TAC,R-99-PN\n")
    f.write("GTE,ZZ,No aplica\n")   
    f.write("ADQ,1,,,,,,,,,,860070698,1,31,Black & Decker de Colombia S.A.S\n") 
    f.write("TCR,O-13\n")
    f.write("GTA,01,IVA\n") 
    f.write("TOT," + "%s"%doc.net_amount.replace('.','').replace(',','.') + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP,0.00,COP,0.00,COP,,,,\n")
    f.write("TIM,true,0.00,COP\n")
    f.write("IMP,01," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.tax_amount.replace('.','').replace(',','.') + ",COP,0.00\n")	
    f.write("TIM,true," + "%s"%doc.amount_RTE.replace('.','').replace(',','.') + ",COP\n")
    f.write("IMP,06," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.amount_RTE.replace('.','').replace(',','.') + ",COP," + "%s"%doc.percent_RTE.replace(',','.') + "\n")	
    f.write("DRF,"+ "%s"%numRes.autorization + "," + "%s"%numRes.start_date_res + "," + "%s"%numRes.end_date_res + "," + "%s"%numRes.prefijo_res + "," + "%s"%numRes.initial_range_res + "," + "%s"%numRes.end_range_res + "\n")
    f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")
    f.write("MEP,1,2," +  "%s"%doc.payment_date + "\n") ## VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
    f.write("ITE,1,1,94," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.')  + ",COP,," + "%s"%doc.item_description + ",1," + "%s"%doc.zSupplierID  + ",1,94,1," + "%s"%doc.net_amount.replace('.','').replace(',','.') + ",COP,,,,\n") # validar codigo vendedor
    f.write("TII," + "%s"%doc.tax_amount.replace('.','').replace(',','.') + ",COP,false\n")
    f.write("IIM,01," + "%s"%doc.tax_amount.replace('.','').replace(',','.') + ",COP," + "%s"%doc.net_amount.replace('.','').replace(',','.') + ",COP,0.00\n")
    f.write("REF,SETT" + "%s"%doc.num_documento.replace('Documento-','') + ",," + "%s"%fecha_anulacion[:10] + "\n")  # fecha del documento a anular
    f.write("CDN,SETT" + "%s"%doc.num_documento.replace('Documento-','') + ",5,Anulacion\n") 
    f.write("ORP,SETT" + "%s"%doc.num_documento.replace('Documento-','') + "\n")

    f.close()

