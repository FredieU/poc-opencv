# POC OpenCV Scripts
A collection of scripts to manipulate images or a video feed for Machine Learning.

## Setup
```sh
pip install -r requirements.txt
```

## Usage
Run a specific script with

```
python main.py -s SCRIPT_NAME
```
where `SCRIPT_NAME` is one of the following:

- `colours` - Scans a webcam feed for pixels of the provided colour
- `corners` - Scans a webcam feed for corners
- `faces` - Scans a webcam feed for faces and eyes
- `templates` - Scans a provided image for instances of a provided template image
