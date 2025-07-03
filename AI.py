import pygame
import json
import random
from queue import Queue
import heapq

pygame.init()

file_path = 'sample.json'
with open(file_path, 'r') as f:
    river_data = json.load(f)

GRID_HEIGHT = len(river_data)
GRID_WIDTH = len(river_data[0]) if GRID_HEIGHT > 0 else 0

CELL_SIZE = 15
WINDOW_WIDTH = GRID_HEIGHT * CELL_SIZE  
WINDOW_HEIGHT = GRID_WIDTH * CELL_SIZE  

WATER_COLOR = (0, 255, 255)
OBSTACLE_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 0)
HIGHLIGHT_COLOR = (255, 165, 0)
BUTTON_COLOR = (200, 200, 255)
SELECTED_COLOR = (255, 165, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("River Path finding")

start = (0, 0)
end = (GRID_HEIGHT - 1, GRID_WIDTH - 1)

boat_image = pygame.image.load('Boat.jpg')
boat_image = pygame.transform.scale(boat_image, (CELL_SIZE, CELL_SIZE))

menu_width, menu_height = 750, 600
menu_screen = pygame.display.set_mode((menu_width, menu_height))  
pygame.display.set_caption("Select Algorithm")

font = pygame.font.SysFont('Comic Sans MS', 20)
font_large = pygame.font.SysFont('Comic Sans MS', 30)

algorithm = None
is_random_matrix = False

def draw_input_menu(selected_option=None):
    menu_screen.fill((128, 128, 128))  
    
    title_text = font_large.render("Select Algorithm", True, (0, 0, 0))
    menu_screen.blit(title_text, (menu_width // 2 - title_text.get_width() // 2, 50))  

    options = ["1. BFS", "2. A*", "3. DFS", "4. Generate Random Matrix"]
    for i, option in enumerate(options):
        option_text = font.render(option, True, (0, 0, 0))
        rect = pygame.Rect(menu_width // 2 - 150, 150 + i * 100, 300, 60)
        
        if selected_option == i:
            pygame.draw.rect(menu_screen, SELECTED_COLOR, rect, border_radius=15)  
        else:
            pygame.draw.rect(menu_screen, BUTTON_COLOR, rect, border_radius=15)  

        pygame.draw.rect(menu_screen, (50, 50, 255), rect, width=2, border_radius=15)  
        menu_screen.blit(option_text, (menu_width // 2 - option_text.get_width() // 2, 150 + i * 100 + 15))

    pygame.display.update()

def get_algorithm_choice():
    global algorithm, random_matrix
    input_valid = False
    option = None

    while not input_valid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if menu_width // 2 - 150 <= mouse_x <= menu_width // 2 + 150:
                    if 150 <= mouse_y <= 210:
                        algorithm = "bfs"
                        input_valid = True
                        option = 0
                    elif 250 <= mouse_y <= 310:
                        algorithm = "a_star"
                        input_valid = True
                        option = 1
                    elif 350 <= mouse_y <= 410:
                        algorithm = "dfs"
                        input_valid = True
                        option = 2
                    elif 450 <= mouse_y <= 510:
                        random_matrix = True
                        generate_random_matrix()
                        input_valid = True
                        option = None

        draw_input_menu(selected_option=get_selected_option())

def get_selected_option():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if menu_width // 2 - 150 <= mouse_x <= menu_width // 2 + 150:
        if 150 <= mouse_y <= 210:
            return 0
        elif 250 <= mouse_y <= 310:
            return 1
        elif 350 <= mouse_y <= 410:
            return 2
        elif 450 <= mouse_y <= 510:
            return 3
    return None

def generate_random_matrix():
    obstacle_count = 75
    global river_data
    river_data = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    all_positions = [(i, j) for i in range(GRID_HEIGHT) for j in range(GRID_WIDTH)]
    random.shuffle(all_positions)

    count = 0
    for i, j in all_positions:
        if count >= obstacle_count:
            break
        if (i, j) != (0, 0) and (i, j) != (GRID_HEIGHT - 1, GRID_WIDTH - 1):
            river_data[i][j] = 1
            count += 1

    choose_algorithm_for_random_matrix()

def choose_algorithm_for_random_matrix():
    global algorithm
    selected_option = None
    while selected_option is None:
        menu_screen.fill((128, 128, 128))  

        title_text = font_large.render("Select Algorithm for Random Matrix", True, (0, 0, 0))
        menu_screen.blit(title_text, (menu_width // 2 - title_text.get_width() // 2, 50))  

        options = ["1. BFS", "2. A*", "3. DFS"]
        for i, option in enumerate(options):
            rect = pygame.Rect(menu_width // 2 - 150, 150 + i * 100, 300, 60)
            pygame.draw.rect(menu_screen, SELECTED_COLOR if get_selected_option() == i else BUTTON_COLOR, rect, border_radius=15)
            pygame.draw.rect(menu_screen, (50, 50, 255), rect, width = 2, border_radius=15)
            option_text = font.render(option, True, (0, 0, 0))
            menu_screen.blit(option_text, (menu_width // 2 - option_text.get_width() // 2, 150 + i * 100 + 15))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if menu_width // 2 - 150 <= mouse_x <= menu_width // 2 + 150:
                    if 150 <= mouse_y <= 210:
                        algorithm = "bfs"
                        selected_option = 0
                    elif 250 <= mouse_y <= 310:
                        algorithm = "a_star"
                        selected_option = 1
                    elif 350 <= mouse_y <= 410:
                        algorithm = "dfs"
                        selected_option = 2

def draw_grid(data):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            cell_value = data[row][col]
            color = WATER_COLOR if cell_value == 0 else OBSTACLE_COLOR
            pygame.draw.rect(screen, color, (row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_path(path):
    for node in path:
        pygame.draw.rect(screen, PATH_COLOR, (node[0] * CELL_SIZE, node[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for node in path:
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, (node[0] * CELL_SIZE, node[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(boat_image, (node[0] * CELL_SIZE, node[1] * CELL_SIZE))
        pygame.display.flip()
        pygame.time.delay(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def display_energy_used(energy):
    text_color = (0, 0, 0)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    
    text_surface = font.render(f"Energy Used: {energy}", True, text_color)
    text_rect = text_surface.get_rect()
    
    text_rect.center = (100, 150)
    screen.blit(text_surface, text_rect)

def display_state(number_of_state):
    text_color = (0, 0, 0)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    
    text_surface = font.render(f"Number of checked node: {number_of_state}", True, text_color)
    text_rect = text_surface.get_rect()
    
    text_rect.center = (165, 180)
    screen.blit(text_surface, text_rect)

def bfs(grid, start, end):
    queue = Queue()
    queue.put([start])
    visited = set()
    visited.add(start)
    counter = 1

    while not queue.empty():
        path = queue.get()
        node = path[-1]

        if node == end:
            return (path, counter)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (node[0] + dx, node[1] + dy)
            if (
                0 <= neighbor[0] < GRID_HEIGHT
                and 0 <= neighbor[1] < GRID_WIDTH
                and neighbor not in visited
                and grid[neighbor[0]][neighbor[1]] == 0
            ):
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.put(new_path)
                counter += 1

    return []

def a_star(grid, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, end), 0, start, []))
    counter = 1
    closed_set = set()
    while open_list:
        _, g, current, path = heapq.heappop(open_list)

        if current == end:
            return (path + [current], counter)

        if current in closed_set:
            continue

        closed_set.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (
                0 <= neighbor[0] < GRID_HEIGHT
                and 0 <= neighbor[1] < GRID_WIDTH
                and grid[neighbor[0]][neighbor[1]] == 0
            ):
                heapq.heappush(open_list, (g + 1 + heuristic(neighbor, end), g + 1, neighbor, path + [current]))
                counter += 1

    return []

def dfs(grid, start, end):
    stack = [(start, [start])]
    visited = set()
    counter = 1

    while stack:
        node, path = stack.pop()

        if node == end:
            return (path, counter)

        if node in visited:
            continue

        visited.add(node)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (node[0] + dx, node[1] + dy)
            if (
                0 <= neighbor[0] < GRID_HEIGHT
                and 0 <= neighbor[1] < GRID_WIDTH
                and neighbor not in visited
                and grid[neighbor[0]][neighbor[1]] == 0
            ):
                stack.append((neighbor, path + [neighbor]))
                counter += 1
    return []


get_algorithm_choice()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    draw_grid(river_data)

    if algorithm == "bfs":
        optimal_path, counter = bfs(river_data, start, end)
    elif algorithm == "a_star":
        optimal_path, counter = a_star(river_data, start, end)
    elif algorithm == "dfs":
        optimal_path, counter = dfs(river_data, start, end)

    energy_used = len(optimal_path) - 1

    display_energy_used(energy_used)

    display_state(counter)

    draw_path(optimal_path)
    
    pygame.display.flip()

    break

pygame.quit()
