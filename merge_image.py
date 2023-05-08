import cv2
import os
import numpy as np

# 매개변수 4개 (자른 이미지들의 접두사, 열 개수, 행 개수, 병합 이미지 이름)
def main(input_filename_prefix, column_num, row_num, output_filename):
    path, target_files = read_image(input_filename_prefix)
    merge_image(path, column_num, row_num, target_files, output_filename)

# 이미지 파일 경로 지정
def read_image(input_filename_prefix):
    path = os.getcwd()
    dirname = "/image/new_image"
    path = path + dirname
    # 디렉토리 내 파일 리스트를 불러옴
    file_list = os.listdir(path)

    # 파일명에 해당하는 파일 리스트 추출
    target_files = [file for file in file_list if input_filename_prefix in file]

    return (path, target_files)

def merge_image(path, column_num, row_num, target_files, output_filename):
    dir_len = len(target_files)

    # 자른 이미지 -> 첫 이미지
    cut_img_zero_path = os.path.join(path, target_files[0])
    cut_img_zero = cv2.imread(cut_img_zero_path)
    cut_img_zero_height, cut_img_zero_width = cut_img_zero.shape[:2]

    # 빈 이미지 생성
    img_merged = np.zeros((cut_img_zero_height * row_num, cut_img_zero_width * column_num, 3), dtype=np.uint8)

    # 디렉토리 내 "input_filename_prefix" 파일 개수가 행렬과 일치
    if dir_len == (column_num * row_num):
        # 추출된 파일들을 읽어와서 처리
        for file in target_files:
            # 자른 이미지
            cut_img_path = os.path.join(path, file)
            print(cut_img_path)
            cut_img = cv2.imread(cut_img_path)
            cut_img_height, cut_img_width = cut_img.shape[:2]

            for row in range(row_num):
                for col in range(column_num):
                    # 변환된 이미지를 빈 이미지에 덮어씌우기
                    y, x = row * cut_img_height, col * cut_img_width
                    img_merged[y:y + cut_img_height, x:x + cut_img_width] = cut_img

        # 합쳐진 이미지 저장
        cv2.imwrite('merged_image.jpg', img_merged)
    else:
        print("디렉토리 내 'prefix_output_filename' 파일의 개수가 원하는 행렬의 개수와 맞지 않습니다. \n확인 부탁드립니다.")