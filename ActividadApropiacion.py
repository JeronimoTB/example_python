'''
#Cajero Electronico
SaldoCajero= 500000
SaldoCuenta = 120000
ValorRetirar = 50000
Contraseña = 8765
NúmeroCuenta = 5000400030002000
TipoCuenta = "Corriente"
print("\n",SaldoCajero,"\n", SaldoCuenta,"\n", ValorRetirar,"\n", Contraseña,"\n", NúmeroCuenta,"\n", TipoCuenta)
'''
'''
#Usar un chat
EstadoAmigo = "Activo"
NombreUsuarios = "JeroToBe"
ContenidoMensaje = "Hola amigo, ¿Como estas?"
print("\n",EstadoAmigo,"\n", NombreUsuarios,"\n", ContenidoMensaje)
'''
'''
#Pagar con tarjeta de credito 
TasaInteres= "20%"
LímiteTarjeta=5000000
Contraseña=5634
NúmeroCuenta = 5000400030001000
NúmeroIdentificación = 30304040786
'''
'''
#Lavar la ropa
Opciones = "Lavadora"
AguaDisponible = "8L"
JabonesDisponibles = 3
DetergentesDisponibles = 2
NumeroCamisas = 6
NumeroPantalones = 3
NumeroMedias = 6
'''
'''
#Hablar por telefono
EstadoAmigo = "No disponible"
NumeroAmigo = 3015749865
SaldoTelefonico = 0
Dinero = 12000
CostoMinutero = 400
ModeloTelefono = "Motorola E20"
ValorRecarga = 3000
'''


Almacen_WC = {
    "Articulo" : "Precio",
    "Zapatos" : 350000,
    "Tenis" : 280000,
    "Camisetas" : 175000,
    "Jeans" : 200000

}
#Muestra en la consola los artículos y precios actuales
print(Almacen_WC)

#También mostrar el costo total de los cuatro artículos
print("El costo total de los cuatro articulos es $", Almacen_WC["Zapatos"]+Almacen_WC["Tenis"]+Almacen_WC["Camisetas"]+Almacen_WC["Jeans"])

#	Además, el promedio de venta
print("El promedio de precios es $",int((Almacen_WC["Zapatos"]+Almacen_WC["Tenis"]+Almacen_WC["Camisetas"]+Almacen_WC["Jeans"])/4))

#	Subir el precio de los Jeans en un 6.2%
print("El aumento de los Jeans en un 6.2% es igual a $", int(Almacen_WC["Jeans"] * 0.062))

#	Disminuir el precio de los Zapatos en un 0.8%
print("La disminucion de los Zapatos en un 0.8% es igual a $", int(Almacen_WC["Jeans"] * 0.008))

#	Por último, mostrar el nuevo valor de los Zapatos y de los Jeans
TasaSubida = int(Almacen_WC["Jeans"] * 0.062)
print("El nuevo precio de los Jeans es $",int(Almacen_WC["Jeans"]+ TasaSubida))


TasaDisminuida = int(Almacen_WC["Zapatos"] * 0.008)
print("El nuevo precio de los Zapatos es $",int(Almacen_WC["Zapatos"] - TasaDisminuida))