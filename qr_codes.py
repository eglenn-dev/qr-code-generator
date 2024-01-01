import segno
from datetime import datetime

IMAGE_OUTPUT_PATH = 'static/generated/'

def main():
    # Main function for testing.
    url = 'https://eglenn.app'
    make_qr_code(url)

def make_qr_code(url, scale='', background='', code_color='', border_color=''):
    # If the default values were used, then set them to a standard black and white colors for the QR code.
    if scale == '' or scale == '0' or scale == 0:
        scale = 8
    if background == '' or background == '#':
        background = '#FFFFFF'
    if code_color == '' or code_color == '#':
        code_color = '#000000'
    if border_color == '' or border_color == '#':
        # Use the background color if the border color is not specified
        border_color = background

    # Creating the file path with the name
    file_name_path = f'{IMAGE_OUTPUT_PATH}qr-code_{get_current_time()}.png'

    # Generate the qr code data to the img object
    img = segno.make_qr(url)
    # Save the QR code to the filepath with the user specified customizations
    img.save(
        file_name_path, # Name and path of the file
        scale=scale, # Scale factor for size of the image
        light=background, # General background color for the qr code
        dark=code_color, # Color of the data of the qr code
        quiet_zone=border_color # Color of the border. All space around the qr code.
    )
    
    # Return the image file path as a string
    return file_name_path

def get_current_time():
    now = datetime.now()
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    # Returning the current date and time
    return f'{month}{day}-{hour}{minute}{second}'

if __name__ == '__main__':
    main()
