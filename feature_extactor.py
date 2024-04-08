import os
import cv2
import pandas as pd
from datetime import timedelta

file_path = 'video.mp4'
creation_time = os.path.getctime(file_path)

gyro_data = pd.read_csv('gyro.csv')
gyro_data['recording_time'] = pd.to_datetime(gyro_data['recording_time'])

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)

frame_number = 0
while True:
    # Read the next frame
    ret, frame = cap.read()

    # If the frame could not be retrieved, we've reached the end of the video
    if not ret:
        break

    # Calculate the timestamp of the current frame in seconds
    timestamp = frame_number / fps

    # Find the corresponding gyroscope data
    gyro_row = gyro_data.iloc[(gyro_data['recording_time'] - timedelta(seconds=timestamp)).abs().argsort()[:1]]

    # Process the frame and gyroscope data here...

    # Increment the frame number
    frame_number += 1

# Release the video capture object
cap.release()