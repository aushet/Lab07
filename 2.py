import pygame
import os

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player Task 2")

# Инициализация микшера
pygame.mixer.init()

# Путь к папке с музыкой
music_folder = "/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/7lab/"


# Список песен
songs = [
    r"C:\Users\асер\Downloads\Kendrick_Lamar_-_tv_off_78618013.mp3",
    r"C:\Users\асер\Downloads\SpotiDownloader.com - Ransom - Lil Tecca.mp3",
    r"C:\Users\асер\Downloads\SpotiDownloader.com - Дом 50 - V $ X V PRiNCE.mp3"
]

# Проверяем существование файлов перед загрузкой
songs = [os.path.join(music_folder, song) for song in songs if os.path.exists(os.path.join(music_folder, song))]

if not songs:
    print("Ошибка: нет доступных песен в указанной папке!")
    pygame.quit()
    exit()

current_song = 0  # Индекс первой песни

# Загрузка изображения (фон)
background_path = os.path.join(music_folder, r"C:\Users\асер\Downloads\174452-gamilton_park-centralnyj_park-park-neboskreb-vershina_skaly-3840x2160.jpg")

if os.path.exists(background_path):
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Подгоняем размер
else:
    print("Ошибка: Файл фона не найден! Используется черный экран.")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 0, 0))  # Черный фон

# Функции управления музыкой
def play_music():
    """Проигрывает текущую песню."""
    print("Playing:", songs[current_song])
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

def stop_music():
    """Останавливает музыку."""
    print("Music stopped")
    pygame.mixer.music.stop()

def next_song():
    """Переключает на следующую песню."""
    global current_song
    stop_music()
    current_song = (current_song + 1) % len(songs)
    print("Next song:", songs[current_song])
    play_music()

def prev_song():
    """Переключает на предыдущую песню."""
    global current_song
    stop_music()
    current_song = (current_song - 1) % len(songs)
    print("Previous song:", songs[current_song])
    play_music()

# Загружаем и запускаем первую песню
play_music()

running = True
while running:
    screen.blit(background, (0, 0))  # Устанавливаем фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Нажатие клавиши
            print(f"Key pressed: {event.key}")
            if event.key == pygame.K_w:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_d:
                next_song()
            elif event.key == pygame.K_a:
                prev_song()
        elif event.type == pygame.KEYUP:
            print(f"Key released: {event.key}")

    pygame.display.flip()

pygame.quit()