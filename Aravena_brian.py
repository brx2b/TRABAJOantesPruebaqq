#DECLARAMOS LAS VARIABLES A USAAAR

Nresa="SUSHI KILLER"  #NOMBRE DEL DELIVERY, EMPRESA O COMPAÑIA

elec=0
t1=0
t2=0
t3=0
t4=0

import time
import random

pikachuroll=4500
otakuroll=5000
pulpovenenoso=5200
anguilaelectrica=4800

print("---Bienvenido a nuestro local", Nresa,"--- \n") #BIENVENIDA Y EL NOMBRE DEl DELIVERY o "empresa"

while True:
    try:
       
        print("1) Pikachu Roll $4500 \n2) Otaku Roll $5000 \n3) Pulpo venenoso Roll $5200 \n4) Anguila Eléctrica Roll $4800 \n5) Salir del programa (Ver total final a pagar) \n")
        elec=int(input("Ingresa la opción deseada: ")) #INGRESA LA OPCIÓN DESEADA
    except:
     print("Error ingrese un valor válido") #en caso de error mostrar este mensaje...
    if elec==1:
        print("\n**USTED SELECCIONO PIKACHU MOLIDO ROLL**") #Muestra la elección
        try:   
         cant1=int(input(f"Ingrese la cantidad deseada de este elemento(${pikachuroll}): \n")) #CUANTOS DESEA
         t1=cant1*pikachuroll   #SE MULTIPLICA LA CANTIDAD POR EL PRECIO DEL PIKACHU MOLIDO
         print(f"Saldrá ${t1} en total\n")  #SE MUESTRA EL TOTAL
        except:
            print("Ingresa un valor válido") #en caso de error mostrar este mensaje...
        
    elif elec==2:
        print("**USTED SELECCIONO OTAKU ROLL**")
        try:
            cant2=int(input(f"Ingrese la cantidad deseada de este elemento(${otakuroll}): \n"))
            t2=cant2*otakuroll
            print(f"Saldrá ${t2} en total\n")
        except:
            print("Ingrese un valor válido")#en caso de error mostrar este mensaje...


    elif elec==3:
        print("**USTED SELECCIONO PULPO VENENOSO ROLL (probabilidad de morir)")
        try:
            cant3=int(input(f"Ingrese la cantidad deseada de este elemento(${pulpovenenoso}): \n"))
            t3=cant3*otakuroll
            print(f"Saldrá ${t3} en total\n")
        except:
            print("Ingrese un valor válido")#en caso de error mostrar este mensaje...


    elif elec==4:
        print("**USTED SELECCIONO ANGUILA ELÉCTRICA (un poco picante)")
        try:
            cant4=int(input(f"Ingrese la cantidad deseada de este elemento(${anguilaelectrica}): \n"))
            t4=cant4*otakuroll
            print(f"Saldrá ${t4} en total\n")
        except:
            print("Ingrese un valor válido")#en caso de error mostrar este mensaje...


    elif elec==5:
        print(f"Gracias por preferir nuestro menú! \n siempre seras bienvenido en {Nresa}") #En caso de seleccionar salir se mostrara el mensaje

        break
print("Espere mientras calculamos su total a pagar...\n") #Al salir del programa se mostrara este mensaje y habra un tiempo random para mostrar el precio total final
tf=t1+t2+t3+t4 #se suman todos los precios
tiempR=random.randint(3, 10) #Se declarara la variable del random
time.sleep(tiempR) #Hace que se pause o haya un tiempo de espera dependiendo de la variable tiempR que puede variar entre 3 y 10 segundos

print(f"PRECIO TOTAL FINAL: ${tf}") #Muentra finalmente el total de todo el pedido realizado por el usuario

#HECHO POR BRIAN ARAVENA INGENiERÍA EN INFORMÁTICA
#09-05-2024 
#20-747-180-1 RUT