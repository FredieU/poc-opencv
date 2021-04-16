import argparse
from colour_detector import scan_colour
from corner_detector import scan_corners
from template_matcher import match_template
from face_detector import scan_faces

scripts = {
    'colours': scan_colour,
    'corners': scan_corners,
    'faces': scan_faces,
    'templates': match_template,
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='POC OpenCV script runner.')
    parser.add_argument(
        '-s',
        '--script',
        help='Name of the script to run among (colours, corners, faces, templates)',
        required=True
    )
    args = parser.parse_args()

    script = scripts[args.script]

    script()
