inputList = ['borderColor', 'codeColor', 'backgroundColor'];
previewList = ['borderPreview', 'codePreview', 'backgroundPreview']

function updateColorPreview() {    
    for (let i = 0; i < previewList.length; i++) {
        var colorInput = document.getElementById(inputList[i]).value;
        var colorPreview = document.getElementById(previewList[i]);
        //  Check that validity of the hex code
        var hexRegex = /^#([0-9a-f]{3}){1,2}$/i;
        if (hexRegex.test(colorInput)) {
            // Set the color of the box
            colorPreview.style.backgroundColor = colorInput;
        } else {
            // Reset preview if the input is not a valid hex code
            colorPreview.style.backgroundColor = 'transparent';
        }
    }
}

function enforceHashtag() {
    inputList.forEach((input) => {
        document.getElementById(input).addEventListener('input', function () {
            var input = this;
            var value = input.value;
        
            // Check if the '#' character is missing or at the beginning
            if (value.indexOf('#') !== 0) {
                input.value = '#' + value; // Add '#' character
            }
            // Update the color of the preview box
            updateColorPreview();
        });
    });
}