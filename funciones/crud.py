import base_datos.base_datos as bd

def dinero_region(regionnum):
    region=0
    consumo=0
    tarifa=0
    if regionnum == "1":
        tarifa= buscar_tarifa_sopladora("guayaquil")
        consumo= buscar_generador_Sopladora("guayaquil")
        region=consumo*tarifa
        tarifa= buscar_tarifa_coca("guayaquil")
        consumo= buscar_generador_Coca("guayaquil")
        region=region+(consumo*tarifa)
        return region
    elif regionnum == "2":
        tarifa= buscar_tarifa_sopladora("quito")
        consumo= buscar_generador_Sopladora("quito")
        region=consumo*tarifa
        tarifa= buscar_tarifa_sopladora("loja")
        consumo= buscar_generador_Sopladora("loja")
        region=region+(consumo*tarifa)
        tarifa= buscar_tarifa_coca("quito")
        consumo= buscar_generador_Coca("quito")
        region=region+(consumo*tarifa)
        return region
    elif regionnum == "3":
        return 0

def buscar_ciudad(ciudad):
    for h in bd.informacion:
        valor=''
    for valor in h['costa']:
        if valor == ciudad:
            A=valor
            return A
        else:
            continue
    for valor in h['oriente']:
        if valor == ciudad:
            A=valor
            return A
        else:
            continue
    for valor in h['sierra']:
        if valor == ciudad:
            A=valor      
            return A
        else:
            continue
             
    
def buscar_generador_Coca(ciudad):
    for h in bd.consumo_energia: 
        compania=h['Coca Codo Sinclair']
        for m in h['Coca Codo Sinclair']:
            if(m==ciudad):
                cons1=compania[ciudad]
                cons2=cons1['consumos']
                total =sum(cons2) 
                return total
            else:
                continue  
        

def buscar_generador_Sopladora(ciudad):   
    for h in bd.consumo_energia:
        compania=h['Sopladora'] 
        for m in h['Sopladora']:
            if(m==ciudad):
                cons1=compania[ciudad]
                cons2=cons1['consumos']
                total2 =sum(cons2) 
                return total2
            else:
                continue

    
def buscar_tarifa_sopladora(ciudad):
    for h in bd.consumo_energia:
        compania=h['Sopladora'] 
        for m in h['Sopladora']:
            if(m==ciudad):
                cons1=compania[ciudad]
                cons2=cons1['tarifa']
                tarifa=cons2
                return tarifa
            else:
                continue

def buscar_tarifa_coca(ciudad):
    for h in bd.consumo_energia:
        compania=h['Coca Codo Sinclair'] 
        for m in h['Coca Codo Sinclair']:
            if(m==ciudad):
                cons1=compania[ciudad]
                cons2=cons1['tarifa']
                tarifa=cons2
                return tarifa
            else:
                continue

def buscar_generador_Coca_mensual(ciudad,mes):
    for h in bd.consumo_energia: 
        compania=h['Coca Codo Sinclair']
        for m in h['Coca Codo Sinclair']:
            if(m==ciudad):
                cons1=compania[ciudad]
                cons2=cons1['consumos'][mes]
                return cons2
            else:
                continue  

def buscar_generador_Sopladora_mensual(ciudad,mes):   
    for h in bd.consumo_energia:
        compania=h['Sopladora'] 
        for m in h['Sopladora']:
            if(m==ciudad):
                cons1=compania[ciudad]
                cons2=cons1['consumos'][mes]
                return cons2
            else:
                continue

def consumo_mensual(mes):
    mes=int(mes)
    mes=mes-1
    nombre_mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    nombre_mes=nombre_mes[mes]
    consumo_mes=buscar_generador_Coca_mensual("quito",mes)
    tarifa_mes=buscar_tarifa_coca("quito")
    total_mes_coca= consumo_mes*tarifa_mes
    consumo_mes=buscar_generador_Coca_mensual("guayaquil",mes)
    tarifa_mes=buscar_tarifa_coca("guayaquil")
    total_mes_coca= total_mes_coca+(consumo_mes*tarifa_mes)
    consumo_mes=buscar_generador_Sopladora_mensual("guayaquil",mes)
    tarifa_mes=buscar_tarifa_sopladora("guayaquil")
    total_mes_sopladora= consumo_mes*tarifa_mes
    consumo_mes=buscar_generador_Sopladora_mensual("quito",mes)
    tarifa_mes=buscar_tarifa_sopladora("quito")
    total_mes_sopladora= total_mes_sopladora+(consumo_mes*tarifa_mes)
    consumo_mes=buscar_generador_Sopladora_mensual("loja",mes)
    tarifa_mes=buscar_tarifa_sopladora("loja")
    total_mes_sopladora= total_mes_sopladora+(consumo_mes*tarifa_mes)
    total_mensual= total_mes_sopladora+total_mes_coca
    # print("\nLos valores de consumo del mes de",nombre_mes,"son:")
    # print("\nCoca Codo Sinclair: $",total_mes_coca)
    # print("Sopladora: $",total_mes_sopladora)
    # print("\nTOTAL: $", total_mes_sopladora+total_mes_coca)
    return (nombre_mes,total_mes_coca,total_mes_sopladora,total_mensual)
