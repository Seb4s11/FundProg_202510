import datetime

#Diccionario de los productos con código, nombre y precio
PRODUCTS = {
    1: {"name": "Galleta", "price": 1200},
    2: {"name": "Botella con Agua", "price": 2500},
    3: {"name": "Paquete de Papas Fritas", "price": 3600},
    4: {"name": "Pan", "price": 900}
}
#Lista de las denominaciones válidas
DENOMINATIONS = [100, 200, 500, 1000, 2000, 5000, 10000]

#Archivo donde estará el historial de cada compra
HISTORIAL_FILE = "Historial__de_compras.txt"

#Programa principal
def main():
    mostrar_bienvenida()
    while True:
        total_money = input_money()
        if total_money is None:
            print("Programa finalizando...\nVuelva pronto :)")
            break

        product_code = select_product()
        if product_code is None:
            continue

        product = PRODUCTS[product_code]
        if validate_payment(total_money, product["price"]):
            print(f"\nUsted ha comprado '{product['name']}' por ${product['price']}")
            print("¡Producto entregado!")
            change = total_money - product["price"]
            return_change(change)
            guardar_historial(product['name'], product['price'], total_money, change)
        else:
            print("Transacción cancelada por fondos insuficientes.")

#Función de mensajes
def mostrar_bienvenida():
    print("\n" + "_" * 55)
    print("  ¡Bienvenido a la Máquina Expendedora!")
    print("  Aquí podrás adquirir productos fácilmente.")
    print("  Aceptamos las siguientes denominaciones:")
    print(" ", DENOMINATIONS)
    print("  Para salir, puedes ingresar -1 en cualquier momento.")
    print("_" * 55 + "\n")

#Función para mostrar los productos
def show_menu():
    print("\n" + "__" * 30)
    print("Productos Disponibles")
    print("Código \t| Precio \t| Nombre")
    print("-" * 40)
    for code, details in PRODUCTS.items():
        print(f"{code} \t\t| ${details['price']} \t| {details['name']}")
    print("__" * 30)

#Función para ingresar el dinero
def input_money():
    total = 0
    print("__" * 30)
    print("\nPor favor, ingrese su dinero.")
    print("Denominaciones válidas:", DENOMINATIONS)
    print("Ingrese -1 para salir, 0 para seleccionar producto.")

    while True:
        try:
            user_input = int(input("Monto: "))
            if user_input == -1:
                return None
            elif user_input == 0:
                break
            elif user_input in DENOMINATIONS:
                total += user_input
                print(f"Saldo actual: ${total}")
            else:
                print("Denominación no válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    return total

#Función para seleccionar el producto
def select_product():
    show_menu()
    while True:
        try:
            code = int(input("Ingrese el código del producto (0 para cancelar): "))
            if code == 0:
                print("Compra cancelada.")
                return None
            if code in PRODUCTS:
                product = PRODUCTS[code]
                print(f"Producto seleccionado: '{product['name']}' - Precio: ${product['price']}")
                return code
            else:
                print("Código inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

#Función para validad el pago
def validate_payment(total, price):
    if total >= price:
        print("Pago aceptado. Procesando compra...")
        return True
    else:
        print(f"Saldo insuficiente. Tiene ${total}, necesita ${price}.")
        return False

#Función para dar el cambio
def return_change(change):
    if change > 0:
        print(f"\nSu cambio es: ${change}")
        denominations = sorted(DENOMINATIONS, reverse = True)
        for denom in denominations:
            count = change // denom
            if count > 0:
                print(f"{count} x ${denom}")
                change %= denom
    else:
        print("No hay cambio. Gracias por su compra.")

#Función que guarda el historial
def guardar_historial(nombre_producto, precio, dinero_ingresado, cambio):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha} | Producto: {nombre_producto} | Precio: ${precio} | Ingresado: ${dinero_ingresado} | Cambio: ${cambio}\n"
    with open("Historial_de_compras.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)

#Ejecución del programa principal
if __name__ == '__main__':
    main()