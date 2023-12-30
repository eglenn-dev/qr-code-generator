import segno
from datetime import datetime

IMAGE_FILE_PATH = '/static/'


def main():
    url = 'https://eglenn.app'
    make_qr_code(url)


def make_qr_code(url, scale, background, code_color, border_color):
    if scale == '' or scale == '0' or scale == 0:
        scale = 8
    if background == '' or background == '#':
        background = '#FFFFFF'
    if code_color == '' or code_color == '#':
        code_color = '#000000'
    if border_color == '' or border_color == '#':
        border_color = '#FFFFFF'

    file_name_path = "static/generated/qr-code_" + get_current_time() + ".png"

    img = segno.make_qr(url)
    img.save(
        file_name_path, # Name and path of the file
        scale=scale, # Scale factor for size of the image
        light=background, # General background color for the qr code
        dark=code_color, # Color of the data of the qr code
        quiet_zone=border_color # Color of the border. All space around the qr code.
    )

    return file_name_path

def get_current_time():
    now = datetime.now()
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    return month + month + day + hour + minute + second

if __name__ == '__main__':
    main()
