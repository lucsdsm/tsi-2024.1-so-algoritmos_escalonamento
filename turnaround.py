algoritmo = input("Algoritmo desejado (Fifo/SJF/RR): ")

if (algoritmo == "Fifo" or algoritmo == "SJF" or algoritmo == "RR"):
    quantidade_processos = int(input("Quantidade de processos para serem simulados: "))
    lista_tempos = []
    lista_tempos_turnaround = []
    media = 0

    # Digitar os tempos dos processos de acordo com a quantidade de processos.
    for x in range(quantidade_processos):
        tempo_processo = int(input(f"Tempo do processo {x+1}: ")) # Inicia uma variável para armazenar o tempo.
        novo_tempo = [tempo_processo] # Transforma a variável em uma lista.
        lista_tempos = lista_tempos + novo_tempo # Concatena a variável "novo_tempo" com a lista de tempos.

    # Fifo
    if algoritmo == "Fifo":
        # Adiciona à lista de tempos de turnaround levando em consideração apenas os tempos de cada processo com o tempo do processo anterior.
        tempo_turnaround = 0
        for x in lista_tempos:
            tempo_turnaround = tempo_turnaround + x # Adiciona o valor de turnaround ao valor de x.
            lista_tempos_turnaround = lista_tempos_turnaround + [tempo_turnaround] # Concatena a variável "lista_tempos_turnaround" com a variável "tempo_turnaround".

        # Calcular média
        for x in lista_tempos_turnaround:
            media = media + x
        
        media = media / quantidade_processos

        print(f"Seguindo o algoritmo {algoritmo}, os tempos de turnaround de cada processo são: \n{lista_tempos_turnaround}\nA média de tempo para cada processo será de {media:.1f} segundos.")

    # SJF
    elif algoritmo == "SJF":
        for x in lista_tempos:
            turnaround = x
            for y in lista_tempos:
                if x <= y:
                    pass
                elif x > y:
                    turnaround = turnaround + y
                    print(f"{x} > {y}; turnaround = {turnaround}")
            lista_tempos_turnaround = lista_tempos_turnaround + [turnaround]   

        # Calcular média
        for x in lista_tempos_turnaround:
            media = media + x
        
        media = media / quantidade_processos 

        print(f"Seguindo o algoritmo {algoritmo}, os tempos de turnaround de cada processo são: \n{lista_tempos_turnaround}\nA média de tempo para cada processo será de {media:.2f} segundos.")
else:
    print(f"'{algoritmo}' não é um algoritmo válido (Fifo/SJF). Digite um algoritmo válido.")
        