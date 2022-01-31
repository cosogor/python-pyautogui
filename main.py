# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    pyautogui.click() # Click the mouse at its current location.
    pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
#    pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    pyautogui.doubleClick() # Double click the mouse at the
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    pyautogui.press('esc') # Simulate pressing the Escape key.
    pyautogui.keyDown('shift')
    pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
    pyautogui.keyUp('shift')
    pyautogui.hotkey('ctrl', 'c')


    pyautogui.alert('This is an alert box.')
    pyautogui.confirm('Shall I proceed?')
    pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
    pyautogui.prompt('What is your name?')
    pyautogui.password('Enter password (text will be hidden)')


    im1 = pyautogui.screenshot()
    im1.save('my_screenshot.png')
    im2 = pyautogui.screenshot('my_screenshot2.png')

    button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
    button7location
    buttonx, buttony = pyautogui.center(button7location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found

    buttonx, buttony = pyautogui.locateCenterOnScreen('button.png')  # returns (x, y) of matching region
    buttonx, buttony
    pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('pyautogui samples started')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
