import time
import pyautogui
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Certificate:

    def install(self):
        logging.info('Start certificate installation.')

        self._install_webpki()
        self._click_in_webpki_extension()
        self._click_in_import_pfx()
        self._find_certificate()
        self._type_password_certificate()

    def _click_in_webpki_extension(self):

        logging.info('Click in WebPki extension.')

        screen_width, screen_height = pyautogui.size()
        self._move_and_click((screen_width - 185), 55)

    def _click_in_import_pfx(self):

        logging.info('Click in import PFX.')

        screen_width, screen_height = pyautogui.size()
        self._move_and_click((screen_width - 310), 400)

    def _move_and_click(self, x, y, duration=2):

        time.sleep(duration)
        pyautogui.moveTo(x, y, duration=0.25)
        time.sleep(0.50)
        pyautogui.click(x, y)
        time.sleep(duration)

    def _install_webpki(self):

        logging.info('Installing WebPki extension.')

        self._go_to_chrome_web_store_web_pki_extension()
        self._click_in_add_to_chrome()
        self._confirm_extension_installation()

    def _confirm_extension_installation(self):

        logging.info('Confirm extension installation.')

        pyautogui.press('tab', presses=2, interval=0.50)
        pyautogui.hotkey('enter')
        time.sleep(1)

    def _click_in_add_to_chrome(self):

        logging.info('Click in add to chrome.')

        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)
        pyautogui.write('Add to Chrome')
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(0.5)

    def _go_to_chrome_web_store_web_pki_extension(self):

        logging.info('Go to chrome webstore webPki extension.')

        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write('https://chromewebstore.google.com/detail/web-pki/dcngeagmmhegagicpcmpinaoklddcgon?pli=1')
        pyautogui.press('enter')
        time.sleep(2)

    def _find_certificate(self):

        logging.info('Find certificate.')

        time.sleep(1)
        pyautogui.press('/')
        pyautogui.write('home/selenium/Downloads/decoded_certificate.pfx')
        pyautogui.press('enter')

    def _type_password_certificate(self):

        logging.info("Typing password certificate.")

        self._click_in_enter_the_pfx_password()
        time.sleep(0.5)
        pyautogui.write(self._get_password_certificate())
        time.sleep(1)
        pyautogui.press('enter')

    def _click_in_enter_the_pfx_password(self):

        logging.info('Click in enter the PFX password.')

        screen_width, screen_height = pyautogui.size()
        self._move_and_click((screen_width - 625), 512)

    def _get_password_certificate(self):
        try:
            file_path = '/home/selenium/Downloads/certificate_password.txt'

            with open(file_path, 'r') as file:
                return file.read()

        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


certificate = Certificate()
certificate.install()
