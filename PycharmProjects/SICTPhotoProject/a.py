import cv2
import time
import os
import tkinter
from PIL import Image, ImageTk
from cv2 import VIDEOWRITER_PROP_FRAMEBYTES
from skimage.transform import resize
import keyboard
import pyautogui


def image_capture():
    print("hi")

    # cv2.imwrite("save_image" + str(n) + ".jpg", frame)
    # print(str(n) + "번째 사진")
    # n += 1


result_count = 0
n = 1
window = tkinter.Tk()  # 인스턴스 생성
window.title("SMART ICT PHOTO 4 CUTS")  # 제목 표시줄
window.geometry("1450x900")  # 너비 x 높이
# window.resizable(False, False) # x축, y축 크기 조정 비활성화'

# 스융네컷 라벨
lbl = tkinter.Label(window, text="스융네컷")
lbl.grid(row=0, column=0)  # 라벨 행, 열 배치

# 동영상 프레임
video_frm = tkinter.Frame(window, bg="white", width=720, height=480)  # 프레임 너비, 높이 설정
video_frm.grid(row=1, column=0)  # 격자 행, 열 배치

# 동영상 라벨
video_label = tkinter.Label(video_frm)
video_label.bind("<Key>", image_capture)
video_label.grid()

# frame1.tkraise()

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
fc = 20.0
codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")
out = cv2.VideoWriter("mycam.avi", codec, fc, (int(cap.get(3)), int(cap.get(4))))


def video_play():
    # 한 장의 이미지(frame)를 가져오기
    # 영상 : 이미지(프레임)의 연속
    # 읽어온 프레임 -> frame
    global n

    ret, frame = cap.read()
    if not (ret):  # 프레임정보를 정상적으로 읽지 못하면
        cap.release()
        return

    img = Image.fromarray(frame)  # Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=img)  # ImageTk 객체로 변환
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    video_label.after(10, video_play)
    # while True:
    #     if keyboard.read_key() == "p":
    #         print("hi")
    # cv2.imwrite("save_image" + str(n) + ".jpg", img)
    # k = cv2.waitKey(5)

    # if n == 5:
    #     return
    # if k == ord("q"):
    #     cv2.imwrite("save_image" + str(n) + ".jpg", frame)
    #     print(str(n) + "번째 사진")
    #     n += 1
    # if k == 27:
    #     break

    # cap.release()
    # cv2.destroyAllWindows()


def image_save():
    result_width = 800
    result_height = 2700

    result = Image.new("L", (result_width, result_height))
    result = Image.open("./damgom.jpg")  # 프레임

    input_img_1 = Image.open("./save_image1.jpg")  # 덮어쓸 사진의 경로
    input_img_2 = Image.open("./save_image2.jpg")  # 덮어쓸 사진의 경로
    input_img_3 = Image.open("./save_image3.jpg")  # 덮어쓸 사진의 경로
    input_img_4 = Image.open("./save_image4.jpg")  # 덮어쓸 사진의 경로

    # input_img_1.resize((int(200), int(200)))
    # input_img_1.save(filename='./save_image1.jpg')
    input_img_1_resized = input_img_1.resize((645, 480))
    input_img_2_resized = input_img_2.resize((645, 480))
    input_img_3_resized = input_img_3.resize((645, 480))
    input_img_4_resized = input_img_4.resize((645, 480))

    result.paste(im=input_img_1_resized, box=(80, 264))
    result.paste(im=input_img_2_resized, box=(80, 798))
    result.paste(im=input_img_3_resized, box=(80, 1332))
    result.paste(im=input_img_4_resized, box=(80, 1866))

    # result_count = 0

    while 1:
        if not (os.path.isfile("./result_image" + str(result_count) + ".png")):
            print("./result_image" + str(result_count) + ".png")
            result.save("./result_image" + str(result_count) + ".png")  # 사진이 저장될 경로
            break
        else:
            result_count += 1
            print("Result : " + str(result_count))


video_play()
window.mainloop()
