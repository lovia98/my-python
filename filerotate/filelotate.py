import os

"""
지정한 폴더에 최신 몇개의 파일만 유지하고 나머지는 삭제
"""
def delete_old_files(path_target, keep_count):
    # 지정한 폴더에서 파일만 추출
    file_list = []
    for f in os.listdir(path_target):
        file_path = os.path.join(path_target, f)
        if os.path.isfile(file_path):
            file_list.append(file_path)

    # 수정날짜 최신순으로 sort
    file_list.sort(key=os.path.getmtime, reverse=True)

    # 유지하고자 하는 갯수만큼 남기고 나머지
    remove_list = file_list[keep_count:]

    for f in remove_list:
        os.remove(f)


#delete_old_files(path_target='./test/', keep_count=5)
