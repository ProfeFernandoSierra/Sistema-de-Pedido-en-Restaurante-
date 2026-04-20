# Requerimientos
# 1. Validación del cliente
# Solicitar:
# •	Nombre → entre 3 y 20 caracteres 
# •	Rut (opcional si quieres exigirlo) → largo mínimo 8 caracteres 
# Si no cumple, volver a pedir los datos.
# ________________________________________
import os, time
os.system("cls")
flag = True
pedido = False

while flag:
    os.system("cls")
    print("1. Agregar Pedido")
    print("2. Ver Resumen")
    print("3. Descargar Boleta")
    print("4. Salir")
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            #debo setear la opcion y cantidad cada vez que ingreso, de lo contrario quedara siempre tomada la opcion que elegi en la 1era instancia
            nombre = ""
            rut = ""
            opc_pedido = 0
            cantidad = 0
            print("1. Agregar Pedido")
            os.system("cls")
            while len(nombre) <= 3 or len(nombre) >= 20:
                nombre = input("ingrese su nombre\n")
            while len(rut) < 8 :
                rut = input("ingrese su rut\n")
            
            print("1. Hamburguesa $5000")
            print("2. Pizza $8000")
            print("3. Ensalada $4000")
            while opc_pedido <= 0 or opc_pedido > 3:
                opc_pedido = int(input("ingrese opcion de producto\n"))
            while cantidad <= 0:
                cantidad = int(input("ingrese cantidad de productos\n"))
            if opc_pedido == 1:
                producto = "Hamburguesa"
                monto_producto = 5000
            elif opc_pedido == 2:
                monto_producto = 8000
                producto = "Pizza"
            else:
                monto_producto = 4000
                producto = "Ensalada"
                
            total = monto_producto * cantidad
            pedido = True
            
        elif opcion == 2:
            print("2. Ver Resumen")
            os.system("cls")
            if pedido:
                print("***RESUMEN***")
                print(f"Cliente: {nombre}")
                print(f"Rut: {rut}")
                print(f"Producto: {producto}")
                print(f"Cantidad: {cantidad}")
                print(f"Total a pagar: ${total}")
                
            else:
                print("No existen pedidos para visualizar")
            time.sleep(4)
        elif opcion == 3:
            print("3. Descargar Boleta")
            os.system("cls")
            if pedido:
                #configuracion de archivo
                with open("boleta.txt", "w") as archivo:
                    archivo.write("***BOLETA***\n")
                    archivo.write(f"Cliente: {nombre}\n")
                    archivo.write(f"Rut: {rut}\n")
                    archivo.write(f"Producto: {producto}\n")
                    archivo.write(f"Cantidad: {cantidad}\n")
                    archivo.write(f"Total a pagar: ${total}\n")
                
                print("Gracias por su compra")
                
                
            else:
                print("No existen pedidos para visualizar")
        elif opcion == 4:
            print("4. Salir")
            os.system("cls")
            flag = False
        else:
            print("opcion ingresa no existe, intenta nuevamente")
        
    except:
        print("el valor debe ser un numero entero")
    
print(nombre)
# 2. Menú principal
# Mostrar continuamente el siguiente menú:
# 1. Agregar pedido
# 2. Ver resumen
# 3. Descargar boleta
# 4. Salir
# Validar que la opción ingresada sea correcta (1–4).
# ________________________________________
# 3. Agregar pedido
# Mostrar:
# 1. Hamburguesa ($5000)
# 2. Pizza ($8000)
# 3. Ensalada ($4000)
# •	Validar opción (1–3) 
# •	Pedir cantidad (entre 1 y 10) 
# •	Guardar los pedidos (pueden usar listas o variables simples) 
# ________________________________________
# 4. Ver resumen
# Mostrar:
# •	Nombre del cliente 
# •	Productos agregados 
# •	Cantidades 
# •	Total acumulado 
# ________________________________________
# 5. Descargar boleta 🧾
# Cuando el usuario seleccione esta opción:
# •	Generar un archivo de texto (por ejemplo: boleta.txt) 
# •	El archivo debe contener: 
# Ejemplo:
# --- BOLETA RESTAURANTE ---

# Cliente: Juan Perez

# Detalle:
# Hamburguesa x2 = $10000
# Pizza x1 = $8000

# TOTAL: $18000

# Gracias por su compra
# 🔹 Validaciones:
# •	No permitir descargar boleta si no hay pedidos 
# •	Confirmar antes de generar (S/N) 
# ________________________________________
# 6. Salir
# Finaliza el programa
