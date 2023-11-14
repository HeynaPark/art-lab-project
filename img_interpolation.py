import cv2
import os
import sys

file_name1 = ''
file_name2 = ''
time1 = 2
time2 = 3
time3 = 2

def interpolate_video(input1, input2, output_path, first_time, duration_time, last_time, mode):
    img1 = cv2.imread(input1)
    img2 = cv2.imread(input2)
    
    if img1 is None:
        print(f"Error: Unable to load image from {input1}")
        return
    if img2 is None:
        print(f"Error: Unable to load image from {input2}")
        return
    
    if img1.shape[0] > img2.shape[0]:
        img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
    elif img1.shape[0] < img2.shape[0]:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    print(img1.shape, img2.shape)
    height, width, channels = img1.shape

    # 출력 비디오 설정
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 30
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    img_duration = fps

    for i in range(img_duration*time1):
        out.write(img1)

    # 보간 이미지 생성 및 비디오 작성
    num_frames = int(duration_time * 30)  # 30 프레임/초로 가정
    for i in range(num_frames):
        alpha = i / num_frames
        interpolated_frame = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        out.write(interpolated_frame)

    for i in range(img_duration*time3):
        out.write(img2)

    if mode =='aba':
        for i in range(num_frames):
            alpha = i / num_frames
            interpolated_frame = cv2.addWeighted(img2, 1 - alpha, img1, alpha, 0)
            out.write(interpolated_frame)

        for i in range(img_duration*time1):
            out.write(img1)
        

    out.release()
    cv2.destroyAllWindows()

    print('process done.')

def save_file_path1(name):
    global file_name1
    file_name1 = name
    print("input1 : ", file_name1)

def save_file_path2(name):
    global file_name2
    file_name2 = name
    print("input2 : ", file_name2)

def save_time_val(t1,t2,t3):
    global time1, time2, time3
    time1 = int(t1)
    time2 = int(t2)
    time3 = int(t3)
    print(f"time settings : first frame {time1}   interpolation {time2}    last frame {time3}")

def get_available_file_name(base_path, extension):
    new_path = base_path
    counter = 1
    while os.path.exists(new_path):
        new_path = f"{os.path.splitext(base_path)[0]} ({counter}){extension}"
        counter += 1
    return new_path

def start_generate_video():
    current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_name_without_extension = os.path.splitext(os.path.basename(file_name2))[0]
    new_file_path = file_name_without_extension + str(time1) + str(time2) + str(time3) +'.mp4'
    output_str = os.path.join(current_directory, new_file_path)
    # Check if the file already exists
    if os.path.exists(output_str):
        output_str = get_available_file_name(output_str, '.mp4')
    print('output file : ', output_str)

    interpolate_video(file_name1, file_name2, output_str, time1, time2, time3, 'none')

def start_generate_video_aba():
    current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_name_without_extension = os.path.splitext(os.path.basename(file_name2))[0]
    new_file_path = file_name_without_extension + str(time1) + str(time2) + str(time3) +'_aba.mp4'
    output_str = os.path.join(current_directory, new_file_path)
    # Check if the file already exists
    if os.path.exists(output_str):
        output_str = get_available_file_name(output_str, '_aba.mp4')
    print('output file : ', output_str)

    interpolate_video(file_name1, file_name2, output_str, time1, time2, time3, 'aba')


if __name__ == "__main__":

    ### raw_img, difussion_img, output_video_path명을 경로에 맞게 수정해서 사용하시면 됩니다!
    name_str = 'wawa'
    raw_img = "data/" + name_str + ".png"
    difussion_img = "data/" + name_str + "-d.png"
    output_video_path = "output/" + name_str + ".mp4"
    duration_sec = 4
    # interpolate_video(difussion_img , raw_img, output_video_path, duration_sec)
