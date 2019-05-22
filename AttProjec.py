from __future__ import print_function
import subprocess
from gtts import gTTS
from os.path import abspath
import os
import cv2
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey='###YOUR IAMPIKEY CODE###')


def recogImg(img):
    str2 = 'none'
    first = False
    img2 =  abspath(img)
    with open(img2, 'rb') as images_file:
        classes_result = visual_recognition.classify(images_file=images_file, accept_language='en').get_result()

    try:
        for x in range (len(classes_result["images"][0]["classifiers"][0]["classes"])):
        # for x in range(0, 3):

           if classes_result["images"][0]["classifiers"][0]["classes"][x]["class"] == 'person':
               recogFaceImg(img)
           if classes_result["images"][0]["classifiers"][0]["classes"][x]["score"] > 0.65:
               if first == False:
                   str2 = ''
                   first = True
               str2 = (str2 + "  " + (classes_result["images"][0]["classifiers"][0]["classes"][x]["class"]))

               print(format(classes_result["images"][0]["classifiers"][0]["classes"][x]["score"], '.2f'), end=" ")
               print(classes_result["images"][0]["classifiers"][0]["classes"][x]["class"])
    except:
        print("Error ")
    print(str2)
    return str2

def recogUrl(path):
    path[:-1]
    str1 = ''
    classes_result = visual_recognition.classify(url=path).get_result()
    for x in range (len(classes_result["images"][0]["classifiers"][0]["classes"])):
        str1 = (str1 + " or " + (classes_result["images"][0]["classifiers"][0]["classes"][x]["class"]))
        print(format(classes_result["images"][0]["classifiers"][0]["classes"][x]["score"], '.2f'), end=" ")
        print(classes_result["images"][0]["classifiers"][0]["classes"][x]["class"])
    return str1

def recogFaceImg(img):
    img2 = abspath(img)
    with open(img2, 'rb') as images_file:
        classes_result = visual_recognition.detect_faces(images_file=images_file).get_result()
        print(format(classes_result["images"][0]["faces"][0]["gender"]["score"], '.2f'), end=" ")
        print(classes_result["images"][0]["faces"][0]["gender"]["gender"])
        print(format(classes_result["images"][0]["faces"][0]["age"]["score"], '.2f'), end=" ")
        print("Age: " + str(classes_result["images"][0]["faces"][0]["age"]["min"]), end=" ~ ")
        print(str(classes_result["images"][0]["faces"][0]["age"]["max"]))
        # print(json.dumps(classes_result, indent=2))




def takePicture():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # width=640
    cap.set(4, 480)  # height=480

    if cap.isOpened():
        _, frame = cap.read()
        cap.release()  # releasing camera immediately after capturing picture
        if _ and frame is not None:
            cv2.imwrite('img.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()

def showCamera():
    subprocess.call(" python webCam.py 1", shell=True)

def voice(str):
    tts = gTTS(text= str, lang='en')
    tts.save("sound.mp3")
def wait():
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def main():
    choice ='0'
    while choice != 'q':
        print("Main Choice: Choose 1 of 6 choices")
        print("Choose 1 URL")
        print("Choose 2 Face Image")
        print("Choose 3 Image Jpg")
        print("Choose 4 Cam Picture")
        print("Choose 5 Cam Picture and Sound")
        print("Choose 6 Cam")
        print("Choose q Exit")

        choice = input ("Please make a choice: ")

        if choice == "1":
            urlImag = input("Enter Url:")
            print(urlImag)
            recogUrl(urlImag)
            wait()
        if choice == "2":
            takePicture()
            recogFaceImg("img.jpg")
            wait()

        elif choice == "3":
            file = input("Enter name of the file ")
            recogImg("resources/" + file)
            wait()

        elif choice == "4":

            takePicture()
            recogImg("img.jpg")
            wait()

        elif choice == "5":
            takePicture()
            x = recogImg("img.jpg")
            voice(x)
            os.system("afplay sound.mp3")
            wait()

        elif choice == "6":
            print("Type \'q\' to exit ")
            showCamera()
            wait()
        elif choice == "q":
            break
        else:
            pass


main()










