#Colecciones
#Listas
Serplista = ["Boa","Pitón", "Venenosa", "culebra venenosa", "rayada" ]
#Encontar los elementos en una lista Listas
print(Serplista[2])
print(Serplista[0])
#Usar len para contar los elementos
Cantidad_serpientes = len(Serplista)
print(Cantidad_serpientes)
#Acceder a los elementos de la lista
serpiente_uno = Serplista[0]
serpiente_dos = Serplista[1]
print(serpiente_uno,serpiente_dos)
#Modificar los elementos de una lista
Serplista[0] = "Boa Constrictor"
print (Serplista)
Serplista[1] = "Pitón gigante"
print(Serplista)
Serplista[3] = "culebra venenosa de la selva"
print(Serplista)
#Agregar elementos a una lista
Serplista.append("vibora Fucsia")
Serplista.append("vibora marrón, "  "culebra amarilla")
print(Serplista)
#Borrar elementos de una lista
Serplista.remove("vibora Fucsia")
print(Serplista)
#Invertir la lista
Serplista.reverse()
print(Serplista)
#Comprobar si un eleento esta en la lista
print("Pitón" in Serplista)
#Contar el nímero de veces de un elemento en la lista
print(Serplista.count("Boa Constrictor"))