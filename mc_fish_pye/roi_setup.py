import json
from pynput import mouse
import os


def capture_roi():
    print("\n[ROI Setup] Click twice on the screen to define your region of interest (top-left, then bottom-right)")
    click_hist = []

    def on_click(x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            click_hist.append((x, y))
            print(f"Registered click #{len(click_hist)} at ({x}, {y})")
            if len(click_hist) >= 2:
                # Stop listener when two points are captured
                return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    if len(click_hist) != 2:
        raise Exception("You must click two distinct points to define the ROI.")

    x1, y1 = click_hist[0]
    x2, y2 = click_hist[1]

    roi = {
        'x1': min(x1, x2),
        'x2': max(x1, x2),
        'y1': min(y1, y2),
        'y2': max(y1, y2)
    }
    print(f"[ROI] Selected region: {roi}")
    return roi

def update_config_with_roi(config_path, roi):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, 'r') as f:
        config = json.load(f)

    config['detection']['roi'] = roi

    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    print(f"[Config] Updated ROI in {config_path}")
