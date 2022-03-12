/**
 * Displays the increment value to be applied by the slider in the slider's
 * submit button text.
 */
function changeSliderValue()
{
    let sliderElement = document.querySelector('#custom_increment_slider');
    let sliderValueStr = sliderElement.value;
    let submitButtonElement = document.querySelector('#custom_increment_submit');
    submitButtonElement.value = "Increment " + sliderValueStr;
}

/**
 * Called when the page loads, it sets a timer for .3s and calls a function
 * that changes the color of the text displaying the numbers back to black. It
 * appears red every time the page loads for 0.3s because... I don't because
 * it's cool.
 */
function setTimer()
{
    setTimeout(changeNumberColor, 300);
}

/**
 * Changes the number text color back to black.
 */
function changeNumberColor()
{
    let numberElem = document.querySelector('#number_display');
    let realNumberElem = document.querySelector('#real_number_display');
    numberElem.style.color = 'black';
    realNumberElem.style.color = 'black';
}