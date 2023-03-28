# fatqat: simple ground control station + img proc apps 4 UAVs.
Tested on: Ubuntu 20.04 [✔️]

## Installation:
`git clone https://github.com/suleyman-kaya/fatqat && cd fatqat && bash project_requirements/requirements.bash`

## Usage:
Ground control station only:
`python3 fatqat.py --mode gcs --connect <CONNECTION_STRING>`

<br>

Image processing applications:
`python3 fatqat.py --mode imgproc --cam_src <CAMERA_SOURCE> --ir_cam_src <IR_CAMERA_SOURCE> --app <IMG_PROC_APP_PATH>`

## Screenshots:
![screenshot](Screenshots/scrot.png)
