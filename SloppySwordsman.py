import pygame


import time
import random
import os
import pickle


import sys
import fileinput

pygame.init()

pygame.mixer.init()
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (222,41,16)
green = (0,255,0)
gold = (255, 222, 0)
gold2 = (198, 191, 0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
car_width = 40
car_height = 54
UI =(149, 165, 166)
emerald =(39, 174, 96)
pomegranate =(192, 57, 43)
pom =(231, 76, 60)
em =(46, 204, 113)
cover = pygame.image.load(os.path.join("data", 'cover.png'))
pygame.display.set_caption('Ricey : Sloppy Swordsman')

townbackground = pygame.image.load(os.path.join("data", 'town.png'))
clock = pygame.time.Clock()
expo = pygame.image.load(os.path.join("data", 'expo.png'))
controls = pygame.image.load(os.path.join("data", 'controls.png'))
alert = pygame.image.load(os.path.join("data", 'alert.png'))


right = False
pause = False
left = False
top = False
bottom = False
yes = "no"
zero = 0

damage = 0
WD = False
AD = False
DD = False
SD = False
pygame.mixer.music.load(os.path.join("data", 'town.mp3'))
disable = False
global disable
pygame.mixer.music.play(-1)
afterpause = False
message = pygame.image.load(os.path.join("data", 'message.png'))
still = pygame.image.load(os.path.join("data", 'back1.png'))
layer = pygame.image.load(os.path.join("data", 'backgroundlayer.png'))
layer2 = pygame.image.load(os.path.join("data", 'backgroundlayer2.png'))
oldguyimg = pygame.image.load(os.path.join("data", 'oldguy.png'))


oldguyimg2 = pygame.image.load(os.path.join("data", 'oldguy2.png'))
palace = pygame.image.load(os.path.join("data", 'palace.png'))
enemy1 = pygame.image.load(os.path.join("data", 'enemy1.png'))
enemy2 = pygame.image.load(os.path.join("data", 'enemy2.png'))
enemy3 = pygame.image.load(os.path.join("data", 'enemy3.png'))
battleenemy1 = pygame.image.load(os.path.join("data", 'battleenemy1.png'))
battleenemy2 = pygame.image.load(os.path.join("data", 'battleenemy2.png'))
battleenemy3 = pygame.image.load(os.path.join("data", 'battleenemy3.png'))
battlebackground = pygame.image.load(os.path.join("data", 'battlebackground.png'))
emperorimg=  pygame.image.load(os.path.join("data", 'emperor1.png'))
emperorimg2= pygame.image.load(os.path.join("data", 'emperor2.png'))
battleemperor = pygame.image.load(os.path.join("data", 'battleemperor.png'))
inventoryimg = pygame.image.load(os.path.join("data", 'inventory.png'))
dead = pygame.image.load(os.path.join("data", 'rip.png'))



enemydict = {'Health':20,'Maxhealth':20,'Attackmin':4,'Attackmax': 10,'Goldmin':5,'Goldmax':10}
emperordict = {'Health':35,'Maxhealth':35,'Attackmin':8,'Attackmax': 10,'Goldmin':10,'Goldmax':15}

savereadis = False
playerreadis = False

try:
    
    with open('save.pkl','rb') as infile:
        saveread = pickle.load(infile)
    savereadis = True
    with open('player.pkl','rb') as infile:
        playerread = pickle.load(infile)
        playerreadis = True
except:
    print "Savefile not found."
    print "Creating Savefile...."
    savefile = ['Placeholder']
    playerfile = {"X":360,"Y":450,"Health":30,'Maxhealth':30,"Healthafterdojo":50,"Attackmin":5,"Attackmax":15,"Potions":0,'Gold':0,'town':1}
    
    
    with open('save.pkl','wb') as outfile:
        pickle.dump(savefile,outfile)
    with open('save.pkl','rb') as infile:
        saveread = pickle.load(infile)

    with open('player.pkl','wb') as outfile:
        pickle.dump(playerfile,outfile)
    with open('player.pkl','rb') as infile:
        playerread = pickle.load(infile)

    

    print "Save Loaded."

    savefile = saveread
    playerfile = playerread
    
        
    


if savereadis == True:
    

    savefile = saveread

    print "Save Loaded."
    print saveread
if savereadis == True:
    playerfile = playerread
    print "Player Data Loaded."
    print playerread



        




def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,y,font,size,color,x = None):

    largeText=pygame.font.Font(os.path.join("data", font),size)
    TextSurf, TextRect=text_objects(text, largeText, color)
    if x == None:
        TextRect.center=((display_width/2),(y))
    else:
        TextRect.center=((x),(y))
    gameDisplay.blit(TextSurf, TextRect)

def button2(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        for event in pygame.event.get():

            click = pygame.mouse.get_pressed()
            if click[0] == 1 and action != None:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font(os.path.join("data", "freesansbold.ttf"),20)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)



def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font(os.path.join("data", "freesansbold.ttf"),20)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def test():
    health = str(playerfile['Health'])
    maxhealth = str(playerfile['Maxhealth'])
    potions = str(playerfile['Potions'])
    dmg = playerfile['Attackmin']
    dmeg = playerfile['Attackmax']

    damage = '  %d to %d' %(dmg,dmeg)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(inventory,(0,0))

        message_display(health,305,'freesansbold.ttf',20,black,190)
        message_display(maxhealth,333,'freesansbold.ttf',20,black,233)
        message_display(damage,355,'freesansbold.ttf',20,black,218)
        message_display(potions,140,'freesansbold.ttf',20,black,470)
        #button('Use')
        mouse = pygame.mouse.get_pos()
        500,130

        print mouse
        pygame.display.update()
def buttons(msg,x,y,w,h,ic,ac,aktion,ex,ye,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get:
    
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()
                action2(ex,ye)
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)







def op():
    pygame.mixer.music.load(os.path.join("data", 'op.mp3'))
    pygame.mixer.music.play(-1)
    
    gameDisplay.blit(cover,(0,0))

    pygame.display.update()
    clock.tick(15)
    time.sleep(3)
    if "Yes_Expo" in saveread:

        game_intro()
    if 'Yes_Tutorial' in saveread:
        game_intro()
    else:
        exposition()
        
    


def quitgame():
    quit()

def save():
    
    
    with open('save.pkl','wb') as outfile:
        pickle.dump(savefile,outfile)
    print "Saved...."
    with open('save.pkl','rb') as infile:
        saveread = pickle.load(infile)
    print "savefile",savefile
    print "saveread"
    print saveread


                
def saveplayer():
    print playerfile
    with open('player.pkl','wb') as outfile:
        pickle.dump(playerfile,outfile)
    

    with open('player.pkl','rb') as infile:
        playerread = pickle.load(infile)
    print playerread

def tutorial():


    exposition = True

    savefile.extend(['Yes_Tutorial'])
    save()
    print savefile


    while exposition:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(controls,(0,0))

        button(">",750,550,50,50,emerald,em,game_intro)
        pygame.display.update()

        clock.tick(15)



                
                         
def exposition():
    
    
    exposition = True

    savefile.extend(['Yes_Expo'])
    save()
    print savefile
	
    
    while exposition:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        gameDisplay.blit(expo,(0,0))
        
        button(">",750,550,50,50,emerald,em,tutorial)
        pygame.display.update()
        
        clock.tick(15)




def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        gameDisplay.fill(red)
        
        
        
        message_display("Sloppy Swordsman",300,"chinyen.ttf",60,gold)
        message_display("Ricey",200,"chinyen.ttf",100,gold)
        button("Start",350,450,100,50,emerald,em,save_checker)

        


        pygame.display.update()
        clock.tick(60)
    


#def say(x,y,text):
    
   # pygame.draw.polygon(gameDisplay, white,((x,y),(x + 1, y - 13),(x + 12 ,y - 13)))

   # pygame.draw.rect(gameDisplay,white,(x - 152 , y - 128 ,310,115))

    
    #pygame.draw.polygon(gameDisplay, white,((392,322),(393,309),(404,309)))
    #pygame.draw.rect(gameDisplay,white,(240,194,309,115))

   # pygame.display.update()
   # message_display("THIS IS A TEST TEST TEST TEST ETSTTTSSKDFJDSKLFJJJJJJJJJJJJJJJJJJJJSDFSDHFSDFHKJSFHJDSKHFJSKDHFKJSDFHJKSDFHJKDS",x,y,"freesansbold.ttf",20,black)



    

def save_checker():
    if playerfile['town'] == 1:

        game_loop()

    if playerfile['town'] == 2:
        game_loop2()
    if playerfile['town'] == 3:
        game_loop3()
    if playerfile['town'] == 4:
        game_loop4()




def say_(text):
    global pause
    global afterpause
    global x
    global y
    pause = True
    afterpause = True
    x = 300
    y = 300
    if pause == True:
        
        gameDisplay.blit(message,(0,400))
        message_display(text,420,"freesansbold.ttf",10,black)
        buttons(">",750,350,50,50,emerald,em,char,x,y,game_loop,)

        pygame.display.update()
        clock.tick(60)


def heal():
    global disable
    health = playerfile["Health"]
    maxhealth = playerfile["Maxhealth"]
    potions = playerfile["Potions"]
    helth = health + 10
    potin = potions - 1
    healsound = pygame.mixer.Sound(os.path.join("data", 'heal.ogg'))



    if playerread['Potions']  >= 0 and health != maxhealth and disable != True:
        potionamount = playerfile['Potions']
        potionsub = potionamount - 1


        if health + 10 < maxhealth:
            for key,value in playerfile.items():
                playerfile["Potions"] = potionsub
                playerfile['Health'] = helth
            saveplayer()
            healsound.play()
            disable = True
            print 'healing 1'
            inventory()

        elif health + 10 > maxhealth:
            difference = maxhealth - health
            for key,value in playerfile.items():
                playerfile["Potions"] = potionsub

                playerfile['Health'] = maxhealth
            disable = True
            print 'healing 2'
            healsound.play()
            inventory()
        saveplayer()
        difference = 10
        if disable == True:
            inventory()



def inventory():
    global disable
    health = str(playerfile['Health'])
    maxhealth = str(playerfile['Maxhealth'])
    potions = str(playerfile['Potions'])
    goldz = playerfile['Gold']
    gould = 'Gold - %d' %goldz
    dmg = playerfile['Attackmin']
    dmeg = playerfile['Attackmax']

    damage = '  %d to %d' %(dmg,dmeg)
    disable = False









    while True:
        mouse = pygame.mouse.get_pos()

        gameDisplay.blit(inventoryimg,(0,0))

        message_display(health,305,'freesansbold.ttf',20,black,190)
        message_display(maxhealth,333,'freesansbold.ttf',20,black,233)
        message_display(damage,355,'freesansbold.ttf',20,black,218)
        message_display(potions,140,'freesansbold.ttf',20,black,470)
        message_display(gould,190,'freesansbold.ttf',20,gold,420)

        button2('Use',500,130,50,50,emerald,em,heal)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:








                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:


                    save_checker()
        pygame.display.update()
        clock.tick(15)

def updatecheck():
    y = playerfile['Y']
    y -= 10
    for key,value in playerfile.items():
        playerfile["Y"] = y
    saveplayer()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:








                pygame.quit()
                quit()

        gameDisplay.fill(UI)
        message_display('This part is not yet downloaded!',100,'freesansbold.ttf',40,red)
        message_display('Check bokchoybuddhaboii.com for more info.',400,'freesansbold.ttf',38,black)
        button('OK',350,500,100,50,emerald,em,save_checker)
        pygame.display.update()








    
def game_loop():
    pygame.mixer.music.fadeout(500)
    pygame.mixer.music.load(os.path.join("data", 'town.mp3'))
    pygame.mixer.music.play(-1)
        
    print playerread
    if playerread['X'] != 360 and playerread['Y'] != 450:
        
        x = playerread['X']
        y = playerread['Y']
    else:
        
        x = 360
        y = 450

    global afterpause
    global x
    global y
    x_change = 0
    y_change = 0
    zero = 0
    gameExit = False
    chary = y
    charx = x
    xleft = 38
    xright = 167
    ytop = 161
    ybottom = 322
    left_images = []
    left_images.append( pygame.image.load(os.path.join("data", 'left1.png') ))
    left_images.append( pygame.image.load(os.path.join("data", 'left2.png') ))
    left_images.append( pygame.image.load(os.path.join("data", 'left3.png') ))
    right_images = []
    right_images.append( pygame.image.load(os.path.join("data", 'right1.png') ))
    right_images.append( pygame.image.load(os.path.join("data", 'right2.png') ))
    right_images.append( pygame.image.load(os.path.join("data", 'right3.png') ))
    forward_images = []
    forward_images.append( pygame.image.load(os.path.join("data", 'forward1.png') ))
    forward_images.append( pygame.image.load(os.path.join("data", 'forward2.png') ))
    forward_images.append( pygame.image.load(os.path.join("data", 'forward3.png') ))
    back_images = []
    back_images.append( pygame.image.load(os.path.join("data",'back1.png') ))
    back_images.append( pygame.image.load(os.path.join("data", 'back2.png') ))
    back_images.append( pygame.image.load(os.path.join("data", 'back3.png') ))
    left_current = 1
    right_current = 0
    forward_current = 0
    back_current = 0

    left_walking = True
    left_walking_steps = 0
    left_current = (left_current + 1) % len(left_images)
    left_player = left_images[ left_current ]

    right_walking = False
    right_walking_steps = 0
    right_current = (right_current + 1) % len(right_images)
    right_player = right_images[ right_current ]

    forward_walking = False
    forward_walking_steps = 0
    forward_current = (forward_current + 1) % len(forward_images)
    forward_player = forward_images[ forward_current ]

    back_walking = False
    back_walking_steps = 0
    back_current = (back_current + 1) % len(back_images)
    back_player = back_images[ back_current ]

    

                            
                        

                        
                    
                    
                    
                

    def refresh():
        
        game_loop()
    def oldguy():
        yessiree = True

        if 'oldguy' not in saveread:
            for key,value in playerfile.items():
                playerfile["Potions"] = 3
            saveplayer()
            savefile.extend(['oldguy'])
            save()
        if 'emperordefeated' in saveread:
            savefile.extend(['oldguyfinal'])
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load(os.path.join("data", 'dojo.mp3'))
        pygame.mixer.music.play(-1)
        while yessiree:
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()





            gameDisplay.fill(white)
            if 'emperordefeated' not in saveread:

                gameDisplay.blit(oldguyimg,(0,0))
            if 'emperordefeated' in saveread:
                gameDisplay.blit(oldguyimg2,(0,0))
                for key,value in playerfile.items():
                    playerfile["Maxhealth"] = 50
                    playerfile["Health"] = 50
                    playerfile["Attackmin"] = 10
                    playerfile["Attackmax"] = 20



            button('>',750,550,50,50,em,emerald,game_loop)

            pygame.display.update()
            clock.tick(15)
            save()
            saveplayer()
            
        
        

    

    
    
    
   

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

              
                
                
                
                


                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    
                    x_change = -8
                    left_walking = True
                    left_walking_steps = 5
                    

                if event.key == pygame.K_d:
                    
                    x_change = 8
                    right_walking = True
                    right_walking_steps = 5
                    


                if event.key == pygame.K_w:
                    

                    y_change = -8
                    forward_walking = True
                    forward_walking_steps = 5
                    



                if event.key == pygame.K_s:
                    print 'print detectteteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

                    y_change = 8
                    back_walking = True
                    back_walking_steps = 5
                if event.key == pygame.K_ESCAPE:

                    inventory()


                    


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                    left_current = 1
                    left_walking = False
                    right_walking = False
                    saveplayer()

                    
                
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                    forward_walking = False
                    back_walking = False
                    if  not y < 0:
                        saveplayer()
                    
        
                
        
        
        WD = False
        AD = False
        DD = False
        SD = False
        say = False
        pause = False
        #print 'Player - ' + str(x) + ',' + str(y)



        if left_walking == True:
        
            if left_walking_steps > 0:
                left_current = (left_current + 1) % len(left_images)
                left_player = left_images[ left_current ]
                
                
                if left_current == 3:
                    left_current 
            else:
                left_walking = False





        if right_walking == True:
        
            if right_walking_steps > 0:
                right_current = (right_current + 1) % len(right_images)
                right_player = right_images[ right_current ]
                
                
                
            else:
                right_walking = False

        if forward_walking == True:
        
            if forward_walking_steps > 0:
                forward_current = (forward_current + 1) % len(forward_images)
                forward_player = forward_images[ forward_current ]
                
                
                
            else:
                forward_walking = False


        if back_walking == True:
        
            if back_walking_steps > 0:
                back_current = (back_current + 1) % len(back_images)
                back_player = back_images[ back_current ]
                
                
                
            else:
                back_walking = False
                

        charRect = pygame.Rect(x,y,car_width,car_height)

        
        houseRectleft1 = pygame.Rect(36,167,10,151)
        houseRectright1 = pygame.Rect(164,167,5,151)
        houseRecttop1 = pygame.Rect(36,165,130,5)
        houseRectbottom1 = pygame.Rect(36,318,130,5)



        houseRectleft2 = pygame.Rect(598,128,5,145)
        houseRectright2 = pygame.Rect(721,128,5,145)
        houseRecttop2 = pygame.Rect(598,123,128,5)
        houseRectbottom2 = pygame.Rect(598,273,128,5)

        houseRectleft3 = pygame.Rect(633,379,5,143)
        houseRectright3 = pygame.Rect(756,379,5,143)
        houseRecttop3 = pygame.Rect(633,374,128,5)
        houseRectbottom3 = pygame.Rect(633,522,128,5)

        dojoRectleft = pygame.Rect(304,214,10,101)
        dojoRectright = pygame.Rect(462,214,5,101)
        dojoRectbottom = pygame.Rect(304,315,163,7)

        manRectleft = pygame.Rect(377,321,10,45)
        manRectright = pygame.Rect(402,321,5,45)
        manRectbottom = pygame.Rect(377,366,30,5)

        pagodaleft = pygame.Rect(300,154,5,53)
        pagodaright = pygame.Rect(465,154,5,53)
        pagodatop = pygame.Rect(300,154,170,5)


        

        
        
        if houseRectleft1.collidepoint(x + car_width,y) or houseRectleft1.collidepoint(x + car_width,y + car_height) or houseRectleft2.collidepoint(x + car_width,y) or houseRectleft2.collidepoint(x + car_width,y + car_height) or houseRectleft3.collidepoint(x + car_width,y) or houseRectleft3.collidepoint(x + car_width,y + car_height) or dojoRectleft.collidepoint(x + car_width,y) or dojoRectleft.collidepoint(x + car_width,y + car_height):
            
            x -= 8

        if houseRectright1.collidepoint(x,y) or houseRectright1.collidepoint(x,y + car_height) or houseRectright2.collidepoint(x,y) or houseRectright2.collidepoint(x,y + car_height) or houseRectright3.collidepoint(x,y) or houseRectright3.collidepoint(x,y + car_height) or dojoRectright.collidepoint(x,y) or dojoRectright.collidepoint(x,y + car_height):
            x += 8
        if houseRecttop1.collidepoint(x,y + car_height) or houseRecttop1.collidepoint(x + car_width,y + car_height) or houseRecttop2.collidepoint(x,y + car_height) or houseRecttop2.collidepoint(x + car_width,y + car_height) or houseRecttop3.collidepoint(x,y + car_height) or houseRecttop3.collidepoint(x + car_width,y + car_height):
            y -= 8
        if houseRectbottom1.collidepoint(x,y) or houseRectbottom1.collidepoint(x + car_width,y) or houseRectbottom2.collidepoint(x,y) or houseRectbottom2.collidepoint(x + car_width,y) or houseRectbottom3.collidepoint(x,y) or houseRectbottom3.collidepoint(x + car_width,y) or dojoRectbottom.collidepoint(x,y) or dojoRectbottom.collidepoint(x + car_width,y) or manRectbottom.collidepoint(x,y) or manRectbottom.collidepoint(x + car_width,y):
            y += 8
            
        if manRectleft.collidepoint(x + car_width,y) or manRectleft.collidepoint(x + car_width,y + car_height):
            for key,value in playerfile.items():
                playerfile["X"] = x - 20
            oldguy()
            
            
            
            
        
            
                
            
            
        if pagodatop.collidepoint(x,y + car_height) or pagodatop.collidepoint(x + car_width,y + car_height):
            y -= 8
        if pagodaleft.collidepoint(x + car_width,y) or pagodaleft.collidepoint(x + car_width,y + car_height):
            x-=8
        
        if pagodaright.collidepoint(x,y) or pagodaright.collidepoint(x,y + car_height) or manRectright.collidepoint(x,y) or manRectright.collidepoint(x,y + car_height):
            x+=8
        
        if not pause:
        
            gameDisplay.fill(white)
            gameDisplay.blit(townbackground,(0,0))
        if afterpause:
            char(83,406)
            afterpause = False


            
            
        #pygame.draw.rect(gameDisplay,green,(300,154,170,5))
        #pygame.draw.rect(gameDisplay,red,(300,154,5,53))
        #pygame.draw.rect(gameDisplay,green,(465,154,5,53))

        #pygame.draw.rect(gameDisplay,green,(36,318,130,2))

        #pygame.draw.rect(gameDisplay,black,(36,165,130,2))

        #pygame.draw.rect(gameDisplay,red,(36,167,10,151))

        #pygame.draw.rect(gameDisplay,white,(164,167,2,151))
        

        #pygame.draw.rect(gameDisplay,green,(598,273,128,5))

        #pygame.draw.rect(gameDisplay,black,(598,123,128,5))

        #pygame.draw.rect(gameDisplay,red,(598,128,5,145))

        #pygame.draw.rect(gameDisplay,white,(756,128,5,145))


        #pygame.draw.rect(gameDisplay,green,(633,522,128,5))
        #pygame.draw.rect(gameDisplay,black,(633,374,128,5))
        #pygame.draw.rect(gameDisplay,red,(633,379,5,143))
        #pygame.draw.rect(gameDisplay,white,(756,379,5,143))

        #pygame.draw.rect(gameDisplay,green,(304,315,163,5))
        #pygame.draw.rect(gameDisplay,red,(304,214,5,101))
        #pygame.draw.rect(gameDisplay,white,(462,214,5,101))

        #pygame.draw.rect(gameDisplay,green,(377,366,30,2))
        #pygame.draw.rect(gameDisplay,red,(377,321,5,45))
        #pygame.draw.rect(gameDisplay,white,(402,321,5,45))
        #377 366
        #30


        #pygame.draw.polygon(gameDisplay, white,((392,322),(393,309),(404,309)))
        #pygame.draw.rect(gameDisplay,white,(240,194,309,115))
        #384 309





        
        
            


        











        left_walking == True

        if left_walking == True:
            
            gameDisplay.blit(left_player,(x,y))

        elif right_walking == True:
            
            gameDisplay.blit(right_player,(x,y))

        elif back_walking == True:
            
            gameDisplay.blit(back_player,(x,y))
        elif forward_walking == True:
            
            gameDisplay.blit(forward_player,(x,y))
        else:
            gameDisplay.blit(still,(x,y))
        if 'oldguyfinal' in saveread:
            gameDisplay.blit(layer2,(0,0))
        else:

            gameDisplay.blit(layer,(0,0))
        #pygame.draw.rect(gameDisplay,red,(304,214,5,101))
        #pygame.draw.rect(gameDisplay,green,(462,214,5,101))
        #pygame.draw.rect(gameDisplay,white,(304,315,163,5))


        
        
            
        





        mouse = pygame.mouse.get_pos()
        print mouse



        

        

        if x > display_width- car_width:
            x -= 8
        if x < 0:
            x += 8

        if y + car_height > display_height:
            if 'emperordefeated' in saveread:
                try:
                    import extension
                    for key,value in playerfile.items():
                        playerfile['X'] = x
                        playerfile["Y"] = 0
                    saveplayer()

                    extension.game_loop3()
                except:
                    updatecheck()




            else:
                y -= 8
        if y < 0:
            for key,value in playerfile.items():
                playerfile['town'] = 2
                saveplayer()
            if x < 192:

                for key,value in playerfile.items():
                    playerfile['X'] = 195
                    playerfile["Y"] = display_height - car_height

                saveplayer()
            elif x > 608:
                for key,value in playerfile.items():
                    playerfile['X'] = 605 - car_width
                    playerfile["Y"] = display_height - car_height
                
                
                saveplayer()
                    
            else:
                for key,value in playerfile.items():
                    playerfile['X'] = x
                    playerfile["Y"] = display_height - car_height
                saveplayer()

                
            
            game_loop2()

        x += x_change
        y += y_change
        if  not y < 0:
            for key,value in playerfile.items():
                playerfile["X"] = x
                playerfile["Y"] = y

        

        pygame.display.update()
        clock.tick(10)





def game_loop2():
    pygame.mixer.music.fadeout(500)


    print playerread['Y']
    x = playerread['X']
    if playerread['Y'] != 546:
        
        y = playerread['Y']
    else:
        y = display_height - car_height
    
    pygame.mixer.music.load(os.path.join("data", 'town2.mp3'))
    pygame.mixer.music.play(-1)


    x_change = 0
    y_change = 0
    zero = 0
    gameExit = False

    xleft = 38
    xright = 167
    ytop = 161
    ybottom = 322
    left_images = []
    left_images.append( pygame.image.load(os.path.join("data", 'left1.png') ))
    left_images.append( pygame.image.load(os.path.join("data", 'left2.png') ))
    left_images.append( pygame.image.load(os.path.join("data", 'left3.png') ))
    right_images = []
    right_images.append( pygame.image.load(os.path.join("data", 'right1.png') ))
    right_images.append( pygame.image.load(os.path.join("data", 'right2.png') ))
    right_images.append( pygame.image.load(os.path.join("data", 'right3.png') ))
    forward_images = []
    forward_images.append( pygame.image.load(os.path.join("data", 'forward1.png') ))
    forward_images.append( pygame.image.load(os.path.join("data", 'forward2.png') ))
    forward_images.append( pygame.image.load(os.path.join("data", 'forward3.png') ))
    back_images = []
    back_images.append( pygame.image.load(os.path.join("data",'back1.png') ))
    back_images.append( pygame.image.load(os.path.join("data", 'back2.png') ))
    back_images.append( pygame.image.load(os.path.join("data", 'back3.png') ))
    left_current = 1
    right_current = 0
    forward_current = 0
    back_current = 0

    left_walking = True
    left_walking_steps = 0
    left_current = (left_current + 1) % len(left_images)
    left_player = left_images[ left_current ]

    right_walking = False
    right_walking_steps = 0
    right_current = (right_current + 1) % len(right_images)
    right_player = right_images[ right_current ]

    forward_walking = False
    forward_walking_steps = 0
    forward_current = (forward_current + 1) % len(forward_images)
    forward_player = forward_images[ forward_current ]

    back_walking = False
    back_walking_steps = 0
    back_current = (back_current + 1) % len(back_images)
    back_player = back_images[ back_current ]

    def buttonwiththreeargs(msg,x,y,w,h,ic,ac,action,arg1,arg2,arg3,arg4):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

            if click[0] == 1:
                action(arg1,arg2,arg3,arg4)
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText,black)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)
    def emperor():

        saveplayer()

        yessiree = True
        while yessiree:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()





            gameDisplay.fill(white)
            if 'emperordefeated' in saveread:
                gameDisplay.blit(emperorimg2,(0,0))

                button('>',750,550,50,50,em,emerald,game_loop2)
                save()
                for key,value in playerfile.items():
                    playerfile["Y"] += 10
                saveplayer()

            if 'emperordefeated' not in saveread:
                gameDisplay.blit(emperorimg,(0,0))

                buttonwiththreeargs('Fight',750,550,50,50,em,emerald,battle,'emperordefeated',battleemperor,emperordict,emperor)
                button('Later',0,550,50,50,em,emerald,game_loop2)
                for key,value in playerfile.items():
                    playerfile["Y"] += 10
                saveplayer()

            print playerfile['Y']
            pygame.display.update()
            clock.tick(15)
    def battle(enemy,battleperson,enemydict,destination):

        
        
        

        if "dojocompletejnwwjw" in saveread:
            attackmin = playerfile["Attackmin"] + 10
            attackmax = playerfile["Attackmax"] + 10
            health = playerfile["Health"] * 2
            maxhealth = playerfile["Maxhealth"] * 2
        else:
            attackmin = playerfile["Attackmin"]
            attackmax = playerfile["Attackmax"]
            health = playerfile["Health"]
            maxhealth = playerfile["Maxhealth"]
        damage = random.randrange(attackmin,attackmax)
        enemyhealth = enemydict["Health"]
        enemymaxhealth = enemydict["Health"]
        enemyattackmin = enemydict["Attackmin"]
        enemyattackmax = enemydict["Attackmax"]
        enemydamage = random.randrange(enemyattackmin,enemyattackmax)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        swordsound = pygame.mixer.Sound(os.path.join("data", 'sword.ogg'))
        damagesound = pygame.mixer.Sound(os.path.join("data", 'damagesound.ogg'))
        healsound = pygame.mixer.Sound(os.path.join("data", 'heal.ogg'))
        
        attackrect = pygame.Rect(330,407,136,30)
        damagedenemy = False
        timerenemy = 1000
        placeofhold = False
        potionrect = pygame.Rect(333,506,136,30)

        
        
        

        

            
       
                 
        while True:
            
            mouse =  pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            damage = random.randrange(attackmin,attackmax)
            enemydamage = random.randrange(enemyattackmin,enemyattackmax)
            enemytotal = "%d / %d" % (enemyhealth,enemymaxhealth)
            healthtotal = "%d / %d" % (health,maxhealth)
            

                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()    
            
                

                if attackrect.collidepoint(mouse[0],mouse[1]) and click[0] == 1:
                    

                    
                    print "clicked"
                    placeofhold = True
                            
                    enemyhealth -= damage
                            
                    print "took away enemy health"

                    swordsound = pygame.mixer.Sound(os.path.join("data", 'sword.ogg'))

                                
                    pygame.mixer.Sound.play(swordsound)
                    blitdamage(damage)
                        
                                
                                
                    damagedenemy = True
                        


                    if damagedenemy == True and health > 0:
                        time.sleep(1.5)
                        placeofhold = False
                        damagesound = pygame.mixer.Sound(os.path.join("data", 'damagesound.ogg'))
                        health -= enemydamage
                        pygame.mixer.Sound.play(damagesound)
                        blitenemydamage(enemydamage)
                        print "took away health"

                        damaged = True
                        damagedenemy = False
                if potionrect.collidepoint(mouse[0],mouse[1]) and click[0] == 1:
                    print 'potions workx'
                    if playerread['Potions']  >= 0:
                        potionamount = playerfile['Potions']
                        potionsub = potionamount - 1


                        for key,value in playerfile.items():
                            playerfile["Potions"] = potionsub
                        difference = 10
                        health += 10
                        if health > maxhealth:
                            difference = maxhealth - health
                            health = maxhealth

                        healsound.play()
                        blitheal(difference)
                        damagedenemy = True



                        if damagedenemy == True:
                            time.sleep(1.5)
                            placeofhold = False
                            damagesound = pygame.mixer.Sound(os.path.join("data", 'damagesound.mp3'))
                            health -= enemydamage
                            blitenemydamageafterheal(enemydamage)

                            damagesound.play()
                            damaged = True
                            damagedenemy = False
                            
                    
                        
                        
                            
                    
                        
                            
                            


            if enemyhealth <= 0:
                gameDisplay.blit(message,(0,400))

                pre = playerfile['Gold']
                for key,value in playerfile.items():
                    gold1 = random.randrange(enemydict['Goldmin'],enemydict['Goldmax'])
                    guld = '+ %d gold' %gold1

                total = pre + gold1
                for key,value in playerfile.items():

                    playerfile["Gold"] = total

                message_display(guld,500,'freesansbold.ttf',50,gold2,400)

                pygame.display.update()

                coins = pygame.mixer.Sound(os.path.join("data", 'coin.ogg'))

                pygame.mixer.Sound.play(coins)
                time.sleep(2)


                savefile.extend([enemy])
                save()
                for key,value in playerfile.items():
                            playerfile["Health"] = health
                saveplayer()
                pygame.mixer.music.fadeout(3000)
                destination()
            if health <= 0:



                for key,value in playerfile.items():
                        playerfile["Health"] = maxhealth
                saveplayer()
                pygame.mixer.music.fadeout(3000)

                for key,value in playerfile.items():
                    playerfile["Y"] = 450
                    playerfile['town'] = 1

                save()
                gameDisplay.blit(dead,(0,0))
                pygame.display.update()



                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join("data", 'sad.mp3'))
                pygame.mixer.music.play(-1)
                time.sleep(15)


                game_loop()

            
            #pygame.draw.rect(gameDisplay,green,(330,407,136,30))

                
                
            enemytotal = "%d / %d" % (enemyhealth,enemymaxhealth)
            healthtotal = "%d / %d" % (health,maxhealth)
            gameDisplay.fill(black)
            gameDisplay.blit(battlebackground,(0,0))
            gameDisplay.blit(battleperson,(22,132))
            message_display(healthtotal,440,'freesansbold.ttf',20,black,760)
            
            
            pygame.display.update()
                        
            #return damage



            def blitdamage(damage):
                minusdamage = "-%d" %damage
                message_display(minusdamage,100,'freesansbold.ttf',30,red,50)
                pygame.display.update()
                clock.tick(60)

            def blitenemydamage(enemydamage):

                timer = 100
                while timer > 1:
                    minusdamage = "-%d" %enemydamage
                    message_display(minusdamage,100,'freesansbold.ttf',30,red,750)
                    timer -= 1
                    pygame.display.update()
                    clock.tick(60)
            def blitheal(amount):

                timer = 100
                while timer > 1:
                    minusdamage = "+%d" %amount
                    message_display(minusdamage,100,'freesansbold.ttf',30,green,750)
                    timer -= 1
                    pygame.display.update()
                    clock.tick(60)
            def blitenemydamageafterheal(enemydamage):

                timer = 100
                while timer > 1:
                    minusdamage = "-%d" %enemydamage
                    message_display(minusdamage,100,'freesansbold.ttf',30,red,700)
                    timer -= 1
                    pygame.display.update()
                    clock.tick(60)






    


    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    
                    x_change = -8
                    left_walking = True
                    left_walking_steps = 5

                if event.key == pygame.K_d:
                    
                    x_change = 8
                    right_walking = True
                    right_walking_steps = 5


                if event.key == pygame.K_w:
                    

                    y_change = -8
                    forward_walking = True
                    forward_walking_steps = 5


                        
                if event.key == pygame.K_s:
                    
                    y_change = 8
                    back_walking = True
                    back_walking_steps = 5
                if event.key == pygame.K_ESCAPE:

                    inventory()



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                    left_current = 1
                    left_walking = False
                    right_walking = False
                    saveplayer()
                    
                
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                    forward_walking = False
                    back_walking = False
                    if y + car_height > display_height:
                        
                        saveplayer()
        
                
        
        

        #print 'Player - ' + str(x) + ',' + str(y)
        gameDisplay.fill(white)
        gameDisplay.blit(palace,(0,0))
        #print 'GAME 2222222222'


        if left_walking == True:
        
            if left_walking_steps > 0:
                left_current = (left_current + 1) % len(left_images)
                left_player = left_images[ left_current ]
                
                
                if left_current == 3:
                    left_current 
            else:
                left_walking = False





        if right_walking == True:
        
            if right_walking_steps > 0:
                right_current = (right_current + 1) % len(right_images)
                right_player = right_images[ right_current ]
                
                
                
            else:
                right_walking = False

        if forward_walking == True:
        
            if forward_walking_steps > 0:
                forward_current = (forward_current + 1) % len(forward_images)
                forward_player = forward_images[ forward_current ]
                
                
                
            else:
                forward_walking = False


        if back_walking == True:
        
            if back_walking_steps > 0:
                back_current = (back_current + 1) % len(back_images)
                back_player = back_images[ back_current ]
                
                
                
            else:
                back_walking = False
                

        charRect = pygame.Rect(x,y,car_width,car_height)

        
        
        

        
        
        


        bottomlefttree = pygame.Rect(180,412,10,198)
        bottomrighttree = pygame.Rect(611,412,10,198)
        
        toplefttree = pygame.Rect(120,230,10,177)
        toprighttree = pygame.Rect(672,230,10,177)
        
        bottomleftbottomtree = pygame.Rect(125,406,65,5)
        bottomrightbottomtree = pygame.Rect(605,406,65,5)
        
        toplefttoptree = pygame.Rect(129,225,240,5)
        toprighttoptree = pygame.Rect(428,225,241,5)







        if toplefttoptree.collidepoint(x,y) or toplefttoptree.collidepoint(x + car_width,y) or toprighttoptree.collidepoint(x,y) or toprighttoptree.collidepoint(x + car_width,y):
            y += 8
        if bottomleftbottomtree.collidepoint(x,y + car_height) or bottomleftbottomtree.collidepoint(x + car_width,y + car_height) or bottomrightbottomtree.collidepoint(x,y + car_height) or bottomrightbottomtree.collidepoint(x + car_width,y + car_height):
            y -= 8
 
        if toplefttree.collidepoint(x,y) or toplefttree.collidepoint(x,y + car_height) or bottomlefttree.collidepoint(x,y) or bottomlefttree.collidepoint(x,y + car_height):
            x+=8
        if toprighttree.collidepoint(x + car_width,y) or toprighttree.collidepoint(x + car_width,y + car_height) or bottomrighttree.collidepoint(x + car_width,y) or bottomrighttree.collidepoint(x + car_width,y + car_height):
            x -= 8
        
        
        


        #pygame.draw.rect(gameDisplay,white,(180,412,10,198))
        #pygame.draw.rect(gameDisplay,white,(120,230,10,177))
        #pygame.draw.rect(gameDisplay,green,(125,406,65,5))
        #pygame.draw.rect(gameDisplay,green,(129,225,240,5))
        #pygame.draw.rect(gameDisplay,green,(428,225,241,5))

        
        #99 tree height
        #65 tree width
            
        





        
        
            


        











        left_walking == True

        if left_walking == True:
            
            gameDisplay.blit(left_player,(x,y))

        elif right_walking == True:
            
            gameDisplay.blit(right_player,(x,y))

        elif back_walking == True:
            
            gameDisplay.blit(back_player,(x,y))
        elif forward_walking == True:
            
            gameDisplay.blit(forward_player,(x,y))
        else:
            gameDisplay.blit(still,(x,y))


        
        
            
        





        mouse = pygame.mouse.get_pos()
        
        print mouse

        



        

        

        if x > display_width- car_width:
            x -= 8
        if x < 0:
            x += 8

        if y + car_height > display_height:

            for key,value in playerfile.items():
                playerfile["Y"] = 0
                playerfile['town'] = 1

            saveplayer()
            game_loop()

        if y < 0:
            y+=8
        if y < 194:

            emperor()
        if playerfile['Y'] <= 455 and playerfile["Y"] > 422:
            if not 'enemy1' in saveread:
                gameDisplay.blit(alert,(201,420))
                pygame.display.update()
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load(os.path.join("data", "battlemusic.mp3"))
                pygame.mixer.music.play()

                battle('enemy1',battleenemy1,enemydict,game_loop2)
        if playerfile['Y'] <= 376 and playerfile["Y"] > 339:
            if not 'enemy2' in saveread:

                pygame.mixer.music.fadeout(1000)
                gameDisplay.blit(alert,(595,350))
                pygame.display.update()
                pygame.mixer.music.load(os.path.join("data", "battlemusic.mp3"))
                pygame.mixer.music.play()

                battle('enemy2',battleenemy2,enemydict,game_loop2)
        if playerfile['Y'] <= 273 and playerfile["Y"] > 248:
            if not 'enemy3' in saveread:
                gameDisplay.blit(alert,(201,250))
                pygame.display.update()

                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load(os.path.join("data", "battlemusic.mp3"))
                pygame.mixer.music.play()

                battle('enemy3',battleenemy3,enemydict,game_loop2)
            

        x += x_change
        y += y_change
        for key,value in playerfile.items():
            playerfile["X"] = x
            playerfile["Y"] = y








        pygame.display.update()
        clock.tick(10)






op()
