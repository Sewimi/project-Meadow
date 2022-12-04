import pygame
import entities
import random
import time

HIGHEST_INITIATIVE = 7

class World:

    def __init__(self,size,parent_width,parent_height) -> None:
        self.size=size
        self.display_width = parent_width * 0.8
        self.display_height = parent_height *0.8
        self.cell_h = self.display_height / size  
        self.cell_w = self.display_width / size
        self.cells=[[None for j in range(size)] for i in range(size)]
        self.load_texures()
        self.initiative_order = [[]for i in range(HIGHEST_INITIATIVE)]
        # self.test = entities.Animal(3,3,self.cells)
        # self.cells[self.test.y][self.test.x] = self.test
        self.initialise_entities()

    def initialise_entities(self):
        for _ in range(10):
            animal=entities.Wolf(random.randint(0,self.size-1),random.randint(0,self.size-1),self.cells,self.initiative_order)
            self.cells[animal.y][animal.x] = animal
            self.add_to_intitiative_order(animal)
        for _ in range(10):
            animal=entities.Sheep(random.randint(0,self.size-1),random.randint(0,self.size-1),self.cells,self.initiative_order)
            self.cells[animal.y][animal.x] = animal
            self.add_to_intitiative_order(animal)
        for _ in range(10):
            animal=entities.Fox(random.randint(0,self.size-1),random.randint(0,self.size-1),self.cells,self.initiative_order)
            self.cells[animal.y][animal.x] = animal
            self.add_to_intitiative_order(animal)

    def add_entitiy(self,entity):
        x=random.randint(0,self.size-1)
        y=random.randint(0,self.size-1)
        while self.cells[y][x] is not None:
            x=random.randint(0,self.size-1)
            y=random.randint(0,self.size-1)
            animal=entities.Fox(x,y,self.cells,self.initiative_order)
        self.cells[animal.y][animal.x] = animal
        self.add_to_intitiative_order(animal)


    def add_to_intitiative_order(self,animal):
        self.initiative_order[HIGHEST_INITIATIVE-animal.initiative].append(animal)

    def load_texures(self):
        self.grass_default_link = "./textures/background/bg.png"
        self.grass_default_texture = pygame.image.load(self.grass_default_link)
        self.grass_default_texture = pygame.transform.scale(self.grass_default_texture,(self.cell_w,self.cell_h))

    def draw(self,screen):
        for r_ind,row in enumerate(self.cells):
            for ind,cell in enumerate(row):
                screen.blit(self.grass_default_texture,(((ind*self.cell_w)//1),((r_ind*self.cell_h)//1)))
                if cell is not None:
                    im=cell.image
                    im=pygame.transform.scale(im,(self.cell_w,self.cell_h))
                    screen.blit(im,(((ind*self.cell_w)//1),((r_ind*self.cell_h)//1)))

    def update(self,dt):
        c=0
        # for r_ind,row in enumerate(self.cells):
        #     for ind,cell in enumerate(row):
        #         if cell is not None:
        #             cell.update(dt)
                    
        for i in self.initiative_order:
            for entity in i:
                entity.update(dt)

        for r_ind,row in enumerate(self.cells):
            for ind,cell in enumerate(row):
                if cell is not None:
                    if isinstance(cell,entities.Fox):
                        c+=1

        # print(c,"real number-------------------------------------")
        # print(len(self.initiative_order[0]),"number in initiative-----------------")
 