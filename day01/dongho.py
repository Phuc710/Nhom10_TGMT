import cv2 as cv
import numpy as np
import math

# ===== Cấu hình =====
size = 500
center = (size//2, size//2)
radius = 200

hour = 10
minute = 10
second = 0

# ===== Hàm vẽ kim =====
def draw_hand(img, angle_deg, length, color, thickness):
    angle_rad = math.radians(angle_deg - 90)
    x = int(center[0] + length * math.cos(angle_rad))
    y = int(center[1] + length * math.sin(angle_rad))
    cv.line(img, center, (x, y), color, thickness)

while True:
    img = np.zeros((size, size, 3), dtype=np.uint8)

    # ===== Vòng tròn =====
    cv.circle(img, center, radius, (180, 255, 180), 3)

    # ===== Số La Mã =====
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, "XII", (center[0]-25, center[1]-radius+35), font, 1, (255, 0, 255), 2)
    cv.putText(img, "III", (center[0]+radius-45, center[1]+10), font, 1, (255, 0, 0), 2)
    cv.putText(img, "VI", (center[0]-15, center[1]+radius-10), font, 1, (255, 255, 255), 2)
    cv.putText(img, "IX", (center[0]-radius+10, center[1]+10), font, 1, (255, 0, 0), 2)

    # ===== Tính góc =====
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6
    second_angle = second * 6

    # ===== Vẽ kim =====
    draw_hand(img, hour_angle, 80, (0, 255, 0), 6)      # Kim giờ
    draw_hand(img, minute_angle, 130, (255, 0, 0), 4)  # Kim phút
    draw_hand(img, second_angle, 160, (0, 0, 255), 2)  # Kim giây

    # ===== Tâm =====
    cv.circle(img, center, 6, (0, 255, 255), -1)

    cv.imshow("CLOCK", img)

    key = cv.waitKey(0) & 0xFF

    # ESC để thoát
    if key == ord('q'):
        break

    # SPACE = tăng 1 phút
    if key == 32:
        minute += 1
        if minute >= 60:
            minute = 0
            hour += 1
            if hour >= 24:
                hour = 0

cv.destroyAllWindows()
