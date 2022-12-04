import pygame
import random


# mlecz, koka , lis jeż


class Entity:

    def load_texures(self,texture):
        self.default_texture=texture
        self.default_img = pygame.image.load(self.default_texture)

        self.image=self.default_img

    def __init__(self,x,y,cells,initiative_order_f):
        super().__init__()      
        self.load_texures("./textures/grass/grass_default.png")
        self.strength = 0
        self.initiative = 1
        self.x=x
        self.y=y
        self.cells=cells
        self.c_size=len(cells)
        self.initiative_order_f = initiative_order_f

    def out_of_boudns(self):
        if self.y == self.c_size:
            self.y=0
        if self.x == self.c_size:
            self.x=0
        if self.y == -1:
            self.y = self.c_size-1
        if self.x == -1:
            self.x = self.c_size-1


    def del_from_initiative(self,):
        initiative_order = self.initiative_order_f
        for ind_r,initiative_row in enumerate(initiative_order):
            for ind,entity in enumerate(initiative_row):
                if self is entity:

                    initiative_order[ind_r].pop(ind)

    def update(self,dt):
        pass
    
    def assign_position(self):
        self.cells[self.y][self.x] = self  

    def collision(self):
        pass

    def check_collision(self):
        if self.cells[self.y][self.x] is not None:
            return True
        return False

class Animal(Entity):

    def __init__(self, x, y, cells,initiative_order_f):
        super().__init__(x, y, cells,initiative_order_f)
        self.load_texures("./textures/animals/animal_default.png")
    
    def move(self):
        self.cells[self.y][self.x] = None
        chng_x = 0
        chng_y = 0
        while chng_y == 0 and chng_x == 0:
            chng_x = random.randint(-1,1)
            chng_y = random.randint(-1,1)
            self.x += chng_x
            self.y += chng_y

        self.out_of_boudns()      
       

        if self.check_collision():
            self.collision()  

        else:
            self.assign_position()

    def collision(self):
        super().collision()
        self.fight(self.cells[self.y][self.x])

    def fight(self,opponent):
        if self.strength >= opponent.strength:
            self.assign_position()
            if opponent.strength == 0:
                pass
            opponent.del_from_initiative()
        if self.strength < opponent.strength:
            self.cells[self.y][self.x] = opponent
            self.del_from_initiative()

    def update(self, dt):
        super().update(dt)
        self.move()


class Plant(Entity):
    

    def __init__(self, x, y, cells):
        super().__init__(x, y, cells)
        self.strength = 0
        self.initiative = 0

    def spread(self):
        pass

    def get_eaten(self,eater):
        pass
    

class Wolf(Animal):

    def __init__(self, x, y, cells,initiative_order_f):
        super().__init__(x, y, cells,initiative_order_f)
        self.initiative = 5
        self.strength = 9
        self.load_texures("./textures/animals/Wolf.png")


class Sheep(Animal):

    def __init__(self, x, y, cells,initiative_order_f):
        super().__init__(x, y, cells,initiative_order_f)
        self.initiative = 4
        self.strength = 4
        self.load_texures("./textures/animals/Sheep.png")


class Fox(Animal):

    def __init__(self, x, y, cells,initiative_order_f):
        super().__init__(x, y, cells,initiative_order_f)
        self.initiative = 7
        self.strength = 3
        self.load_texures("./textures/animals/Fox.png")


    def move(self):
        self.cells[self.y][self.x] = None
        chng_x = 0
        chng_y = 0
        while chng_y == 0 and chng_x == 0:
            chng_x = random.randint(-1,1)
            chng_y = random.randint(-1,1)
            self.x += chng_x
            self.y += chng_y

        self.out_of_boudns()      
       
        if self.check_collision():
            if self.cells[self.y][self.x].strength <= self.strength:
                self.assign_position()
            else:
                self.x -= chng_x
                self.y -= chng_y
                self.out_of_boudns()   
                self.assign_position()

        else:
            self.assign_position()