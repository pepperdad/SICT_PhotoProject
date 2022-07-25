import cv2
import time
import os
import tkinter
from PIL import Image, ImageTk
from skimage.transform import resize

window = tkinter.Tk()  # 인스턴스 생성
window.title("SMART ICT PHOTO 4 CUTS")  # 제목 표시줄
window.geometry("1450x900")  # 너비 x 높이
# window.resizable(False, False) # x축, y축 크기 조정 비활성화

main_frame = tkinter.Frame(window)
frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)
frame4 = tkinter.Frame(window)
frame5 = tkinter.Frame(window)

main_frame.grid(row=0, column=0, sticky="nsew")
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=0, sticky="nsew")
frame4.grid(row=0, column=0, sticky="nsew")
frame5.grid(row=0, column=0, sticky="nsew")


def openFrame(frame):
    if frame == main_frame:
        frame.tkraise()
    if frame == frame1 or frame == frame2 or frame == frame3 or frame == frame4:
        frame.tkraise()
        video_play()
    if frame == frame5:
        global result_image
        result_image = tkinter.PhotoImage(
            file="./result_image" + str(result_count) + ".png"
        ).subsample(4)
        print("./result_image" + str(result_count) + ".png")
        # result_image = Image.open("./result_image" + str(result_count) + ".png")
        # result_image = result_image.resize((200, 675), Image.ANTIALIAS)
        # result_image_resized = tkinter.PhotoImage(result_image)
        result_frame_label = tkinter.Label(frame5, image=result_image)
        result_frame_label.pack()
        frame.tkraise()


dam_frame = tkinter.PhotoImage(file="./dam_frame.png")

result_count = 0
result_image = ""

# main frame
label = tkinter.Label(main_frame, text="스융네컷에 온 것을 환영합니다!", font=("system", 20))
# label.place(x=5, y=5)
label.pack()
info = tkinter.Label(main_frame, text="원하는 프레임을 선택해주세요!", font=("system", 20))
# info.place(x=5, y=30)
info.pack()
btn = tkinter.Button(main_frame, image=dam_frame, command=lambda: [openFrame(frame1)])
btn2 = tkinter.Button(main_frame, image=dam_frame, command=lambda: [openFrame(frame2)])
btn3 = tkinter.Button(main_frame, image=dam_frame, command=lambda: [openFrame(frame3)])
btn4 = tkinter.Button(main_frame, image=dam_frame, command=lambda: [openFrame(frame4)])
btn.pack(side="left", padx=50)
btn2.pack(side="left", padx=50)
# btn2.place(x=1400,y=400)
btn3.pack(side="left", padx=50)
btn4.pack(side="left", padx=50)

# 농담곰 frame
label = tkinter.Label(frame1, text="농담곰 프레임!!!!!!!!", font=("system", 20))
label.pack()
back_btn = tkinter.Button(
    frame1,
    text="뒤로가기",
    font=("system", 20),
    compound="c",
    command=lambda: [openFrame(main_frame)],
)
back_btn.pack()
dam_frame_label = tkinter.Label(frame1, image=dam_frame)
dam_frame_label.pack(side="right")
# frm = tkinter.Frame(frame1, bg="white", width=720, height=480)  # 프레임 너비, 높이 설정
# frm.pack(side="left")  # 격자 행, 열 배치
# lbl1 = tkinter.Label(frm)
# lbl1.pack()

# 결과 frame
label3 = tkinter.Label(frame5, text="잠시만 기다려주세요", font=("system", 20))
label3.pack()

# 윈도우는 이거 있어야함?
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("스융네컷 가즈아")

# 동영상에서 사진 찍는 (윈도우)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 맥 # 웹캠은 2 ?


def video_play():  # frame1 자리 변수로 만들기
    # 동영상 프레임
    video_frm = tkinter.Frame(
        frame1, bg="white", width=720, height=480
    )  # 프레임 너비, 높이 설정
    video_frm.pack(side="left")  # 격자 행, 열 배치
    video_label = tkinter.Label(video_frm)
    video_label.pack()
    # frame1.tkraise()

    cap = cv2.VideoCapture(0)
    # time.sleep(2)
    cap.set(3, 600)
    cap.set(4, 500)
    fc = 20.0
    codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")
    out = cv2.VideoWriter("mycam.avi", codec, fc, (int(cap.get(3)), int(cap.get(4))))

    n = 1
    while True:
        # 한 장의 이미지(frame)를 가져오기
        # 영상 : 이미지(프레임)의 연속
        # 읽어온 프레임 -> frame
        ret, frame = cap.read()

        if not (ret):  # 프레임정보를 정상적으로 읽지 못하면
            break  # while문을 빠져나가기

        out.write(frame)
        cv2.imshow("frame", frame)
        # cv2.imshow("frame", video_label)
        k = cv2.waitKey(5)
        # frame1.tkraise()
        # # OpenCV 동영상
        # lbl1.imgtk = imgtk
        # lbl1.configure(image=imgtk)
        # lbl1.after(10, video_play)

        if n == 5:
            break
        if k == ord("q"):
            cv2.imwrite("save_image" + str(n) + ".jpg", frame)
            print(str(n) + "번째 사진")
            n += 1

        if k == 27:
            break

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
    global result_count
    while 1:
        if not (os.path.isfile("./result_image" + str(result_count) + ".png")):
            print("./result_image" + str(result_count) + ".png")
            result.save("./result_image" + str(result_count) + ".png")  # 사진이 저장될 경로
            break
        else:
            result_count += 1
            print("Result : " + str(result_count))

    cap.release()
    cv2.destroyAllWindows()
    openFrame(frame5)


"""
# Mac
cap = cv2.VideoCapture(0)
# cap.set(3, 720)
# cap.set(4, 1080)
def video_play():
    ret, frame = cap.read() # 프레임이 올바르게 읽히면 ret은 True
    if not ret:
        cap.release() # 작업 완료 후 해제
        return
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(frame) # Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=img) # ImageTk 객체로 변환
    # OpenCV 동영상
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(10, video_play)

video_play()
"""

# frm.grid(row=1, column=0) # 격자 행, 열 배치

openFrame(main_frame)
window.mainloop()
