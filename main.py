import pygame
pygame.init()
import random
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)
# Colors
WHITE=(255,255,255)
BLACK=(0,0,0)

# === Creatures ===
summoned_creature = None
creature_summoned = False
class Creature:
    def __init__(self,attack,defense,health,rarity,color):
        self.attack=attack
        self.defense=defense
        self.health=health
        self.rarity=rarity
        self.color=color

common = Creature(attack=5, defense=5, health=5, rarity=60, color=(211, 211, 211))
uncommon = Creature(attack=8, defense=8, health=8, rarity=20, color=(70, 130, 180))
rare = Creature(attack=10, defense=10, health=10, rarity=14, color=(60, 179, 113))
epic = Creature(attack=12, defense=12, health=12, rarity=5, color=(147, 112, 219))
legendary = Creature(attack=15, defense=15, health=15, rarity=1, color=(255, 215, 0))

# Define position and radius for the summoned creature
circle_pos = (275, 275)
circle_radius = 25

# Health System - UI Bar - Bigger in Battle & Smaller in Over World
class Health:
    def __init__(self):

        # HP Vars
        self.CURRENT_HP = 100
        self.MAX_HP = 100

        # HP Design
        self.HP_bg = (90, 90, 90)  # Color for Background
        self.HP_fg = (255, 0, 0)  # Color for Foreground
        self.HP_border_size = 5  # Size for Border
        self.HP_border_color = (0, 0, 0)  # Color for Border

        # Initialising HP Bar

        # For Over World - (ow)
        self.HP_bar_ow = pygame.rect.Rect(20, HEIGHT - 60, 270, 40)
        self.HP_bar_ow_current = pygame.rect.Rect(20 + self.HP_border_size, HEIGHT - 60, (270 - self.HP_border_size / self.MAX_HP * self.CURRENT_HP), 40)  # HP Currently is 100%

        # For Battle
        self.HP_bar_battle = pygame.rect.Rect(20, 20, 270, 30)
        self.HP_bar_battle_current = pygame.rect.Rect(20 + self.HP_border_size, 20, (270 - self.HP_border_size / self.MAX_HP * self.CURRENT_HP), 30)  # HP Currently is 100%

        # TESTING DEVELOPER ONLY
        self.button_health_add = pygame.rect.Rect(WIDTH - 100, 100, 50, 50)
        self.button_health_minus = pygame.rect.Rect(WIDTH - 100, 200, 50, 50)
        self.button_health_setter = pygame.rect.Rect(WIDTH - 100, 300, 50, 50)

    # Health Adding / Setting
    def update_health(self, health_amount=0, health_set=None):
        if health_set is not None:
            self.CURRENT_HP = health_set
        else:
            if 0 <= self.CURRENT_HP + health_amount <= 100:
                self.CURRENT_HP += health_amount

    # Updating UI Visual Health
    def draw(self):

        # Over World Mode
        if UI == "Overworld":
            pygame.draw.rect(screen, self.HP_bg, self.HP_bar_ow)  # Draws Background Bar
            self.HP_bar_ow_current = pygame.rect.Rect(20 + self.HP_border_size, HEIGHT - 60, ((270 - (self.HP_border_size * 2)) / self.MAX_HP * self.CURRENT_HP), 40)  # HP Currently
            pygame.draw.rect(screen, self.HP_fg, self.HP_bar_ow_current)  # Draws Current Bar
            pygame.draw.rect(screen, self.HP_border_color, self.HP_bar_ow, self.HP_border_size)  # Draws Border Bar

        # Battle Mode
        elif UI == "Battle":
            pygame.draw.rect(screen, self.HP_bg, self.HP_bar_battle)  # Draws Background Bar
            self.HP_bar_battle_current = pygame.rect.Rect(20 + self.HP_border_size, 20, ((270 - (self.HP_border_size * 2)) / self.MAX_HP * self.CURRENT_HP), 30)  # HP Currently
            pygame.draw.rect(screen, self.HP_fg, self.HP_bar_battle_current)  # Draws Current Bar
            pygame.draw.rect(screen, self.HP_border_color, self.HP_bar_battle, self.HP_border_size)  # Draws Border Bar

        # TESTING DEVELOPER ONLY
        pygame.draw.rect(screen, (0, 128, 0), self.button_health_add)
        pygame.draw.rect(screen, (128, 0, 0), self.button_health_minus)
        pygame.draw.rect(screen, (0, 0, 128), self.button_health_setter)


health_ui = Health()

def summon_creature():
    roll = random.randint(1, 100)

    if roll <= legendary.rarity:
        return legendary
    elif roll <= legendary.rarity + epic.rarity:
        return epic
    elif roll <= legendary.rarity + epic.rarity + rare.rarity:
        return rare
    elif roll <= legendary.rarity + epic.rarity + rare.rarity + uncommon.rarity:
        return uncommon
    else:
        return common


# UI config
UI="Start" # We can edit this and make it something like "Start" for the start screen
# === Player Vars ===
player= pygame.Rect(275,275,25,25)
speed=3

# === Start Screen Vars ===
load_button_text =font.render('Load game', True, WHITE)
load_button = pygame.Rect(200,500,100,50)
new_game_text =font.render('New game', True, WHITE)
new_game_button=pygame.Rect(0,500,100,50)
# === Oveworld Vars ===

#=== added these ===
MAP_WIDTH = 6000
MAP_HEIGHT = 6000
stepped_on_grass=False
grass_color=(0,128,0)
grass_test = pygame.Rect(0,500,30,30)
health_cross_color=(128,0,0)
health_cross_test=pygame.Rect(100,500,30,30)
collision_map = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))


exit_button_text=font.render('exit', True, WHITE)
exit_button = pygame.Rect(0,0,100,50)
# === Battle Vars ===
run_text =font.render('Run', True, WHITE)
run_button=pygame.Rect(400,500,100,50)
choose_attack_text =font.render('Choose attack', True, WHITE)
choose_attack_button = pygame.Rect(200,500,100,50)
items_text =font.render('Items', True, WHITE)
items_button=pygame.Rect(0,500,100,50)


# === Overworld Functions === (added this too)
def color_detection(rect):
    global UI, creature_summoned, stepped_on_grass
    corners = [
        (rect.left, rect.top),
        (rect.right - 1, rect.top),
        (rect.left, rect.bottom - 1),
        (rect.right - 1, rect.bottom - 1)
    ]
    on_grass = False
    for corner in corners:
        x, y = corner
        if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
            color = collision_map.get_at((x, y))
            if color[:3] == grass_color:
                on_grass = True
            if color[:3] == health_cross_color:
                pass
    if on_grass and not stepped_on_grass:
        UI = "Battle"
        stepped_on_grass = True
    if not on_grass:
        stepped_on_grass = False


running=True
while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
                # TESTING DEVELOPER ONLY
        if events.type == pygame.MOUSEBUTTONDOWN:
            if health_ui.button_health_add.collidepoint(events.pos):
                health_ui.update_health(health_amount=20)
            if health_ui.button_health_minus.collidepoint(events.pos):
                health_ui.update_health(health_amount=-20)
            if health_ui.button_health_setter.collidepoint(events.pos):
                health_ui.update_health(health_set=100)
        # === Button Functions ===
        if UI == "Start":
            if events.type == pygame.MOUSEBUTTONDOWN:
                if load_button.collidepoint(events.pos):
                    UI = "Overworld"
                if new_game_button.collidepoint(events.pos):
                    UI = "Overworld"
        
                    
            
            pass
        if UI == "Overworld":
            if events.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(events.pos):
                    UI = "Start"
            pass
        if UI == "Battle":
            if events.type == pygame.MOUSEBUTTONDOWN:
                if run_button.collidepoint(events.pos):
                    UI = "Overworld"
    screen.fill((WHITE))
    
    if UI == "Start":
        screen.fill((WHITE))
        # === Draw Everything ===
        pygame.draw.rect(screen, BLACK, load_button) # Exit button
        screen.blit(load_button_text, load_button)
        pygame.draw.rect(screen, BLACK, new_game_button) # Exit button
        screen.blit(new_game_text, new_game_button)
        
        pass
    if UI == "Overworld":
        screen.fill((WHITE))
        color_detection(player)
        # === Movement ===
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: 
            player.x -= speed
        if keys[pygame.K_RIGHT]: 
            player.x += speed
        if keys[pygame.K_UP]: 
            player.y -= speed
        if keys[pygame.K_DOWN]: 
            player.y += speed
        # === Draw Everything ===

        #=== also added this ===
        pygame.draw.rect(screen,grass_color,grass_test)
        pygame.draw.rect(collision_map, grass_color, grass_test)
        pygame.draw.rect(screen,health_cross_color,health_cross_test)
        pygame.draw.rect(collision_map,health_cross_color,health_cross_test)


        pygame.draw.rect(screen, BLACK, exit_button) # Exit button
        pygame.draw.rect(screen, BLACK, player) # Player
        screen.blit(exit_button_text, exit_button)
    if UI == "Battle":
        screen.fill(WHITE)

        if not creature_summoned:
            summoned_creature = summon_creature()
            creature_summoned = True

        # === Draw Creature ===
        if summoned_creature:
            pygame.draw.circle(screen, summoned_creature.color, circle_pos, circle_radius)

        # === Draw Buttons ===
        pygame.draw.rect(screen, BLACK, run_button)
        screen.blit(run_text, run_button)
        pygame.draw.rect(screen, BLACK, choose_attack_button)
        screen.blit(choose_attack_text, choose_attack_button)
        pygame.draw.rect(screen, BLACK, items_button)
        screen.blit(items_text, items_button)
    health_ui.draw() # Draws Health Bar UI
    
    pygame.display.flip()
    clock.tick(60)



# === Core Systems ===
# - Main menu (Start, Load, Quit)
# - Creature database / list of available creatures
# - Player inventory / collection screen
# - Creature stats and levels
# - Creature abilities/moves
# - Turn-based battle system
# - Random wild encounters
# - Map with explorable areas
# - Movement system

# === Battle System ===
# - Battle wild creatures
# - Creature turns with move selection
# - Abilities with types, damage, cooldowns
# - Status effects (burn, stun, etc.)
# - Win/lose conditions and rewards

# === Creature Design ===
# - Name, type, rarity
# - HP, attack, defense, speed
# - Moveset (1-4 abilities)
# - Evolution system
# - Visuals (static sprite or idle animation)

# === Map System ===
# - Grid-based overworld map
# - Wild encounter zones
# - Trainer NPCs to battle
# - Towns for healing, shops, quests

# === UI Components ===
# - Health bars
# - Battle menu (fight, switch, run, etc.)
# - Collection screen with filters
# - Gacha summon screen
# - Main HUD during map exploration

# === Save/Load ===
# - Save player progress (creatures, items, gacha pulls)
# - Load from save file

# === Assets Needed ===
# - Creature sprites
# - Battle backgrounds
# - Tileset for maps
# - UI icons/buttons
# - Sound effects and music
