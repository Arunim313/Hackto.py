pip install pygame
import pygame, random
from random import randrange, shuffle
pygame.init()
screen = pygame.display.set_mode([400,400])
clock = pygame.time.Clock()
cells = []
MAP_WIDTH = 20
MAP_HEIGHT = 20
size = 20
steps = 0
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    draw_map()
    do_step()
    pygame.display.flip()
    clock.tick(3)
    print("Steps: " + str(steps))
    steps+=1
pygame.quit()
size = 20
# the model for our cells
class Cell:
    def __init__(self,x,y,dead,value):
        self.x = x
        self.y = y
        self.dead = dead
        self.value = value
        MAP_WIDTH = 20
MAP_HEIGHT = 20
steps = 0
# initialize the simulation map
def init_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            dead  = True if randrange(10) > 3 else False
            power = randrange(1,255)
            cell = Cell(x,y,dead,power)
            cells.append(cell)
            # draw graphics for the map with Pygame
def draw_map():
    for cell in cells:
        color = (0, 0, cell.value)
        pygame.draw.rect(screen, color, pygame.Rect(cell.x*size, cell.y*size, size, size))
        # do the next simulation step (generation)
def do_step():
    shuffle(cells)
    for cell in cells:
        if not cell.dead:
            neighbors = get_living_neighbors(cell)
            if len(neighbors) > 0:
                shuffle(neighbors)
                prey = neighbors[randrange(len(neighbors))]
                swap_cells(cell, prey)
                # get a cell from the grid
def get_cell(x,y):
    for cell in cells:
        if cell.x == x and cell.y == y:
            return cell
          # find the neighbors of a cell that are alive
def get_living_neighbors(cell):
    neighbors = []
    for y in range(-1,1):
        for x in range(-1,1):
            if cell.x + x < 0 or cell.x + x > MAP_WIDTH-1 or cell.y + y < 0 or cell.y + y > MAP_HEIGHT-1:
                pass
            else:
                neighbor_cell = get_cell(cell.x + x, cell.y + y)
                if not neighbor_cell.dead:
                    neighbors.append(neighbor_cell)
   return neighbors
def swap_cells(cellA, cellB):
    tempX = cellB.x
    tempY = cellB.y
    cellB.x = cellA.x
    cellB.y = cellA.y
    cellA.x = tempX
    cellA.y = tempY
    # we start the program here
init_map()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    draw_map()
    do_step()
    pygame.display.flip()
    clock.tick(3)
    print("Steps: " + str(steps))
    steps+=1
pygame.quit()
