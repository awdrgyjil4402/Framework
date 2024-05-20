import pygame, sys
from PIL import Image


pygame.init()

# -- Physics --

    # todo: add collisions, gravity here
def collide_wall(self, entity, wall_group):  # Intended to stop players clipping through walls
    if pygame.sprite.spritecollide(entity, wall_group, False):
        pass

def collide_entity(self, entity1, entity2):  # Intended for player-enemy collisions, can do player-player and enemy-enemy collisions
        if pygame.sprite.collide_rect(entity1, entity2):  # For now, this is essentially a rename of collide_rect, and pretty useless
            return True

    # todo: add mask collision
    # todo: gravity, jump(for hypothetical platformer game)

# -- Assets --

# todo: particle effects
def extract_frames(sheet_path, frame_width, frame_height):
    # Load the sheet image
    sheet = pygame.image.load(sheet_path).convert_alpha()

    frames = []
    sheet_width, sheet_height = sheet.get_size()

    # Calculate the number of frames horizontally and vertically in the sheet
    num_frames_x = sheet_width // frame_width
    num_frames_y = sheet_height // frame_height

    # Extract each frame from the sheet and append it to the frames list
    for y in range(num_frames_y):
        for x in range(num_frames_x):
            frame_rect = pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height)
            frame = sheet.subsurface(frame_rect)
            frames.append(frame)

    return frames
    
class Particle(pygame.sprite.Sprite):
    pass

# todo: image, sound and data management

# -- Maps --

    # todo: map management

# -- Other --

    # todo: other useful functions

def start(width=800, height=800):
    pygame.init()
    screen_width = width
    screen_height = height
    global screen, clock
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

def engine_draw():
    pass


# todo: error handling, gui, game states