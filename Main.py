# ================================================================================
# ==============================Initialization.... ===============================
# ================================================================================
import random
import pygame, sys
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hebrew Vocabulary Learning")

points = 0
# Game Icon
icon = pygame.image.load("HVLicon.png")
pygame.display.set_icon(icon)

Words = ["Fruit", "Apple", "Watermelon", "Orange", "Pear", "Strawberries", "Grapes", "Pineapple", "Avocado", "Lemon",
         "Melon", "Cherries", "Peach", "Banana", "Apricot", "Blueberries", "Coconut", "Fig", "Kiwi", "Mango",
         "Nectarine", "Papaya", "Plum", "Rasberry", "Pomegranite", "Loquat", "Persimmon", "DatePalm", "Mandarin",
         "Grapefruit",
         "Tomato", "BellPepper", "Potato", "Carrot", "Celery", "Onion", "Garlic", "Cabbage", "Cucumber", "Lettuce",
         "Eggplant", "Pumkin", "Beetroot", "Corn", "Radish", "Mushroom", "Pea", "Olives", "Milk", "Butter"]

# Sate = [pygame.mixer.music.pause(),pygame.mixer.music.unpause()]


# ================================================================================
# ============================== Colors ==========================================
# ================================================================================

# Colors
BRIGHTWHITE = (255, 255, 255)
WHITE = (240, 248, 255)
BRIGHTBLACK = (48, 48, 48)
BLACK = (0, 0, 0)
BRIGHTRED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GLOWGREEN = (0, 255, 127)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (255, 215, 0)
DARKYELLOW = (255, 193, 37)
DARKGRAY = (40, 40, 40)
DARKTURQUOISE = (3, 54, 73)
BRIGHTPINK = (255, 182, 193)
PINK = (224, 102, 255)
BRIGHTPURPLE = (209, 95, 238)
PURPLE = (125, 38, 205)
GREY = (210, 210, 210)

# ================================================================================
# ============================== Images Directory ================================
# ================================================================================

# Game Background
Background_image = pygame.image.load("Bubblesbg.JPG")
Background_image = pygame.transform.scale(Background_image, (screen_width, screen_height))

# Background Frame
BackgroundFrame = pygame.image.load("BackgroundFrame.jpg")
BackgroundFrame = pygame.transform.scale(BackgroundFrame, (screen_width, screen_height))

# Speaker image when music is playing
Speaker = pygame.image.load("Speaker.png")
Speaker = pygame.transform.scale(Speaker, (100, 100))

# Speaker image when music isn't playing
SpeakerX = pygame.image.load("SpeakerX.png")
SpeakerX = pygame.transform.scale(SpeakerX, (100, 100))

# Are you sure?
AreYouSureImg = pygame.image.load("AreYouSure.jpg")
AreYouSureImg = pygame.transform.scale(AreYouSureImg, (screen_width, screen_height))

# Score board
Score = pygame.image.load("SCORE.jpg")
Score = pygame.transform.scale(Score, (100, 100))

# A message when a player didn't choose a set and is trying to
# enter the game
ChooseSet = pygame.image.load("ChooseSet.jpg")
ChooseSet = pygame.transform.scale(ChooseSet, (800, 600))

# ============================== Vocabulary Images =============================


FruitImg = pygame.image.load("Images Directory/Fruit.jpg")
FruitImgL = pygame.transform.scale(FruitImg, (300, 300))
FruitImgS = pygame.transform.scale(FruitImg, (150, 150))

AppleImg = pygame.image.load("Images Directory/Apple.jpg")
AppleImgL = pygame.transform.scale(AppleImg, (300, 300))
AppleImgS = pygame.transform.scale(AppleImg, (150, 150))

WatermelonImg = pygame.image.load("Images Directory/Watermelon.jpg")
WatermelonImgL = pygame.transform.scale(WatermelonImg, (300, 300))
WatermelonImgS = pygame.transform.scale(WatermelonImg, (150, 150))

OrangeImg = pygame.image.load("Images Directory/Orange.jpg")
OrangeImgL = pygame.transform.scale(OrangeImg, (300, 300))
OrangeImgS = pygame.transform.scale(OrangeImg, (150, 150))

PearImg = pygame.image.load("Images Directory/Pear.jpg")
PearImgL = pygame.transform.scale(PearImg, (300, 300))
PearImgS = pygame.transform.scale(PearImg, (150, 150))

StrawberriesImg = pygame.image.load("Images Directory/Strawberries.jpg")
StrawberriesImgL = pygame.transform.scale(StrawberriesImg, (300, 300))
StrawberriesImgS = pygame.transform.scale(StrawberriesImg, (150, 150))

GrapesImg = pygame.image.load("Images Directory/Grapes.jpg")
GrapesImgL = pygame.transform.scale(GrapesImg, (300, 300))
GrapesImgS = pygame.transform.scale(GrapesImg, (150, 150))

PineappleImg = pygame.image.load("Images Directory/Pineapple.jpg")
PineappleImgL = pygame.transform.scale(PineappleImg, (300, 300))
PineappleImgS = pygame.transform.scale(PineappleImg, (150, 150))

AvodacoImg = pygame.image.load("Images Directory/Avocado.png")
AvodacoImgL = pygame.transform.scale(AvodacoImg, (300, 300))
AvodacoImgS = pygame.transform.scale(AvodacoImg, (150, 150))

LemonImg = pygame.image.load("Images Directory/Lemon.jpg")
LemonImgL = pygame.transform.scale(LemonImg, (300, 300))
LemonImgS = pygame.transform.scale(LemonImg, (150, 150))

MelonImg = pygame.image.load('Images Directory/Melon.png')
MelonImgL = pygame.transform.scale(MelonImg, (300, 300))
MelonImgS = pygame.transform.scale(MelonImg, (150, 150))

CherriesImg = pygame.image.load('Images Directory/Cherries.jpg')
CherriesImgL = pygame.transform.scale(CherriesImg, (300, 300))
CherriesImgS = pygame.transform.scale(CherriesImg, (150, 150))

PeachImg = pygame.image.load('Images Directory/Peach.jpg')
PeachImgL = pygame.transform.scale(PeachImg, (300, 300))
PeachImgS = pygame.transform.scale(PeachImg, (150, 150))

BananaImg = pygame.image.load('Images Directory/Banana.jpg')
BananaImgL = pygame.transform.scale(BananaImg, (300, 300))
BananaImgS = pygame.transform.scale(BananaImg, (150, 150))

ApricotImg = pygame.image.load('Images Directory/Apricot.jpg')
ApricotImgL = pygame.transform.scale(ApricotImg, (300, 300))
ApricotImgS = pygame.transform.scale(ApricotImg, (150, 150))

BlueberriesImg = pygame.image.load('Images Directory/Blueberries.jpg')
BlueberriesImgL = pygame.transform.scale(BlueberriesImg, (300, 300))
BlueberriesImgS = pygame.transform.scale(BlueberriesImg, (150, 150))

CoconutImg = pygame.image.load('Images Directory/Coconut.jpg')
CoconutImgL = pygame.transform.scale(CoconutImg, (300, 300))
CoconutImgS = pygame.transform.scale(CoconutImg, (150, 150))

FigImg = pygame.image.load('Images Directory/Fig.jpg')
FigImgL = pygame.transform.scale(FigImg, (300, 300))
FigImgS = pygame.transform.scale(FigImg, (150, 150))

KiwiImg = pygame.image.load('Images Directory/Kiwi.jpg')
KiwiImgL = pygame.transform.scale(KiwiImg, (300, 300))
KiwiImgS = pygame.transform.scale(KiwiImg, (150, 150))

MangoImg = pygame.image.load('Images Directory/Mango.jpg')
MangoImgL = pygame.transform.scale(MangoImg, (300, 300))
MangoImgS = pygame.transform.scale(MangoImg, (150, 150))

NectarineImg = pygame.image.load('Images Directory/Nectarine.jpg')
NectarineImgL = pygame.transform.scale(NectarineImg, (300, 300))
NectarineImgS = pygame.transform.scale(NectarineImg, (150, 150))

PapayaImg = pygame.image.load('Images Directory/Papaya.jpg')
PapayaImgL = pygame.transform.scale(PapayaImg, (300, 300))
PapayaImgS = pygame.transform.scale(PapayaImg, (150, 150))

PlumImg = pygame.image.load('Images Directory/Plum.jpg')
PlumImgL = pygame.transform.scale(PlumImg, (300, 300))
PlumImgS = pygame.transform.scale(PlumImg, (150, 150))

RasberryImg = pygame.image.load('Images Directory/Raspberry.jpg')
RasberryImgL = pygame.transform.scale(RasberryImg, (300, 300))
RasberryImgS = pygame.transform.scale(RasberryImg, (150, 150))

PomegraniteImg = pygame.image.load('Images Directory/Pomegranite.jpg')
PomegraniteImgL = pygame.transform.scale(PomegraniteImg, (300, 300))
PomegraniteImgS = pygame.transform.scale(PomegraniteImg, (150, 150))

LoquatImg = pygame.image.load('Images Directory/Loquat.jpg')
LoquatImgL = pygame.transform.scale(LoquatImg, (300, 300))
LoquatImgS = pygame.transform.scale(LoquatImg, (150, 150))

PersimmonImg = pygame.image.load('Images Directory/Persimmon.jpg')
PersimmonImgL = pygame.transform.scale(PersimmonImg, (300, 300))
PersimmonImgS = pygame.transform.scale(PersimmonImg, (150, 150))

DatePalmImg = pygame.image.load('Images Directory/DatePalm.jpg')
DatePalmImgL = pygame.transform.scale(DatePalmImg, (300, 300))
DatePalmImgS = pygame.transform.scale(DatePalmImg, (150, 150))

MandarinImg = pygame.image.load('Images Directory/Mandarin.jpg')
MandarinImgL = pygame.transform.scale(MandarinImg, (300, 300))
MandarinImgS = pygame.transform.scale(MandarinImg, (150, 150))

GrapefruitImg = pygame.image.load('Images Directory/Grapefruit.png')
GrapefruitImgL = pygame.transform.scale(GrapefruitImg, (300, 300))
GrapefruitImgS = pygame.transform.scale(GrapefruitImg, (150, 150))

TomatoImg = pygame.image.load('Images Directory/Tomato.jpg')
TomatoImgL = pygame.transform.scale(TomatoImg, (300, 300))
TomatoImgS = pygame.transform.scale(TomatoImg, (150, 150))

BellPepperImg = pygame.image.load('Images Directory/BellPepper.jpg')
BellPepperImgL = pygame.transform.scale(BellPepperImg, (300, 300))
BellPepperImgS = pygame.transform.scale(BellPepperImg, (150, 150))

PotatoImg = pygame.image.load('Images Directory/Potato.jpg')
PotatoImgL = pygame.transform.scale(PotatoImg, (300, 300))
PotatoImgS = pygame.transform.scale(PotatoImg, (150, 150))

CarrotImg = pygame.image.load('Images Directory/Carrot.jpg')
CarrotImgL = pygame.transform.scale(CarrotImg, (300, 300))
CarrotImgS = pygame.transform.scale(CarrotImg, (150, 150))

CeleryImg = pygame.image.load('Images Directory/Celery.png')
CeleryImgL = pygame.transform.scale(CeleryImg, (300, 300))
CeleryImgS = pygame.transform.scale(CeleryImg, (150, 150))

OnionImg = pygame.image.load('Images Directory/Onion.jpg')
OnionImgL = pygame.transform.scale(OnionImg, (300, 300))
OnionImgS = pygame.transform.scale(OnionImg, (150, 150))

GarlicImg = pygame.image.load('Images Directory/Garlic.jpg')
GarlicImgL = pygame.transform.scale(GarlicImg, (300, 300))
GarlicImgS = pygame.transform.scale(GarlicImg, (150, 150))

CabbageImg = pygame.image.load('Images Directory/Cabbage.jpg')
CabbageImgL = pygame.transform.scale(CabbageImg, (300, 300))
CabbageImgS = pygame.transform.scale(CabbageImg, (150, 150))

CucumberImg = pygame.image.load('Images Directory/Cucumber.png')
CucumberImgL = pygame.transform.scale(CucumberImg, (300, 300))
CucumberImgS = pygame.transform.scale(CucumberImg, (150, 150))

LettuceImg = pygame.image.load('Images Directory/Lettuce.png')
LettuceImgL = pygame.transform.scale(LettuceImg, (300, 300))
LettuceImgS = pygame.transform.scale(LettuceImg, (150, 150))

EggplantImg = pygame.image.load('Images Directory/Eggplant.jpg')
EggplantImgL = pygame.transform.scale(EggplantImg, (300, 300))
EggplantImgS = pygame.transform.scale(EggplantImg, (150, 150))

PumkinImg = pygame.image.load('Images Directory/Pumkin.jpg')
PumkinImgL = pygame.transform.scale(PumkinImg, (300, 300))
PumkinImgS = pygame.transform.scale(PumkinImg, (150, 150))

BeetrootImg = pygame.image.load('Images Directory/Beetroot.jpg')
BeetrootImgL = pygame.transform.scale(BeetrootImg, (300, 300))
BeetrootImgS = pygame.transform.scale(BeetrootImg, (150, 150))

CornImg = pygame.image.load('Images Directory/Corn.png')
CornImgL = pygame.transform.scale(CornImg, (300, 300))
CornImgS = pygame.transform.scale(CornImg, (150, 150))

RadishImg = pygame.image.load('Images Directory/Radish.jpg')
RadishImgL = pygame.transform.scale(RadishImg, (300, 300))
RadishImgS = pygame.transform.scale(RadishImg, (150, 150))

MushroomImg = pygame.image.load('Images Directory/Mushroom.jpg')
MushroomImgL = pygame.transform.scale(MushroomImg, (300, 300))
MushroomImgS = pygame.transform.scale(MushroomImg, (150, 150))

PeaImg = pygame.image.load('Images Directory/Pea.jpg')
PeaImgL = pygame.transform.scale(PeaImg, (300, 300))
PeaImgS = pygame.transform.scale(PeaImg, (150, 150))

OlivesImg = pygame.image.load('Images Directory/Olives.jpg')
OlivesImgL = pygame.transform.scale(OlivesImg, (300, 300))
OlivesImgS = pygame.transform.scale(OlivesImg, (150, 150))

MilkImg = pygame.image.load('Images Directory/Milk.jpg')
MilkImgL = pygame.transform.scale(MilkImg, (300, 300))
MilkImgS = pygame.transform.scale(MilkImg, (150, 150))

ButterImg = pygame.image.load('Images Directory/Butter.jpg')
ButterImgL = pygame.transform.scale(ButterImg, (300, 300))
ButterImgS = pygame.transform.scale(ButterImg, (150, 150))
# ============================== Words Images ====================================


FruitWord = pygame.image.load('Hebrew Words/Slide1.jpg')
FruitWord = pygame.transform.scale(FruitWord, (150, 100))
# FruitWord=pygame.image.load('Hebrew Words/Slide1.jpg')
# FruitWord=pygame.transform.scale(FruitWord,(150,100))
AppleWord = pygame.image.load('Hebrew Words/Slide2.jpg')
AppleWord = pygame.transform.scale(AppleWord, (150, 100))
WatermelonWord = pygame.image.load('Hebrew Words/Slide3.jpg')
WatermelonWord = pygame.transform.scale(WatermelonWord, (150, 100))
OrangeWord = pygame.image.load('Hebrew Words/Slide4.jpg')
OrangeWord = pygame.transform.scale(OrangeWord, (150, 100))
PearWord = pygame.image.load('Hebrew Words/Slide5.jpg')
PearWord = pygame.transform.scale(PearWord, (150, 100))
StrawberriesWord = pygame.image.load('Hebrew Words/Slide6.jpg')
StrawberriesWord = pygame.transform.scale(StrawberriesWord, (150, 100))
GrapesWord = pygame.image.load('Hebrew Words/Slide7.jpg')
GrapesWord = pygame.transform.scale(GrapesWord, (150, 100))
PineappleWord = pygame.image.load('Hebrew Words/Slide8.jpg')
PineappleWord = pygame.transform.scale(PineappleWord, (150, 100))
AvocadoWord = pygame.image.load('Hebrew Words/Slide9.jpg')
AvocadoWord = pygame.transform.scale(AvocadoWord, (150, 100))
LemonWord = pygame.image.load('Hebrew Words/Slide10.jpg')
LemonWord = pygame.transform.scale(LemonWord, (150, 100))
MelonWord = pygame.image.load('Hebrew Words/Slide11.jpg')
MelonWord = pygame.transform.scale(MelonWord, (150, 100))
CherriesWord = pygame.image.load('Hebrew Words/Slide12.jpg')
CherriesWord = pygame.transform.scale(CherriesWord, (150, 100))
PeachWord = pygame.image.load('Hebrew Words/Slide13.jpg')
PeachWord = pygame.transform.scale(PeachWord, (150, 100))
BananaWord = pygame.image.load('Hebrew Words/Slide14.jpg')
BananaWord = pygame.transform.scale(BananaWord, (150, 100))
ApricotWord = pygame.image.load('Hebrew Words/Slide15.jpg')
ApricotWord = pygame.transform.scale(ApricotWord, (150, 100))
BlueberriesWord = pygame.image.load('Hebrew Words/Slide16.jpg')
BlueberriesWord = pygame.transform.scale(BlueberriesWord, (150, 100))
CoconutWord = pygame.image.load('Hebrew Words/Slide17.jpg')
CoconutWord = pygame.transform.scale(CoconutWord, (150, 100))
FigWord = pygame.image.load('Hebrew Words/Slide18.jpg')
FigWord = pygame.transform.scale(FigWord, (150, 100))
KiwiWord = pygame.image.load('Hebrew Words/Slide19.jpg')
KiwiWord = pygame.transform.scale(KiwiWord, (150, 100))
MangoWord = pygame.image.load('Hebrew Words/Slide20.jpg')
MangoWord = pygame.transform.scale(MangoWord, (150, 100))
NectarineWord = pygame.image.load('Hebrew Words/Slide21.jpg')
NectarineWord = pygame.transform.scale(NectarineWord, (150, 100))
PapayaWord = pygame.image.load('Hebrew Words/Slide22.jpg')
PapayaWord = pygame.transform.scale(PapayaWord, (150, 100))
PlumWord = pygame.image.load('Hebrew Words/Slide23.jpg')
PlumWord = pygame.transform.scale(PlumWord, (150, 100))
RasberryWord = pygame.image.load('Hebrew Words/Slide24.jpg')
RasberryWord = pygame.transform.scale(RasberryWord, (150, 100))
PomegraniteWord = pygame.image.load('Hebrew Words/Slide25.jpg')
PomegraniteWord = pygame.transform.scale(PomegraniteWord, (150, 100))
LoquatWord = pygame.image.load('Hebrew Words/Slide26.jpg')
LoquatWord = pygame.transform.scale(LoquatWord, (150, 100))
PersimmonWord = pygame.image.load('Hebrew Words/Slide27.jpg')
PersimmonWord = pygame.transform.scale(PersimmonWord, (150, 100))
DatePalmWord = pygame.image.load('Hebrew Words/Slide28.jpg')
DatePalmWord = pygame.transform.scale(DatePalmWord, (150, 100))
MandarinWord = pygame.image.load('Hebrew Words/Slide29.jpg')
MandarinWord = pygame.transform.scale(MandarinWord, (150, 100))
GrapefruitWord = pygame.image.load('Hebrew Words/Slide30.jpg')
GrapefruitWord = pygame.transform.scale(GrapefruitWord, (150, 100))
TomatoWord = pygame.image.load('Hebrew Words/Slide31.jpg')
TomatoWord = pygame.transform.scale(TomatoWord, (150, 100))
BellPepperWord = pygame.image.load('Hebrew Words/Slide32.jpg')
BellPepperWord = pygame.transform.scale(BellPepperWord, (150, 100))
PotatoWord = pygame.image.load('Hebrew Words/Slide33.jpg')
PotatoWord = pygame.transform.scale(PotatoWord, (150, 100))
CarrotWord = pygame.image.load('Hebrew Words/Slide34.jpg')
CarrotWord = pygame.transform.scale(CarrotWord, (150, 100))
CeleryWord = pygame.image.load('Hebrew Words/Slide35.jpg')
CeleryWord = pygame.transform.scale(CeleryWord, (150, 100))
OnionWord = pygame.image.load('Hebrew Words/Slide36.jpg')
OnionWord = pygame.transform.scale(OnionWord, (150, 100))
GarlicWord = pygame.image.load('Hebrew Words/Slide37.jpg')
GarlicWord = pygame.transform.scale(GarlicWord, (150, 100))
CabbageWord = pygame.image.load('Hebrew Words/Slide38.jpg')
CabbageWord = pygame.transform.scale(CabbageWord, (150, 100))
CucumberWord = pygame.image.load('Hebrew Words/Slide39.jpg')
CucumberWord = pygame.transform.scale(CucumberWord, (150, 100))
LettuceWord = pygame.image.load('Hebrew Words/Slide40.jpg')
LettuceWord = pygame.transform.scale(LettuceWord, (150, 100))
EggplantWord = pygame.image.load('Hebrew Words/Slide41.jpg')
EggplantWord = pygame.transform.scale(EggplantWord, (150, 100))
PumkinWord = pygame.image.load('Hebrew Words/Slide42.jpg')
PumkinWord = pygame.transform.scale(PumkinWord, (150, 100))
BeetrootWord = pygame.image.load('Hebrew Words/Slide43.jpg')
BeetrootWord = pygame.transform.scale(BeetrootWord, (150, 100))
CornWord = pygame.image.load('Hebrew Words/Slide44.jpg')
CornWord = pygame.transform.scale(CornWord, (150, 100))
RadishWord = pygame.image.load('Hebrew Words/Slide45.jpg')
RadishWord = pygame.transform.scale(RadishWord, (150, 100))
MushroomWord = pygame.image.load('Hebrew Words/Slide46.jpg')
MushroomWord = pygame.transform.scale(MushroomWord, (150, 100))
PeaWord = pygame.image.load('Hebrew Words/Slide47.jpg')
PeaWord = pygame.transform.scale(PeaWord, (150, 100))
OlivesWord = pygame.image.load('Hebrew Words/Slide48.jpg')
OlivesWord = pygame.transform.scale(OlivesWord, (150, 100))
MilkWord = pygame.image.load('Hebrew Words/Slide49.jpg')
MilkWord = pygame.transform.scale(MilkWord, (150, 100))
ButterWord = pygame.image.load('Hebrew Words/Slide50.jpg')
ButterWord = pygame.transform.scale(ButterWord, (150, 100))

# ================================================================================
# ============================== Music & Sounds Directory ========================
# ================================================================================

# Menu Background Music
pygame.mixer.music.load('Stardrive.mp3')

Fruit = pygame.mixer.Sound('Sounds/Fruit.wav')
Apple = pygame.mixer.Sound('Sounds/Apple.wav')
Watermelon = pygame.mixer.Sound('Sounds/Watermelon.wav')
Orange = pygame.mixer.Sound('Sounds/Orange.wav')
Pear = pygame.mixer.Sound('Sounds/Pear.wav')
Strawberries = pygame.mixer.Sound('Sounds/Strawberries.wav')
Grapes = pygame.mixer.Sound('Sounds/Grapes.wav')
Pineapple = pygame.mixer.Sound('Sounds/Pineapple.wav')
Avocado = pygame.mixer.Sound('Sounds/Avocado.wav')
Lemon = pygame.mixer.Sound('Sounds/Lemon.wav')
Melon = pygame.mixer.Sound('Sounds/Melon.wav')
Cherries = pygame.mixer.Sound('Sounds/Cherries.wav')
Peach = pygame.mixer.Sound('Sounds/Peach.wav')
Banana = pygame.mixer.Sound('Sounds/Banana.wav')
Apricot = pygame.mixer.Sound('Sounds/Apricot.wav')
Blueberries = pygame.mixer.Sound('Sounds/Blueberries.wav')
Coconut = pygame.mixer.Sound('Sounds/Coconut.wav')
Fig = pygame.mixer.Sound('Sounds/Fig.wav')
Kiwi = pygame.mixer.Sound('Sounds/Kiwi.wav')
Mango = pygame.mixer.Sound('Sounds/Mango.wav')
Nectarine = pygame.mixer.Sound('Sounds/Nectarine.wav')
Papaya = pygame.mixer.Sound('Sounds/Papaya.wav')
Plum = pygame.mixer.Sound('Sounds/Plum.wav')
Rasberry = pygame.mixer.Sound('Sounds/Rasberry.wav')
Pomegranite = pygame.mixer.Sound('Sounds/Pomegranite.wav')
Loquat = pygame.mixer.Sound('Sounds/Loquat.wav')
Persimmon = pygame.mixer.Sound('Sounds/Persimmon.wav')
DatePalm = pygame.mixer.Sound('Sounds/DatePalm.wav')
Mandarin = pygame.mixer.Sound('Sounds/Mandarin.wav')
Grapefruit = pygame.mixer.Sound('Sounds/Grapefruit.wav')
Tomato = pygame.mixer.Sound('Sounds/Tomato.wav')
BellPepper = pygame.mixer.Sound('Sounds/BellPepper.wav')
Potato = pygame.mixer.Sound('Sounds/Potato.wav')
Carrot = pygame.mixer.Sound('Sounds/Carrot.wav')
Celery = pygame.mixer.Sound('Sounds/Celery.wav')
Onion = pygame.mixer.Sound('Sounds/Onion.wav')
Garlic = pygame.mixer.Sound('Sounds/Garlic.wav')
Cabbage = pygame.mixer.Sound('Sounds/Cabbage.wav')
Cucumber = pygame.mixer.Sound('Sounds/Cucumber.wav')
Lettuce = pygame.mixer.Sound('Sounds/Lettuce.wav')
Eggplant = pygame.mixer.Sound('Sounds/Eggplant.wav')
Pumkin = pygame.mixer.Sound('Sounds/Pumkin.wav')
Beetroot = pygame.mixer.Sound('Sounds/Beetroot.wav')
Corn = pygame.mixer.Sound('Sounds/Corn.wav')
Radish = pygame.mixer.Sound('Sounds/Radish.wav')
Mushroom = pygame.mixer.Sound('Sounds/Mushroom.wav')
Pea = pygame.mixer.Sound('Sounds/Pea.wav')
Olives = pygame.mixer.Sound('Sounds/Olives.wav')
Milk = pygame.mixer.Sound('Sounds/Milk.wav')
Butter = pygame.mixer.Sound('Sounds/Butter.wav')
Correct = pygame.mixer.Sound('Sounds/Correct.wav')
Wrong = pygame.mixer.Sound('Sounds/Wrong.wav')


def Correct_Sound():
    pygame.mixer.Sound.play(Correct)


def Wrong_Sound():
    pygame.mixer.Sound.play(Wrong)


def Fruit_Sound():
    pygame.mixer.Sound.play(Fruit)


def Apple_Sound():
    pygame.mixer.Sound.play(Apple)


def Watermelon_Sound():
    pygame.mixer.Sound.play(Watermelon)


def Orange_Sound():
    pygame.mixer.Sound.play(Orange)


def Pear_Sound():
    pygame.mixer.Sound.play(Pear)


def Strawberries_Sound():
    pygame.mixer.Sound.play(Strawberries)


def Grapes_Sound():
    pygame.mixer.Sound.play(Grapes)


def Pineapple_Sound():
    pygame.mixer.Sound.play(Pineapple)


def Avocado_Sound():
    pygame.mixer.Sound.play(Avocado)


def Lemon_Sound():
    pygame.mixer.Sound.play(Lemon)


def Melon_Sound():
    pygame.mixer.Sound.play(Melon)


def Cherries_Sound():
    pygame.mixer.Sound.play(Cherries)


def Peach_Sound():
    pygame.mixer.Sound.play(Peach)


def Banana_Sound():
    pygame.mixer.Sound.play(Banana)


def Apricot_Sound():
    pygame.mixer.Sound.play(Apricot)


def Blueberries_Sound():
    pygame.mixer.Sound.play(Blueberries)


def Coconut_Sound():
    pygame.mixer.Sound.play(Coconut)


def Fig_Sound():
    pygame.mixer.Sound.play(Fig)


def Kiwi_Sound():
    pygame.mixer.Sound.play(Kiwi)


def Mango_Sound():
    pygame.mixer.Sound.play(Mango)


def Nectarine_Sound():
    pygame.mixer.Sound.play(Nectarine)


def Papaya_Sound():
    pygame.mixer.Sound.play(Papaya)


def Plum_Sound():
    pygame.mixer.Sound.play(Plum)


def Rasberry_Sound():
    pygame.mixer.Sound.play(Rasberry)


def Pomegranite_Sound():
    pygame.mixer.Sound.play(Pomegranite)


def Loquat_Sound():
    pygame.mixer.Sound.play(Loquat)


def Persimmon_Sound():
    pygame.mixer.Sound.play(Persimmon)


def DatePalm_Sound():
    pygame.mixer.Sound.play(DatePalm)


def Mandarin_Sound():
    pygame.mixer.Sound.play(Mandarin)


def Grapefruit_Sound():
    pygame.mixer.Sound.play(Grapefruit)


def Tomato_Sound():
    pygame.mixer.Sound.play(Tomato)


def BellPepper_Sound():
    pygame.mixer.Sound.play(BellPepper)


def Potato_Sound():
    pygame.mixer.Sound.play(Potato)


def Carrot_Sound():
    pygame.mixer.Sound.play(Carrot)


def Celery_Sound():
    pygame.mixer.Sound.play(Celery)


def Onion_Sound():
    pygame.mixer.Sound.play(Onion)


def Garlic_Sound():
    pygame.mixer.Sound.play(Garlic)


def Cabbage_Sound():
    pygame.mixer.Sound.play(Cabbage)


def Cucumber_Sound():
    pygame.mixer.Sound.play(Cucumber)


def Lettuce_Sound():
    pygame.mixer.Sound.play(Lettuce)


def Eggplant_Sound():
    pygame.mixer.Sound.play(Eggplant)


def Pumkin_Sound():
    pygame.mixer.Sound.play(Pumkin)


def Beetroot_Sound():
    pygame.mixer.Sound.play(Beetroot)


def Corn_Sound():
    pygame.mixer.Sound.play(Corn)


def Radish_Sound():
    pygame.mixer.Sound.play(Radish)


def Mushroom_Sound():
    pygame.mixer.Sound.play(Mushroom)


def Pea_Sound():
    pygame.mixer.Sound.play(Pea)


def Olives_Sound():
    pygame.mixer.Sound.play(Olives)


def Milk_Sound():
    pygame.mixer.Sound.play(Milk)


def Butter_Sound():
    pygame.mixer.Sound.play(Butter)


# ================================================================================
# ============================== Functions =======================================
# ================================================================================

def text_objects_Text(text, color, size):
    font = pygame.font.Font(None, size)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, size, x_displace=0, y_displace=0):
    textSurf, textRect = text_objects_Text(msg, color, size)
    textRect.center = screen_width / 2 + x_displace, screen_height / 2 + y_displace
    screen.blit(textSurf, textRect)


# ============================ Button Creator Function ===========================

def text_objects(text, color, size):
    font = pygame.font.Font(None, size)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# Special Write function for buttons, exclusively!!!!
def Write(text, color, size, x, y, width, height):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = (x + width / 2), (y + height / 2)
    screen.blit(textSurf, textRect)


# parameters: x, y coordinates; width and height of button; color when mouse is on; color when mouse is off;
# text inside the button; color and size of the text inside the button

def Create_button(x, y, width, height, Hover, NotHover, text, color, size):
    Rectangle = [x, y, width, height]
    mouse = pygame.mouse.get_pos()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, Hover, (x, y, width, height))
        Write(text, color, size, x, y, width, height)

    else:
        pygame.draw.rect(screen, NotHover, (x, y, width, height))
        Write(text, color, size, x, y, width, height)

    return (Rectangle)


def Select_button(Switch, x, y, width, height, OnHover, OffHover, OnNotHover, OffNotHover, OnText, OffText, OnColor,
                  OffColor, OnSize, OffSize):
    Rectangle = [x, y, width, height]

    Hover = [OffHover, OnHover]
    NotHover = [OffNotHover, OnNotHover]
    text = [OffText, OnText]
    color = [OnColor, OffColor]
    size = [OnSize, OffSize]

    Create_button(x, y, width, height, Hover[Switch], NotHover[Switch], text[Switch], color[Switch], size[Switch])

    return (Rectangle)


def Select_button(Switch, x, y, width, height, OnHover, OffHover, OnNotHover, OffNotHover, OnText, OffText, OnColor,
                  OffColor, OnSize, OffSize):
    Rectangle = [x, y, width, height]

    Hover = [OffHover, OnHover]
    NotHover = [OffNotHover, OnNotHover]
    text = [OffText, OnText]
    color = [OnColor, OffColor]
    size = [OnSize, OffSize]

    Create_button(x, y, width, height, Hover[Switch], NotHover[Switch], text[Switch], color[Switch], size[Switch])

    return (Rectangle)


# ============================ Grid Function  ====================================
# "Gapsize" is the distance between each pair of horizontal and vertical lines.

GapSize = 100


def Grid(GapSize):
    StartX = GapSize
    LinesCounterX = 0
    TotalLinesX = screen_width / GapSize

    while LinesCounterX < TotalLinesX:
        pygame.draw.lines(screen, BLACK, False, [(StartX, 0), (StartX, screen_height)], 1)
        StartX += GapSize
        LinesCounterX += 1

    StartY = GapSize
    LinesCounterY = 0
    TotalLinesY = screen_height / GapSize

    while LinesCounterY < TotalLinesY:
        pygame.draw.lines(screen, BLACK, False, [(0, StartY), (screen_width, StartY)], 1)
        StartY += GapSize
        LinesCounterY += 1


# A function that controls music by clicking an image.
# It takes the switch as input and the image and it's position.
# When the music is turned off, it puts a red x over the image

def X(PositionX, PositionY, Width=100, Height=100):
    pygame.draw.line(screen, RED, (PositionX, PositionY), (PositionX + Width, PositionY + Height), 4)
    pygame.draw.line(screen, RED, (PositionX, PositionY + Height), (PositionX + Width, PositionY), 4)


# def Music_Control(Switch, PositionX, PositionY):
#    global State
#    global Image
#    switch=0
#    if Switch=="On":
#        switch+=1

#    if Switch=="Off":
#        switch=0

#    else:
#        print("You can only choose 'On' or 'Off' for the Switch variable")

#    Sate[switch]
#    Image[switch]


# ================================================================================
# ============================== Menu Loop =======================================
# ================================================================================

def Menu_Loop():
    # Switch="On"
    MenuExit = False
    screen.fill(WHITE)
    screen.blit(Background_image, (0, 0))
    # Grid(50)
    pygame.mixer.music.unpause()
    pygame.display.update()
    counter = 0

    while not MenuExit:

        if counter == 0:
            screen.blit(Speaker, (700, 0))
            # X(700, 0, 100, 100)
            pygame.display.update()

        message_to_screen("Welcome To", WHITE, 70, x_displace=0, y_displace=-250)
        message_to_screen("Arie's Hebrew Games", WHITE, 70, x_displace=0, y_displace=-150)
        EXIT = Create_button(475, 250, 150, 150, BRIGHTRED, RED, "Quit", BLACK, 45)
        PLAY = Create_button(175, 250, 150, 150, BRIGHTGREEN, GREEN, "New Game", BLACK, 45)
        PRACTICE = Create_button(325, 250, 150, 150, BRIGHTBLUE, BLUE, "Practice", BLACK, 45)
        # SETS = Create_button(screen_width*0.40, 0, 160, 160, BRIGHTBLUE, BLUE, "Sets", BLACK, 45)

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (EXIT[0] < mouse[0] < EXIT[0] + EXIT[2] and EXIT[1] < mouse[1] < EXIT[1] + EXIT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                pygame.quit()
                sys.exit()
            # elif (700 < mouse[0] < 800 and 0 < mouse[1] < 100) and (event.type == pygame.MOUSEBUTTONDOWN) and (Switch=="On"):
            #    Music_Control("Off", 700, 0)
            #    Switch="Off"

            # elif (700 < mouse[0] < 800 and 0 < mouse[1] < 100) and (event.type == pygame.MOUSEBUTTONDOWN) and (Switch=="Off"):
            # Music_Control("On", PositionX, PositionY)
            # Switch="On"

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (PRACTICE[0] < mouse[0] < PRACTICE[0] + PRACTICE[2] and PRACTICE[1] < mouse[1] < PRACTICE[1] +
                  PRACTICE[3]) and (event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            elif (PLAY[0] < mouse[0] < PLAY[0] + PLAY[2] and PLAY[1] < mouse[1] < PLAY[1] + PLAY[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set_Choice()


# ================================================================================
# ============================== Game Practice Loop ==============================
# ================================================================================

def Game_Practice_Menu():
    pygame.mixer.music.unpause()
    practiceExit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))
    # screen.blit(ArrowButton,(700,200))
    # Grid(50)
    pygame.display.update()
    while not practiceExit:

        message_to_screen("Select A Set", BLACK, 70, x_displace=0, y_displace=-175)
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        # Moves to the next set of categories
        # RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))

        # Category buttons: Left Column
        SET1 = Create_button(150, 200, 200, 50, BRIGHTBLUE, BLUE, "Set 1", WHITE, 35)
        SET2 = Create_button(150, 300, 200, 50, BRIGHTBLUE, BLUE, "Set 2", WHITE, 35)
        SET3 = Create_button(150, 400, 200, 50, BRIGHTBLUE, BLUE, "Set 3", WHITE, 35)
        SET4 = Create_button(450, 250, 200, 50, BRIGHTBLUE, BLUE, "Set 4", WHITE, 35)
        SET5 = Create_button(450, 350, 200, 50, BRIGHTBLUE, BLUE, "Set 5", WHITE, 35)

        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Menu_Loop()

            elif (SET1[0] < mouse[0] < SET1[0] + SET1[2] and SET1[1] < mouse[1] < SET1[1] + SET1[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set1_Loop()

            elif (SET2[0] < mouse[0] < SET2[0] + SET2[2] and SET2[1] < mouse[1] < SET2[1] + SET2[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set2_Loop()

            elif (SET3[0] < mouse[0] < SET3[0] + SET3[2] and SET3[1] < mouse[1] < SET3[1] + SET3[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set3_Loop()

            elif (SET4[0] < mouse[0] < SET4[0] + SET4[2] and SET4[1] < mouse[1] < SET4[1] + SET4[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set4_Loop()

            elif (SET5[0] < mouse[0] < SET5[0] + SET5[2] and SET5[1] < mouse[1] < SET5[1] + SET5[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set5_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 1 Loop ======================================
# ================================================================================
def Set1_Loop():
    pygame.mixer.music.pause()
    Set1Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set1Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(FruitImgS, (50, 50))
        screen.blit(FruitWord, (50, 200))

        screen.blit(AppleImgS, (300, 50))
        screen.blit(AppleWord, (300, 200))

        screen.blit(WatermelonImgS, (550, 50))
        screen.blit(WatermelonWord, (550, 200))

        # Second Row
        screen.blit(OrangeImgS, (50, 350))
        screen.blit(OrangeWord, (50, 500))

        screen.blit(PearImgS, (300, 350))
        screen.blit(PearWord, (300, 500))

        screen.blit(StrawberriesImgS, (550, 350))
        screen.blit(StrawberriesWord, (550, 500))

        # Next Page Button

        RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (50 < mouse[0] < 200 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Fruit_Sound()

            elif (300 < mouse[0] < 450 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Apple_Sound()

            elif (550 < mouse[0] < 700 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Watermelon_Sound()

            # Second Row
            elif (50 < mouse[0] < 200 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Orange_Sound()

            elif (300 < mouse[0] < 450 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Pear_Sound()

            elif (550 < mouse[0] < 700 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Strawberries_Sound()

            elif (RIGHT[0] < mouse[0] < RIGHT[0] + RIGHT[2] and RIGHT[1] < mouse[1] < RIGHT[1] + RIGHT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set1Tail_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 1 Loop Tail =================================
# ================================================================================
def Set1Tail_Loop():
    pygame.mixer.music.pause()
    Set1Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set1Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(GrapesImgS, (200, 50))
        screen.blit(GrapesWord, (200, 200))

        screen.blit(PineappleImgS, (450, 50))
        screen.blit(PineappleWord, (450, 200))

        # Second Row
        screen.blit(AvodacoImgS, (200, 350))
        screen.blit(AvocadoWord, (200, 500))

        screen.blit(LemonImgS, (450, 350))
        screen.blit(LemonWord, (450, 500))

        # Previous Page Button

        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (200 < mouse[0] < 350 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Grapes_Sound()

            elif (450 < mouse[0] < 550 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Pineapple_Sound()



            # Second Row
            elif (200 < mouse[0] < 350 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Avocado_Sound()

            elif (450 < mouse[0] < 550 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Lemon_Sound()



            elif (LEFT[0] < mouse[0] < LEFT[0] + LEFT[2] and LEFT[1] < mouse[1] < LEFT[1] + LEFT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set1_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            # ================================================================================


# ============================== Set 2 Loop ======================================
# ================================================================================
def Set2_Loop():
    pygame.mixer.music.pause()
    Set2Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set2Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(MelonImgS, (50, 50))
        screen.blit(MelonWord, (50, 200))

        screen.blit(CherriesImgS, (300, 50))
        screen.blit(CherriesWord, (300, 200))

        screen.blit(PeachImgS, (550, 50))
        screen.blit(PeachWord, (550, 200))

        # Second Row
        screen.blit(BananaImgS, (50, 350))
        screen.blit(BananaWord, (50, 500))

        screen.blit(ApricotImgS, (300, 350))
        screen.blit(ApricotWord, (300, 500))

        screen.blit(BlueberriesImgS, (550, 350))
        screen.blit(BlueberriesWord, (550, 500))

        # Next Page Button

        RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (50 < mouse[0] < 200 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Melon_Sound()

            elif (300 < mouse[0] < 450 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Cherries_Sound()

            elif (550 < mouse[0] < 700 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Peach_Sound()

            # Second Row
            elif (50 < mouse[0] < 200 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Banana_Sound()

            elif (300 < mouse[0] < 450 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Apricot_Sound()

            elif (550 < mouse[0] < 700 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Blueberries_Sound()

            elif (RIGHT[0] < mouse[0] < RIGHT[0] + RIGHT[2] and RIGHT[1] < mouse[1] < RIGHT[1] + RIGHT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set2Tail_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 2 Loop Tail =================================
# ================================================================================
def Set2Tail_Loop():
    pygame.mixer.music.pause()
    Set2Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set2Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(CoconutImgS, (200, 50))
        screen.blit(CoconutWord, (200, 200))

        screen.blit(FigImgS, (450, 50))
        screen.blit(FigWord, (450, 200))

        # Second Row
        screen.blit(KiwiImgS, (200, 350))
        screen.blit(KiwiWord, (200, 500))

        screen.blit(MangoImgS, (450, 350))
        screen.blit(MangoWord, (450, 500))

        # Previous Page Button

        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (200 < mouse[0] < 350 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Coconut_Sound()

            elif (450 < mouse[0] < 550 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Fig_Sound()

            # Second Row
            elif (200 < mouse[0] < 350 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Kiwi_Sound()

            elif (450 < mouse[0] < 550 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Mango_Sound()

            elif (LEFT[0] < mouse[0] < LEFT[0] + LEFT[2] and LEFT[1] < mouse[1] < LEFT[1] + LEFT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set2_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            # ================================================================================


# ============================== Set 3 Loop ======================================
# ================================================================================
def Set3_Loop():
    pygame.mixer.music.pause()
    Set3Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set3Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(NectarineImgS, (50, 50))
        screen.blit(NectarineWord, (50, 200))

        screen.blit(PapayaImgS, (300, 50))
        screen.blit(PapayaWord, (300, 200))

        screen.blit(PlumImgS, (550, 50))
        screen.blit(PlumWord, (550, 200))

        # Second Row
        screen.blit(RasberryImgS, (50, 350))
        screen.blit(RasberryWord, (50, 500))

        screen.blit(PomegraniteImgS, (300, 350))
        screen.blit(PomegraniteWord, (300, 500))

        screen.blit(LoquatImgS, (550, 350))
        screen.blit(LoquatWord, (550, 500))

        # Next Page Button

        RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (50 < mouse[0] < 200 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Nectarine_Sound()

            elif (300 < mouse[0] < 450 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Papaya_Sound()

            elif (550 < mouse[0] < 700 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Plum_Sound()

            # Second Row
            elif (50 < mouse[0] < 200 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Rasberry_Sound()

            elif (300 < mouse[0] < 450 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Pomegranite_Sound()

            elif (550 < mouse[0] < 700 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Loquat_Sound()

            elif (RIGHT[0] < mouse[0] < RIGHT[0] + RIGHT[2] and RIGHT[1] < mouse[1] < RIGHT[1] + RIGHT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set3Tail_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 3 Loop Tail =================================
# ================================================================================
def Set3Tail_Loop():
    pygame.mixer.music.pause()
    Set3Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set3Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(PersimmonImgS, (200, 50))
        screen.blit(PersimmonWord, (200, 200))

        screen.blit(DatePalmImgS, (450, 50))
        screen.blit(DatePalmWord, (450, 200))

        # Second Row
        screen.blit(MandarinImgS, (200, 350))
        screen.blit(MandarinWord, (200, 500))

        screen.blit(GrapefruitImgS, (450, 350))
        screen.blit(GrapefruitWord, (450, 500))

        # Previous Page Button

        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (200 < mouse[0] < 350 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Persimmon_Sound()

            elif (450 < mouse[0] < 550 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                DatePalm_Sound()

            # Second Row
            elif (200 < mouse[0] < 350 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Mandarin_Sound()

            elif (450 < mouse[0] < 550 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Grapefruit_Sound()

            elif (LEFT[0] < mouse[0] < LEFT[0] + LEFT[2] and LEFT[1] < mouse[1] < LEFT[1] + LEFT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set3_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 4 Loop ======================================
# ================================================================================
def Set4_Loop():
    pygame.mixer.music.pause()
    Set4Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set4Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(TomatoImgS, (50, 50))
        screen.blit(TomatoWord, (50, 200))

        screen.blit(BellPepperImgS, (300, 50))
        screen.blit(BellPepperWord, (300, 200))

        screen.blit(PotatoImgS, (550, 50))
        screen.blit(PotatoWord, (550, 200))

        # Second Row
        screen.blit(CarrotImgS, (50, 350))
        screen.blit(CarrotWord, (50, 500))

        screen.blit(CeleryImgS, (300, 350))
        screen.blit(CeleryWord, (300, 500))

        screen.blit(OnionImgS, (550, 350))
        screen.blit(OnionWord, (550, 500))

        # Next Page Button

        RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (50 < mouse[0] < 200 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Tomato_Sound()

            elif (300 < mouse[0] < 450 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                BellPepper_Sound()

            elif (550 < mouse[0] < 700 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Potato_Sound()

            # Second Row
            elif (50 < mouse[0] < 200 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Carrot_Sound()

            elif (300 < mouse[0] < 450 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Celery_Sound()

            elif (550 < mouse[0] < 700 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Onion_Sound()

            elif (RIGHT[0] < mouse[0] < RIGHT[0] + RIGHT[2] and RIGHT[1] < mouse[1] < RIGHT[1] + RIGHT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set4Tail_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 4 Loop Tail =================================
# ================================================================================
def Set4Tail_Loop():
    pygame.mixer.music.pause()
    Set3Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set3Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(GarlicImgS, (200, 50))
        screen.blit(GarlicWord, (200, 200))

        screen.blit(CabbageImgS, (450, 50))
        screen.blit(CabbageWord, (450, 200))

        # Second Row
        screen.blit(CucumberImgS, (200, 350))
        screen.blit(CucumberWord, (200, 500))

        screen.blit(LettuceImgS, (450, 350))
        screen.blit(LettuceWord, (450, 500))

        # Previous Page Button

        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (200 < mouse[0] < 350 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Garlic_Sound()

            elif (450 < mouse[0] < 550 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Cabbage_Sound()

            # Second Row
            elif (200 < mouse[0] < 350 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Cucumber_Sound()

            elif (450 < mouse[0] < 550 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Lettuce_Sound()

            elif (LEFT[0] < mouse[0] < LEFT[0] + LEFT[2] and LEFT[1] < mouse[1] < LEFT[1] + LEFT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set4_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 5 Loop ======================================
# ================================================================================
def Set5_Loop():
    pygame.mixer.music.pause()
    Set5Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set5Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(EggplantImgS, (50, 50))
        screen.blit(EggplantWord, (50, 200))

        screen.blit(PumkinImgS, (300, 50))
        screen.blit(PumkinWord, (300, 200))

        screen.blit(BeetrootImgS, (550, 50))
        screen.blit(BeetrootWord, (550, 200))

        # Second Row
        screen.blit(CornImgS, (50, 350))
        screen.blit(CornWord, (50, 500))

        screen.blit(RadishImgS, (300, 350))
        screen.blit(RadishWord, (300, 500))

        screen.blit(MushroomImgS, (550, 350))
        screen.blit(MushroomWord, (550, 500))

        # Next Page Button

        RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))
        # LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (50 < mouse[0] < 200 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Eggplant_Sound()

            elif (300 < mouse[0] < 450 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Pumkin_Sound()

            elif (550 < mouse[0] < 700 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Beetroot_Sound()

            # Second Row
            elif (50 < mouse[0] < 200 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Corn_Sound()

            elif (300 < mouse[0] < 450 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Radish_Sound()

            elif (550 < mouse[0] < 700 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Mushroom_Sound()

            elif (RIGHT[0] < mouse[0] < RIGHT[0] + RIGHT[2] and RIGHT[1] < mouse[1] < RIGHT[1] + RIGHT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set5Tail_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set 5 Loop Tail =================================
# ================================================================================
def Set5Tail_Loop():
    pygame.mixer.music.pause()
    Set5Exit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))

    # Grid(50)
    pygame.display.update()

    while not Set5Exit:
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        # First Row
        screen.blit(PeaImgS, (200, 50))
        screen.blit(PeaWord, (200, 200))

        screen.blit(OlivesImgS, (450, 50))
        screen.blit(OlivesWord, (450, 200))

        # Second Row
        screen.blit(MilkImgS, (200, 350))
        screen.blit(MilkWord, (200, 500))

        screen.blit(ButterImgS, (450, 350))
        screen.blit(ButterWord, (450, 500))

        # Previous Page Button

        LEFT = Create_button(0, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        Triangle = pygame.draw.polygon(screen, BLACK, ((35, 275), (35, 325), (15, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Practice_Menu()

            # First Row
            elif (200 < mouse[0] < 350 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Pea_Sound()

            elif (450 < mouse[0] < 550 and 50 < mouse[1] < 300) and (event.type == pygame.MOUSEBUTTONDOWN):
                Olives_Sound()

            # Second Row
            elif (200 < mouse[0] < 350 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Milk_Sound()

            elif (450 < mouse[0] < 550 and 350 < mouse[1] < 600) and (event.type == pygame.MOUSEBUTTONDOWN):
                Butter_Sound()

            elif (LEFT[0] < mouse[0] < LEFT[0] + LEFT[2] and LEFT[1] < mouse[1] < LEFT[1] + LEFT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set5_Loop()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Set Choice Loop =================================
# ================================================================================

def Set_Choice():
    pygame.mixer.music.unpause()
    global points
    Switch1 = 0
    Switch2 = 0
    Switch3 = 0
    Switch4 = 0
    Switch5 = 0
    setchoiceExit = False
    screen.fill(WHITE)
    screen.blit(BackgroundFrame, (0, 0))
    # screen.blit(ArrowButton,(700,200))
    # Grid(50)

    WordsImages = [FruitImgL, AppleImgL, WatermelonImgL, OrangeImgL, PearImgL, StrawberriesImgL, GrapesImgL,
                   PineappleImgL, AvodacoImgL, LemonImgL, MelonImgL, CherriesImgL, PeachImgL, BananaImgL,
                   ApricotImgL, BlueberriesImgL, CoconutImgL, FigImgL, KiwiImgL, MangoImgL, NectarineImgL,
                   PapayaImgL, PlumImgL, RasberryImgL, PomegraniteImgL, LoquatImgL, PersimmonImgL, DatePalmImgL,
                   MandarinImgL, GrapefruitImgL, TomatoImgL, BellPepperImgL, PotatoImgL, CarrotImgL,
                   CeleryImgL, OnionImgL, GarlicImgL, CabbageImgL, CucumberImgL, LettuceImgL, EggplantImgL,
                   PumkinImgL, BeetrootImgL, CornImgL, RadishImgL, MushroomImgL, PeaImgL, OlivesImgL, MilkImgL,
                   ButterImgL]

    ImageWords = [FruitWord, AppleWord, WatermelonWord, OrangeWord, PearWord, StrawberriesWord, GrapesWord,
                  PineappleWord, AvocadoWord, LemonWord, MelonWord, CherriesWord, PeachWord, BananaWord, ApricotWord,
                  BlueberriesWord, CoconutWord, FigWord, KiwiWord, MangoWord, NectarineWord, PapayaWord, PlumWord,
                  RasberryWord, PomegraniteWord, LoquatWord, PersimmonWord, DatePalmWord, MandarinWord, GrapefruitWord,
                  TomatoWord, BellPepperWord, PotatoWord, CarrotWord, CeleryWord, OnionWord, GarlicWord, CabbageWord,
                  CucumberWord, LettuceWord, EggplantWord, PumkinWord, BeetrootWord, CornWord, RadishWord, MushroomWord,
                  PeaWord, OlivesWord, MilkWord, ButterWord]

    ImagesCollector = []
    WordsCollector = []

    pygame.display.update()
    while not setchoiceExit:

        message_to_screen("Make a selection", BLACK, 70, x_displace=0, y_displace=-175)
        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)
        PLAY = Create_button(300, 500, 200, 100, BRIGHTBLUE, BLUE, "Play", BLACK, 45)
        # Moves to the next set of categories
        # RIGHT = Create_button(750, 250, 50, 100, BRIGHTBLUE, BLUE, None, BLACK, 45)
        # Triangle = pygame.draw.polygon(screen, BLACK, ((765, 275), (765, 325), (785, 300)))

        # Category buttons: Left Column
        SET1 = Select_button(Switch1, 150, 200, 200, 50, BRIGHTPURPLE, BRIGHTBLUE, PURPLE, BLUE, "Set 1", "Set 1",
                             BLACK, WHITE, 35, 35)
        SET2 = Select_button(Switch2, 150, 300, 200, 50, BRIGHTPURPLE, BRIGHTBLUE, PURPLE, BLUE, "Set 2", "Set 2",
                             BLACK, WHITE, 35, 35)
        SET3 = Select_button(Switch3, 150, 400, 200, 50, BRIGHTPURPLE, BRIGHTBLUE, PURPLE, BLUE, "Set 3", "Set 3",
                             BLACK, WHITE, 35, 35)
        SET4 = Select_button(Switch4, 450, 250, 200, 50, BRIGHTPURPLE, BRIGHTBLUE, PURPLE, BLUE, "Set 4", "Set 4",
                             BLACK, WHITE, 35, 35)
        SET5 = Select_button(Switch5, 450, 350, 200, 50, BRIGHTPURPLE, BRIGHTBLUE, PURPLE, BLUE, "Set 5", "Set 5",
                             BLACK, WHITE, 35, 35)

        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                points = 0
                Menu_Loop()

            # elif (PLAY[0] < mouse[0] < PLAY[0] + PLAY[2] and PLAY[1] < mouse[1] < PLAY[1] + PLAY[3]) and (event.type == pygame.MOUSEBUTTONDOWN):
            #    Game_Loop(WordsImages,ImageWords)

            elif (SET1[0] < mouse[0] < SET1[0] + SET1[2] and SET1[1] < mouse[1] < SET1[1] + SET1[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch1 == 0):
                Switch1 += 1
                k = 0
                while k < 10:
                    ImagesCollector.append(WordsImages[k])
                    WordsCollector.append(ImageWords[k])
                    k += 1

            elif (SET1[0] < mouse[0] < SET1[0] + SET1[2] and SET1[1] < mouse[1] < SET1[1] + SET1[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch1 == 1):
                Switch1 -= 1
                k = 9
                while -1 < k:
                    ImagesCollector.remove(WordsImages[k])
                    WordsCollector.remove(ImageWords[k])
                    k -= 1

            elif (SET2[0] < mouse[0] < SET2[0] + SET2[2] and SET2[1] < mouse[1] < SET2[1] + SET2[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch2 == 0):
                Switch2 += 1

                k = 10
                while k < 20:
                    ImagesCollector.append(WordsImages[k])
                    WordsCollector.append(ImageWords[k])
                    k += 1

            elif (SET2[0] < mouse[0] < SET2[0] + SET2[2] and SET2[1] < mouse[1] < SET2[1] + SET2[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch2 == 1):
                Switch2 -= 1

                k = 19
                while 9 < k:
                    ImagesCollector.remove(WordsImages[k])
                    WordsCollector.remove(ImageWords[k])
                    k -= 1

            elif (SET3[0] < mouse[0] < SET3[0] + SET3[2] and SET3[1] < mouse[1] < SET3[1] + SET3[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch3 == 0):
                Switch3 += 1
                k = 20
                while k < 30:
                    ImagesCollector.append(WordsImages[k])
                    WordsCollector.append(ImageWords[k])
                    k += 1


            elif (SET3[0] < mouse[0] < SET3[0] + SET3[2] and SET3[1] < mouse[1] < SET3[1] + SET3[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch3 == 1):
                Switch3 -= 1
                k = 29
                while 19 < k:
                    ImagesCollector.remove(WordsImages[k])
                    WordsCollector.remove(ImageWords[k])
                    k -= 1

            elif (SET4[0] < mouse[0] < SET4[0] + SET4[2] and SET4[1] < mouse[1] < SET4[1] + SET4[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch4 == 0):
                Switch4 += 1
                k = 30
                while k < 40:
                    ImagesCollector.append(WordsImages[k])
                    WordsCollector.append(ImageWords[k])
                    k += 1

            elif (SET4[0] < mouse[0] < SET4[0] + SET4[2] and SET4[1] < mouse[1] < SET4[1] + SET4[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch4 == 1):
                Switch4 -= 1
                k = 39
                while 29 < k:
                    ImagesCollector.remove(WordsImages[k])
                    WordsCollector.remove(ImageWords[k])
                    k -= 1

            elif (SET5[0] < mouse[0] < SET5[0] + SET5[2] and SET5[1] < mouse[1] < SET5[1] + SET5[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch5 == 0):
                Switch5 += 1
                k = 40
                while k < 50:
                    ImagesCollector.append(WordsImages[k])
                    WordsCollector.append(ImageWords[k])
                    k += 1

            elif (SET5[0] < mouse[0] < SET5[0] + SET5[2] and SET5[1] < mouse[1] < SET5[1] + SET5[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Switch5 == 1):
                Switch5 -= 1
                k = 49
                while 39 < k:
                    ImagesCollector.remove(WordsImages[k])
                    WordsCollector.remove(ImageWords[k])
                    k -= 1

            elif (PLAY[0] < mouse[0] < PLAY[0] + PLAY[2] and PLAY[1] < mouse[1] < PLAY[1] + PLAY[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                if ImagesCollector == [] or WordsCollector == []:
                    Error_Loop()
                else:
                    Game_Loop(ImagesCollector, WordsCollector)

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ============================== Error Message ===================================
# ================================================================================
def Error_Loop():
    pygame.mixer.music.unpause()
    errorExit = False
    screen.fill(WHITE)
    screen.blit(ChooseSet, (0, 0))
    pygame.display.update()
    while not errorExit:
        # OK = Create_button(150, 450, 150, 75, BRIGHTRED, RED, "Ok!", BLACK, 45)
        GOTIT = Create_button(300, 500, 200, 100, BRIGHTGREEN, GREEN, "Got It!", BLACK, 45)
        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            # if (OK[0] < mouse[0] < OK[0] + OK[2] and OK[1] < mouse[1] < OK[1] + OK[3]) and (event.type == pygame.MOUSEBUTTONDOWN):
            #    Set_Choice()

            if (GOTIT[0] < mouse[0] < GOTIT[0] + GOTIT[2] and GOTIT[1] < mouse[1] < GOTIT[1] + GOTIT[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set_Choice()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


# ================================================================================
# ======================================= Game Loop ==============================
# ================================================================================

def Game_Loop(WordsImages, ImageWords):
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(0.2)
    Images = WordsImages
    Words = ImageWords
    # Grid(50)
    global points
    readinggameExit = False
    screen.fill(WHITE)
    screen.blit(Background_image, (0, 0))

    # "WordsImages" is the list of all the large images
    # WordsImages = [FruitImgL, AppleImgL, WatermelonImgL, OrangeImgL]
    # ImageSounds = [Fruit_Sound(),Apple_Sound(),Watermelon_Sound(),Orange_Sound()]
    # Generating a random number between 0 and the kength of the images list
    # WordsImages=[FruitImgL, AppleImgL, WatermelonImgL, OrangeImgL, PearImgL, StrawberriesImgL, GrapesImgL, PineappleImgL,AvodacoImgL, LemonImgL, MelonImgL, CherriesImgL, PeachImgL, BananaImgL, ApricotImgL, BlueberriesImgL, CoconutImgL, FigImgL, KiwiImgL, MangoImgL, NectarineImgL, PapayaImgL, PlumImgL, RasberryImgL, PomegraniteImgL, LoquatImgL, PersimmonImgL, DatePalmImgL, MandarinImgL, GrapefruitImgL, TomatoImgL, BellPepperImgL, PotatoImgL, CarrotImgL, CeleryImgL, OnionImgL, GarlicImgL, CabbageImgL, CucumberImgL, LettuceImgL, EggplantImgL, PumpkinImgL, BeetrootImgL, CornImgL, RadishImgL, MushroomImgL, PeaImgL, OlivesImgL, MilkImgL, ButterImgL, CheeseImgL, SourCreamImgL, IceCreamImgL, SausageImgL, EggImgL, BeefImgL, ChickenImgL, LambImgL, DessertImgL, CakeImgL]
    for x in range(1):
        Random_Number = random.randint(0, len(WordsImages) - 1)
    RandomImage = WordsImages[Random_Number]

    Random_Numbers = []
    for x in range(2):
        Random_Numbers.append(random.randint(0, len(WordsImages) - 1))

    while (Random_Numbers[0] == Random_Number) or (Random_Numbers[1] == Random_Number):
        Random_Numbers = []
        for x in range(2):
            Random_Numbers.append(random.randint(0, len(WordsImages) - 1))

    # =========================================
    # Random_Numbers=[]
    # for x in range(2):
    #    Random_Numbers.append(random.randint(0,len(WordsImages)-1))

    # ImageWords=[FruitWord, AppleWord, WatermelonWord, OrangeWord, PearWord, StrawberriesWord, GrapesWord, PineappleWord, AvocadoWord, LemonWord, MelonWord, CherriesWord, PeachWord, BananaWord, ApricotWord, BlueberriesWord, CoconutWord, FigWord, KiwiWord, MangoWord, NectarineWord, PapayaWord, PlumWord, RaspberryWord, PomegranateWord, LoquatWord, PersimmonWord, DatePalmWord, MandarinWord, GrapefruitWord, TomatoWord, BellPepperWord, PotatoWord, CarrotWord, CeleryWord, OnionWord, GarlicWord, CabbageWord, CucumberWord, LettuceWord, EggplantWord, PumpkinWord, BeetrootWord, CornWord, RadishWord, MushroomWord, PeaWord, OlivesWord, MilkWord, ButterWord, CheeseWord, SourCreamWord, IceCreamWord, SausageWord, EggWord, BeefWord, ChickenWord, LambWord, DessertWord, CakeWord]

    # Collection of 2 random words and 1 specific word matching the photo

    Mixed_Group = [Random_Numbers[0], Random_Numbers[1], Random_Number]

    # =========================================

    # The X-coordinate positions of each WordImage

    Positions = [200, 400, 600]

    Position1 = random.choice(Positions)
    Positions.remove(Position1)
    Position2 = random.choice(Positions)
    Positions.remove(Position2)
    Position3 = random.choice(Positions)
    Positions.remove(Position3)
    # print(Position1,Position2,Position3)
    # print(Positions)

    pygame.display.update()

    while not readinggameExit:

        BACK = Create_button(700, 0, 100, 50, BRIGHTRED, RED, "Back", BLACK, 45)

        screen.blit(ImageWords[Mixed_Group[0]], (Position1, 400))
        screen.blit(ImageWords[Mixed_Group[1]], (Position2, 400))
        screen.blit(ImageWords[Mixed_Group[2]], (Position3, 400))

        # print(ImageWords[Random_Numbers[0]])

        screen.blit(RandomImage, (300, 100))
        screen.blit(Speaker, (400, 0))

        screen.blit(Score, (21, 40))
        SCORE = Create_button(43, 80, 60, 60, BRIGHTYELLOW, WHITE, str(points), BLACK, 35)

        # Grid(10)
        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            if (BACK[0] < mouse[0] < BACK[0] + BACK[2] and BACK[1] < mouse[1] < BACK[1] + BACK[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):

                AreYouSure(WordsImages, ImageWords)


            elif (Position1 < mouse[0] < Position1 + 150 and 400 < mouse[1] < 500) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Mixed_Group[0] == Random_Number):

                points += 1
                Correct_Sound()
                Game_Loop(WordsImages, ImageWords)

            elif (Position1 < mouse[0] < Position1 + 150 and 400 < mouse[1] < 500) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Mixed_Group[0] != Random_Number):

                points -= 1
                Wrong_Sound()
                Game_Loop(WordsImages, ImageWords)


            elif (Position2 < mouse[0] < Position2 + 150 and 400 < mouse[1] < 500) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Mixed_Group[1] == Random_Number):

                points += 1
                Correct_Sound()
                Game_Loop(WordsImages, ImageWords)

            elif (Position2 < mouse[0] < Position2 + 150 and 400 < mouse[1] < 500) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Mixed_Group[1] != Random_Number):

                points -= 1
                Wrong_Sound()
                Game_Loop(WordsImages, ImageWords)


            elif (Position3 < mouse[0] < Position3 + 150 and 400 < mouse[1] < 500) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Mixed_Group[2] == Random_Number):

                points += 1
                Correct_Sound()
                Game_Loop(WordsImages, ImageWords)

            elif (Position3 < mouse[0] < Position3 + 150 and 400 < mouse[1] < 500) and (
                    event.type == pygame.MOUSEBUTTONDOWN) and (Mixed_Group[2] != Random_Number):

                points -= 1
                Wrong_Sound()
                Game_Loop(WordsImages, ImageWords)

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


#
##
# ============================== "Are You Sure?" =================================
# ================================================================================
def AreYouSure(WordImages, ImageWords):
    questionExit = False
    screen.fill(WHITE)
    screen.blit(AreYouSureImg, (0, 0))
    pygame.display.update()
    while not questionExit:
        YES = Create_button(150, 450, 150, 75, BRIGHTRED, RED, "Yes", BLACK, 45)
        NO = Create_button(500, 450, 150, 75, BRIGHTGREEN, GREEN, "No", BLACK, 45)
        pygame.display.update()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            if (YES[0] < mouse[0] < YES[0] + YES[2] and YES[1] < mouse[1] < YES[1] + YES[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Set_Choice()

            elif (NO[0] < mouse[0] < NO[0] + NO[2] and NO[1] < mouse[1] < NO[1] + NO[3]) and (
                    event.type == pygame.MOUSEBUTTONDOWN):
                Game_Loop(WordImages, ImageWords)

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


pygame.mixer.music.play(-1, 0.0)

Menu_Loop()