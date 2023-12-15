import time
import pyautogui
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Certificate:

    def install(self):
        logging.info('Start certificate installation.')

        self._openChromeSettings()
        self._openManageCertificates()
        self._openImportCertificate()
        self._findCertificate()
        self._typePasswordCertificate()

    def _openChromeSettings(self):
        logging.info('Open chrome settings.')

        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write('chrome://settings/security?search=cert\n')
        pyautogui.press('enter')

    def _openManageCertificates(self):
        logging.info('Open manage certificates.')

        time.sleep(1)
        pyautogui.press('tab', presses=7, interval=0.75)
        pyautogui.press('enter')

    def _openImportCertificate(self):
        logging.info('Open import certificate.')

        time.sleep(1)
        pyautogui.press('tab', presses=2, interval=0.75)
        pyautogui.press('enter')

    def _findCertificate(self):
        logging.info('Find certificate.')

        time.sleep(1)
        pyautogui.press('/')
        pyautogui.write('home/selenium/Downloads/decoded_certificate.pfx')
        pyautogui.press('enter')

    def _typePasswordCertificate(self):
        logging.info('Typing password certificate.')

        time.sleep(1)
        pyautogui.write(self._getPasswordCertificate())
        pyautogui.press('enter')

    def _getPasswordCertificate(self):
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
