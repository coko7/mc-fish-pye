#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mc_fish_pye.roi_setup import capture_roi, update_config_with_roi

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.json')

if __name__ == "__main__":
    try:
        roi = capture_roi()
        update_config_with_roi(CONFIG_PATH, roi)
        print("ROI setup complete. Please review config.json if needed.")
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
