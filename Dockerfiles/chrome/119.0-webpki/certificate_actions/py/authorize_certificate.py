import logging as log
import pyautogui as screen
import sys

log.basicConfig(stream=sys.stdout, level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AuthorizeCertificate:
    log.info("Clicking at the center of the screen.")
    
    center_x, center_y = (dimension / 2 for dimension in screen.size())
    screen.click(center_x, center_y)
    
    log.debug("Clicked at ({}, {}).".format(center_x, center_y))
    
    log.info("Pressing 'Tab' key twice.")
    
    screen.press('tab', presses=2, interval=0.5)

    log.debug("Pressed 'Tab' key twice successfully.")
    log.info("Pressing 'Enter' key.")
    
    screen.press('enter')
    
    log.debug("Pressed 'Enter' key successfully.")
    log.info("Action completed successfully.")


if __name__ == "__main__":
    AuthorizeCertificate()