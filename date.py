# Como importar datetime (Python lo trae por defecto)
from datetime import datetime

#Establecer una fecha mediante datetime, tiene multiples usos y puede ser altamente exacto su formato es: (año, mes, dia, hora, minuto, segundo, micorsegundo)
birthday = datetime(2005, 9, 26, 2, 25, 12)

#se puede hacer uso de uno de los datos especificos almacenados en una variable igual a un datetime
print(birthday)
print(birthday.day)
print(birthday.month)
print(birthday.weekday())

#El siguiente modulo permite usar el datetime para saber la hora en el momento que es ejecutado
this_moment = datetime.now()
print(this_moment)

#Los datetime se pueden restar entre si para determinar cuanto tiempo hay en dos fechas
age_difference = datetime(2007, 4, 6) - datetime(2005, 9, 26)
print(age_difference)

age_of_this_year = datetime.now() - datetime(2023, 1 , 1)
print(age_of_this_year)

time_of_live = datetime.now() - datetime(2005, 9, 26)
print(time_of_live)

#strptime como el nombre lo dice permite pasar una string independientemente de como este escrita al formato de almacenar hora de python
#sigue un formato muy especial que a continuacion voy a demostrara, es necesario entrar a la web de python para saber como estan almacenados
#los comandos para cada formato de referirse a una fecha en especifico datetime.strptime("las fecha en string", "una string que le dice al programa como lidiar como la anterior string")

parsed_date = datetime.strptime("Jan 15, 2018","%b %d, %Y")
print(parsed_date)

#se puede hacer lo mismo que el anterior

print(parsed_date.month)

#strftime perimite pasar un datetime a una string:

example = datetime.strftime(datetime.now(), "%b %d, %Y")

the_day = datetime(2023, 9, 10) - datetime.now()
print(the_day)