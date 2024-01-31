import pygame, sys
from pygame.math import Vector2 as V

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pos = V(350, 430)
        self.radius = 20
        self.state = 0
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.rect = pygame.draw.circle(screen, pygame.Color("black"), self.pos, self.radius + 3)

    def drawButton(self):
        flip_text = "flip!"
        flip_surface = flip_font.render(flip_text, True, pygame.Color("white"))
        flip_pos = V(350, 429)
        flip_rect = flip_surface.get_rect(center=flip_pos)

        pygame.draw.circle(screen, pygame.Color("black"), self.pos, self.radius + 3)
        if self.state == 1:
            pygame.draw.circle(screen, (209, 19, 19), self.pos, self.radius - 1)
        else:
            pygame.draw.circle(screen, pygame.Color("red"), self.pos, self.radius)
        screen.blit(flip_surface, flip_rect)

class Bit(pygame.sprite.Sprite):
    def __init__(self, pos, state=0):
        super().__init__()

        self.colors = {0: pygame.Color("white"), 1: (222, 2, 2)}
        self.pos = pos
        self.radius = 8
        self.state = state
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.rect = pygame.draw.circle(screen, self.colors[self.state], self.pos, self.radius)

    def drawBit(self):
        pygame.draw.circle(screen, self.colors[self.state], self.pos, self.radius)

class Moves:
    def __init__(self, state=0):
        self.moves = state

    def drawMoves(self):
        moves_text = f"Moves made: {self.moves}"
        moves_surface = target_font.render(moves_text, True, pygame.Color("black"))
        moves_pos = V(350, 210)
        moves_rect = moves_surface.get_rect(center=moves_pos)
        screen.blit(moves_surface, moves_rect)

class Count:
    def __init__(self):
        self.flip_count = 3
        self.size = V(20, 10)

        self.up_image = pygame.image.load("flip-main/graphics/uparrow.png").convert_alpha()
        self.up_image = pygame.transform.scale(self.up_image, self.size)
        self.up_rect = pygame.Rect(340, 323, self.size.x, self.size.y)

        self.down_image = pygame.transform.flip(self.up_image, False, True)
        self.down_rect = pygame.Rect(339, 340, self.size.x, self.size.y)

    def drawCount(self):
        count_text = f"{self.flip_count}"
        count_surface = target_font.render(count_text, True, pygame.Color("black"))
        count_pos = V(350, 350)
        count_rect = count_surface.get_rect(center=count_pos)
        screen.blit(count_surface, count_rect)

    def drawUpArrow(self):
        screen.blit(self.up_image, self.up_rect)

    def drawDownArrow(self):
        screen.blit(self.down_image, self.down_rect)

class QBits:
    def __init__(self, states):
        self.qbit_height = 135
        self.states = states

    def drawQBits(self):
        self.qbits = [Bit(V(210, self.qbit_height), self.states[0]),
                      Bit(V(250, self.qbit_height), self.states[1]),
                      Bit(V(290, self.qbit_height), self.states[2]),
                      Bit(V(330, self.qbit_height), self.states[3]),
                      Bit(V(370, self.qbit_height), self.states[4]),
                      Bit(V(410, self.qbit_height), self.states[5]), 
                      Bit(V(450, self.qbit_height), self.states[6]),
                      Bit(V(490, self.qbit_height), self.states[7])]
        for bit in self.qbits:
            bit.drawBit()

class GBits:
    def __init__(self, states=[0 for i in range(8)]):
        self.gbit_height = 270
        self.states = states

    def drawGBits(self):
        self.gbits = [Bit(V(210, self.gbit_height), self.states[0]), 
                      Bit(V(250, self.gbit_height), self.states[1]), 
                      Bit(V(290, self.gbit_height), self.states[2]),
                      Bit(V(330, self.gbit_height), self.states[3]),
                      Bit(V(370, self.gbit_height), self.states[4]),
                      Bit(V(410, self.gbit_height), self.states[5]), 
                      Bit(V(450, self.gbit_height), self.states[6]),
                      Bit(V(490, self.gbit_height), self.states[7])]
        for bit in self.gbits:
            bit.drawBit()

class MainMenuButton:
    def __init__(self, pos, text):
        self.pos = pos
        self.text = text
        self.surface = retry_font.render(self.text, True, pygame.Color("black"))
        self.rect = self.surface.get_rect(center=self.pos)

class StartScreen:
    def __init__(self):
        self.how_to_play_button = MainMenuButton(V(350, 275), "HOW TO PLAY")
        self.play_button = MainMenuButton(V(350, 340), "PLAY")

    def drawElements(self):
        self.drawLogo()
        self.drawHowToPlay()
        self.drawPlay()

    def drawLogo(self):
        logo_pos = V(360, 140)
        logo_size = V(250, 125)
        logo_image = pygame.image.load("flip-main/graphics/logo.png").convert_alpha()
        logo_image = pygame.transform.scale(logo_image, logo_size)
        logo_rect = logo_image.get_rect(center=logo_pos)

        screen.blit(logo_image, logo_rect)

    def drawHowToPlay(self):
        screen.blit(self.how_to_play_button.surface, self.how_to_play_button.rect)

    def drawPlay(self):
        screen.blit(self.play_button.surface, self.play_button.rect)

class Tutorial:
    def __init__(self):
        self.qbits = pygame.image.load("flip-main/graphics/eg.png").convert_alpha()
        self.qbits = pygame.transform.scale(self.qbits, (250, 25))
        self.qbits_rect = pygame.Rect(75, 180, 200, 20)

        self.harrow_size = 80
        self.left_arrow = pygame.image.load("flip-main/graphics/leftarrow.png").convert_alpha()
        self.left_arrow = pygame.transform.scale(self.left_arrow, (self.harrow_size, self.harrow_size))
        self.left_arrow_rect = pygame.Rect(450, 130, self.harrow_size, self.harrow_size)
        self.right_arrow = pygame.transform.flip(self.left_arrow, True, False)
        self.right_arrow_rect = pygame.Rect(530, 130, self.harrow_size, self.harrow_size)

        self.varrow_size = V(20, 10)
        self.up_arrow = pygame.image.load("flip-main/graphics/uparrow.png").convert_alpha()
        self.up_arrow = pygame.transform.scale(self.up_arrow, (self.varrow_size.x, self.varrow_size.y))
        self.up_arrow_rect = pygame.Rect(190, 319, self.varrow_size.x, self.varrow_size.y)
        self.down_arrow = pygame.transform.flip(self.up_arrow, False, True)
        self.down_arrow_rect = pygame.Rect(190, 363, self.varrow_size.x, self.varrow_size.y)

        self.button_pos = V(532, 345)
        self.radius = 20
        self.button = pygame.Surface((self.radius * 2, self.radius * 2))
        self.button_rect = pygame.draw.circle(screen, pygame.Color("black"), self.button_pos, self.radius + 3)

        self.back_size = V(30, 30)
        self.back = pygame.image.load("flip-main/graphics/return.png").convert_alpha()
        self.back = pygame.transform.scale(self.back, (self.back_size.x, self.back_size.y))
        self.back_rect = pygame.Rect(10, 10, self.back_size.x, self.back_size.y)

    def drawElements(self):
        self.drawTitle()
        self.drawTarget()
        self.drawArrows()
        self.drawCount()
        self.drawButton()
        self.drawReturn()

    def drawTitle(self):
        title_text = "HOW TO PLAY"
        title_pos = V(350, 60)
        title_surface = target_font.render(title_text, True, pygame.Color("black"))
        title_rect = title_surface.get_rect(center=title_pos)

        screen.blit(title_surface, title_rect)

    def drawTarget(self):
        target_text = "Target: 2 moves"
        target_surface = target_font.render(target_text, True, pygame.Color("black"))
        target_pos = V(200, 130)
        target_rect = target_surface.get_rect(midtop=target_pos)
        target_box_rect = pygame.Rect(40, 118, 320, 100)

        ex_text1 = "This is your goal. Reach it within"
        ex_text2 = "the number of moves indicated to win!"
        ex_surface1 = ex_font.render(ex_text1, True, pygame.Color("black"))
        ex_surface2 = ex_font.render(ex_text2, True, pygame.Color("black"))
        ex_pos1, ex_pos2 = V(200, 245), V(200, 270)
        ex_rect1 = ex_surface1.get_rect(center=ex_pos1)
        ex_rect2 = ex_surface2.get_rect(center=ex_pos2)

        pygame.draw.rect(screen, pygame.Color("black"), target_box_rect, 3)
        screen.blit(target_surface, target_rect)
        screen.blit(self.qbits, self.qbits_rect)
        screen.blit(ex_surface1, ex_rect1)
        screen.blit(ex_surface2, ex_rect2)

    def drawArrows(self):
        ex_text1 = "Use LEFT and RIGHT arrow keys to shift"
        ex_text2 = "the bits by 1 bit in each direction."
        ex_surface1 = ex_font.render(ex_text1, True, pygame.Color("black"))
        ex_surface2 = ex_font.render(ex_text2, True, pygame.Color("black"))
        ex_pos1, ex_pos2 = V(525, 245), V(525, 270)
        ex_rect1 = ex_surface1.get_rect(center=ex_pos1)
        ex_rect2 = ex_surface2.get_rect(center=ex_pos2)

        screen.blit(self.left_arrow, self.left_arrow_rect)
        screen.blit(self.right_arrow, self.right_arrow_rect)
        screen.blit(ex_surface1, ex_rect1)
        screen.blit(ex_surface2, ex_rect2)
        
    def drawCount(self):
        count_text = "Flip: 5 bits"
        count_pos = V(195, 345)
        count_surface = target_font.render(count_text, True, pygame.Color("black"))
        count_rect = count_surface.get_rect(center=count_pos)

        ex_text1 = "Use UP and DOWN arrow keys to change the"
        ex_text2 = "number of bits to be flipped from the start."
        ex_text3 = "You can flip at least 3 and at most 6 bits."
        ex_surface1 = ex_font.render(ex_text1, True, pygame.Color("black"))
        ex_surface2 = ex_font.render(ex_text2, True, pygame.Color("black"))
        ex_surface3 = ex_font.render(ex_text3, True, pygame.Color("black"))
        ex_pos1, ex_pos2, ex_pos3 = V(195, 400), V(195, 425), V(195, 450)
        ex_rect1 = ex_surface1.get_rect(center=ex_pos1)
        ex_rect2 = ex_surface2.get_rect(center=ex_pos2)   
        ex_rect3 = ex_surface3.get_rect(center=ex_pos3)       

        screen.blit(count_surface, count_rect)
        screen.blit(self.up_arrow, self.up_arrow_rect)
        screen.blit(self.down_arrow, self.down_arrow_rect)
        screen.blit(ex_surface1, ex_rect1)
        screen.blit(ex_surface2, ex_rect2)
        screen.blit(ex_surface3, ex_rect3)

    def drawButton(self):
        flip_text = "flip!"
        flip_surface = flip_font.render(flip_text, True, pygame.Color("white"))
        flip_pos = V(531, 344)
        flip_rect = flip_surface.get_rect(center=flip_pos)

        ex_text1 = "Press ENTER to flip the bits!"
        ex_text2 = "Each flip counts as a single move."
        ex_surface1 = ex_font.render(ex_text1, True, pygame.Color("black"))
        ex_surface2 = ex_font.render(ex_text2, True, pygame.Color("black"))
        ex_pos1, ex_pos2 = V(532, 400), V(532, 425)
        ex_rect1 = ex_surface1.get_rect(center=ex_pos1)
        ex_rect2 = ex_surface2.get_rect(center=ex_pos2)    

        pygame.draw.circle(screen, pygame.Color("black"), self.button_pos, self.radius + 3)
        pygame.draw.circle(screen, pygame.Color("red"), self.button_pos, self.radius)
        screen.blit(flip_surface, flip_rect)
        screen.blit(ex_surface1, ex_rect1)
        screen.blit(ex_surface2, ex_rect2)

    def drawReturn(self):
        screen.blit(self.back, self.back_rect)

class Levels:
    def __init__(self):
        self.xs, self.ys = [180, 265, 350, 435, 520], [230, 330]
        self.lev_poss = [V(self.xs[0], self.ys[0]),
                         V(self.xs[1], self.ys[0]),
                         V(self.xs[2], self.ys[0]),
                         V(self.xs[3], self.ys[0]),
                         V(self.xs[4], self.ys[0]),
                         V(self.xs[0], self.ys[1]),
                         V(self.xs[1], self.ys[1]),
                         V(self.xs[2], self.ys[1]),
                         V(self.xs[3], self.ys[1]),
                         V(self.xs[4], self.ys[1])]
        self.lev_texts = [f"{i}" for i in range(1, 11)]
        self.lev_surfaces = [target_font.render(self.lev_texts[i], True, pygame.Color("black")) for i in range(10)]
        self.lev_rects = [self.lev_surfaces[i].get_rect(center=self.lev_poss[i]) for i in range(10)]

    def drawElements(self):
        self.drawTitle()
        self.drawLevels()

    def drawTitle(self):
        title_text = "Levels"
        title_pos = V(350, 90)
        title_surface = level_font.render(title_text, True, pygame.Color("black"))
        title_rect = title_surface.get_rect(center=title_pos)

        screen.blit(title_surface, title_rect)

    def drawLevels(self):
        for i in range(10):
            screen.blit(self.lev_surfaces[i], self.lev_rects[i])

class MainGame:
    def __init__(self, level, state=[0, [0 for i in range(8)]]):
        self.bit_count = 8
        self.level = level
        self.qbit_states = levels_directory[level][0]
        self.min_moves = levels_directory[level][1]
        self.qbits = QBits(self.qbit_states)
        self.gbits = GBits(state[1])
        self.moves = Moves(state[0])
        self.count = Count()
        self.button = Button()

        self.retry_bg_rect1 = pygame.Rect(305, 209, 90, 35)
        self.retry_bg_rect2 = pygame.Rect(305, 215, 90, 35)
        self.next_bg_rect = pygame.Rect(274, 258, 150, 35)
        self.menu_bg_rect1 = pygame.Rect(274, 307, 150, 35)
        self.menu_bg_rect2 = pygame.Rect(274, 270, 150, 35)

        self.help_size = V(34, 34)
        self.help = pygame.image.load("flip-main/graphics/help.png").convert_alpha()
        self.help = pygame.transform.scale(self.help, (self.help_size.x, self.help_size.y))
        self.help_rect = pygame.Rect(9, 9, self.help_size.x, self.help_size.y)

        self.replay_size = V(30, 30)
        self.replay = pygame.image.load("flip-main/graphics/replay.png").convert_alpha()
        self.replay = pygame.transform.scale(self.replay, (self.replay_size.x, self.replay_size.y))
        self.replay_rect = pygame.Rect(50, 11, self.replay_size.x, self.replay_size.y)

        self.menu_size = V(30, 29)
        self.menu = pygame.image.load("flip-main/graphics/menu.png").convert_alpha()
        self.menu = pygame.transform.scale(self.menu, (self.menu_size.x, self.menu_size.y))
        self.menu_rect = pygame.Rect(90, 11, self.menu_size.x, self.menu_size.y)

    def drawElements(self):
        self.drawHelp()
        self.drawReplay()
        self.drawMenu()
        self.drawTarget()
        self.qbits.drawQBits()
        self.gbits.drawGBits()
        self.moves.drawMoves()
        self.drawFlip()
        self.count.drawCount()
        self.button.drawButton()
        self.drawFlipArrows()
        self.drawLevel()

    def drawHelp(self):
        screen.blit(self.help, self.help_rect)

    def drawReplay(self):
        screen.blit(self.replay, self.replay_rect)

    def drawMenu(self):
        screen.blit(self.menu, self.menu_rect)

    def drawFlipArrows(self):
        if self.count.flip_count == 3:
            self.count.down_rect = pygame.Rect(339, 370, 0, 0)
            self.count.drawUpArrow()
        elif 3 < self.count.flip_count < 6:
            self.count.up_rect = pygame.Rect(340, 323, self.count.size.x, self.count.size.y)
            self.count.down_rect = pygame.Rect(339, 370, self.count.size.x, self.count.size.y)
            self.count.drawUpArrow()
            self.count.drawDownArrow()
        elif self.count.flip_count == 6:
            self.count.up_rect = pygame.Rect(340, 323, 0, 0)
            self.count.drawDownArrow()

    def drawTarget(self):
        if self.min_moves == 1:
            target_text = "Target: 1 move"
            target_pos = V(350, 73)
        else:
            target_text = f"Target: {self.min_moves} moves"
            target_pos = V(347, 73)
        target_surface = target_font.render(target_text, True, pygame.Color("black"))
        target_rect = target_surface.get_rect(midtop=target_pos)
        target_box_rect = pygame.Rect(180, 62, 340, 100)

        pygame.draw.rect(screen, pygame.Color("black"), target_box_rect, 3)
        screen.blit(target_surface, target_rect)

    def rotateLeft(self):
        self.gbits.states = self.gbits.states[1:] + self.gbits.states[:1]

    def rotateRight(self):
        self.gbits.states = self.gbits.states[-1:] + self.gbits.states[:-1]

    def drawFlip(self):
        flip_text = "Flip:    bits"
        flip_surface = target_font.render(flip_text, True, pygame.Color("black"))
        flip_pos = V(345, 350)
        flip_rect = flip_surface.get_rect(center=flip_pos)
        screen.blit(flip_surface, flip_rect)

    def flipBits(self, count):
        new, old = self.gbits.states[:count], self.gbits.states[count:]
        for bit in range(len(new)):
            new[bit] = (new[bit] + 1) % 2
        self.gbits.states = new + old

    def checkWin(self):
        if self.qbits.states == self.gbits.states:
            if self.moves.moves <= self.min_moves: return 2
            else: return 1
        else: return 0 
        
    def drawEnd(self):
        box_size1, box_size2 = V(420, 280), V(420, 250)
        box_pos = V(138, 100)
        box_image = pygame.image.load("flip-main/graphics/win.png").convert_alpha()
        box_image1 = pygame.transform.scale(box_image, box_size1)
        box_image2 = pygame.transform.scale(box_image, box_size2)
        box_rect1 = pygame.Rect(box_pos.x, box_pos.y, box_size1.x, box_size1.y)
        box_rect2 = pygame.Rect(box_pos.x, box_pos.y, box_size2.x, box_size2.y)

        retry_pos1, retry_pos2 = V(350, 226), V(350, 232)
        retry_text = "RETRY (R)"
        retry_surface = flip_font.render(retry_text, True, pygame.Color("black"))
        retry_rect1 = retry_surface.get_rect(center=retry_pos1)
        retry_rect2 = retry_surface.get_rect(center=retry_pos2)

        next_pos = V(350, 274)
        next_text = "NEXT LEVEL (N)"
        next_surface = flip_font.render(next_text, True, pygame.Color("black"))
        next_rect = next_surface.get_rect(center=next_pos)

        menu_pos1, menu_pos2 = V(350, 324), V(350, 286)
        menu_text = "LEVEL SELECT (L)"
        menu_surface = flip_font.render(menu_text, True, pygame.Color("black"))
        menu_rect1 = menu_surface.get_rect(center=menu_pos1)
        menu_rect2 = menu_surface.get_rect(center=menu_pos2)

        if self.level == len(levels_directory) - 1:
            screen.blit(box_image2, box_rect2)
            pygame.draw.rect(screen, pygame.Color("gray"), self.retry_bg_rect2)
            pygame.draw.rect(screen, pygame.Color("black"), self.retry_bg_rect2, 2)
            pygame.draw.rect(screen, pygame.Color("gray"), self.menu_bg_rect2)
            pygame.draw.rect(screen, pygame.Color("black"), self.menu_bg_rect2, 2)
            screen.blit(retry_surface, retry_rect2)
            screen.blit(menu_surface, menu_rect2)
        else:
            screen.blit(box_image1, box_rect1)
            pygame.draw.rect(screen, pygame.Color("gray"), self.retry_bg_rect1)
            pygame.draw.rect(screen, pygame.Color("black"), self.retry_bg_rect1, 2)
            pygame.draw.rect(screen, pygame.Color("gray"), self.next_bg_rect)
            pygame.draw.rect(screen, pygame.Color("black"), self.next_bg_rect, 2)
            pygame.draw.rect(screen, pygame.Color("gray"), self.menu_bg_rect1)
            pygame.draw.rect(screen, pygame.Color("black"), self.menu_bg_rect1, 2)
            screen.blit(retry_surface, retry_rect1)
            screen.blit(next_surface, next_rect)
            screen.blit(menu_surface, menu_rect1)
    
    def drawWin(self):
        if self.checkWin() == 2:
            win_text = "YOU WIN!"
            win_pos = V(350, 155)
            win_surface = win_font.render(win_text, True, pygame.Color("black"))
            win_rect = win_surface.get_rect(center=win_pos)
            screen.blit(win_surface, win_rect)
        
        elif self.checkWin() == 1:
            win_text = "YOU LOSE!"
            win_pos = V(350, 155)
            win_surface = win_font.render(win_text, True, pygame.Color("black"))
            win_rect = win_surface.get_rect(center=win_pos)
            screen.blit(win_surface, win_rect)

    def retry(self):
        self.gbits.states = [0 for i in range(self.bit_count)]
        self.count.flip_count = 3
        self.moves.moves = 0

    def drawLevel(self):
        level_text = f"Level {self.level + 1}"
        level_surface = retry_font.render(level_text, True, pygame.Color("black"))
        level_pos = V(353, 22)
        level_rect = level_surface.get_rect(center=level_pos)
        screen.blit(level_surface, level_rect)

def startScreen(screen):
    clock = pygame.time.Clock()
    start_screen = StartScreen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_screen.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    levels(screen)
                elif start_screen.how_to_play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    tutorial(screen, -1)
        screen.fill((31, 158, 237))
        start_screen.drawElements()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def tutorial(screen, prev, state=None):
    clock = pygame.time.Clock()
    tutorial = Tutorial()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if tutorial.back_rect.collidepoint(pygame.mouse.get_pos()):
                    if prev == -1:
                        startScreen(screen)
                    else:
                        mainGame(screen, prev, state)
        screen.fill((31, 158, 237))
        tutorial.drawElements()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def levels(screen):
    clock = pygame.time.Clock()
    levels = Levels()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for level in range(10):
                    if levels.lev_rects[level].collidepoint(pygame.mouse.get_pos()):
                        mainGame(screen, level)

        screen.fill((31, 158, 237))
        levels.drawElements()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def mainGame(screen, level, state=[0, [0 for i in range(8)]]):
    clock = pygame.time.Clock()
    main_game = MainGame(level, state)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if main_game.retry_bg_rect1.collidepoint(pygame.mouse.get_pos()) or (main_game.replay_rect.collidepoint(pygame.mouse.get_pos()) and main_game.checkWin() == 0):
                    main_game.retry()
                elif main_game.next_bg_rect.collidepoint(pygame.mouse.get_pos()):
                    mainGame(screen, level + 1)
                elif main_game.menu_bg_rect1.collidepoint(pygame.mouse.get_pos()) or (main_game.menu_rect.collidepoint(pygame.mouse.get_pos()) and main_game.checkWin() == 0):
                    levels(screen)
                elif main_game.help_rect.collidepoint(pygame.mouse.get_pos()) and main_game.checkWin() == 0:
                    tutorial(screen, level, [main_game.moves.moves, main_game.gbits.states])
                elif event.key == pygame.K_UP and main_game.count.flip_count < 6:
                    main_game.count.flip_count += 1
                elif event.key == pygame.K_DOWN and main_game.count.flip_count > 3:
                    main_game.count.flip_count -= 1

            elif event.type == pygame.KEYDOWN and 0 < main_game.checkWin() <= 2:
                if event.key == pygame.K_r:
                    main_game.retry()
                elif event.key == pygame.K_n and level <= (len(levels_directory) - 1):
                    mainGame(screen, level + 1)
                elif event.key == pygame.K_l:
                    levels(screen)
                    
            elif event.type == pygame.KEYDOWN and main_game.checkWin() == 0:
                if event.key == pygame.K_r:
                    main_game.retry()
                elif event.key == pygame.K_LEFT:
                    main_game.rotateLeft()
                elif event.key == pygame.K_RIGHT:
                    main_game.rotateRight()
                elif event.key == pygame.K_UP and main_game.count.flip_count < 6:
                    main_game.count.flip_count += 1
                elif event.key == pygame.K_DOWN and main_game.count.flip_count > 3:
                    main_game.count.flip_count -= 1
                elif event.key == pygame.K_RETURN:
                    main_game.button.state = 1
                    main_game.moves.moves += 1
                    main_game.flipBits(main_game.count.flip_count)
            else:
                main_game.button.state = 0

        screen.fill((31, 158, 237))
        main_game.drawElements()
        if main_game.qbit_states == main_game.gbits.states:
            main_game.drawEnd()
            main_game.drawWin()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

levels_directory = {0: ([1, 1, 1, 0, 0, 0, 0, 0], 1),
                    1: ([1, 0, 0, 0, 0, 1, 1, 1], 1),
                    2: ([0, 0, 0, 0, 1, 1, 0, 0], 2),
                    3: ([1, 0, 0, 0, 1, 0, 0, 0], 2),
                    4: ([1, 1, 1, 0, 0, 1, 1, 0], 2),
                    5: ([1, 0, 0, 1, 1, 1, 0, 0], 2),
                    6: ([0, 0, 1, 0, 1, 0, 1, 0], 3),
                    7: ([1, 0, 1, 0, 1, 1, 0, 1], 3),
                    8: ([1, 0, 0, 1, 1, 0, 0, 1], 4),
                    9: ([0, 1, 0, 1, 0, 1, 0, 1], 4)} 

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
win_font = pygame.font.Font("flip-main/fonts/futura medium bt.ttf", 48)
level_font = pygame.font.Font("flip-main/fonts/futura medium bt.ttf", 40)
target_font = pygame.font.Font("flip-main/fonts/futura medium bt.ttf", 30)
retry_font = pygame.font.Font("flip-main/fonts/futura medium bt.ttf", 21)
flip_font = pygame.font.Font("flip-main/fonts/futura medium bt.ttf", 16)
ex_font = pygame.font.Font("flip-main/fonts/futura light bt.ttf", 18)

startScreen(screen)
