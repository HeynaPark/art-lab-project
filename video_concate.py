import cv2

def combine_videos(video1_path, video2_path, output_path):
    cap1 = cv2.VideoCapture(video1_path)
    cap2 = cv2.VideoCapture(video2_path)

    if not cap1.isOpened():
        print(f"Error: Couldn't open video file {video1_path}")
        return
    if not cap2.isOpened():
        print(f"Error: Couldn't open video file {video2_path}")
        return

    # 영상 크기 가져오기
    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 두 비디오의 프레임 크기를 동일하게 맞춤
    new_width = min(width1, width2)
    new_height = min(height1, height2)

    # 출력 비디오 설정
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 30, (new_width, new_height))

    while True:
        ret1, frame1 = cap1.read()

        if ret1:
            # 프레임 크기 조정
            for _ in range(2):
                frame1 = cv2.resize(frame1, (new_width, new_height))
                out.write(frame1)
        else:
            break  # 첫 번째 비디오가 끝나면 종료
          
    while True:
        ret2, frame2 = cap2.read()

        if ret2:
            # 프레임 크기 조정
            frame2 = cv2.resize(frame2, (new_width, new_height))
            out.write(frame2)
        else:
            break  # 두 번째 비디오가 끝나면 종료
    cap1.release()
    cap2.release()
    out.release()
    cv2.destroyAllWindows()
    print('process done.')


if __name__ == "__main__":
    video1_path = "data/gogh_reverse.mp4"  # 두 번째 비디오 파일 경로 입력
    video2_path = "output/gogh.mp4"  # 첫 번째 비디오 파일 경로 입력
    output_path = "output/gogh_concate.mp4"  # 출력 비디오 파일 경로 입력

    combine_videos(video1_path, video2_path, output_path)
