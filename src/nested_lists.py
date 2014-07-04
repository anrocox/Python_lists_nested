#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: anroco

It is possible to have a nested lists in python?

¿Es posible tener una listas anidadas en python?
'''

#create a list with lists as items
lista = [['hello', 'world'], [0, 2, 2, 6]]
print (lista)

#The first [] indicates the index of the outer list and
#the second [] indicates the index nested lists.
print(lista[0][1])
print(lista[1][3])

#add new items
lista.append([True, False])
print(lista)

#update value items
lista[1][2] = 4
print(lista)
