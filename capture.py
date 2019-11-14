import cv2
import datetime
import os

def capture_camera():
    cap = cv2.VideoCapture(0)

    now = datetime.datetime.now()
    dir_name = now.strftime('%Y%m%d_%H%M%S')
    os.makedirs('./images/' + dir_name)

    while True:
        # Read and show
        size = (800, 450)
        window_name = 'Camera capture'
        ret, frame = cap.read()
        if not ret:
            print("Failed to open camera.")
        frame = cv2.resize(frame, size)
        cv2.imshow(window_name, frame)

        # Write
        now = datetime.datetime.now()
        filename = './images/' + dir_name + '/' + now.strftime('%H%M%S') + '.jpg'
        ret = cv2.imwrite(filename, frame)
        if not ret:
            print("Failed to write image.")

        # Wait
        k = cv2.waitKey(1)
        if k == 27: # Esc Key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_camera()

