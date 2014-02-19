import xml.etree.ElementTree as ET

class Device:
    def __init__ (self,id_device,user_agent,fall_back):
        self.id = id_device
        self.user = user_agent
        self.fall = fall_back

    def mostrarDevice (self):
                print ('Device: id='+self.id+' user_agent='+self.user+' fall_back='+self.fall)

class Group:
    def __init__ (self,id_group):
        self.id = id_group

    def mostrarGroup (self):
                print ('Group: id='+self.id)
    
class Capability:
    def __init__ (self,name,value):
        self.name = name
        self.value = value

    def mostrarCapability (self):
                print ('Capability: name='+self.name+' value='+self.value)

class General:
    def __init__ (self,Device,Group,Capability):
        self.device = Device
        self.group = Group
        self.capability = Capability

def limpiarComentario(lineas):
	flag = 0
	nuevasLineas = []
	for str in lineas:
		if '<devices>' in str:
			flag = 1
		if flag == 1:
			nuevasLineas.append(str)
	return nuevasLineas

def limpiarNulos(lineas):
        nuevaslineas = []
        for str in lineas:
                nuevaslinea = str.translate('""')
                nuevaslineas.append(nuevaslinea)
        return nuevaslineas

def limpiarEspaciosBlancos(lineas):
        nuevaslineas = []
        for str in lineas:
                nuevaslinea = str.replace('<',' ').replace('>',' ').replace('=',' ').replace('/',' ').split()
                nuevaslineas.append(limpiarNulos(nuevaslinea))
        return nuevaslineas

def creadDevice2 (idt,ust,fbt):
	return Device(idt,ust,fbt)


def crearDevice(arregloSplit):
	ide=""
	user_agente=""
	fall_backu=""
	dispo = Device(ide,user_agente,fall_backu)
	for i in range(len(arregloSplit)):
		if arregloSplit[i] == 'id':
			ide=arregloSplit[i+1]
		else:
			if arregloSplit[i] == 'user_agent':
				user_agente = arregloSplit[i+1]
			else:
				if arregloSplit[i] == 'fall_back':
					fall_backu = arregloSplit[i+1]
	return Device(ide,user_agente,fall_backu)

def crearGroup(arregloSplit):
	ide=""
	for indice in range(len(arregloSplit)):
		if arregloSplit[indice] == 'id':
			ide = arregloSplit[indice+1]
	return Group(ide)

def crearCapability(arregloSplit):
	namep = ""
	valuep = ""
	for indice in range(len(arregloSplit)):
		if arregloSplit[indice] == 'name':
			namep = arregloSplit[indice+1]
		else:
			if arregloSplit[indice] == 'value':
				valuep = arregloSplit[indice+1]
	return Capability(namep,valuep)

def crearGeneral(lista):
    base =[]
    d=Device("","","")
    g=Group("")
    c=Capability("","")
    gro=General(d,g,c)
    for n in range(len(lista)):
        lis=lista[n]
        for s in range(len(lis)):
            if 'device' in lis[s]:
                d=crearDevice(lis)
            if 'group' in lis[s]:
            	if len(lis[s])!=1:
            		g=crearGroup(lis)
            if 'capability' in lis[s]:
            	c=crearCapability(lis)
            gro=General(d,g,c)
            base.append(gro)
    return base

def  mostrarTodo(lista):
    for n in range(len(lista)):
        print ('devId '+lista[n].device.id)
        print ('devUsr '+lista[n].device.user)
        print ('devFB '+lista[n].device.fall)
        print ('GrId '+lista[n].group.id)
        print ('cbN '+lista[n].capability.name)
        print ('cbV '+lista[n].capability.value)

def mostrarNumDev(lista):
	cont = 0
	for i in range(len(lista)):
		if 'device' in lista[i]:
			cont = cont +1
	print (cont/2)
	return cont 

def mostrarNumGr(lista):
	cont = 0
	for i in range(len(lista)):
		if 'group' in lista[i]:
			cont = cont +1
	print (cont/2)
	return cont 

def mostrarNumCb(lista):
	cont = 0
	for i in range(len(lista)):
		if 'capability' in lista[i]:
			cont = cont +1
	print (cont)
	return cont 

def buscarDevice(arregloSplit,member,tipe):
	contador = 0
	for i in range(len(arregloSplit)):
		if arregloSplit[i].device.fall == member:
			if arregloSplit[i+1] == tipe:
				print (arregloSplit[i+1])
				contador = contador+1
	return contador


with open('prueba.xml') as archivo:
        lineasCodigo = archivo.read().splitlines()
nuevasLineas = limpiarComentario(lineasCodigo)
espaciosRemovidos = limpiarEspaciosBlancos(nuevasLineas)
crearTotal = crearGeneral(espaciosRemovidos)
mostrarTodo(crearTotal)
dispou = buscarDevice(crearTotal,'fall_back','root')
print (dispou)


#arbolPrincipal = ET.parse('wurfl23.xml')
#raiz = arbolPrincipal.getroot()
#device = []
#group = []
#capability = []

#for devices in raiz:
#	print (devices.tag, devices.attrib)
#
#for deviceT in raiz.iter('device'):
#	device.append(deviceT.get('user_agent'))
#
#for groupT in raiz.iter('group'):
#	group.append(groupT.get('id'))
#
#for i in range(len(device)):
#	if(device[i]=='DO_NOT_MATCH_GENERIC_MOBILE'):
#		print(device.get('id'))