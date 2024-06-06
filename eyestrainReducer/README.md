# Eye Strain Manager

The Eye Strain Manager is a simple desktop application built using Python and Tkinter. It helps users follow the 20-20-20 rule to prevent eye strain while working on screens for extended periods.

## Introduction

The 20-20-20 rule suggests that for every 20 minutes spent looking at a screen, you should take a break and look at something 20 feet away for at least 20 seconds. This practice helps reduce eye strain and discomfort caused by prolonged screen exposure.

## Features

- **Popup Reminder**: The app pops up a reminder window every 20 minutes, reminding the user to take a break.
- **Minimization**: After displaying the reminder, the app automatically minimizes itself after 20 seconds, allowing the user to continue their work uninterrupted.
- **Start Button**: The user can manually start the reminder process by clicking the "Start" button.
- **Installed exe**: For windows eye_manager.zip is provided where the exe is already installed please use the same

## Usage
### Windows:
1. Download the eye_manager.zip extract the contents and start using Manage_eye_strain.exe directly

### Mac and other os
1. We need to either use the eye_manager.py file directly `python eye_manager.py` after cloning the repo
2. We can also create exe using pyinstaller, run the following in cmd in the repo's dir
   `pip install -r requirments.txt`
   `pyinstaller -n "Manage_eye_strain" --icon=app_icon.ico --windowed eye_manager.py`
3. Copy the exe file from dist to the root folder
   
## Dependencies

- **Tkinter**: Python's standard GUI library for creating desktop applications.
- **Playsound**: A Python library to play sound files.
