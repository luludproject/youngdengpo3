import pandas as pd

# 엑셀 파일에서 첫 번째 열의 키워드를 읽어옵니다.
df = pd.read_excel('하수구_강남구.xlsx', usecols=[0], header=None)  # 'keywords.xlsx'를 엑셀 파일 이름으로 변경

# 파일에 작성할 XML 텍스트를 담을 리스트를 만듭니다.
xml_lines = []

for keyword in df[0]:
    xml_text = f"""
<url>
<loc>https://gangnamgu.jianhomecare.com/블로그/{keyword}</loc>
<changefreq>yearly</changefreq>
<priority>0.80</priority>
</url>
"""
    xml_lines.append(xml_text)

# 생성된 XML 텍스트를 파일에 저장합니다.
with open('output.xml', 'w', encoding='utf-8') as file:
    file.write('\n'.join(xml_lines))

print("파일 생성이 완료되었습니다.")
