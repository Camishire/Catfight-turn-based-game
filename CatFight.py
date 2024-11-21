import array
from ast import Num
from asyncio.windows_events import NULL
import numbers
import random
from tkinter import BUTT, CENTER, Label
from turtle import back
import pygame
import sys
import math
import json
from collections import deque
from pyllist import sllist
import json

pygame.init()

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("CAT FIGHT")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, window_size)

font = pygame.font.Font("8-BIT WONDER.TTF", 80)
button_font = pygame.font.Font("8-BIT WONDER.TTF", 40)

text = font.render("CAT", True, WHITE)
text1 = font.render("FIGHT", True, BLACK)

text_rect = text.get_rect(center=(225, 100))
text_rect1 = text1.get_rect(center=(525, 100))
floating_speed = 0.002
amplitude = 4 
time = 0



NoOfPl = button_font.render("NUMBER OF PLAYERS", True, BLACK)
NoOfPl_rect = NoOfPl.get_rect(center=(400, 50))
Opl=font.render("ONE", True, BLACK)
Opl_rect = Opl.get_rect(center=(400, 100))
Tpl=font.render("TWO", True, BLACK)
Tpl_rect = Opl.get_rect(center=(400, 100))
NoOfPl_rect = NoOfPl.get_rect(center=(400, 50))
Opl_rect = Opl.get_rect(center=(400, 200))
Tpl_rect = Opl.get_rect(center=(375, 325))

Number = 0

Label1 = button_font.render("SELECT YOUR", True, BLACK)
Label1_rect = Label1.get_rect(center=(400, 200))
Label2 = button_font.render("CHARACTER", True, BLACK)
Label2_rect = Label1.get_rect(center=(430, 250))
P1 = button_font.render("P1", True, BLACK)
P1_rect = Label1.get_rect(center=(580, 100))
P2 = button_font.render("P2", True, BLACK)
P2_rect = Label1.get_rect(center=(580, 100))
Winner_label = button_font.render("WINNER", True, BLACK)
Winner_label_rect = Winner_label.get_rect(center=(415, 275))
TIE_label = button_font.render("TIE", True, BLACK)
TIE_label_rect = Winner_label.get_rect(center=(480, 310))

color1_image = pygame.image.load("whitepaw1.png")
color1_image = pygame.transform.scale(color1_image, (300, 300))
color1_rect = color1_image.get_rect(center=(415, 500))
color2_image = pygame.image.load("blackpaw1.png")
color2_image = pygame.transform.scale(color2_image, (300, 300))
color2_rect = color2_image.get_rect(center=(680, 500))
color3_image = pygame.image.load("orangepaw1.png")
color3_image = pygame.transform.scale(color3_image, (300, 300))
color3_rect = color3_image.get_rect(center=(150, 500))

P1_color = P2_color = P1_move = P2_move = 0
attack_combos = []
damage_values = []
with open("combos.json") as f:
    data = json.load(f)

    for combo, damage in data.items():
        attack_combos.append(combo)
        damage_values.append(damage)
       
P1_first=P1_last=P2_first=P2_last=-1
P1_queue = deque()
P2_queue = deque()
stack = deque()


P1_newhealth=P2_newhealth=0
P1_temp = P2_temp = ""
temp = 0
reset = 1


P1_combo_text = button_font.render(P1_temp, True, BLACK)
P2_combo_text = button_font.render(P2_temp, True, BLACK)
P1_combo_text_rect = P1_combo_text.get_rect(center=(50, 100))
P2_combo_text_rect = P2_combo_text.get_rect(center=(650, 100))


def game_logic(P1_move, P2_move):
    global P1_health, P2_health
    global Number
    
    if P1_move == P2_move :
        return
    elif P1_move == 1:
        if P2_move == 2 :
             P1_health -= 10
        if P2_move == 3 :
             P2_health -= 10
    elif P1_move == 2 :
        if P2_move == 1 :
             P2_health -= 10
        if P2_move == 3 :
             P1_health -= 10
    elif P1_move == 3 :
        if P2_move == 1 :
             P1_health -= 10
        if P2_move == 2 :
             P2_health -= 10
    
    return


game_state = True
running = True
secondmenu = False
charselect = False
maingame = False
winner = False

while game_state :
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    secondmenu = True
                    running = False

        window.blit(background_image, (0, 0))

        button_rect = pygame.Rect(500, 270, 240, 80)
        button_text = button_font.render("START", True, BLACK)
       
        float_offset = int(amplitude * math.sin(time))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        text_rect.y = 100 + float_offset
        text_rect1.y = 100 + float_offset
        button_rect.y = 270 + float_offset
        button_text_rect.centery = button_rect.centery
        time += floating_speed

        window.blit(text, text_rect)
        window.blit(text1, text_rect1)
        pygame.draw.rect(window, WHITE, button_rect)
        window.blit(button_text, button_text_rect)
        pygame.display.update()
        
    while secondmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                secondmenu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Opl_rect.collidepoint(event.pos):
                    charselect = True
                    Number = 1
                    secondmenu = False
                if Tpl_rect.collidepoint(event.pos):
                    charselect = True
                    Number = 2
                    secondmenu = False

        window.blit(background_image, (0, 0))
    
        float_offset = int(amplitude * math.sin(time))
        NoOfPl_rect.y = 50 + float_offset
        Opl_rect.y = 200 + float_offset
        Tpl_rect.y = 350 + float_offset

        time += floating_speed
    
        window.blit(NoOfPl, NoOfPl_rect)
        window.blit(Opl, Opl_rect)
        window.blit(Tpl, Tpl_rect)

        pygame.display.update()

    P1_color = 0
    P2_color = 0
    while charselect :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                charselect = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Number == 2 :
                    if P1_color > 0 and color1_rect.collidepoint(event.pos) :
                        P2_color = 1
                        maingame = True
                        charselect = False
                    if P1_color > 0 and color2_rect.collidepoint(event.pos) :
                        P2_color = 2
                        maingame = True
                        charselect = False
                    if P1_color > 0 and color3_rect.collidepoint(event.pos) :
                        P2_color = 3
                        maingame = True
                        charselect = False
                else :
                    P2_color = 2
                    maingame = True
                    charselect = False
                
                if P1_color == 0 and color1_rect.collidepoint(event.pos) : P1_color = 1
                elif P1_color == 0 and color2_rect.collidepoint(event.pos): P1_color = 2
                elif P1_color == 0 and color3_rect.collidepoint(event.pos): P1_color = 3
              
        window.blit(background_image, (0, 0))
    
        float_offset = int(amplitude * math.sin(time))
        Label1_rect.y = 200 + float_offset
        Label2_rect.y = 250 + float_offset
        P1_rect.y = 300 + float_offset
        P2_rect.y = 300 + float_offset

        time += floating_speed
        window.blit(Label1, Label1_rect)
        window.blit(Label2, Label2_rect)
        if P1_color == 0 :
            window.blit(P1, P1_rect)
        if P1_color > 0 and Number == 2 :
            window.blit(P2, P2_rect)
        window.blit(color1_image, color1_rect)
        window.blit(color2_image, color2_rect)
        window.blit(color3_image, color3_rect)
        pygame.display.update()
    
    if P1_color == 1:
            P1_paw1 = color1_image
            P1_paw2 = 0
            P1_paw3 = pygame.image.load("whitepaw3.png")
            P1_paw4 = pygame.image.load("whitepaw4.png")
            P1_paw5 = pygame.image.load("whitepaw5.png")

    if P1_color == 2:
            P1_paw1 = color2_image
            P1_paw2 = 0
            P1_paw3 = pygame.image.load("blackpaw3.png")
            P1_paw4 = pygame.image.load("blackpaw4.png")
            P1_paw5 = pygame.image.load("blackpaw5.png")
        
    if P1_color == 3:
            P1_paw1 = color3_image
            P1_paw2 = 0
            P1_paw3 = pygame.image.load("orangepaw3.png")
            P1_paw4 = pygame.image.load("orangepaw4.png")
            P1_paw5 = pygame.image.load("orangepaw5.png")
    if P2_color == 1:
            P2_paw1 = color1_image
            P2_paw3 = pygame.image.load("whitepaw3.png")
            P2_paw4 = pygame.image.load("whitepaw4.png")
            P2_paw5 = pygame.image.load("whitepaw5.png")
    if P2_color == 2:
            P2_paw1 = color2_image
            P2_paw3 = pygame.image.load("blackpaw3.png")
            P2_paw4 = pygame.image.load("blackpaw4.png")
            P2_paw5 = pygame.image.load("blackpaw5.png")
    if P2_color == 3:
            P2_paw1 = color3_image
            P2_paw3 = pygame.image.load("orangepaw3.png")
            P2_paw4 = pygame.image.load("orangepaw4.png")
            P2_paw5 = pygame.image.load("orangepaw5.png")
    


    P2_paw1_img = pygame.transform.scale(P2_paw1, (400, 400))
    P2_paw1_img = pygame.transform.rotate(P2_paw1_img, 270)


    health_images = {
        100: pygame.image.load("100health.png"),
        90: pygame.image.load("90health.png"),
        80: pygame.image.load("80health.png"),
        70: pygame.image.load("70health.png"),
        60: pygame.image.load("60health.png"),
        50: pygame.image.load("50health.png"),
        40: pygame.image.load("40health.png"),
        30: pygame.image.load("30health.png"),
        20: pygame.image.load("20health.png"),
        10: pygame.image.load("10health.png"),
        0: pygame.image.load("0health.png")
    }

    P1_paw1_img = pygame.transform.scale(P1_paw1, (400, 400))
    P1_paw1_img = pygame.transform.rotate(P1_paw1_img, 270)

    P1_health = 100
    P1_health = max(0, P1_health)
    P2_health = 100
    P2_health = max(0, P2_health)

    button_font = pygame.font.Font("8-BIT WONDER.TTF", 24)
    button_rect = pygame.Rect(0, 450, 275, 100)
    button_rect1 = pygame.Rect(525, 450, 310, 100)
    line1_text = button_font.render("A ROCK", True, BLACK)
    line2_text = button_font.render("S PAPER", True, BLACK)
    line3_text = button_font.render("D SCISSORS", True, BLACK)
    line11_text = button_font.render("ROCK LEFT", True, BLACK)
    line22_text = button_font.render("PAPER UP", True, BLACK)
    line33_text = button_font.render("SCISSORS RIGHT", True, BLACK)
    line4_text = button_font.render("BACK", True, BLACK)
    line1_rect = line1_text.get_rect(center=(button_rect.left+80, button_rect.top + 20))
    line2_rect = line2_text.get_rect(center=(button_rect.left+95, button_rect.top + 50))
    line3_rect = line3_text.get_rect(center=(button_rect.left+125, button_rect.top + 80))
    line4_rect = line4_text.get_rect(center=(400, 50))
    line11_rect = line11_text.get_rect(center=(button_rect1.right-135, button_rect1.top + 20))
    line22_rect = line22_text.get_rect(center=(button_rect1.right-125, button_rect1.top + 50))
    line33_rect = line33_text.get_rect(center=(button_rect1.right-145, button_rect1.top + 80))

    P1_temp=""
    P2_temp=""
    P1_queue.clear
    P2_queue.clear
    P1_last = -1
    P2_last = -1
    P1_first = -1
    P2_first = -1
    temp1 = temp2 = temp3 = 0
    
    def combocheck(P1_move, P2_move) :
        global P1_first, P1_last, P2_first, P2_last, P1_health, P2_health, P1_temp, P2_temp
        print( "P2 MOVE!!!! ", P2_move)
        
        if P1_first == -1 and P1_last == -1 :
           P1_queue.append(P1_move)
           P1_first = P1_last = 0
           P1_temp = str(P1_move)
           print ("STEP 1 : " , P1_queue)
           print ("FIRST, LAST " , P1_first, P1_last)
        else :
            P1_queue.append(P1_move)
            P1_last += 1
            temp1=len(P1_temp)
            if temp1 <= 2 :
                P1_temp += str(P1_move)
            else :
                P1_temp = P1_temp[1:]
                P1_temp += str(P1_move)
            print ("STEP 2 : " , P1_queue)
            print ("FIRST, LAST " , P1_first, P1_last)
            
        if P1_newhealth<P1_oldhealth :
            P1_temp = str(P1_move)
            P1_first=P1_last
            print ("STEP 3 : " , P1_queue)
            print ("FIRST, LAST " , P1_first, P1_last)
        elif P1_last - P1_first == 2  :
            temp3 = P1_queue[P1_last]
            P1_queue.pop()
            P1_last -= 1
            temp2 = P1_queue[P1_last]
            P1_queue.pop()
            P1_last -= 1
            if temp3 == temp2 :
                temp1 = P1_queue[P1_last]
                P1_queue.pop()
                P1_last -= 1
                if temp3 == temp2 == temp1 :
                    P1_temp = str(temp1) + str(temp2) + str(temp3)
                P1_queue.append(temp1)
                P1_last += 1
            P1_queue.append(temp2)
            P1_last += 1
            P1_queue.append(temp3)
            P1_last += 1 #BUTINAI PABAIGOJ LAST=FIRST
            print ("STEP 4 : " , P1_queue)
            print ("FIRST, LAST " , P1_first, P1_last)
        
        temp1 = len(P1_temp)
        print ("TEMP1 AND LEN", P1_temp, temp1)
        if temp1 == 3 :
            for i in range(len(attack_combos)) :
                if attack_combos[i] ==  P1_temp :
                    P2_health += damage_values[i]
                    P1_first = P1_last
                    print ("STEP 5 : " , P1_queue)
                    print ("FIRST, LAST " , P1_first, P1_last)
            P1_first = P1_last
        print()


        if P2_first == -1 and P2_last == -1 :
           P2_queue.append(P2_move)
           P2_first = P2_last = 0
           P2_temp = str(P2_move)
           print ("STEP 1 : " , P2_queue)
           print ("FIRST, LAST " , P2_first, P2_last)
        else :
            P2_queue.append(P2_move)
            P2_last += 1
            temp1=len(P2_temp)
            if temp1 <= 2 :
                P2_temp += str(P2_move)
            else :
                P2_temp = P2_temp[1:]
                P2_temp += str(P2_move)
            print ("STEP 2 : " , P2_queue)
            print ("FIRST, LAST " , P2_first, P2_last)
            
        if P2_newhealth<P2_oldhealth :
            P2_temp = str(P2_move)
            P2_first=P2_last
            print ("STEP 3 : " , P2_queue)
            print ("FIRST, LAST " , P2_first, P2_last)
        elif P2_last - P2_first == 2  :
            temp3 = P2_queue[P2_last]
            P2_queue.pop()
            P2_last -= 1
            temp2 = P2_queue[P2_last]
            P2_queue.pop()
            P2_last -= 1
            if temp3 == temp2 :
                temp1 = P2_queue[P2_last]
                P2_queue.pop()
                P2_last -= 1
                if temp3 == temp2 == temp1 :
                    P2_temp = str(temp1) + str(temp2) + str(temp3)
                P2_queue.append(temp1)
                P2_last += 1
            P2_queue.append(temp2)
            P2_last += 1
            P2_queue.append(temp3)
            P2_last += 1 #BUTINAI PABAIGOJ LAST=FIRST
            print ("STEP 4 : " , P2_queue)
            print ("FIRST, LAST " , P2_first, P2_last)
        
        temp1 = len(P2_temp)
        print ("TEMP1 AND LEN", P2_temp, temp1)
        if temp1 == 3 :
            for i in range(len(attack_combos)) :
                if attack_combos[i] ==  P2_temp :
                    P1_health += damage_values[i]
                    P2_first = P2_last
                    print ("STEP 5 : " , P2_queue)
                    print ("FIRST, LAST " , P2_first, P2_last)
            P2_first = P2_last
        
        P1_move = P2_move = 0
        print()

    def returning(x, y) :
        for i in range(x) :
            stack.pop()
        P1_health, P2_health, P1_first, P1_last, P2_first, P2_last, P1_temp, P2_temp = stack[-2]
        print(P1_health, P2_health, P1_first, P1_last, P2_first, P2_last, P1_temp, P2_temp)
            
            
        

    while maingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                maingame = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("How many times would you like to return? [1-2-3]")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    reset = 1
                    returning(reset, P1_last)
                    print(1)
                elif event.key == pygame.K_2:
                    reset = 2
                    returning(reset, P1_last)
                    print(2)
                elif event.key == pygame.K_3:
                    reset = 3
                    returning(reset, P1_last)
                    print(3)
        
                if Number == 2 and P2_move == 0:
                    if event.key == pygame.K_b:
                        P2_move = 1
                        P2_paw1_img = P2_paw3
                    elif event.key == pygame.K_n:
                        P2_move = 2
                        P2_paw1_img = P2_paw4
                    elif event.key == pygame.K_m:
                        P2_move = 3
                        P2_paw1_img = P2_paw5
        
                elif P1_move == 0:
                    if event.key == pygame.K_a:
                        P1_move = 1
                        P1_paw1_img = P1_paw3
                    elif event.key == pygame.K_s:
                        P1_move = 2
                        P1_paw1_img = P1_paw4
                    elif event.key == pygame.K_d:
                        P1_move = 3
                        P1_paw1_img = P1_paw5
            
                    if Number == 1:
                        P2_move = random.randint(1, 3)
                        if P2_move == 1:
                            P2_paw1_img = P2_paw3
                        elif P2_move == 2:
                            P2_paw1_img = P2_paw4
                        elif P2_move == 3:
                            P2_paw1_img = P2_paw5

                
                        
                        
                       
            if P1_move != 0 and P2_move!= 0 :
                P1_oldhealth=P1_health
                P2_oldhealth=P2_health
                game_logic(P1_move, P2_move)
                P1_newhealth=P1_health
                P2_newhealth=P2_health
                combocheck(P1_move, P2_move)
                stack.append((P1_health, P2_health, P1_first, P1_last, P2_first, P2_last, P1_temp, P2_temp))
                print (stack[P1_last])
                P2_move = 0
                P1_move = 0
                reset = 1
                P1_combo_text = button_font.render(str(P1_temp), True, BLACK)
                P2_combo_text = button_font.render(P2_temp, True, BLACK)
                    
            
        if P1_health <= 0 or P2_health <= 0 :
                P1_queue.clear()
                P2_queue.clear()
                P1_first=P1_last=P2_first=P2_last=temp1=temp2=temp3=-1
                P1_temp=P2_temp=""
                maingame = False
                winner = True
                break
        # image configs
        if reset == 1 :
            P1_healthbar = health_images.get(P1_health)
            P2_healthbar = health_images.get(P2_health)
            P2_healthbar = pygame.transform.flip(P2_healthbar, True, False)
            P1_paw1_img = pygame.transform.scale(P1_paw1_img, (400, 400))
            P2_paw1_img = pygame.transform.scale(P2_paw1_img, (400, 400))
            P2_paw1_img = pygame.transform.flip(P2_paw1_img, 1, 0)
            window.blit(background_image, (0, 0))
            window.blit(P1_paw1_img, (0, 125))
            window.blit(P2_paw1_img, (400, 125))
            window.blit(P1_healthbar, (25, 10))
            window.blit(P2_healthbar, (565, 10))
            pygame.draw.rect(window, WHITE, button_rect)
            pygame.draw.rect(window, WHITE, button_rect1)
            window.blit(line1_text, line1_rect)
            window.blit(line2_text, line2_rect)
            window.blit(line3_text, line3_rect)
            window.blit(line4_text, line4_rect)
            window.blit(line11_text, line11_rect)
            window.blit(line22_text, line22_rect)
            window.blit(line33_text, line33_rect)
            window.blit(P1_combo_text, P1_combo_text_rect)
            window.blit(P2_combo_text, P2_combo_text_rect)
            pygame.display.update()   
            reset = 0

    CONTPLAY_label = button_font.render("PLAY", True, BLACK)
    CONTPLAY_rect = CONTPLAY_label.get_rect(center=(360, 375))
    EXIT_label = button_font.render("EXIT", True, BLACK)
    EXIT_label_rect = EXIT_label.get_rect(center=(460, 375))

    while winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                winner = False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if CONTPLAY_rect.collidepoint(event.pos):
                    winner = False
                    running = True
                    break
                if EXIT_label_rect.collidepoint(event.pos):
                    game_state = False
                    winner = False
                    
        if P1_health > P2_health : win="P1"
        elif P2_health > P1_health : win="P2"
        else : win = "TIE"
        
        dictionary = {
            "WHO WON? : ": win,
            "HEALTH-DIFFERENCE : ": abs(P1_health-P2_health)
        }
        
        json_object = json.dumps(dictionary, indent=4)
        
        
                    
        window.blit(background_image, (0, 0))
        window.blit(Winner_label, Winner_label_rect)
        window.blit(CONTPLAY_label, CONTPLAY_rect)
        window.blit(EXIT_label, EXIT_label_rect)
        if P1_health > P2_health : window.blit(P1, P1_rect)
        elif P2_health > P1_health : window.blit(P2, P2_rect)
        else : window.blit(TIE_label, TIE_label_rect)
        pygame.display.update()
    with open("winners.json", "a") as outfile:
        outfile.write(json_object)

pygame.quit()
sys.exit()
