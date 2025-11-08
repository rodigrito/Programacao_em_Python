def system():
    alunos = []
    notas  = []

    insert = input('deseja inserir as notas')
    while insert ==  's':
          nome = input('Digite o nome do aluno')
          nota = int(input('nota: '))   
          notas.append(nota)
          alunos.append(nome) 
          insert = input('deseja inserir as notas')

          print(f'''Alunos: {alunos}  - Notas  {notas}''')
          m1 = media(notas)
          m2 = mediana(notas)
          print('Media', m1,'mediana',  m2)
          moda  =  mode(notas )
          print(moda)


        #   d1 = desvio(notas)
        #   m3 = mod(notas)
        #   print(d1, m3)
          



    else: 
       pass
        #  m1 = media(notas)
        #  m2 = mediana(notas)
        #  m3 = moda(nota)
        #  d1 = desvio(notas)
        #  print(m1, m2, m3,d1)
         
          

            # print(f'MEDIA -  {media1}MODA - {moda1}MEDIANA- {mediana1}DESVIO - {desvio1}')                  


system()    
    


     




from statistics import mean


def media(lista):
    media  =  mean(lista)
    return media
