# implementation of card game - Memory

import simplegui
import random



deck = []
exposed = []

card1 = 0
card2 = 0

state = 0
turns = 0


def new_game():
    global deck, state, exposed, card1, card2, turns
    
    deck = range(8) + range(8)
    random.shuffle(deck)
    
    exposed = [False for x in deck] 
    
    state = turns = card1 = card2 = 0
    

def mouseclick(pos):
    
    card_num = pos[0] // 50
    
    if (exposed[card_num] != True):
        exposed[card_num] = True
        
        global card1, card2, state, turns
        
        if state == 0:
            state = 1
            card1 = card_num
            
        elif state == 1:
            state = 2
            card2 = card_num
            turns += 1
      
        else:
            state = 1
                           
            if (deck[card1] != deck[card2]):
                exposed[card1] = exposed[card2] = False 
                
            card1 = card_num    
    
 
def draw(canvas):    
    x = 0
    i = 0
    for num in deck:
        if exposed[i] == False:
            canvas.draw_line((x, 0), (x, 100), 2, 'yellow')
            canvas.draw_line((x, 0), (x+50, 0), 200, 'green')
        else:    
            canvas.draw_text(str(num), [x , 90], 115, "red")
        x += 50
        i += 1
    
    label.set_text("Turns = " + str(turns))   

    

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))


frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
