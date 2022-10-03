#s.9 nr.20
print("wie heist du ")
name=input(">")
print("dein name enthält",str(len(name)),"zeichen!")


#s.10 nr.21
print("wie heißt dein vorname?")
vorname=input(">")
print("wie heißt dein nachname?")
nachname=input(">")
print("dein vorname enthält",str(len(vorname+nachname)),"zeichen!")



#s.10 nr.22
print("wie heißt dein vorname? bitte in klein")
vorname=input(">")
print("wie heißt dein nachname?bitte in klein")
nachname=input(">")
print(vorname.capitalize(),nachname.capitalize())


#s.10 nr.23
print("gib die erste zeile eines gedichtes")
gedicht=input(">")
print("dein satz enthält", str(len(gedicht)),"zeichen!")


#s.10 Nr.24
print("bitte word eingeben")
word=input(">")
print(" ",word.lower())

s.10nr.26
print("Bitte gib deinen Vornamen ein.")

vorname =  input("Vorname => ")

if len(vorname) < 5:
    nachname = input("Bitte Nachname eingeben => ")
    Gesamter name = vorname + " " + nachname
    upper Gesamter name = Gesamter name.upper()
    print(upper Gesamter name)
          
else:
    Lower Vorname = vorname.lower()
    print(Lower Vorname)

s.10nr.26
s = "DIenr  diesmt  Sdienrn eb eisstte  HLielhfree rz,u rd eSre lsbiscthh inlafceh  iumnmde rn aucnhs eürbee rofbleürssstieg  Mmaaxcihmte.."
print(len(s))
print(s[::2])
print(s[1::2])







 Mathe py.
 
 import math

#nr. 27

print("Bitte gib eine ganze Zahl ein die ich mit 2 multipliziren soll")
ZahlA = float((input("zahl >")))
Zahl1 = (ZahlA *2)
ZahlB = float(Zahl1)
print(ZahlB)
 # nr.28
print("Bitte gib eine Zahl ein die ich mit 2 multipliziren und auf 2 nachkommastellen runden soll")
Zahl1 = (input("zahl >"))
Zahl2 = float(Zahl1)
Zahl3 = Zahl2 * 2
ZahlE = round(Zahl3 ,2)
print(ZahlE)
 
 
 #nr. 29

print("Bitte gib eine zahl höher als 500 und ich berechne dir die Wurzel daraus!")
ZahlE = float(int(input("Zahl >")))
ZahlF = math.sqrt(ZahlE)
print("Tada dein ergebnis ist " + str(ZahlF))

#nr. 30

print(round(math.pi,5))




))

#nr. 31

print("Bitte gib den Radius eines Kreises an")
ZahlG = int(input(">"))
KreisFl = int(ZahlF**2 * math.pi)
KreisUf = ZahlG * 2* math.pi
print("Der Kreisumfang beträgt " + str(round(KreisUf,2)) + "\(mm/cm/m\)\ , und die Fläche des Kreises beträgt " + str(round(KreisFl,2)) + " \(mm²/cm²/m²/km²\)") 

# 32 
#RZ = Radius Zylinder
#HZ = Höhe Zylinder
#FZ = Fläche Zylinder
#VZ = Volumen Zylinder

print("Bitte gib den Radius und die höhe eines Zylinders an")
RZ = int(input("Radius =>"))
HZ = int(input("Höhe =>"))
FZ = int(RZ**2 * math.pi)

