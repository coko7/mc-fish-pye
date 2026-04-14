from pynput.mouse import Listener
from pynput import mouse

click_hist = [];

def compute_roi_from_clicks():
    if len(click_hist) != 2:
        raise Exception("Invalid click history: cannot compute ROI")

    return {
        'x1': click_hist[0][0],
        'x2': click_hist[1][0],
        'y1': click_hist[0][1],
        'y2': click_hist[1][1],
    }

def on_move(x, y):
    print(x, y)


def on_click(x, y, button, pressed):
    print(x, y, button, pressed)
    if button == mouse.Button.left:
        click_hist.append((x, y))


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


def setup():
    while len(click_hist) < 2:
        print("Awaiting click") 

    roi = compute_roi_from_clicks()
    print("configured ROI:", roi)


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
