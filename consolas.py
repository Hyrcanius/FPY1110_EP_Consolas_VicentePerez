consolas = {}
ventas = {}

def menu_int():
    print("======== MENU ========")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")

def agregar_con(consolas, ventas):
    sigla = input("Ingrese la sigla: ")
    val_1 = val_sigla(sigla)
    if val_1 == False:
        print("Ingreso inválido.")
        return
    
    nombre = input("Ingrese el nombre: ").strip()
    val_2 = val_nombre(nombre)
    if val_2 == False:
        print("Ingreso inválido.")
        return

    fabricante = input("Ingrese el fabricante: ").strip()
    val_3 = val_fab(fabricante)
    if val_3 == False:
        print("Ingreso inválido")
        return

    ano = int(input("Ingrese el año: "))
    val_4 = val_ano(ano)
    if val_4 == False:
        print("Ingreso inválido.")
        return

    precio = float(input("Ingrese el precio: "))
    val_5 = val_precio(precio)
    if val_5 == False:
        print("Ingreso inválido.")
        return

    stock = int(input("Ingrese el stock: "))
    val_6 = val_stock(stock)
    if val_6 == False:
        print("Ingreso inválido.")
        return
    
    

def val_sigla(consolas, sigla):
    if len(sigla) < 2 or len(sigla) > 5:
        return False
    
    if sigla.isupper() == False:
        return False
    
    if sigla in consolas:
        return False
    
    return True

def val_nombre(nombre):
    if len(nombre) < 3 or len(nombre) > 40:
        return False

    if not nombre:
        return False
    
    return True

def val_fab(fabricante):
    if len(fabricante) < 2 or len(fabricante) > 30:
        return False
    
    if not fabricante:
        return False
    
    return True

def val_ano(ano):
    if ano < 1972 or ano > 2025:
        return False

    return True

def val_precio(precio):
    if precio <= 0:
        return False
    
    return True

def val_stock(stock):
    if stock < 0:
        return False
    
    return True