#!/bin/python3

def pesoArbol(arbol):
	if type(arbol) == int:
		return arbol
	elif len(arbol) == 1:
		return pesoArbol(arbol[0])
	else:
		result = 0
		n = len(arbol)
		for i in range(n):
			result+=pesoArbol(arbol[i])
		return result

def cantidadElementos(arbol):
	if type(arbol) == int:
		return 1
	elif len(arbol) == 1:
		return cantidadElementos(arbol[0])
	else:
		result = 0
		n = len(arbol)
		for i in range(n):
			result+=cantidadElementos(arbol[i])
		return result

def pesoPromArbol(arbol):
	return pesoArbol(arbol)/cantidadElementos(arbol)


def alturaArbol(arbol):
	if type(arbol) == int:
		print("IF 1")
		return 1
	elif len(arbol) == 1:
		print("IF 2")
		return alturaArbol(arbol[0])
	elif len(arbol) == 2 and type(arbol[0]) == int:
		print("IF 3")
		return 1+max(alturaArbol(arbol[0]),alturaArbol(arbol[1]))
	else:
		result = []
		n = len(arbol)
		for i in range(n):
			print("FOR")
			result.append(alturaArbol(arbol[i]))
		return max(result)
