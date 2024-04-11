#SIGNO ZODIACAL



print('Descubre tu signo zodiacal!')


nom = input("Ingresa tu nombre : ").lower() 

día = int(input("Ingresa tu día de nacimiento : "))

mes = input("Ingresa tu mes de nacimiento (ej: abril, mayo, junio): ").lower()

if mes == 'diciembre':
    signo_zodiaco = 'Sagitario' if (día < 22) else 'Capricornio'

elif mes == 'enero':
    signo_zodiaco = 'Capricornio' if (día < 20) else 'Acuario'

elif mes == 'febrero':
    signo_zodiaco = 'Acuario' if (día < 19) else 'Piscis'

elif mes == 'marzo':
    signo_zodiaco = 'Piscis' if (día < 21) else 'Aries'
    
elif mes == 'abril':
    signo_zodiaco = 'Aries' if (día < 20) else 'Tauro'

elif mes == 'mayo':
    signo_zodiaco = 'Tauro' if (día < 21) else 'Géminis'
    
elif mes == 'junio':
    signo_zodiaco = 'Géminis' if (día < 21) else 'Cáncer'

elif mes == 'julio':
    signo_zodiaco = 'Cáncer' if (día < 23) else 'Leo'
    
elif mes == 'agosto':
    signo_zodiaco = 'Leo' if (día < 23) else 'Virgo'

elif mes == 'septiembre':
    signo_zodiaco = 'Virgo' if (día < 23) else 'Libra'

elif mes == 'octubre':
    signo_zodiaco = 'Libra' if (día < 23) else 'Escorpio'
    
elif mes == 'noviembre':
    signo_zodiaco = 'Escorpio' if (día < 22) else 'Sagitario'


print( "Hola,",  nom , "Tu Signo Zodiacal es :" , signo_zodiaco)
input("Presiona 'ENTER' para cerrar el programa.")
