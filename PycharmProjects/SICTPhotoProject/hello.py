import cv2
import numpy as np
import cvgui

# 마우스 이벤트를 위한 딕셔너리.
# 마우스 콜백함수에 넣어서 항상 업데이트되도록 한다.
mouseValue = {"x": 0, "y": 0, "down": False}


def mouseCallback(event, x, y, flags, param):
    mouseValue["x"], mouseValue["y"] = x, y
    mouseValue["down"] = True if flags == cv2.EVENT_FLAG_LBUTTON else False

# 사용할 창의 이름을 SMART ICT PHOTO 4 CUTS로 정하고, 마우스 콜백을 지정한다.
win_title = "SMART ICT PHOTO 4 CUTS"
cv2.namedWindow(win_title)
cv2.setMouseCallback(win_title, mouseCallback)

# (height, width, channel) 300x300x3 크기의 빈 이미지를 생성해 배경으로 사용한다.
frame = np.zeros((600, 900, 3), np.uint8)

# 사용 예. 메인루프 진입 전 생성해 준다.
title = cvgui.GUI(text="스융네컷에 온 것을 환영합니다!", x=5, y=5, w=100, h=40, textSize=20, border=False, textAlign="left",
                  readOnly=True)
info = cvgui.GUI(text="q키나 창의 x버튼을 눌러 종료할 수 있습니다.", x=5, y=25, w=100, h=40, textSize=15, border=False, textAlign="left",
                 readOnly=True)
btn = cvgui.GUI(text="버튼", x=10, y=60, w=100, h=40)
toggle = cvgui.GUI(text="토글", x=120, y=60, w=100, h=40, toggle=True)
text = cvgui.GUI(text="a 키를 눌러 텍스트를 바꿀 수 있습니다.", x=10, y=100, w=100, h=40, textSize=15, border=False, textAlign="left",
                 readOnly=True)
maker = cvgui.GUI(text="만든이 : 만들오", x=190, y=130, w=100, h=20, textSize=12, textAlign="right", border=False,
                  readOnly=True)

# 메인루프
while True:
    # 배경 색상을 칠한다. OpenCV는 BGR(Blue,Green, Red) 순서.
    frame[:] = (90, 90, 90)

    # 생성한 GUI들을 frame에 추가한다.
    # .add(frame, mouseValue) 후 리턴값들
    # NORMAL : 선택되지 않은 상태
    # HOVER : 마우스가 위에 있는 상태
    # CLICK : 클릭한 경우(1회)
    # DOWN : 마우스로 누르고 있는 상태
    title.add(frame, mouseValue)
    info.add(frame, mouseValue)

    btn_value = btn.add(frame, mouseValue)
    if btn_value != "NORMAL" and btn_value != "HOVER":
        print(btn_value)
    if toggle.add(frame, mouseValue) == "CLICK": print("HELLO")
    text.add(frame, mouseValue)
    if maker.add(frame, mouseValue) == "DOWN":
        print("만들오입니다.")

    cv2.imshow(win_title, frame)
    key = cv2.waitKey(33)

    # q키 또는 X버튼을 누르면 종료
    if key == ord("q") or cv2.getWindowProperty(win_title, cv2.WND_PROP_VISIBLE) < 1:
        break
    elif key == ord("a"):
        msg = cvgui.askStr()
        text.changeText(msg)

cv2.destroyAllWindows()
