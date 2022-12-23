import pyautogui
import cv2
import time
import numpy as np

# Set the duration of the recording (in seconds)
duration = 10

# Get the size of the screen
screen_width, screen_height = pyautogui.size()

# Set the codec and create the VideoWriter object
video = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('screen_recording.mp4', video, 20.0, (screen_width, screen_height))

# Start the recording
start_time = time.time()
while time.time() - start_time < duration:
    # Capture the screen
    img = np.array(pyautogui.screenshot())

    # Write the frame to the output video file
    out.write(img)

# Release the VideoWriter object
out.release()