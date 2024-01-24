FROM selenoid/vnc_chrome:119.0

USER root

RUN apt update -y

RUN apt-get update && apt-get install --reinstall sudo

RUN apt install -y pip xauth python3-tk python3-dev python3-xlib && \
mkdir /home/selenium/install_certificate

RUN pip install pyautogui

RUN echo "selenium=(ALL:ALL) NOPASSWD:ALL > /etc/sudoers.d/selenium"

WORKDIR /home/selenium

# Create Xauthority
RUN touch /home/selenium/.Xauthority && chmod 777 /home/selenium/.Xauthority

COPY entrypoint.sh /
COPY ./ /home/selenium/install_certificate

RUN chmod +x /entrypoint.sh && chmod +x /home/selenium/install_certificate/install_certificate.sh

ENV XAUTHORITY=/home/selenium/.Xauthority

## Install WebPki
WORKDIR /home/selenium/Downloads

RUN curl -o /home/selenium/Downloads/webpki.deb https://get.webpkiplugin.com/Downloads/1705408638734/setup-deb-64

RUN apt install /home/selenium/Downloads/webpki.deb

USER selenium

ENTRYPOINT ["/entrypoint.sh"]
