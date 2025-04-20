import pygame
pygame.init()

WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)
# Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
# UI config
UI="Overworld" # We can edit this and make it something like "Start" for the start screen
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
            pass
    screen.fill((WHITE))
    
    if UI == "Start":
        screen.fill((WHITE))

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
