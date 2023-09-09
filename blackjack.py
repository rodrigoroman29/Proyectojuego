#Carlos Rodrigo Roman Flores #A00838197
#Este es un programa que intenta replicar el famoso juego de black jack

lista = []
lista2 = []
lista3 = []

DineroTotal = 200

def random():
    import random
    n = random.randint(1,13)
    return n


def OneMore():
    C=random()
    
    if C==11 or C==12 or C==13 :       
        C=10
        lista.insert((len(lista)),(C))
                    
    else : 
        lista.insert((len(lista)),(C))
    print(lista)
    
    
def doble(opcion,apuesta):   
    C=random()
    
    if C==11 or C==12 or C==13 :       
        C=10
        lista.insert((len(lista)),(C))
                    
    else :
        lista.insert((len(lista)),(C))       
        
    apuesta += (apuesta*2)
    opcion = 0
    
    return (opcion,apuesta)


## preguntas mate
            

##Variables Start         
count = 0
count2=0
CartaOponete = 0
x = 0
y = 2

countEx=0

sumaLista = 0
sumaLista3= 0

apuesta = 0

## Start

print('Bienvenido!       - Para Salir presione 5')
while True:
    print('ˆˆˆˆˆˆˆˆ\n')
    if count2 == 0:
        print('* NUEVA MANO:')
        print('Saldo: ', DineroTotal)
        apuesta = (int(input('Introduce la cantidad que apostaras: $')))
        if apuesta > DineroTotal:
            print('lo siento  fueiste despachado del casino por falta de dinero')
            break
        else:
            DineroTotal -=  apuesta
        print()
        count2+=1
        
    for i in range(0,y):
        C=random()
        C2=random()       
            
        if C==11 or C==12 or C==13 :      
            count = count+1 
            C=10
            lista.insert((len(lista)),(C))            
                     
        else :
            count = count+1 
            lista.insert((len(lista)),(C))
            
        if count != 1:
            print('Tu: ',lista)
            
 # Start Oponente:
        if count == 1:    

            CartaOponete = C2
            if CartaOponete ==11 or CartaOponete ==12 or CartaOponete ==13:
                CartaOponete = 10
                    
            lista2.insert(len(lista2),CartaOponete)
                
            lista2.insert(len(lista2),'?')
            print('- Oponente: ',lista2)
        count += 1    

        
    if x >= 1:
        print('\n\n')
        print('- Oponente:',lista2)
        print('- Tus Cartas : ',lista)
    x += 1
    
##inicio del menu principal
    
    print()   
    print('Opciones')
    print('0. Stand')
    print('1. Hit')
    print('2. Doble') 
    try:
        opcion = int(input('Opción: '))
        
    except ValueError:
        opcion = -1        
        
    if opcion == 5:
        print('Gracias por usar la app, Lo esperamos pronto.')
        break          
  
    elif opcion == 1:
        OneMore()
        y = 0
        
    elif opcion == 2:
        opcion,apuesta = doble(opcion,apuesta)
 
 #cierre 
    if opcion == 0:       
        lista3.insert(len(lista3),CartaOponete)      
        for i in lista3:
            sumaLista3 += i
            
        C2= random()
        
        if C2==11 or C2==12 or C2==13 :  
            C2 = 10
            lista3.insert(len(lista3),C2)
          
        elif 1 == C2:
            if (sumaLista3+10) <= 21:
                C2 = 11
            else:
                C2 = 1 
                
        else:
            lista3.insert(len(lista3),C2)
            
        sumaLista3=0
        
        for i in lista3:
            sumaLista3 += i
     
        while sumaLista3 < 17:
            C2= random()
            
            if C2==11 or C2==12 or C2==13 :
                C2 = 10
                lista3.insert(len(lista3),C2)
                sumaLista3+=C2
               
            elif 1 == C2:
                if (sumaLista3+10) <= 21:
                    C2 = 11
                    lista3.insert(len(lista3),C2)
                    sumaLista3+=C2
                else:
                    C2 = 1
                    lista3.insert(len(lista3),C2)
                    sumaLista3+=C2
                
            else:
                lista3.insert(len(lista3),C2)
                sumaLista3+=C2


    #filtros para Ases
        sumaLista=0
        for i in lista:
            sumaLista += i
            
        sumaLista3=0    
        for i in lista3:
            sumaLista3 += i
            
        if 1 in lista: 
            ind = (lista.index(1))
            if (sumaLista+10) <= 21:
                lista[ind] = 11                
                
        if 1 in lista3:
            ind = (lista3.index(1))
            if (sumaLista3+10) <= 21:
                lista3[ind] = 11               
                
        sumaLista=0           
        for i in lista:
            sumaLista += i
            
        sumaLista3=0            
        for i in lista3:
            sumaLista3 += i
            
   
        print('Resultados - Oponente: ', lista3)
        print('Resultados - Tu: ',lista)
        
        x=0        
        
        if sumaLista > 21:
            print('Perdiste         - Para Salir presione 5.')
            
        elif sumaLista3 > 21:
            DineroTotal = DineroTotal + apuesta*2
            print('Ganaste!         - Para Salir presione 5.')            
               
        elif sumaLista > sumaLista3 and sumaLista <= 21:
            DineroTotal = DineroTotal + apuesta*2
            print('Ganaste!- Para Salir presione 5.')
            
        elif sumaLista3 > sumaLista and sumaLista3 <= 21:
            
            print('Perdiste         - Para Salir presione 5.')
            
        elif sumaLista3 == sumaLista:
            print('  Push           - Para Salir presione 5.')  

        else :
            pass
        
        
        if DineroTotal <= 0:
            respuesta=input('Te gustaria jugar un juego para ganar dinero? si/no')
            if respuesta == 'no':
                break
                        
            elif respuesta == 'si':
                import turtle
                bob = turtle
        
                bob.speed(0)
                bob.ht()
                bob.lt(180)
                bob.penup()
                bob.fd(200)

                bob.pendown()


                def casa():
                    bob.rt(90)
                    bob.fd(40)
                    bob.lt(90)
                    
                    bob.fd(35)
                    bob.rt(120)
                    bob.fd(35)
                    bob.rt(120)
                    bob.fd(35)
                    
                    bob.lt(240)

                    bob.fd(35)
                    bob.lt(90)
                    
                    bob.fd(40)
                    bob.lt(90)
                    bob.fd(35)
                
                def jardin():
                    for i in range(20):
                        bob.rt(75)
                        bob.fd(10)
                        bob.rt(135)
                        bob.fd(10)
                        bob.lt(35)
                        bob.lt(175)
                        
                casa()
                bob.lt(142.5)    
                jardin()

                bob.lt(220)
                bob.fd(40)

                bob.lt(179)

                casa()


                bob.lt(142.5)    
                jardin()


                bob.rt(142.5)



               ##castillo

                def triangulo():
                    bob.fd(35)
                    bob.lt(120)
                    bob.fd(35)
                    bob.lt(120)
                    bob.fd(35)

                        
                def torre():
                    
                    bob.fd(70)
                    bob.lt(90)
                    
                    bob.fd(35)
                    bob.rt(120)
                    bob.fd(35)
                    bob.rt(120)
                    bob.fd(35)
                    
                    bob.lt(240)

                    bob.fd(35)
                    bob.lt(90)
                    
                    bob.fd(70)
                    bob.lt(90)
                    bob.fd(35)
                    


                def barda():
                    for i in range(7):
                        bob.lt(90)
                        bob.fd(5)
                        bob.rt(90)
                        bob.fd(5) 
                        bob.lt(90)
                        bob.fd(5)
                        bob.lt(90)
                        bob.fd(5)
                        bob.lt(180)
                        
                        
                bob.lt(90)    
                torre()
                bob.fd(106)

                bob.lt(90)
                torre()

                bob.lt(180)
                bob.fd(35)
                bob.rt(90)
                bob.fd(45)

                barda()

                bob.lt(90)
                bob.penup()
                bob.fd(400)
                bob.lt(90)
                bob.fd(44)
                bob.lt(90)
                bob.fd(20)
                
                bob.st()
                bob.shape('turtle')
                                                
                countT=0
                countF=0
                countS=0
                puntos = 0

                def avanzar():
                    import turtle
                    bob = turtle
                    bob.speed(1)
                    bob.fd(195)

                def regreso():
                    import turtle
                    bob.lt(180)
                    bob.fd(195)
                    bob.lt(180)


                def first(puntos,countF):
                        if countF == 0:
                            print('5x - 2 = 2x + 7')
                            R = input('Cual es el valor de X? ')
                            
                            if R == '3':
                                puntos += 1
                                avanzar()

                            
                        elif  countF == 1:
                            print('1+2*5ˆ2')
                            R = input('Cual es la respuesta: ')
                            if R == '51':
                                puntos += 1
                                avanzar()
                                
                        elif countF == 2:
                            print('Si tres ninos cazan tres conejos en tres minutos')
                            R = input('Cuanto tardara treita ninos en cazar treita conejos?')
                            if R == '3':
                                puntos += 1
                                avanzar()
                            
                        elif countF == 3:
                            print('Pan , pan y pan,pan y pan y medio,cuatro medios panes y tres panes y medio.')
                            R = input('Cuantos panes  son? ')
                            if R == '3':
                                puntos += 1
                                avanzar()
                                                
                        countF+=1    
                        return (puntos,countF)
                                    
                def second(puntos,countS):
                    ##este si llevara yn else para restar -1 si la respuesta es in correcta
                        if countS == 0:
                            print('[6,2,12]\n[4,5,20]\n[24,10,?]')
                            R = input('Cual es el valor del numero faltante')
                            if R == '240':
                                puntos += 1
                                avanzar()
                            else:
                                regreso()
                                puntos-=1
                            
                        elif  countS == 1:
                            print('El monstruo del lago Ness mide 80 metros más la mitad de lo que mide, ¿cuánto mide el monstruo del lago Ness?')
                            R = input('Cual es la respuesta: ')
                            if R == '160':
                                avanzar()
                                puntos += 1
                            else:
                                puntos-=1
                                regreso()
                                
                        elif countS == 2:
                            print('@ + @ + @ = 60\n @ + $ + $ = 30\n$ - & \n& + @ x $ =?')
                            R = input('Cual es el valor del numero faltante')
                            if R == '207':
                                avanzar()
                                puntos += 1
                            else:
                                puntos-=1
                                regreso()
                            
                        elif countS == 3:
                            print('A cuanto equibale el numero pi')
                            R = input('Cual es la respuesta: ')
                            if R == '3.141592':
                                avanzar()
                                puntos += 1
                            else:
                                puntos-=1
                                regreso()
                                
                        countS+=1    
                        return (puntos,countS)
                  
                def third(puntos,countT):
                    ##este si llevara yn else para restar -1 si la respuesta es in correcta
                        if countT == 0:
                            print('Alberto, Benjamin y Carlota hicieron un total de 20 sandwiches.\n  Benjamín hizo 3 veces más que Alberto, y Carlota hizo el doble que Benjamín.')
                            R = input('¿Cuántos sándwiches hizo Alberto?')
                            if R == '2':
                                puntos += 1
                                bob.lt(360)
                                
                            else:
                                puntos-=1
                                regreso()
                            
                        elif  countT == 1:
                            print('Si 10 + x es 5 más que 10,')
                            R = input('¿cuál es el valor de 2x?')
                            if R == '10':
                                bob.lt(360)
                                puntos += 1
                            else:
                                puntos-=1
                                regreso()
                                
                        elif countT == 2:
                            print('adivina cuanto  anos tengos abiendo  que la tercera parte \n de ellos menos 1 es igual a  la  sexta parte?')
                            R = input('Cual es el valor del numero faltante')
                            if R == '6':
                                print('P')
                                bob.lt(360)
                                puntos += 1
                            else:
                                puntos-=1
                                regreso()
                            
                        elif countT == 3:
                            print('7/5+2/3-1')
                            print('Expresa tu resultado en fracciones')
                            R = input('16/15')
                            if R == '3':
                                bob.lt(360)
                                puntos += 1
                            else:
                                puntos-=1
                                regreso()
                                
                        countT+=1    
                        return (puntos,countT)
                  

                
                while puntos < 3:   ##Cada  vez que  saques  una repuesta bien te podras
                    ## dar cuenta que la tortuga  avanzahasta  llegar   a su  castillo 
                    if  puntos == 0:
                        puntos,countF= first(puntos,countF)
                        print('estos  son   tus puntos',puntos)
                    
                    
                    if puntos == 1:
                        print('Pasate de nivel al dos')
                        puntos,countS= second(puntos,countS)
                        print(' estos  son   tus puntos',puntos)
                    
                    if puntos == 2:
                        print('Pasate de nivel tres')
                        puntos,countT = third(puntos,countT)
                        print(' estos  son   tus puntos',puntos)
                        
                    if puntos == 3:
                        print('Ganste el juego Bob a llegado a su castillo!')
                        print('Te has ganado $100 para jugar  Black Jack')
                        bob.lt(180)
                        avanzar()
                        avanzar()
                        bob.lt(180)
                        
                       
                        ##turtle avanza de nivel
                        
                    
                     ## esto para que la segunda vez que juega tenga que evolver a juntar puntos
                    
                DineroTotal += 100
                puntos = 0

                print('Bienvendido al Black Jack')
        lista=[]
        lista2=[]
        lista3=[]
        count=0
        count2=0
        y = 2
        sumaLista=0
        sumaLista3=0
        import turtle
bob = turtle

bob.speed(0)
bob.ht()
bob.lt(180)
bob.penup()
bob.fd(200)

bob.pendown()


def casa():
    bob.rt(90)
    bob.fd(40)
    bob.lt(90)
    
    bob.fd(35)
    bob.rt(120)
    bob.fd(35)
    bob.rt(120)
    bob.fd(35)
    
    bob.lt(240)

    bob.fd(35)
    bob.lt(90)
    
    bob.fd(40)
    bob.lt(90)
    bob.fd(35)

def jardin():
    for i in range(20):
        bob.rt(75)
        bob.fd(10)
        bob.rt(135)
        bob.fd(10)
        bob.lt(35)
        bob.lt(175)
        
    

casa()
bob.lt(142.5)    
jardin()

bob.lt(220)
bob.fd(40)

bob.lt(179)

casa()


bob.lt(142.5)    
jardin()


bob.rt(142.5)


   
##castillo


def triangulo():
    bob.fd(35)
    bob.lt(120)
    bob.fd(35)
    bob.lt(120)
    bob.fd(35)

        
def torre():
    
    bob.fd(70)
    bob.lt(90)
    
    bob.fd(35)
    bob.rt(120)
    bob.fd(35)
    bob.rt(120)
    bob.fd(35)
    
    bob.lt(240)

    bob.fd(35)
    bob.lt(90)
    
    bob.fd(70)
    bob.lt(90)
    bob.fd(35)
    


def barda():
    for i in range(7):
        bob.lt(90)
        bob.fd(5)
        bob.rt(90)
        bob.fd(5) 
        bob.lt(90)
        bob.fd(5)
        bob.lt(90)
        bob.fd(5)
        bob.lt(180)
        

        
bob.lt(90)    
torre()
bob.fd(106)

bob.lt(90)
torre()

bob.lt(180)
bob.fd(35)
bob.rt(90)
bob.fd(45)

barda()


bob.lt(90)
bob.penup()
bob.fd(400)
bob.lt(90)
bob.fd(44)
bob.lt(90)
bob.fd(20)

bob.st()
bob.shape('turtle')

def avanzar():
    bob.speed(1)
    bob.fd(195)

    
avanzar()

## este for es de celebracion
bob.lt(360)
avanzar()

## este while es de celebracion
R=False 

while R == False:
    bob.lt(360)
    ##cuando le pique continuear se saldra del loop
    R= bool(input('Quieres Continuar? True\False '))