consolas = {
    "PS5": ["PlayStation 5", "Sony", 2020]
}
ventas = {
    "PS5": [649990.0, 15]
}

def menu_int():
    print("======== MENU ========")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    op = int(input("-> "))
    return op

def agregar_con(consolas, ventas):
    sigla = input("Ingrese la sigla: ")
    val_1 = val_sigla(consolas,sigla)
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
    
    consolas[sigla] = [nombre, fabricante, ano]
    ventas[sigla] = [precio, stock]

def buscar_con(consolas, ventas):
    sigla = input("Ingrese la sigla: ")
    if sigla in consolas:
        print("=== Consola Encontrada ===")
        print(f"Sigla            :  {sigla}")
        print(f"Nombre           :  {consolas[sigla][0]}")
        print(f"Fabricante       :  {consolas[sigla][1]}")
        print(f"Año lanz.        :  {consolas[sigla][2]}")
        print(f"Precio           :  ${ventas[sigla][0]}")
        print(f"Stock            :  {ventas[sigla][1]} unidades")
    else:
        print("Consola no encontrada.")

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

while True:
    op = menu_int()
    if op == 1:
        agregar_con(consolas,ventas)
    elif op == 2:
        buscar_con(consolas, ventas)
    elif op == 3:
        pass
    elif op == 4:
        pass
    elif op == 5:
        print("Gracias por usar nuestro programa.")
        break