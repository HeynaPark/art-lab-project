import cv2


def interpolate_video(input1, input2, output_path, duration_time):
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
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    img_duration = fps

    for i in range(img_duration):
        out.write(img1)

    # 보간 이미지 생성 및 비디오 작성
    num_frames = int(duration_time * 30)  # 30 프레임/초로 가정
    for i in range(num_frames):
        alpha = i / num_frames
        interpolated_frame = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        out.write(interpolated_frame)

    for i in range(img_duration):
        out.write(img2)

    out.release()
    cv2.destroyAllWindows()

    print('process done.')

if __name__ == "__main__":

    ### raw_img, difussion_img, output_video_path명을 경로에 맞게 수정해서 사용하시면 됩니다!
    name_str = 'scream'
    raw_img = "data/" + name_str + ".png"
    difussion_img = "data/" + name_str + "-d.png"
    output_video_path = "output/" + name_str + "_rev.mp4"
    duration_sec = 4
    interpolate_video(raw_img, difussion_img ,output_video_path, duration_sec)
