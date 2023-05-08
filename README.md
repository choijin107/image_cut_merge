<div align = center>
    <h1>image_cut_merge</h1>
</div>

<h1>[문제]</h1>
1. 하나의 이미지를 M * N 자르기 <br/> 
2. M * N 부분 이미지 → 임의 변환 (mirroring, flipping, 90 degree rotation) <br/> 
3. 임의로 변환된 M * N 부분 이미지 → 하나의 이미지로 병합 <br/> 

- 임의 변환 확률 0.5% (총 8가지의 경우의 수)
- 각각의 자른 이미지를 임의 변환 후 랜덤한 이름으로 저장 (파일명으로 유추 못하도록)
- 병합될 이미지는 4가지의 경우를 갖게 됨. (original, mirroring version, flipping version, 90 degree rotation version)

---

<h1>[풀이]</h1>
1. cut_image.py<br/> 
    - 매개변수<br/> 
        1. image_file_name : 원본 이미지 이름 <br/>
        2. column_num : 열 <br/> 
        3. row_num : 행 <br/> 
        4. prefix_output_filename : 자른 이미지들의 접두사 <br/> 

  - 함수 실행<br/> 
    
        read_image() → cut_image() → make_dir() → random_conversion_image()
       
        
2. merge_image.py
    - 매개변수
        1. input_filename_prefix : 자른 이미지들의 접두사   
        2. column_num : 열
        3. row_num : 행
        4. output_filename : 자른 이미지를 병합한 이미지의 이름
        
    - 함수 실행

        read_image() → merge_image()
        
3. test.py
    - python file 실행
    
        cut_image() → merge_image()

(+) merge_image_template.py 

---
<h1>[코드 구현 결과 - cut ; 성공]</h1>
<h1>[코드 구현 결과 - merge ; 실패]</h1>
    <h3>merge_image.py</h3>
    원본 이미지를 사용하지 않고, 임의 변환된 각각의 자른 이미지를 사용하여 하나의 이미지로 구현해보려 했으나
    상하 또는 좌우 반전이 각기 달라 그에 맞는 4가지 결과 값 중 하나에 부합하도록 합치는게 생각처럼 쉽게 구현되지 않았음.
    (보완점) 상하 반전 혹은 좌우 반전만 되어 있다면 그에 맞는 4가지 결과 값 중 2가지 버전에 부합할 수 있도록
    contour를 이미지의 구분 지점으로 파악하는 Watershed 알고리즘을 이용하여 경계선을 파악해, 합쳐보면 좋을 것 같음.<br/> 
    
    <h3>merge_image_template.py</h3><br/> 
    원본 이미지를 사용하여 임의 변환된 각각의 자른 이미지와 Template Matching 시도
    (원본 이미지의 크기만큼 캔버스를 생성하여, 반복적으로 매칭된 자리의 잘린 이미지의 좌표값에 잘린 이미지 삽입)
    위 코드와 비슷하게, 상하 /좌우 반전이 섞여 있어 해결하기 힘들었음
    만약 임의 변환된 각각의 자른 이미지를 재변환 할 수 있다고 가정한다면, 코드 구현 가능.
    
