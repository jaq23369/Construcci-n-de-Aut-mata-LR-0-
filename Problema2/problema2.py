# FUNCIÓN CERRADURA LR(0)

def imprimir_item(item):
    cabeza, cuerpo, punto = item
    cuerpo_lista = list(cuerpo)
    cuerpo_lista.insert(punto, ".")
    return f"{cabeza} -> {' '.join(cuerpo_lista)}"

def ingresar_gramatica():
    print("\n--- PASO 1: INGRESO DE GRAMÁTICA ---")
    print("Ingrese las producciones. Formato: Cabeza -> cuerpo separado por espacios")
    print("Ejemplo: S -> S S +")
    print("Escriba 'fin' cuando haya terminado de ingresar todas las reglas.\n")
    
    gramatica = {}
    while True:
        linea = input("Regla > ").strip()
        if linea.lower() == 'fin':
            break
        
        if '->' in linea:
            partes = linea.split('->')
            cabeza = partes[0].strip()
            cuerpo = partes[1].strip().split() 
            
            if cabeza not in gramatica:
                gramatica[cabeza] = []
            gramatica[cabeza].append(cuerpo)
        else:
            print("Formato inválido. Recuerde usar '->'.")
            
    return gramatica

def ingresar_items_iniciales():
    print("\n--- PASO 2: INGRESO DE ÍTEMS INICIALES (NÚCLEO) ---")
    print("Ingrese los ítems base uno por uno. Escriba 'fin' en el símbolo izquierdo para terminar.")
    
    items = []
    while True:
        cabeza = input("Símbolo izquierdo (Ej: S') [o 'fin' para calcular]: ").strip()
        if cabeza.lower() == 'fin':
            break
            
        cuerpo = input("Símbolos derechos separados por espacios (Ej: S): ").strip().split()
        punto = int(input("Posición del punto (Número entero, Ej: 0): ").strip())
        

        items.append((cabeza, tuple(cuerpo), punto))
        print("  -> Ítem agregado al conjunto. Ingrese el siguiente o escriba 'fin'.\n")
        
    return items

def cerradura(items_iniciales, gramatica):
    resultado = list(items_iniciales)
    agregados = set() 
    
    for item in resultado:
        agregados.add(str(item))

    print("\n=== CONJUNTO INICIAL ===")
    for item in resultado:
        print(f"  {imprimir_item(item)}")
    print("========================\n")

    cambio = True
    paso = 1

    while cambio:
        cambio = False
        
        for cabeza, cuerpo, punto in resultado:
            if punto < len(cuerpo):
                simbolo = cuerpo[punto] 
                
                # Si el símbolo después del punto es un NO TERMINAL
                if simbolo in gramatica:
                    print(f"[Paso {paso}] Evaluando '{simbolo}' en {imprimir_item((cabeza, cuerpo, punto))}:")
                    
                    for produccion in gramatica[simbolo]:
                        nuevo_item = (simbolo, tuple(produccion), 0)
                        
                        if str(nuevo_item) not in agregados:
                            resultado.append(nuevo_item)
                            agregados.add(str(nuevo_item))
                            cambio = True
                            print(f"  + AGREGADO: {imprimir_item(nuevo_item)}")
                        else:
                            print(f" (Ya existe): {imprimir_item(nuevo_item)}")
                    print("") 
        if cambio:
            paso += 1

    print("=== CERRADURA FINAL COMPLETA ===")
    for item in resultado:
        print(f"  {imprimir_item(item)}")
    print("================================\n")
    
    return resultado



# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    print("Cerraduras LR(0)")
    
    # Ingresar la gramática
    gramatica_usuario = ingresar_gramatica()
    
    # Ingresar la LISTA de ítems iniciales (uno o varios)
    items_iniciales = ingresar_items_iniciales()
    
    # Calcular y mostrar
    if not items_iniciales:
        print("\nNo ingresaste ningún ítem. Saliendo del programa...")
    else:
        print("\nCalculando Cerradura...")
        cerradura(items_iniciales, gramatica_usuario)