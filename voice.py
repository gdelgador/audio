import speech_recognition 
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    # search words
    recognizer = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    words = recognizer.recognize_google(audio, language="es-PE")
    print(words)

    time.sleep(4)

    # init browser
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    url="http://www.google.com"
    driver.get(url)

    time.sleep(4)

    search = driver.find_element_by_name('q')
    search.send_keys(words)
    search.send_keys(Keys.ENTER)


if __name__ == "__main__":
    main()
    os.system("pause")