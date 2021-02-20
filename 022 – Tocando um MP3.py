import pygame
import time

class Test:
    def test_sound(self):
        pygame.mixer.init()
        pygame.mixer.Sound.play(pygame.mixer.Sound('cartola.mp3'))
        time.sleep(10000)


    def mixer(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.musi()


if __name__ == '__main__':
    T = Test()
    T.test_sound()
