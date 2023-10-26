# https://realpython.com/python-generate-qr-code/#creating-animated-qr-codes
import segno
from datetime import datetime

IMAGE_FILE_PATH = '/static/'


def main():
    url = 'https://eglenn.app'
    make_qr_code(url)


def make_qr_code(url, scale=8, border_color='#FFFFFF', code_color='#000000', background_color='#FFFFFF'):

    file_name = "static/qr-code_" + get_current_time() + ".png"

    img = segno.make_qr(url)
    img.save(
        file_name,
        scale=scale,
    )
    # img.save(
    #     file_name,
    #     scale=scale,
    #     light=background_color,
    #     dark=code_color
    # )
    return file_name

def get_current_time():
    now = datetime.now()
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    return month + day + hour + minute + second

if __name__ == '__main__':
    main()
