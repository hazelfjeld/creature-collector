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
exit_button_text=font.render('exit', True, WHITE)
exit_button = pygame.Rect(0,0,100,50)
battle_button_text=font.render('Battle', True, WHITE)
battle_button = pygame.Rect(200,0,100,50)
# === Battle Vars ===
run_text =font.render('Run', True, WHITE)
run_button=pygame.Rect(400,500,100,50)
choose_attack_text =font.render('Choose attack', True, WHITE)
choose_attack_button = pygame.Rect(200,500,100,50)
items_text =font.render('Items', True, WHITE)
items_button=pygame.Rect(0,500,100,50)
running=True
while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
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
                if battle_button.collidepoint(events.pos):
                    UI = "Battle"
                    creature_summoned = False
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
        pygame.draw.rect(screen, BLACK, exit_button) # Exit button
        pygame.draw.rect(screen, BLACK, player) # Player
        screen.blit(exit_button_text, exit_button)
        pygame.draw.rect(screen, BLACK, battle_button)
        screen.blit(battle_button_text,battle_button)
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

# - Creature sprites
# - Battle backgrounds
# - Tileset for maps
# - UI icons/buttons
# - Sound effects and music
