# General Function Documentation & Description

## Python Flask Library Use
This project uses the Flask, a simple web-microframework. All the code that uses [Flask](https://flask.palletsprojects.com/en/3.0.x/) is located in the [app.py](../app.py) file. Here is breakdown of the functions.

### home()
- This simply renders and returns the [index.html](../templates/index.html) template when the root of the app is accessed. 

### qr()
- This function returns the rendered version of the [qr.html](../templates/qr.html) that contains the form with all the information that will be needed to create a qr code. 
- The form on this page uses a POST request to post the form data to the app. It is posted to the /qr-img URL.

### qr_img()
- This function calls the make_qr_code() function that is part of the [qr_codes](../qr_codes.py) imported file. With this all the form data is passed in the that function creates the QR Code and returns the filepath with the file name. 
- The [qr-img.html](../templates/qr-img.html) is rendered with the filepath to the img so that the image can be displayed to the user upon request. 

## Python Segno Library
This project uses the segno library to import key functions that allow for the enocding of the QR code that will later me returned to the user. It also offers support for customization of the QR code's color, among other features. 

### make_qr_code()
- This function takes in customization information about the QR code. Breakdown of the customization information. 

    - url: The URL: that the QR code will point to. 
    - scale: The scale factor on how large the image will be.
    - background: The background color of the QR code.
    - code_color: The color of the typically black encoded squares of data. 
    - border_color: The color of the border. This overrides the background color for the area directly around the code. 

### get_current_time()
- This gets the current date information and compiles it into a string that is then returned. This is important because it is how the next page will pull the information about what QR code to display. 