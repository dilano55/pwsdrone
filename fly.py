import time
class engine:
    def __init__(self):
        self.powerpercentage = 0
frontLeftEngine = engine()
frontRightEngine = engine()
backLeftEngine= engine()
backRightEngine= engine()

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
def flyUporDown(timeduration, powerDuring, powerEnd=30): #timeduration is hoelang de drone met de gegeven kracht moet vliegen hier wordt de kracht van elke motor aangepast
    # als er geen invoer is voor power aan het einde dan wordt deze automatisch 30%(ik neem nu aan dat dit de vereiste kracht is om te zweven)
    setpower(powerDuring, 5)
    time.sleep(timeduration)
    setpower(powerEnd, 5)
def flySideways(direction, power, timeduration):#hier gaan we van of de 2 rechter of de 2 linker motoren de kracht veranderen om zo naar links of rechts te vliegen.
    if direction == "left":
        x = power * 0.5
        y = frontLeftEngine.powerpercentage
        z = y - x
        a = frontRightEngine.powerpercentage
        b = a + x
        setpower(z,4)
        setpower(b,3)
        time.sleep(0.5)
        setpower(y,4)
        setpower(a,3)
        time.sleep(timeduration)
        setpower(z,3)
        setpower(b,4)
        time.sleep(0.5)
        setpower(y,4)
        setpower(a,3)
        #we verminderen de kracht van de linker motoren met de helft van de gekozen kracht en versterken de rechter motoren met de helft van de gekozen kracht.
        #dit laten we dan 0.5 seconden lopen dan is de drone gekanteld naar links dan worden de orginelen krachten van de motoren hersteld en zal de drone voor de gekozen duratie die kankt op vliegen.
        #daarna worden de linker motoren versterkd met de helft van de gekozen kracht en de recter motoren minder sterk met de helft van de kozn kracht voor 0.5 seconden zodat de drone weer recht zweeft.
        #hierna worden de motoren hersteld naar de kracht die voor het zijwaarts vliegen van effect was.






