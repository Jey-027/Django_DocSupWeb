import time
# from wsgiref import validate
# from DocSupWeb.DocSupApp.views import DetFactUpdate
# import views as doc


class CreateFile():
    template_name = 'DocSupAp/enviar_file.html'
    
    def genera_documento(self):
        f = open("C:/load/txt/pruebaDjangofile.txt" ,"w+")
        f.write("ENC,DS,DIAN 2.1: Documento soporte en adquisiciones efectuadas a no obligados a facturar.,DME1503," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1," + "FECHA DE PAGO" + ",2,10,UBL 2.1\n")
        f.write("CUD,123456789ASD0987654321\n")
        f.write("EMI,1,,11001,Bogotá D.C.,110111,Bogotá,11,CRA 72 80-94 OF 902 CTRO EMP. TITAN PLAZA,CO,Colombia,,Black & Decker de Colombia S.A.S,935462718,1,31 \n")
        f.write("TAC,O-13\n")
        f.write("GTE,01,IVA\n")
       #f.write("ADQ,1,,,,,,,,,," + "%s"%cli.list[7] + ",, " + "%s"%cli.list[8] + "," + "%s"%cli.list[2] + "\n")
        f.write("TCR,O-13;O-15\n")  ## VALIDAR SI ES 13 0 15
        f.write("GTA,01,IVA\n") 
        #f.write("TOT," + "%s"%cli.list[20] + ",COP," + "%s"%cli.list[20] + ",COP," + "%s"%cli.list[20] + ",COP," + "%s"%cli.list[20] + ",COP,0.00,COP,0.00,COP,,,,\n")
        f.write("TIM,false,0.00,COP\n")
        #f.write("IMP,01," + "%s"%cli.list[20] + ",COP," + "%s"%cli.list[21] + ",COP,19.00\n")	
        f.write("TIM,true,4000.00,COP\n") ## VALIDAR
        f.write("IMP,06,100000.00,COP,4000.00,COP,4.00\n") ## VALIDAR
        #f.write("DSC,false,0,0.00,COP,01,," + "%s"%cli.list[20] + ",COP,1 \n")
        f.write("DRF,32912731242012,2019-11-26,2022-11-26,DME,1,5000000\n") ## VALIDAR
        f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")

        f.write("MEP,1,2,2020-06-26\n") ## CREAR UNA TABLA DE LOS CODIGOS DE METODO DE PAGO Y TRAER LOS DATOS DE AHI Y VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
        f.write("IDP,IDP1\n")
        f.write("CTS,CE01\n")
        #f.write("ITE,1,1,94," + "%s"%cli.list[20] + ",COP," + "%s"%cli.list[20] + ",COP,," + "%s"%cli.list[17] + ",1,VALIDARCODIGOVENDEDOR,1,94,," + "%s"%cli.list[20] + ",COP,,,,\n")
        #f.write("FCB," + "%s"%cli.list[16] + ",1,Por operación\n")

        f.write("MYM,Carvajal,CTS\n") # PREGUNTAR CARVAJAL
        f.write("IAE,12345,999,,Estándar de adopción del contribuyente\n") # PREGUNTAR CARVAJAL
        #f.write("TII," + "%s"%cli.list[21] + ",COP,false\n")
        #f.write("IIM,01," + "%s"%cli.list[21] + ",COP," + "%s"%cli.list[20] + ",COP,19.00\n") # validar IVA
        #f.write("DIT," + "%s"%cli.list[21] + "\n")
        f.write("NTI,\n")
        f.write("NTI,\n")
        f.write("NTI,\n")
        #f.write("ORP," + "%s"%cli.list[0] + "," + payment_date + "\n")

        f.close()