import random
import os
import sys
import pygame

pygame.init()
info = pygame.display.Info()
clock = pygame.time.Clock()

try:
    dir_path = sys._MEIPASS
except Exception:
    dir_path = os.path.abspath(".")

image_dir_path = os.path.join(dir_path, "images").replace("\\", "\\\\")

closed_tile_path = os.path.join(image_dir_path, "closed.png")
opened_tile_path = os.path.join(image_dir_path, "opened.png")
flag_tile_path = os.path.join(image_dir_path, "flag.png")
mine_tile_path = os.path.join(image_dir_path, "mine.png")
mine_red_tile_path = os.path.join(image_dir_path, "mine_red.png")
mine_wrong_tile_path = os.path.join(image_dir_path, "mine_wrong.png")
text_path = os.path.join(image_dir_path, "text.png")

face_unpressed_tile_path = os.path.join(image_dir_path, "face_unpressed.png")
face_pressed_tile_path = os.path.join(image_dir_path, "face_pressed.png")
face_win_tile_path = os.path.join(image_dir_path, "face_win.png")
face_lose_tile_path = os.path.join(image_dir_path, "face_lose.png")

count_1_tile_path = os.path.join(image_dir_path, "type1.png")
count_2_tile_path = os.path.join(image_dir_path, "type2.png")
count_3_tile_path = os.path.join(image_dir_path, "type3.png")
count_4_tile_path = os.path.join(image_dir_path, "type4.png")
count_5_tile_path = os.path.join(image_dir_path, "type5.png")
count_6_tile_path = os.path.join(image_dir_path, "type6.png")
count_7_tile_path = os.path.join(image_dir_path, "type7.png")
count_8_tile_path = os.path.join(image_dir_path, "type8.png")

digit_background_tile_path = os.path.join(image_dir_path, "nums_background.png")
digit_0_tile_path = os.path.join(image_dir_path, "d0.png")
digit_1_tile_path = os.path.join(image_dir_path, "d1.png")
digit_2_tile_path = os.path.join(image_dir_path, "d2.png")
digit_3_tile_path = os.path.join(image_dir_path, "d3.png")
digit_4_tile_path = os.path.join(image_dir_path, "d4.png")
digit_5_tile_path = os.path.join(image_dir_path, "d5.png")
digit_6_tile_path = os.path.join(image_dir_path, "d6.png")
digit_7_tile_path = os.path.join(image_dir_path, "d7.png")
digit_8_tile_path = os.path.join(image_dir_path, "d8.png")
digit_9_tile_path = os.path.join(image_dir_path, "d9.png")

#----------------------------------------------------------------------------------

closed_tile_image = pygame.image.load(closed_tile_path)
opened_tile_image = pygame.image.load(opened_tile_path)
flag_tile_image = pygame.image.load(flag_tile_path)
mine_tile_image = pygame.image.load(mine_tile_path)
mine_red_tile_image = pygame.image.load(mine_red_tile_path)
mine_wrong_tile_image = pygame.image.load(mine_wrong_tile_path)
text_image = pygame.image.load(text_path)

face_unpressed_tile_image = pygame.image.load(face_unpressed_tile_path)
face_pressed_tile_image = pygame.image.load(face_pressed_tile_path)
face_win_tile_image = pygame.image.load(face_win_tile_path)
face_lose_tile_image = pygame.image.load(face_lose_tile_path)

count_1_tile_image = pygame.image.load(count_1_tile_path)
count_2_tile_image = pygame.image.load(count_2_tile_path)
count_3_tile_image = pygame.image.load(count_3_tile_path)
count_4_tile_image = pygame.image.load(count_4_tile_path)
count_5_tile_image = pygame.image.load(count_5_tile_path)
count_6_tile_image = pygame.image.load(count_6_tile_path)
count_7_tile_image = pygame.image.load(count_7_tile_path)
count_8_tile_image = pygame.image.load(count_8_tile_path)

digit_background_tile_image = pygame.image.load(digit_background_tile_path)
digit_0_tile_image = pygame.image.load(digit_0_tile_path)
digit_1_tile_image = pygame.image.load(digit_1_tile_path)
digit_2_tile_image = pygame.image.load(digit_2_tile_path)
digit_3_tile_image = pygame.image.load(digit_3_tile_path)
digit_4_tile_image = pygame.image.load(digit_4_tile_path)
digit_5_tile_image = pygame.image.load(digit_5_tile_path)
digit_6_tile_image = pygame.image.load(digit_6_tile_path)
digit_7_tile_image = pygame.image.load(digit_7_tile_path)
digit_8_tile_image = pygame.image.load(digit_8_tile_path)
digit_9_tile_image = pygame.image.load(digit_9_tile_path)
digit_images = [digit_0_tile_image, digit_1_tile_image, digit_2_tile_image, digit_3_tile_image, digit_4_tile_image, digit_5_tile_image, digit_6_tile_image, digit_7_tile_image, digit_8_tile_image, digit_9_tile_image]

#height, width, bombs, cell width, cell height
easy = (8, 10, 10, (25, 25))
medium = (14, 18, 40, (25, 25))
hard = (20, 24, 99, (25, 25))

difficulty = medium

rows = difficulty[0]
cols = difficulty[1]
bomb_count = difficulty[2]
rectangle_width = difficulty[3][0]
rectangle_height = difficulty[3][1]

screen_width = rectangle_width * cols
screen_height = (rectangle_height * rows) + 50

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minesweeper")

bomb_positions = []
flag_positions = []
flags = bomb_count

class Cell():
    def __init__(self, x, y):
        self.gridx = x
        self.gridy = y
        self.w = rectangle_width
        self.h = rectangle_height
        self.x = self.gridx * self.w
        self.y = (self.gridy * self.h) + 50
        self.count = 0
        self.bomb = False
        self.flagged = False
        self.open = False
        self.boom = False
        self.updating = True

    def update(self):
        self.w = rectangle_width
        self.h = rectangle_height
        self.x = self.gridx * self.w
        self.y = (self.gridy * self.h) + 50
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if not self.flagged and not self.open:
            self.image = closed_tile_image
        elif self.open:
            if self.bomb:
                self.image = mine_tile_image
            elif self.count == 0:
                self.image = opened_tile_image
            elif self.count == 1:
                self.image = count_1_tile_image
            elif self.count == 2:
                self.image = count_2_tile_image
            elif self.count == 3:
                self.image = count_3_tile_image
            elif self.count == 4:
                self.image = count_4_tile_image
            elif self.count == 5:
                self.image = count_5_tile_image
            elif self.count == 6:
                self.image = count_6_tile_image
            elif self.count == 7:
                self.image = count_7_tile_image
            elif self.count == 8:
                self.image = count_8_tile_image
        if self.flagged:
            self.image = flag_tile_image
        if not self.updating:
            if not self.flagged and self.bomb:
                self.image = mine_tile_image
            elif self.flagged and not self.bomb:
                self.image = mine_wrong_tile_image
            if self.boom:
                self.image = mine_red_tile_image
        self.image = pygame.transform.scale(self.image, self.rect.size)

    def render(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def open_neighbors(self):
        offsets = [
        (-1, -1), #top left
        (0, -1), #top mid
        (1, -1), #top right
        (-1, 0), #left
        (1, 0), #right
        (-1, 1), #bottom left
        (0, 1), #bottom mid
        (1, 1), #bottom right
        ]
        for offset in offsets:
            new_x = self.gridx + offset[0]
            new_y = self.gridy + offset[1]
            if new_x < 0 or new_y < 0 or new_x >= cols or new_y >= rows:
                continue
            neighbor = grid[new_y][new_x]
            if neighbor.bomb == False:
                neighbor.clicked(1)
    
    def open_all(self):
        offsets = [
        (-1, -1), #top left
        (0, -1), #top mid
        (1, -1), #top right
        (-1, 0), #left
        (1, 0), #right
        (-1, 1), #bottom left
        (0, 1), #bottom mid
        (1, 1), #bottom right
        ]
        for offset in offsets:
            new_x = self.gridx + offset[0]
            new_y = self.gridy + offset[1]
            if new_x < 0 or new_y < 0 or new_x >= cols or new_y >= rows:
                continue
            neighbor = grid[new_y][new_x]
            if not neighbor.open:
                neighbor.open = True
                neighbor.updating = False
                neighbor.open_all()

    def clicked(self, btn):
        global flags, flag_positions, lost
        if btn == 1:
            if self.flagged or self.open:
                return
            if self.bomb:
                self.open = True
                self.boom = True
                self.updating = False
                self.open_all()
                lost = True
            elif self.count == 0:
                self.open = True
                self.open_neighbors()
            else:
                self.open = True
        elif btn == 3:
            if self.open:
                return
            if self.flagged:
                self.flagged = False
                flags += 1
                flag_positions.remove((self.gridx, self.gridy))
            elif not self.flagged:
                self.flagged = True
                flags -= 1
                flag_positions.append((self.gridx, self.gridy))

    def is_clicked(self, pos):
        return (self.x + self.w > pos[0]) and (self.x < pos[0]) and (self.y + self.h > pos[1]) and (self.y < pos[1])

class Face():
    def __init__(self):
        self.x = 100
        self.y = 0
        self.image = pygame.transform.scale(face_unpressed_tile_image, (50, 50))
        self.rect = self.image.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height
        self.up = False
        self.down = False

    def update(self):
        if self.up:
            self.up = False
            self.down = False
            self.image = pygame.transform.scale(face_unpressed_tile_image, (50, 50))
            update_difficulty(difficulty)
        if lost:
            self.image = pygame.transform.scale(face_lose_tile_image, (50, 50))
        if won:
            self.image = pygame.transform.scale(face_win_tile_image, (50, 50))
        if self.down:
            self.image = pygame.transform.scale(face_pressed_tile_image, (50, 50))
        if not self.up and not self.down and not won and not lost:
            self.image = pygame.transform.scale(face_unpressed_tile_image, (50, 50))

    def mouse_up(self):
        self.up = True
        self.down = False

    def mouse_down(self):
        self.down = True

    def is_clicked(self, pos):
        return (self.x + self.w > pos[0]) and (self.x < pos[0]) and (self.y + self.h > pos[1]) and (self.y < pos[1])

def generate_grid():
    grid = []
    for y in range(rows):
        grid.append([])
        for x in range(cols):
            grid[y].append(Cell(x, y))
    return grid

def generate_bombs(seed = None):
    global grid
    if seed is None:
        seed = random.randint(0, 123456789)
    random.seed(seed)
    
    bombs_needed = bomb_count
    while bombs_needed > 0:
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        if (x, y) not in bomb_positions:
            bomb_positions.append((x, y))
            grid[y][x].bomb = True
            bombs_needed -= 1

def update_cell_counts():
    global grid
    offsets = [
        (-1, -1), #top left
        (0, -1), #top mid
        (1, -1), #top right
        (-1, 0), #left
        (1, 0), #right
        (-1, 1), #bottom left
        (0, 1), #bottom mid
        (1, 1), #bottom right
    ]
    for bomb_pos in bomb_positions:
        for offset in offsets:
            if bomb_pos[0] + offset[0] >= 0 and bomb_pos[0] + offset[0] < cols and bomb_pos[1] + offset[1] >= 0 and bomb_pos[1] + offset[1] < rows:
                new_pos = (bomb_pos[0] + offset[0], bomb_pos[1] + offset[1])
                if grid[new_pos[1]][new_pos[0]].bomb == False:
                    grid[new_pos[1]][new_pos[0]].count += 1

def get_cell(pos):
    clicked_cell = None
    for y in range(rows):
        for x in range(cols):
            if grid[y][x].is_clicked(pos):
                clicked_cell = grid[y][x]
    return clicked_cell

def update_difficulty(mode = None):
    global difficulty, rows, cols, bomb_count, rectangle_width, rectangle_height, screen_width, screen_height, screen, grid, bomb_positions, flag_positions, lost, won, flags

    if mode:
        difficulty = mode
    elif difficulty == easy:
        difficulty = medium
    elif difficulty == medium:
        difficulty = hard
    elif difficulty == hard:
        difficulty = easy

    bomb_positions = []
    flag_positions = []

    rows = difficulty[0]
    cols = difficulty[1]
    bomb_count = difficulty[2]
    rectangle_width = difficulty[3][0]
    rectangle_height = difficulty[3][1]
    screen_width = rectangle_width * cols
    screen_height = (rectangle_height * rows) + 50
    screen = pygame.display.set_mode((screen_width, screen_height))

    grid = generate_grid()
    generate_bombs()
    update_cell_counts()

    lost = False
    won = False
    flags = bomb_count

def check_win():
    global won
    matches = [flag for flag in flag_positions if flag in bomb_positions]
    spaces_left = 0
    for y in range(rows):
        for x in range(cols):
            cell = grid[y][x]
            if not cell.open and not cell.flagged and not cell.bomb:
                spaces_left += 1

    if flags == 0 and len(matches) == bomb_count and spaces_left == 0 and not lost:
        won = True

def render(surface):
    surface.fill((198, 198, 198))

    for y in range(rows):
        for x in range(cols):
            grid[y][x].update()
            grid[y][x].render(surface)

    flag_str = str(flags)
    if len(flag_str) == 1:
        flag_str = "00" + flag_str
    if len(flag_str) == 2:
        flag_str = "0" + flag_str

    surface.blit(pygame.transform.scale(digit_background_tile_image, (100, 50)), (0, 0))

    cords = [(4, 4), (36, 4), (68, 4)]

    for i in range(len(flag_str)):
        char = flag_str[i]
        char_image = digit_images[int(char)]
        char_image = pygame.transform.scale(char_image, (28, 42))
        surface.blit(char_image, cords[i])

    surface.blit(face.image, (100, 0))

    surface.blit(text_image, (150, 2))

    pygame.draw.line(surface, (128, 128, 128), (0, 1), (599, 1), 3) #top line
    pygame.draw.line(surface, (128, 128, 128), (0, 49), (599, 49), 2) #bottom line
    pygame.draw.line(surface, (128, 128, 128), (0, 0), (0, 49), 2) #left line
    if difficulty == easy:
        pygame.draw.line(surface, (128, 128, 128), (248, 0), (248, 49), 2) #right line
    if difficulty == medium:
        pygame.draw.line(surface, (128, 128, 128), (448, 0), (448, 49), 2) #right line
    if difficulty == hard:
        pygame.draw.line(surface, (128, 128, 128), (598, 0), (598, 49), 2) #right line

    pygame.draw.line(surface, (128, 128, 128), (98, 2), (98, 48), 2) #covering up weird color differences
    pygame.draw.line(surface, (128, 128, 128), (3, 48), (99, 48))

    pygame.display.flip()

def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                update_difficulty(difficulty)
            elif event.key == pygame.K_1:
                update_difficulty(easy)
            elif event.key == pygame.K_2:
                update_difficulty(medium)
            elif event.key == pygame.K_3:
                update_difficulty(hard)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos, event.button, event.touch)
            if not won and not lost:
                clicked_cell = get_cell(event.pos)
                if clicked_cell is not None:
                    clicked_cell.clicked(event.button)
            if face.is_clicked(event.pos):
                face.mouse_down()
        elif event.type == pygame.MOUSEBUTTONUP:
            if face.down:
                face.mouse_up()
        elif event.type == pygame.QUIT:
            running = False

grid = generate_grid()
generate_bombs()
update_cell_counts()

face = Face()

running = True
lost = False
won = False

while running:
    clock.tick(120)
    render(screen)
    events()
    check_win()
    face.update()