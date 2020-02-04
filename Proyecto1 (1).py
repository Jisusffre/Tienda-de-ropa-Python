#-*_coding: utf-8 -*-
import time
class Usuario:
	"""Esta clase nos sirve como representante de 
	   todos aquellos que ingresen al menú"""
	def __init__(self,nombre,apellido,edad,correo,numTarjeta,correoPaypal,contraseñaPaypal,username,contraseña):
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.correo=correo
		self.numTarjeta=numTarjeta
		self.correoPaypal=correoPaypal
		self.contraseñaPaypal=contraseñaPaypal
		self.username=username
		self.contraseña=contraseña

def Registrar():
	"""Esta función nos sirve para registrar al cliente, contando con todas las
		validaciones que se deben hacer"""
	wh=1
	while (wh==1):
		print('****************************************************************')
		print('\nR E G I S T R O')
		print('\nSe debe registrar con un nombre de usuario que cuente ')
		print('de 6-12 letras o numeros. No se permiten caracteres ')
		print('que no sean letras o numeros. También debe registrase ')
		print('con una contraseña de mínimo 10 caracteres. Debe ')
		print('contener, al menos, una letra minúscula y una mayúscula,')
		print('números y un caracter especial.')
		"""En esta parte validamos que el usuario meta el numero correcto de caracteres
		y que sea alfanumerico"""
		wh1=1
		while(wh1==1):
			error=0
			username=input('\nNombre de Usuario:')
			if(len(username)<6):
				print('\nEl nombre se usuario tiene menos de 6 caracteres')
			elif(len(username)>12):
				print('\nEl nombre de usuario tiene más de 12 caracteres')
			else:
				for x in range(len(username)):
					if(ord(username[x:x+1])<48 or ord(username[x:x+1])>122):
						if(ord(username[x:x+1])!=241 and ord(username[x:x+1])!=209):
							print('\nEL NOMBRE DE USUARIO SOLO DEBE TENER NUMERO Y LETRAS')
							error=1
							break
				if(error!=1):
					wh1=0
		"""En esta parte validamos que el usuario meta bien la contraseña"""
		wh1=1
		while(wh1==1):
			contador=0
			contraseña=input('\nContraseña:')
			if(len(contraseña)<10):
				print('\nLA CONTRASEÑA DEBE TENER, MINIMO, 10 CARACTERES')
			else:
				for x in range(len(contraseña)):
					if(ord(contraseña[x:x+1])!=209 or ord(contraseña[x:x+1])!=241):
						if(ord(contraseña[x:x+1])>=33 and ord(contraseña[x:x+1])<=126 ):
							contador=contador+1
				if(contador!=len(contraseña)):
					print('\nLA CONTRASEÑA DEBE TENER AL MENOS UN CARACTER')
					print('ESPECIAL, UN NUMERO, UNA LETRA MAYUSCULA Y UNA ')
					print('LETRA MINUSCULA, SIN ESPACIOS')
				else:
					print('CONTRASEÑA VALIDA')
					wh1=0
		"""En esta parte se meten los datos del usuario y verificamos que sólo escriba su nombre"""
		wh1=1
		print('************************************************************')
		print('\nEscribe información veridica')
		while(wh1==1):
			error=0
			nombre=input('Nombre:')
			for x in range(len(nombre)):
					if(ord(nombre[x:x+1])==32):
						print('SOLO ESCRIBE TU NOMBRE, SIN APELLIDOS')
						error=1
						break
			if(error!=1):
				wh1=0
		apellido=input('Apellido:')
		wh1=1
		while(wh1==1):
			try:
				edad=int(input('Edad:'))
				wh1=0
			except ValueError:
				print('\nMETE UN NUMERO')
		wh1=1
		while(wh1==1):
			error=1
			correo=input('Correo:')
			for x in range(len(correo)):
				if(ord(correo[x:x+1])==64):
					error=1
					for y in range(x,len(correo)):
						if(correo[y:y+4]=='.com'or correo[y:y+3]=='.mx'):
							error=0
			if(error==1):
				print('\nTE FALTA EL '+chr(64)+' O EL .com')
			else:
				print('CORREO VALIDO')
				wh1=0	
		wh1=1
		while(wh1==1):
			try:
				numTarjeta=int(input('Número de tarjeta:'))
				wh1=0
			except ValueError:
				print('\nMETISTE UNA LETRA')

		wh1=1
		while(wh1==1):
			error=1
			correoPaypal=input('Correo de Paypal:')
			for x in range(len(correoPaypal)):
				if(ord(correoPaypal[x:x+1])==64):
					error=1
					for y in range(x,len(correoPaypal)):
						if(correoPaypal[y:y+4]=='.com' or correoPaypal[y:y+3]=='.mx'):
							error=0
			if(error==1):
				print('\nTE FALTA EL '+chr(64)+' O EL .com')
			else:
				print('CORREO VALIDO')
				wh1=0	

		contraseñaPaypal=input('Contrasela de Paypal:')
		wh=0		
		usuario=Usuario(nombre,apellido,edad,correo,numTarjeta,correoPaypal,contraseñaPaypal,username,contraseña)
		return usuario
"""En esta función ingresamos con el username y la contraseña, si no se encuentran
	se le notifica al usuario"""
def Ingresar(listaProductos):
	username=input('Nombre de usuario:')
	if(username in usuarios):
		contraseña=input('\nContraseña:')
		"""Si ingresa procederemos con la compra"""
		if(contraseña in usuarios2):
			carrito = Carrito({}, 0)
			comprando = True
			while(comprando):
				print('================')
				print('LISTA DE ARTICULOS.')
				for producto in listaProductos:
					producto.imprimirProducto()
					time.sleep(1)
				print('=====================')
				print('\n\nEscribe los datos requeridos.')
				clave = input('Ingresa la clave asociada a tu producto: ')
				encontrado = False
				for producto in listaProductos:
					"""Revisamos que la clave y el inventario
					esten en condiciones"""
					if producto.clave == clave and producto.revisarInventario():
						print('El producto existe.')
						print('Quieres agregarlo a tu carrito? ')
						print('1.- SI,')
						print('2.- Cualquier otra entrada se tomara como un NO.')
						opcion = input('Opcion: ')
						if opcion == '1':
							carrito.agregar(producto, producto.getClave())
							producto.setClave(producto.inventario)
							producto.reducirInventario()
							carrito.setTotal(producto.precio)
						encontrado = True
						break
					#else:
						#print('El producto no existe.')
				"""encontrado es un valor booleano que indica 
				si la clave del producto es correcta"""
				if encontrado:
					#proceder a la compra
					carrito.imprimirCarrito()
				else:
					print('El articulo descrito no existe o se encuentra agotado.')
					#Pedir un nuevo intento
				print('Deceas revisar otro articulo? ')
				print('1.- SI,')
				print('2.- Cualquier otra entrada se tomara como un NO.')
				opcion = input('Opcion: ')
				if opcion == '1':
					comprando = True
				else:
					comprando = False
			if len(carrito.articulos) != 0:
				print('<=================>')
				print('PAGO DE ARTICULOS.')
				carrito.imprimirCarrito()
				confirmacion = input('Presiona 1 para confirmar la compra, cualquier otra entrada cancelara la compra: ')
				if confirmacion == '1':	
					continuar = True
					while(continuar):
						correo = input('Ingresa tu correo electronico de PayPal: ')
						contraseña = input('Ingresa tu contraseña: ')
						"""Se validan los datos asociados a la cuenta de paypal
						tenemos que cuidar una excepcion para las claves que 
						ingrese el usuario"""
						try:
							if usuarios2[contraseña].correoPaypal and usuarios2[contraseña].contraseñaPaypal:
								print('El total de articulos esta siendo cargado')
								print('Compra confirmada, vuelva pronto.')
							else:
								print('Correo o contraseña no valida, prueba registrarte antes.')
						except KeyError:
							print('Error en la validacion, revisa los datos.')
							datos = input('Quieres volver a intentarlo (1 = SI, otra entrada = NO)? ')
							if datos != '1':
								continuar = False
				else:
					print('Se ha cancelado la compra.')

			else:
				print('Tu carrito esta vacio.')
		else:
			print('CONTRASEÑA INCORRECTA')
	else:
		print('NOMBRE DE USUARIO NO ENCONTRADO')
#===============================================================================
#===============================================================================
#cd OneDrive\Documentos\Unica\Python
"""Esta parte del código es el menu principal, 
	usuarios es un diccionario que guarda otro diccionario adentro, el cual es usuarios2
	usuarios 2 guarda objetos del tipo usuario""" 
class Producto:

	"""La clase producto se asocia a los productos que se venderan en la tienda
	en dado caso que se quieran tener objetos especificos se pueden crear clases que
	hereden de producto, por el momento no se encontro necesario"""
	def __init__(self, tipo, color, precio, inventario, talla):
		self.precio = precio
		self.tipo = tipo
		self.color = color
		self.inventario = inventario
		self.talla = talla
		self.clave = self.tipo[0] + self.tipo[1] + str(inventario) + self.color[0]

		"""Metodos para revisar los inventarios y reducirlos en 
		caso de que se hagan compras de los articulos"""
	def revisarInventario(self):
		if self.inventario == 0:
			print('Actualmente no tenemos existenacias')
			return False
		else:
			print('Articulo en existencia')
			return True

	def reducirInventario(self):
		self.inventario -= 1 

		"""Tenemos que manejar las claves continuamente por lo cual
		es necesario tener getters y setters de este atributo"""
	def getClave(self):
		return self.clave

	def setClave(self, inventario):
		self.clave = self.tipo[0] + self.tipo[1] + str(inventario) + self.color[0]

	def imprimirProducto(self):
		print('<======================>')
		print('Articulo: ' + self.tipo + '........' + str(self.precio))
		print('Color: ' + self.color)
		print('Talla: '+ self.talla)
		print('inventario: '+ str(self.inventario))
		print('CLAVE del producto: ' + self.clave)




class Carrito:
	"""La clase Carrito es la clase que se va a encargar de los
	procesos de gestion de la compra"""
	def __init__(self, articulos, total):
		self.articulos = articulos
		self.total = total

	def agregar(self, articulo, clave):
		self.articulos[clave] = articulo

	#Funcion para retirar
	"""El atributo de total se asocia a la compra y devido a 
	que esta en constante cambio debemos manejar getters y 
	setters"""

	def setTotal(self, importe):
		self.total += importe

	def getTotal(self): 
		return self.total

	def imprimirCarrito(self):
		print('\n\nArticulos en tu carrito.')
		for producto in self.articulos:
			self.articulos[producto].imprimirProducto()
			#producto.imprimirProducto()
		print('\n\nTotal ........... '+ str(self.getTotal()))

"""Declaramos los articulos en inventario
Atributos de Articulos: tipo, color, precio, inventario, talla"""

pantalonNegro = Producto('Pantalon', 'Negro', 250, 5, 'Mediana')
pantalonAzul = Producto('Pantalon', 'Azul', 300, 3, 'Chica')
pantalonBlanco = Producto('Pantalon', 'Blanco', 250, 4, 'Grande')

playeraRoja = Producto('Playera', 'Roja', 200, 5, 'Mediana')
playeraVerde = Producto('Playera', 'Verde', 200, 4, 'Chica')
playeraAzul = Producto('Playera', 'Azul', 300, 2, 'Grande')

vestidoBlanco = Producto('Vestido', 'Blanco', 800, 5, 'Mediana')
vestidoMorado = Producto('Vestido', 'Morado', 1200, 3, 'Chica')
vestidoNaranja = Producto('Vestido', 'Naranja', 1200, 1, 'Mediana')

listaProductos = [pantalonNegro, pantalonBlanco, pantalonAzul
					, playeraAzul, playeraVerde, playeraRoja
					, vestidoNaranja, vestidoMorado, vestidoBlanco]

"""En esta parte del codigo encontramos 
toda lo asociado al menu con las opciones
de REGISTRO, INGRESAR Y SALIR"""
carrito = Carrito({}, 0)
wh = 1
usuarios={}
usuarios2={}
while(wh==1):
	print('M E N U\n1. Registrar\n2. Ingresar\n3. Salir')
	opcion=input('Opcion:')

	if(opcion=='1'):
		Persona=Registrar()
		usuarios2[Persona.contraseña]=Persona
		usuarios[Persona.username]=usuarios2
		print('\nUSUARIO REGISTRADO')
	elif(opcion=='2'):
		Ingresar(listaProductos)
	elif(opcion=='3'):
		print('\nHasta luego, vuelva pronto')
		wh=0

	else:
		print('OPCION INVALIDA')