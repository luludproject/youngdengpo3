import pandas as pd
from itertools import product

list1 = ["강남", "역삼동", "개포동", "청담동", "삼성동", "대치동", "신사동", "논현동", "압구정동", "세곡동", "자곡동", "율현동", "일원동", "수서동", "도곡동", "논현1동", "논현2동", "삼성1동", "삼성2동", "대치1동", "대치2동", "대치4동", "역삼1동", "역삼2동", "도곡1동", "도곡2동", "개포1동", "개포2동", "개포3동", "개포4동", "일원본동", "일원1동"]

list2 = ["변기막힘", "변기뚫는업체", "변기수리", "싱크대막힘", "하수구막힘", "변기뚫음"]


# 모든 조합 생성
all_combinations = list(product(list1, list2))

# 3개씩 묶어서 새로운 조합 생성
chunk_size = 2
result_combinations = [', '.join(f'{combo[0]}{combo[1]}' for combo in all_combinations[i:i+chunk_size]) for i in range(0, len(all_combinations), chunk_size)]

# 데이터 생성
data = {'Keyword': result_combinations}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임을 엑셀 파일로 저장
excel_file = '하수구_강남구.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'키워드 조합이 {excel_file} 파일로 저장되었습니다.')