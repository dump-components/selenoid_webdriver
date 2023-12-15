FROM selenoid/vnc_chrome:119.0

USER root

RUN apt update -y

RUN apt install -y pip xauth python3-tk python3-dev python3-xlib && \
mkdir /home/selenium/install_certificate

RUN pip install pyautogui

WORKDIR /home/selenium

# Create Xauthority
RUN touch /home/selenium/.Xauthority && chmod 777 /home/selenium/.Xauthority

COPY entrypoint.sh /
COPY ./ /home/selenium/install_certificate

RUN chmod +x /entrypoint.sh && chmod +x /home/selenium/install_certificate/install_certificate.sh

ENV XAUTHORITY=/home/selenium/.Xauthority

USER selenium

ENTRYPOINT ["/entrypoint.sh"]
