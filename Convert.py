
class distance:
	name = "distance"
	key = {'nm': 3.937e-8, 'um': 3.937e-5, 'mm': 0.0393701, 'cm': 0.393701, 
	"in": 1.0, "ft": 12.0, "yd": 36.0, 'fm': 72, "mi": 63360, 'lea': 190080,  
	'dm': 3.93701,'m': 39.3701, 'dam': 393.701, 'hm': 3937.01, 'km':39370.1}
	keynames = ['nm', 'um', 'mm', 'cm', "in", "ft", "yd", 'fm', "mi", 'lea',  
	'dm','m', 'dam', 'hm', 'km']
	length = 14
	
class area:
	name = "area"
	key = {'sq nm': 1.55e-15, 'sq um': 1.55e-9, 'sq cm': 0.1550004774, "sq in": 1, 
	'sq dm': 15.499969, "sq ft": 144,  'ft fm': 864, "sq yd": 1296,  'sq m': 1550.00477401, 
	'sq dam': 155000.4774, 'sq hm': 15500047.74, 'sq km':1.55e+9, "sq mi": 4.014e+9, 'sq nlea': 4.785e+10}
	keynames = ['sq nm', 'sq um', 'sq cm', "sq in", 'sq dm', 
	"sq ft",  'ft fm', "sq yd", 'sq m', 'sq dam', 'sq hm', 
	'sq km', "sq mi", 'sq nlea']
	length = 14

class mass:
	name = "mass"
	key = {'oz': 1, 'lb': 16, 'st': 224, "ton": 32000, 'm ton': 35274, 
	'im ton': 35840, "ug": 3.5274e-8,  "mg": 3.5274e-5, 'g': 0.035274, 'kg':35.274}
	keynames = ['oz', 'lb', 'st', 'ton', 'im ton', 'ug', 'mg', 'g', 'kg']
	length = 9

class volume:
	name = "volume"
	key = {'cc': 1, 'm3': 1e+6, 'tsp': 4.92892, "tbsp": 14.7868, 'fl oz': 29.5735, 
	'cup': 240, "pint": 473.176,  "qt": 946.353, 'gal': 3785.41, 'l': 1000, 'ml': 1, 'ft3': 28316.8, 'i3': 16.3871,
	'im gal': 4546.09, 'im qt': 1136.52, 'im pint': 568.261, 'im cup': 284.131, 'im fl oz': 28.4131, 'im tbsp': 17.7582, 'im tsp': 5.91939}
	keynames = ['cc', 'm3', 'tsp', 'tbsp', 'fl oz', 'cup', 'pint', 'qt', 'gal', 'l', 'ml', 'ft3', 'i3', 'im gal', 'im qt', 'im pint', 'im cup', 'im fl oz', 'im tbsp', 'im tsp']
	length = 20

class energy:
	name = "energy"
	key = {"el v": 1.6022e-19, 'j': 1, 'ft lb':1.35582, 'g cal': 4.184, 'kj': 1000, "b therm": 1055.06, 'wat hr': 3600, "kcal": 4184,  
	   'kwat hr': 3.6e+6, 'us therm': 1.055e+8}
	keynames = ['el v', 'j', 'ft lb', 'g cal', 'kj', 'b therm', 'wat hr', 'kcal', 'kwat hr', 'us therm']
	length = 10

class temperature:
	name = "temperature"
	keynames = ['F', 'R', 'C', 'K']
	length = 4
	def convertTemp(self, number, argument):
		key = {
			'CF': 9/5*(number)+32, 
			'FC': 5/9*(number-32),
			'FK': 5/9*(number - 32) + 273.15,
			'KF': 9/5*(number - 273.15) + 32,
			'FR':number+459.67,
			'RF':number-459.67,
			'KR':number*9/5,
			'RK':number*5/9,
			'CR':number*9/5+491.67,
			'RC':number*5/9-491.67,
			'CK': number + 273, 
			'KC': number - 273
		}
		return key.get(argument, "invalid option")
	

def newUnit(ty, number, argument, argument2):
	
	if ty.name != "temperature":
		return number * ty.key[argument] / ty.key[argument2]
	else:
		return ty.convertTemp(ty, number, argument+argument2)

def unitName(ty, index):
	return ty.keynames[index]

def numberOfUnits(ty):
	return ty.length