import datetime
import sys
import cv2


def video_capture():
    font_face = 1
    thickness = 1
    font_scale = 1
    frame_width = 800
    frame_height = 600

    if cv2.cuda.getCudaEnabledDeviceCount() == 0:
        print("No GPU found or the library is compiled without CUDA support")
        sys.exit(-1)

    # print(cv2.getBuildInformation())
    print(cv2.cuda.printShortCudaDeviceInfo(cv2.cuda.getDevice()))

    capture_device = cv2.VideoCapture()

    capture_device.open(0)
    if not capture_device.isOpened():
        print("Capture device is not opened")
        sys.exit(-1)

    capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    cv2.namedWindow("cam", 1)
    cv2.namedWindow("bw", 1)
    cv2.namedWindow("bw_equalized", 1)

    while True:
        _, frame = capture_device.read()

        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        current_date_time = str(datetime.datetime.now())

        base_line, _ = cv2.getTextSize(current_date_time, font_face, font_scale, thickness)

        pt1 = (0, frame_height - (2 * base_line[1]))
        pt2 = (int(base_line[0] + (0.2 * base_line[0])), frame_height)
        color = (255, 255, 255)
        cv2.rectangle(frame, pt1, pt2, color, -1)

        origin = (int(0.1 * base_line[0]), int(frame_height - (0.5 * base_line[1])))
        cv2.putText(frame, current_date_time, origin, font_face, font_scale, (0, 0, 0))

        frame_bw_eq = cv2.equalizeHist(frame_bw)

        cv2.imshow("cam", frame)
        cv2.imshow("bw", frame_bw)
        cv2.imshow("bw_equalized", frame_bw_eq)

        pressed_key = cv2.waitKey(16)
        if pressed_key == ord('q'):
            break

    cv2.destroyAllWindows()
