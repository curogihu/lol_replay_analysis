import cv2
import os


def save_all_frames(video_path, dir_path, basename, step_frame=60, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()

        if ret:
            if n % step_frame == 0:
                print('n == {}'.format(n / step_frame))
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)

            n += 1
        else:
            return

if __name__ == '__main__':
    # video_path = r"C:\Users\hikozuma\Documents\League of Legends\Highlights\9-22_20191110_1.webm"
    # cap = cv2.VideoCapture(video_path)
    #
    # # 幅
    # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # # 高さ
    # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # # 総フレーム数
    # count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # # fps
    # fps = cap.get(cv2.CAP_PROP_FPS)
    #
    # print("width:{}, height:{}, count:{}, fps:{}".format(width,height,count,fps))

    save_all_frames(r"C:\Users\hikozuma\Documents\League of Legends\Highlights\9-22_20191110_2.webm", r"C:\lol_replay_frames", "VARUS_20191110_02", 30)

# vcap = cv2.VideoCapture(r"C:\Users\hikozuma\Documents\League of Legends\Highlights\9-22_20191110_1.webm", r"C:\lol_replay_frames")
#
# if not vcap.isOpened():
#     print("File Cannot be Opened")
#
# else:
#     print("File Can be Opened")