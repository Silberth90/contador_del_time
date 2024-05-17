import time

def contador():
    tiempo_recreo = 360
    
    # pantalla de inicio del contador
    
    print("=============================================================")
    time.sleep(1)
    print("============Esta por empezar el recreo=======================")
    time.sleep(1)
    print("=============================================================")
    time.sleep(1)
    input("=========preciona ENTER para iniciar el contador=============")


    tiempo_inicial = time.time()
    tiempo_final = tiempo_inicial + tiempo_recreo

    while  time.time() < tiempo_final:
        contador_recreo = time.time() - tiempo_inicial
        tiempo_recreo -= 1

        print(f"Tiempo transcurrido:",tiempo_recreo)
        time.sleep(1)
    print("====Trascurrieron 5 minutos====")

    time.sleep(1)

    print("=======Termico el recreo!========")
contador()