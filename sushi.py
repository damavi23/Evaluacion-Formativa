
cuenta = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
while True:
    try:
        print("*******************************")
        print("Escoga su sushi")
        print("1. Pikachu Roll $4500")
        print("2. Otaku Roll $5000")
        print("3. Pulpo Venenoso Roll $5200")
        print("4. Anguila Eléctrica Roll $4800")
        print("5. Codigo de descuento")
        print("6. Detalle del pedido")
        print("*******************************")
        while True:
            try:
                roll = int(input("Ingrese opción: "))
                if roll == 1:
                    contador1 += 1
                    cuenta += 4500
                    print("1. Pikachu Roll:", contador1)
                    print("2. Otaku Roll:", contador2) 
                    print("3. Pulpo Venenoso Roll:", contador3)
                    print("4. Anguila Eléctrica Roll :", contador4)
                elif roll == 2:
                    contador2 += 1
                    cuenta += 5000
                    print("1. Pikachu Roll:", contador1)
                    print("2. Otaku Roll:", contador2) 
                    print("3. Pulpo Venenoso Roll:", contador3)
                    print("4. Anguila Eléctrica Roll :", contador4)
                elif roll == 3:
                    contador3 += 1
                    cuenta += 5200
                    print("1. Pikachu Roll:", contador1)
                    print("2. Otaku Roll:", contador2) 
                    print("3. Pulpo Venenoso Roll:", contador3)
                    print("4. Anguila Eléctrica Roll :", contador4)
                elif roll == 4:
                    contador4 += 1
                    cuenta += 4800
                    print("1. Pikachu Roll:", contador1)
                    print("2. Otaku Roll:", contador2) 
                    print("3. Pulpo Venenoso Roll:", contador3)
                    print("4. Anguila Eléctrica Roll :", contador4)
                elif roll == 5:
                    codigo = input("Ingrese su codigo de descuento: ")
                    if codigo == "soyotaku":
                        print("Tiene 10% de descuento")
                        print("*******************************")
                        print("Escoga su sushi")
                        print("1. Pikachu Roll $4500")
                        print("2. Otaku Roll $5000")
                        print("3. Pulpo Venenoso Roll $5200")
                        print("4. Anguila Eléctrica Roll $4800")
                        print("5. Codigo de descuento")
                        print("6. Detalle del pedido")
                        print("*******************************")
                    elif codigo != "soyotaku":
                        print("Codigo incorrecto")
                        print("(a) Otro codigo")
                        print("(x) Salir")
                        while True:
                            cod = input("Ingrese opción: ")
                            if cod == "a":
                                codigo = input("Ingrese su codigo de descuento: ")
                                if codigo == "soyotaku":
                                    print("Tiene 10% de descuento")
                                    print("*******************************")
                                    print("Escoga su sushi")
                                    print("1. Pikachu Roll $4500")
                                    print("2. Otaku Roll $5000")
                                    print("3. Pulpo Venenoso Roll $5200")
                                    print("4. Anguila Eléctrica Roll $4800")
                                    print("5. Codigo de descuento")
                                    print("6. Detalle del pedido")
                                    print("*******************************")
                                elif codigo != "soyotaku":
                                    print("Codigo incorrecto")
                                    print("(a) Otro codigo")
                                    print("(x) Salir")
                            elif cod == "x":
                                break
                        print("*******************************")
                        print("Escoga su sushi")
                        print("1. Pikachu Roll $4500")
                        print("2. Otaku Roll $5000")
                        print("3. Pulpo Venenoso Roll $5200")
                        print("4. Anguila Eléctrica Roll $4800")
                        print("5. Codigo de descuento")
                        print("6. Detalle del pedido")
                        print("*******************************")
                elif roll == 6:
                    print("*******************************")
                    print("Detalle del pedido")
                    print("*******************************")
                    print("pikachu roll: ", contador1)
                    print("otaku roll: ", contador2)
                    print("pulpo venenoso roll: ", contador3)
                    print("anguila electrica roll: ", contador4)
                    print("*******************************")
                    print("Total a pagar: ", cuenta)
                    if codigo == "soyotaku":
                        cuenta = cuenta - (cuenta * 0.1)
                        print("Total a pagar con descuento: ", cuenta)
                    elif codigo != "soyotaku":
                        print("No aplica descuento")
                    print("*******************************")
                    print("(1) Desea comprar algo mas?")
                    print("(2) Salir")
                    opc = input("Ingrese opción: ")
                    if opc == "1":
                        while True:
                            try:
                                print("*******************************")
                                print("Escoga su sushi")
                                print("1. Pikachu Roll $4500")
                                print("2. Otaku Roll $5000")
                                print("3. Pulpo Venenoso Roll $5200")
                                print("4. Anguila Eléctrica Roll $4800")
                                print("5. Codigo de descuento")
                                print("6. Detalle del pedido")
                                print("*******************************")
                                while True:
                                    try:
                                        roll = int(input("Ingrese opción: "))
                                        if roll == 1:
                                            contador1 += 1
                                            cuenta += 4500
                                            print("1. Pikachu Roll:", contador1)
                                            print("2. Otaku Roll:", contador2) 
                                            print("3. Pulpo Venenoso Roll:", contador3)
                                            print("4. Anguila Eléctrica Roll :", contador4)
                                        elif roll == 2:
                                            contador2 += 1
                                            cuenta += 5000
                                            print("1. Pikachu Roll:", contador1)
                                            print("2. Otaku Roll:", contador2) 
                                            print("3. Pulpo Venenoso Roll:", contador3)
                                            print("4. Anguila Eléctrica Roll :", contador4)
                                        elif roll == 3:
                                            contador3 += 1
                                            cuenta += 5200
                                            print("1. Pikachu Roll:", contador1)
                                            print("2. Otaku Roll:", contador2) 
                                            print("3. Pulpo Venenoso Roll:", contador3)
                                            print("4. Anguila Eléctrica Roll :", contador4)
                                        elif roll == 4:
                                            contador4 += 1
                                            cuenta += 4800
                                            print("1. Pikachu Roll:", contador1)
                                            print("2. Otaku Roll:", contador2) 
                                            print("3. Pulpo Venenoso Roll:", contador3)
                                            print("4. Anguila Eléctrica Roll :", contador4)
                                        elif roll == 5:
                                            codigo = input("Ingrese su codigo de descuento: ")
                                            if codigo == "soyotaku":
                                                print("Tiene 10% de descuento")
                                        elif roll == 6:
                                            print("*******************************")
                                            print("Detalle del pedido")
                                            print("*******************************")
                                            print("pikachu roll: ", contador1)
                                            print("otaku roll: ", contador2)
                                            print("pulpo venenoso roll: ", contador3)
                                            print("anguila electrica roll: ", contador4)
                                            print("*******************************")
                                            print("Total a pagar: ", cuenta)
                                            if codigo == "soyotaku":
                                                cuenta = cuenta - (cuenta * 0.1)
                                                print("Total a pagar con descuento: ", cuenta)
                                            elif codigo != "soyotaku":
                                                print("Total a pagar: ", cuenta)
                                            print("*******************************")
                                            print("(1) Desea comprar algo mas?")
                                            print("(2) Salir")
                                            opc = input("Ingrese opción: ")
                                            if opc == "2":
                                                break
                                    except:
                                        print("Error formato")
                                break
                            except:
                                print("Error formato")    
                    if opc == "2":
                        break                           
            except:
                print("Error formato")
        break
    except:
        print("Error formato")   
