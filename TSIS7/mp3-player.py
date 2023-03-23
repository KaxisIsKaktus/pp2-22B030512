import pygame
pygame.init()

W = 728
H = 410
FPS = 20

clock = pygame.time.Clock()
LightGREEN = (153, 255, 153)

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("I will never lose the love for the arriving, but I'm born to leave")
sc.fill(LightGREEN)
vagabond = pygame.image.load("C:\pp2\pp2-22B030512\TSIS7\mp3photo\manga-anime-musashi-miyamoto-musashi-hd-wallpaper-preview.jpg")
sc.blit(vagabond, (0, 0))
pygame.display.update()

sweethomePath = "C:\pp2\pp2-22B030512\TSIS7\music\Abigail-Barro-Sweet-home.ogg"
deependPath = "C:\pp2\pp2-22B030512\TSIS7\music\Deep-end.ogg"
boiybulganPath = "C:\pp2\pp2-22B030512\TSIS7\music\dudeontheguitar-MONRO-boiy-bulgan.ogg"
platinaPath = "C:\pp2\pp2-22B030512\TSIS7\music\Jakomo-Platina.ogg"
lovePath = "C:\pp2\pp2-22B030512\TSIS7\music\LOVE.ogg"
musicalfictionPath = "C:\pp2\pp2-22B030512\TSIS7\music\Musical_Fiction-Rudy_Mancuso.ogg"
sonnyboyPath = "C:\pp2\pp2-22B030512\TSIS7\music\Sonny_Boy.ogg"

sweethome = pygame.mixer.music.load(sweethomePath)
musicList = [sweethomePath, deependPath, boiybulganPath, platinaPath, lovePath, musicalfictionPath, sonnyboyPath]
pygame.mixer.music.play(-1)

flPlay = False
index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(musicList):
                    index = 0
                pygame.mixer.music.load(musicList[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pygame.mixer.music.load(musicList[index])
                pygame.mixer.music.play()

    clock.tick(FPS)


'''
#https://python-forum.io/thread-25114.html image as a button
pause = pygame.image.load("C:\pp2\pp2-22B030512\TSIS7\mp3photo\icons8-play-pause-96.png")
sc.blit(pause, (150, 100))

next = pygame.image.load("C:\pp2\pp2-22B030512\TSIS7\mp3photo\icons8-forward-90.png")
back = pygame.transform.rotate(next, 180)
sc.blit(next, (250, 100))
sc.blit(back, (50, 100))
'''