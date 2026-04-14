import cv2
import numpy as np
import pyautogui
import time
import keyboard
import json


def check_catch(config):
    cfg_detect = config['detection']
    cfg_actions = config['actions']
    cfg_roi = cfg_detect['roi']

    x_start = cfg_roi['x1']
    x_end = cfg_roi['x2']
    y_start = cfg_roi['y1']
    y_end = cfg_roi['y2']

    # Take screenshot and crop the region of interest
    screenshot = np.array(pyautogui.screenshot())
    roi = screenshot[y_start:y_end, x_start:x_end]

    # Convert to grayscale image
    grayscale_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Define threshold for detecting black pixels
    threshold = cfg_detect['threshold']  # Adjust this value as needed

    # Set click position to 0,0 otherwise we get weird camera movements in game
    click_x = cfg_actions['clickPos']['x']
    click_y = cfg_actions['clickPos']['y']
    click_pos = (click_x, click_y)

    # Check if ROI is composed of black pixels
    if np.mean(grayscale_roi) < threshold:
        pyautogui.rightClick(click_pos) # Reel in the fish (or treasure!)
        time.sleep(cfg_actions['clickDelay'])
        pyautogui.rightClick(click_pos) # Cast rod again

        return 1

    return 0
    # cv2.imwrite("test.png", grayscale_roi)

def start_init_timer(start_from):
    for count in range(start_from, 0, -1):
        print("{}...".format(count))
        time.sleep(1)

    print("GO! GO! GO! GOOOOOO!!!")


# Load config from json file
config = []
with open('config.json') as file:
    config = json.load(file)


# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Screen is 2560x1440
# big_screen_roi = {'x1': 2375, 'x2': 2385, 'y1': 1285, 'y2': 1342}

# Screen is 2560x1440 (KDE on frack)
# big_screen_roi_frack = {'x1': 2375, 'x2': 2385, 'y1': 1295, 'y2': 1345}

# Screen is 1920x1080
# laptop_screen_roi = {'x1': 1725, 'x2': 1745, 'y1': 930, 'y2': 985}

# roi_width = int(screen_width * 0.1)  # 20% of the screen width
# roi_height = int(screen_height * 0.1)  # 20% of the screen height
#
# roi_x = screen_width - roi_width
# roi_y = screen_height - roi_height

roi = config['detection']['roi']

start_init_timer(config['startTimer'])

catches = 0
while True:
    is_catch = check_catch(config)
    if is_catch:
        catches = catches + 1
        print("Catch:", catches)
        # Sleep time must be greater than MC subtitle fade time
        time.sleep(config['detection']['cooldown'])

    # Stop script when 'ctrl+space' is pressed
    if keyboard.is_pressed('ctrl+space'):
        print("IT'S G-OVER")
        print("You caught:", catches)
        break
