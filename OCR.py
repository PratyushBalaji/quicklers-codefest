from pickletools import pyset
import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Source image
img = cv2.imread("C:/Users/LENOVO/Pictures/test.png")

# img manipulation, etc
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgNoNoise = cv2.medianBlur(img, 3)


def detectChars(img):
    hImg, wImg = img.shape[:2]
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(" ")
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4]),
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
        cv2.putText(img, b[0], (x, hImg - y + 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 255), 1)


def detectWords(img):
    global diagnosis
    hImg, wImg = img.shape[:2]
    boxes = pytesseract.image_to_data(img)
    b = boxes.splitlines()
    b = b[1:]
    diagnosis = ""
    for i in b:
        i = i.split("\t")
        if len(i) == 12:
            if i[11] != "":
                x, y, w, h = int(i[6]), int(i[7]), int(i[8]), int(i[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                # cv2.putText(img, i[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
                diagnosis += i[11]
                diagnosis += " "


    diagnosis = diagnosis.replace(',', '')
    diagnosis = diagnosis.replace('(', '')
    diagnosis = diagnosis.replace(')', '')
    diagnosis = diagnosis.replace('-', '')
    print(diagnosis)
    print("\n")


detectWords(imgGray)

# cv2.imshow("result", imgGray)
# cv2.waitKey(0)


print(diagnosis)
arr = diagnosis.split(' ')
parsed_data = [arr[i] for i in range(len(arr)) if i%2 != 0]
labels = [arr[i] for i in range(len(arr)) if i%2 == 0]
labels.remove(labels[len(labels)-1])


for i in range(len(parsed_data)):
    if parsed_data[i] == 'Yes':
        parsed_data[i] = 1

    elif parsed_data[i] == 'No':
        parsed_data[i] = 0

    else:
        parsed_data.remove[i]

print(labels,parsed_data)

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return



'''for word in diagnosis.split(' '):
    if word.upper() in Cancer_Dict.keys():
        l = extract_from_text(word)
        r = Cancer_Dict[word.upper()](l[0])
        print(r)
'''