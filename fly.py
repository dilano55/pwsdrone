import time
class sensor: #dit moet de input van een sensor nabootsen. deze sensor levert informatie over de pitch yaw en roll.
    #deze informatie is nodig om de drone te kunnen stabiliseren.
    def __init__(self):
        self.pitch = 0
        self.yaw = 0
        self.roll = 0
class engine #hier wordt een class aangemaakt die de motoren moet voorstellen. met een eigenschap: namelijk het ingestelde percentage kracht.
    def __init__(self):
        self.powerpercentage = 0
class drone: #hier maak ik een drone class aan die als enige eigenschappen of de drone naar links/rechts of vooruit/achteruit aan het vliegen is. dit is nodig om te bepalen wanneer stabalisatie nodig is en wanneer niet.
    #als de drone naar voren vliegt is de pitch natuurlijk niet 0 maar hij hoeft ook niet gestabiliseerd te worden want het is hier de bedoeling dat de drone niet rechts hangt
    def __init__(self):
        self.flyingX = False #
        self.flyingY = False
frontLeftEngine = engine()
frontRightEngine = engine()
backLeftEngine= engine()
backRightEngine= engine()
rotationSensor = sensor()
droneStatus = drone()
def setpower(percentage, combination): #een functie om de motoren hun kracht percentage aan te kunnen passen
    # met een invoer voor het percentage kracht en een invoer voor de combinatie van motoren bijvoorbeeld de voorste motoren
    if combination==1: #alleen de voorste motoren( hier mee kun je dus achteruit  vooruit vliegen)
        frontRightEngine.powerpercentage= percentage
        frontLeftEngine.powerpercentage= percentage
    if combination==2: #alleen de achterste motoren( hier mee kun je dus achteruit  vooruit vliegen)
        backLeftEngine.powerpercentage= percentage
        backRightEngine.powerpercentage= percentage
    if combination==3: #alleen de rechter motoren ( hiermee kun je dus opzij vliegen)
         backRightEngine.powerpercentage= percentage
         frontRightEngine.powerpercentage= percentage
    if combination==4: #alleen de linker motoren ( hiermee kun je dus opzij vliegen)
        frontLeftEngine.powerpercentage= percentage
        backLeftEngine.powerpercentage= percentage
    if combination == 5: #alle motoren tegelijk ( hier mee kun je dus zweven naar boven of naar beneden)
         frontRightEngine.powerpercentage= percentage
         frontLeftEngine.powerpercentage= percentage
         backLeftEngine.powerpercentage= percentage
         backRightEngine.powerpercentage= percentage
    if combination == 6: #links voor en rechts achter zo kan de drone draaien om zijn y as in onze drone draaien deze met de klok mee.
        #door deze motoren sterker te zetten gaat de drone naar rechts draaien en door ze zwakker te maken zal de drone naar links draaien.
        frontLeftEngine.powerpercentage = percentage
        backRightEngine.powerpercentage = percentage

def flyY(timeduration, powerDuring, powerEnd=30): #timeduration is hoelang de drone met de gegeven kracht moet vliegen hier wordt de kracht van elke motor aangepast
    # als er geen invoer is voor power aan het einde dan wordt deze automatisch 30%(ik neem nu aan dat dit de vereiste kracht is om te zweven)
    setpower(powerDuring, 5)
    time.sleep(timeduration)
    setpower(powerEnd, 5)
def flyXY(direction, power, timeduration):#hier gaan we van of de 2 van de motoren hun kract aan passen om zo in de x of z richting te kunnen vliegen.
    if direction == "left":
        x = power * 0.5
        y = frontLeftEngine.powerpercentage
        z = y - x
        a = frontRightEngine.powerpercentage
        b = a + x
        setpower(z,4)
        setpower(b,3)
        droneStatus.flyingY = True
        time.sleep(0.5)
        setpower(y,5)
        time.sleep(timeduration)
        setpower(z,3)
        setpower(b,4)
        time.sleep(0.5)
        droneStatus.flyingY = False
        setpower(y,5)
        #we verminderen de kracht van de linker motoren met de helft van de gekozen kracht en versterken de rechter motoren met de helft van de gekozen kracht.
        #dit laten we dan 0.5 seconden lopen dan is de drone gekanteld naar links dan worden de orginelen krachten van de motoren hersteld en zal de drone voor de gekozen duratie die kankt op vliegen.
        #daarna worden de linker motoren versterkd met de helft van de gekozen kracht en de recter motoren minder sterk met de helft van de kozn kracht voor 0.5 seconden zodat de drone weer recht zweeft.
        #hierna worden de motoren hersteld naar de kracht die voor het zijwaarts vliegen van effect was.
    if direction == "right":
        x = power * 0.5
        y = frontRightEngine.powerpercentage
        z = y - x
        a = frontLeftEngine.powerpercentage
        b = a + x
        setpower(z,3)
        setpower(b,4)
        droneStatus.flyingY = True
        time.sleep(0.5)
        setpower(y,5)
        time.sleep(timeduration)
        setpower(z,4)
        setpower(b,3)
        time.sleep(0.5)
        setpower(y,5)
        droneStatus.flyingY = False
    if direction == "forward":
        x = power * 0.5
        y = frontLeftEngine.powerpercentage
        z = y - x
        a = backLeftEngine.powerpercentage
        b = a + x
        setpower(z,1)
        setpower(b,2)
        droneStatus.flyingX = True
        time.sleep(0.5)
        setpower(y,1)
        setpower(a,1)
        time.sleep(timeduration)
        setpower(z,2)
        setpower(a,1)
        time.sleep(0.5)
        setpower(y,1)
        setpower(a,2)
        droneStatus.flyingX = False
    if direction == "backwards":
        x = power * 0.5
        y = backLeftEngine.powerpercentage
        z = y - x
        a = frontLeftEngine.powerpercentage
        b = a + x
        setpower(z,2)
        setpower(b,1)
        droneStatus.flyingX = True
        time.sleep(0.5)
        setpower(y,2)
        setpower(a,1)
        time.sleep(timeduration)
        setpower(z,1)
        setpower(b,2)
        time.sleep(0.5)
        setpower(y,2)
        setpower(a,1)
        droneStatus.flyingX = False
def changeYaw(degrees, power = 5):
    enginePower = frontLeftEngine.powerpercentage
    rotationBefore = rotationSensor.yaw
    rotationAfter = rotationBefore + degrees
    if degrees > 180 and degrees < 360:
        powerReversed = -power
        desiredPower = enginePower + powerReversed
    if degrees <= 180 or degrees > 360:
       desiredPower= enginePower + power
    while rotationSensor.yaw != rotationAfter:
        setpower(desiredPower,6)
    setpower(enginePower,6)
def stabilisation():
    while rotationSensor.pitch != 0 and droneStatus.flyingX == False:
        if rotationSensor.pitch > 180:
            powerBefore = frontLeftEngine.powerpercentage
            adjustmentPower = powerBefore + 5
            setpower(adjustmentPower,2)
        elif droneStatus.flyingX == False:
            powerBefore = backLeftEngine.powerpercentage
            adjustmentPower = powerBefore + 5
            setpower(adjustmentPower,1)
    while rotationSensor.roll != 0 and droneStatus.flyingY == False:
        if rotationSensor.roll > 180:
            powerBefore = frontRightEngine.powerpercentage
            adjustmentPower = powerBefore + 5
            setpower(adjustmentPower,4)
        elif droneStatus.flyingY == False:
            powerBefore = frontLeftEngine.powerpercentage
            adjustmentPower = powerBefore + 5
            setpower(adjustmentPower,3)
