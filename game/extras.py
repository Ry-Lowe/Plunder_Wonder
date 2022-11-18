pygame.init()

screen.fill((255, 255, 255))
gold = pygame.image.load('treasurechest.png')
gold_rect = gold.get_rect()
water = pygame.image.load('tile_73.png')
water_rect = water.get_rect()
ship = pygame.image.load('ship (1).png')
ship = pygame.transform.rotate(ship, 180)
ship_rect = ship.get_rect()
screen_rect = screen.get_rect()
ship_rect.midbottom = screen_rect.midbottom
gold_rect.center = screen_rect.center

for y in range(10):
    for x in range(14):
        screen.blit(water, water_rect)
        water_rect.x += water_rect.width
    water_rect.x = 0
    water_rect.y += water_rect.height

screen.blit(ship, ship_rect)
screen.blit(gold, gold_rect)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_rect.x += 40

            elif event.key == pygame.K_LEFT:
                ship_rect.x -= 40

    for y in range(10):
        for x in range(14):
            screen.blit(water, water_rect)
            water_rect.x += water_rect.width
        water_rect.x = 0
        water_rect.y += water_rect.height
    water_rect.topleft = screen_rect.topleft
    screen.blit(gold, gold_rect)
    screen.blit(ship, ship_rect)

    pygame.display.flip()

#time.sleep(5)