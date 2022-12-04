import pygame
import pygame_gui

class Menu:


    def __init__(self,screen,game) -> None:
        self.win_h = screen.get_height()
        self.win_w = screen.get_width()
        self.game = game
        self.screen=screen
        self.max_button_y = self.win_h-(self.win_h*0.2)
        self.max_button_h = self.win_h*0.2
   

        self.manager = pygame_gui.UIManager((self.win_w,self.win_h),"theme.json")
        self.def_elements()

    def draw(self):
        pygame.draw.rect(self.screen,(230,230,230),pygame.Rect((0,self.max_button_y),(self.win_w*.8,self.max_button_h)))
        self.manager.draw_ui(self.screen)


    def def_elements(self):
        self.nx_trn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, self.max_button_y+self.max_button_h*0.5), (100, 50)), text='Next Turn', manager=self.manager)
      
        self.auto_play = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, self.max_button_y+self.max_button_h*0.2), (100, 50)), text='Auto Play', manager=self.manager)
        self.auto_play_info = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, self.max_button_y+self.max_button_h*0.2), (50, 50)), text='Off', manager=self.manager)

        self.narrator = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.win_w*.8, 0), (self.win_w*.2, self.win_h)), html_text="", manager=self.manager)

        self.add_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((250, self.max_button_y+self.max_button_h*0.2), (50, 50)), text='Add', manager=self.manager)
        self.add_wolf = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, self.max_button_y+self.max_button_h*0.2), (75, 50)), text='Wolf', manager=self.manager)
        self.add_sheep = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((375, self.max_button_y+self.max_button_h*0.2), (75, 50)), text='Sheep', manager=self.manager)
        self.add_fox = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, self.max_button_y+self.max_button_h*0.5), (75, 50)), text='Fox', manager=self.manager)
        self.add_hedgehog= pygame_gui.elements.UIButton(relative_rect=pygame.Rect((525, self.max_button_y+self.max_button_h*0.2), (100, 50)), text='Hedgehog', manager=self.manager)
        self.add_hyena = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((445, self.max_button_y+self.max_button_h*0.2), (75, 50)), text='Hyena', manager=self.manager)

        self.save_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, self.max_button_y+self.max_button_h*0), (75, 50)), text='Save', manager=self.manager)
        self.load_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, self.max_button_y+self.max_button_h*0.3), (75, 50)), text='Load', manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, self.max_button_y+self.max_button_h*0.6), (75, 50)), text='Exit', manager=self.manager)
       

    def handle_button_press(self,event):
        if event.ui_element == self.nx_trn:
            print("nxt turn")
            self.game.next_turn = True
        if event.ui_element == self.auto_play:
            if self.game.auto_play == False:
                self.game.auto_play = True
                self.auto_play_info.set_text("On")
            else:
                self.game.auto_play = False
                self.auto_play_info.set_text("Off")