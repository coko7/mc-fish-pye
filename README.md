# 🎣 mc-fish-pye

AFK auto-fishing script for Minecraft using Python and OpenCV.

So that you can bake many [fish p*y*es](https://en.wikipedia.org/wiki/Fish_pie) with all the fish you get :)

## ⚙️ Setup

### 1. Install [Poetry](https://python-poetry.org/docs/#installation) (recommended)

On Arch Linux:

```bash
sudo pacman -S poetry
# Or follow Poetry's installation instructions for other platforms
```

### 2. Set up the development environment and dependencies

From the project root:

```bash
poetry install
```

This will set up a virtual environment and install all required dependencies.

### 3. (Optional) Activate the virtual environment

```bash
poetry env activate
```

Or you can prefix commands with `poetry run ...` to use the venv without activating.

### 4. Configure the Minecraft ROI (Region of Interest)

Run the ROI setup script from the root directory:

```bash
poetry run python scripts/setup_roi.py
```

- Follow the instructions: click twice on your screen (top-left, bottom-right of the subtitle region).
- The region will be automatically written to `config.json`.

Your `config.json` will look like:

```json
{
  "startTimer": 5,
  "detection": {
    "roi": {
      "x1": 1000,
      "x2": 2000,
      "y1": 1000,
      "y2": 2000
    },
    "threshold": 10,
    "cooldown": 2.5
  },
  "actions": {
    "clickPos": {
      "x": 0,
      "y": 0
    },
    "clickDelay": 0.5
  }
}
```

### 5. Download/import the [resource pack](./resource-pack/) into Minecraft and set the language

- Download the [resource pack](./resource-pack/) and import it (Feel free to zip it if you want)
- In game, select the resource pack and then change your in-game language to "Bionic Fisher Lang"
- Make sure you have the [subtitles](https://minecraft.wiki/w/Subtitles) enabled in **Accessibility Settings**
- In **Accessibility Settings**, disable the transparency of the subtitle background (it should be full black)
- Make sure you do not have **Friendly Creatures** sounds muted in your **Sound Settings**

## 📖 Usage

- Launch Minecraft and make sure you have set your language properly
- Join a world and stand in front of your fishing spot
- Run the `main.py` script with root/admin privileges (required for some keyboard events):

  ```bash
  poetry run python -m mc_fish_pye.main
  # or, if you activated the poetry shell:
  # python -m mc_fish_pye.main
  ```

- Quickly switch window focus to Minecraft and let it do the work
- Enjoy an infinite supply of fish and treasure!
- You can stop the script at any moment by holding the `p` key (or as documented in config/usage)

## ❓ How it works

This script relies on Minecraft subtitles and a custom language to detect when the fishing bobber sinks.

The custom language sets all subtitles to be empty, apart from `subtitles.entity.fishing_bobber.splash`, which is set to "AAAAAAA".

The long string will cause the black background behind the subtitle text to stretch farther than other subtitles.

These additional black pixels are what the script is looking for to detect if your fishing bobber has caught onto something.

Once a catch is detected, the script sends one right click to retrieve the catch, followed immediately by another one to cast the rod again.

After the rod has been cast again, the pixel detection will be deactivated for a few seconds to allow the subtitle to have time to fade away.
