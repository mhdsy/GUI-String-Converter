#!/usr/bin/python3

from decimal import *


def decode(y,z):
    res=""
    data = y.split(" ")
    try:
    	for i in data:
    	    res = res + chr(int(i,z)) 
    	return res
    except:
    	return 'That is an invalid entry.'

def encodeToHex(s):
    res=""
    d = s
    try:
    	for i in d:
    	    res = res + hex(ord(i)).replace('0x', ' ')
    	return res
    except:
    	return 'That is an invalid entry.'

def encodeToOctal(s):
    res=""
    d = s
    try:
    	for i in d:
    	    res = res + oct(ord(i)).replace('0o', ' ')
    	return res
    except:
    	return 'That is an invalid entry.'


def encodeToDec(s):
    res=""
    d = s
    try:
    	for i in d:
    	    res = res + str(ord(i)) + ' '
    	return res
    except:
    	return 'That is an invalid entry.'


def encodeToBinary(s):
    res=""
    d = s
    try:
    	for i in d:
    	    res = res + bin(ord(i)).replace('0b', ' ')
    	return res
    except:
    	return 'That is an invalid entry.'