import openpyxl
import os
import random
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

# 엑셀 파일로부터 키워드 읽기
def read_keywords_from_excel(file_path):
    keywords = []
    column2_values = []
    column3_values = []

    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            area_keyword = row[0]
            column2_value = row[1]
            column3_value = row[2]
            
            if area_keyword:
                keywords.append(str(area_keyword))  # 키워드를 문자열로 저장
            if column2_value:
                column2_values.append(str(column2_value))  # 두 번째 열 값을 문자열로 저장
            if column3_value:
                column3_values.append(str(column3_value))  # 세 번째 열 값을 문자열로 저장
        
    except Exception as e:
      print(f"Error reading Excel file: {e}")

    return keywords, column2_values, column3_values


image_urls = [
	"https://jianhomecare.com/img/11.png",
	"https://jianhomecare.com/img/12.png",
	"https://jianhomecare.com/img/13.png",
	"https://jianhomecare.com/img/14.png",
	"https://jianhomecare.com/img/15.png",
	"https://jianhomecare.com/img/16.png",
	"https://jianhomecare.com/img/17.png",
	"https://jianhomecare.com/img/18.png",
	"https://jianhomecare.com/img/19.png",
	"https://jianhomecare.com/img/3.png",
	"https://jianhomecare.com/img/4.png",
	"https://jianhomecare.com/img/5.png",
	"https://jianhomecare.com/img/about-1.png",
  "https://cdn-thumbs.imagevenue.com/01/7c/a5/ME18XLT4_t.png",
  "https://cdn-thumbs.imagevenue.com/bc/83/eb/ME18XLT5_t.png",
  "https://cdn-thumbs.imagevenue.com/64/48/d0/ME18XLT8_t.png",
  "https://cdn-thumbs.imagevenue.com/91/f3/5c/ME18XLT9_t.png",
  "https://cdn-thumbs.imagevenue.com/82/94/ea/ME18XLTA_t.png",
  "https://cdn-thumbs.imagevenue.com/af/6a/e1/ME18UNP6_t.png",
  "https://cdn-thumbs.imagevenue.com/15/a7/11/ME18UNP7_t.png",
  "https://cdn-thumbs.imagevenue.com/2f/70/dc/ME18UNP9_t.png",
  "https://cdn-thumbs.imagevenue.com/70/43/f1/ME18UNPA_t.png"
]

# 기본 디렉토리 설정
temp_dir = "temp_images/"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
    
# 랜덤 색상 조정 함수
def random_color_adjustment(img):
    # 랜덤 밝기 조정
    brightness = random.uniform(0.5, 1.5)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    
    # 랜덤 대비 조정
    contrast = random.uniform(0.5, 1.5)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    
    # 랜덤 채도 조정
    saturation = random.uniform(0.5, 1.5)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation)
    
    # 랜덤 색조 조정 (색상 이동)
    hue = random.uniform(-0.1, 0.1)
    img = img.convert("HSV")
    h, s, v = img.split()
    h = h.point(lambda p: (p + int(hue * 255)) % 255)
    img = Image.merge("HSV", (h, s, v)).convert("RGB")
    
    # 랜덤 필터 적용
    filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, ImageFilter.SHARPEN]
    img = img.filter(random.choice(filters))
    
    return img
    
# 이미지를 다운로드하고 색 조정하기
def download_and_adjust_image(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        
        # 이미지 색 조정
        with Image.open(output_path) as img:
            # 예: 밝기 조정
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(random.uniform(0.5, 1.5))  # 밝기 조정


						# WebP 포맷으로 저장
            img.save(output_path, format='WEBP')

# 모든 이미지를 다운로드하고 조정
for index, url in enumerate(image_urls):
    output_path = os.path.join(temp_dir, f"image_{index}.webp")
    download_and_adjust_image(url, output_path)

# 랜덤으로 조정된 이미지 선택
adjusted_images = os.listdir(temp_dir)



# HTML 템플릿
html_template = """
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <title>{title} > 블로그 - 즉시 출동!</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <meta
      content="{sep_keyword1},{sep_keyword2}, 강남구변기막힘, 강남변기뚫는업체, 강남하수구막힘, 강남변기수리, 강남싱크대막힘"
      name="keywords"
    />
    <meta
      content="{sep_keyword1},{sep_keyword2} 바로 해결해드립니다. 즉시 출동!"
      name="description"
    />
    <meta
      name="googlebot"
      content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"
    />
    <meta
      name="robots"
      content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"
    />
    <link rel="profile" href="https://gmpg.org/xfn/11" />
    <link rel="canonical" href="https://gangnamgu.jianhomecare.com/블로그/{sep_keyword1}-{sep_keyword2}" />
    <meta property="og:locale" content="ko_KR" />
    <meta property="og:type" content="website" />
    <meta
      property="og:title"
      content="{og_title} > 블로그 - 즉시 출동!"
    />
    <meta
      property="og:description"
      content="{sep_keyword1},{sep_keyword2} 바로 해결해드립니다. 즉시 출동!"
    />
    <meta property="og:url" content="https://gangnamgu.jianhomecare.com/블로그/{sep_keyword1}-{sep_keyword2}" />
    <meta property="og:site_name" content="{sep_keyword1}-{sep_keyword2}" />
    <meta property="og:image" content="../img/변기막힘하수구막힘.png" />
    <meta property="og:image:secure_url" content="../img/변기막힘하수구막힘.png" />
    <meta property="og:image:width" content="500" />
    <meta property="og:image:height" content="500" />
    <meta property="og:image:alt" content="강남구변기막힘" />
    <meta property="og:image:type" content="image/gif" />
    <meta name="twitter:domain" content="{keywords}">
    
    <meta property="article:section" content="강남구변기막힘">
    <meta name="twitter:card" content="summary_large_image" />
    <meta
      name="twitter:title"
      content="{twitter_title} > 블로그 - 즉시 출동!"
    />
    <meta
      name="twitter:description"
      content="{sep_keyword1},{sep_keyword2} 바로 해결해드립니다. 즉시 출동!"
    />
    <meta name="twitter:image" content="img/변기막힘하수구막힘.png" />

    <script src="../js/sujww121.js"></script>
    <script src="../js/fujjhd999.js"></script>

    
    <!-- Favicon -->
    <link rel="shortcut icon" href="../img/favicon.ico" type="image/x-icon" />
    <link rel="icon" href="../img/favicon.ico" type="image/x-icon" />


    <!-- Font Awesome -->
    <link
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css"
      rel="stylesheet"
    />

    <!-- Flaticon Font -->
    <link href="../lib/flaticon/font/flaticon.css" rel="stylesheet" />

    <!-- Libraries Stylesheet -->
    <link
      href="../lib/owlcarousel/assets/owl.carousel.min.css"
      rel="stylesheet"
    />
    <link href="../lib/lightbox/css/lightbox.min.css" rel="stylesheet" />

    <!-- Customized Bootstrap Stylesheet -->
    <link href="../css/style.css" rel="stylesheet" />
  </head>

  <body>
    <!-- Navbar Start -->
    <div class="container-fluid bg-light position-relative shadow">
      <nav
        class="navbar navbar-expand-lg bg-light navbar-light py-3 py-lg-0 px-0 px-lg-5"
      >
        <a href="/" class="navbar-brand font-weight-bold text-secondary">
          <span class="text-primary">강남구변기막힘</span>
        </a>
        <button
          type="button"
          class="navbar-toggler"
          data-toggle="collapse"
          data-target="#navbarCollapse"
          aria-label="{sep_keyword1}"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div
          class="collapse navbar-collapse justify-content-between"
          id="navbarCollapse"
        >
          <div class="navbar-nav font-weight-bold mx-auto py-0">
            <a href="/" class="nav-item nav-link ">홈</a>
            <a href="/서비스" class="nav-item nav-link ">서비스</a>
          
            <a href="/작업사진" class="nav-item nav-link">작업사진</a>
              <a
                href="/블로그"
                class="nav-item nav-link active"
                >블로그</a
              >
              <a href="https://open.kakao.com/o/sDzjD7Nf" class="nav-item nav-link" id="contact">문의하기</a>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <!-- Navbar End -->

    <!-- Header Start -->
    <div class="container-fluid bg-primary mb-5">
      <div
        class="d-flex flex-column align-items-center justify-content-center"
        style="min-height: 400px"
      >
        <h3 class="display-3 font-weight-bold text-align-center text-white">강남구변기막힘</h3>
        <div class="d-inline-flex text-white">
          <p class="m-0"><a class="text-white" href="/">홈</a></p>
          <p class="m-0 px-2">/</p>
          <p class="m-0">블로그</a></p>
          <p class="m-0 px-2">/</p>
          <p class="m-0">{p_text}</p>
        </div>
      </div>
    </div>
    <!-- Header End -->

    <!-- Detail Start -->
    <div class="container py-5">
      <div class="row pt-5">
        <div class="col-lg-8">
          
          <div class="d-flex flex-column text-left mb-3">
            <p class="section-title pr-5">
              <span class="pr-2">{span_text}</span>
            </p>
            <h1 class="mb-3">{h1_text}</h1>
            
          </div>
          <div class="mb-5 d-flex flex-column">


            <img src="../temp_images/{image_url5}" loading="lazy" alt="{alt_text}" style="margin: 0 auto 50px; width: 60%;"/>

            <div class="toc">
              <h2>목차</h2>
              <ul>
                  <li><a href="#section1">1. {sep_keyword1}</a></li>
                  <li><a href="#section2">2. {sep_keyword2}</a></li>
                  <li><a href="#section3">3. 강남구변기막힘 </a></li>
                  <li><a href="#section4">4. 결론</a></li>
              </ul>
          </div>
          
            <h2 class="mb-4" id="section1" style="text-align: center;">{sep_keyword1}</h2>
            <p>
              {p_text}은 {desc}{desc2}{desc3}{desc4}{desc5}{desc6}{desc7}
          </p>
          <img class="mb-4"
            src="../temp_images/{image_url}" loading="lazy" style="margin: 0 auto 50px; width: 60%;"
            alt="{alt_text}"
          />
          
            <p>
              {desc8}{desc9}{desc10}{desc11}{desc12}{desc13}
            </p>


            <h2 class="mb-4" id="section2" style="text-align: center;">{sep_keyword2}</h2>
            <img
              src="../temp_images/{image_url2}" loading="lazy" style="margin: 0 auto 50px; width: 60%;"
              alt="싱크대막힘"
            />
            <p>
              {desc14}{desc15}{desc16}{desc17}
            </p>
            <p>{desc18}{desc19}{desc20}{desc21}{desc22}{desc23}{desc24}{desc25}{desc26}{desc27}</p>

            <h2 class="mb-4" id="section3" style="text-align: center;">강남구변기막힘</h2>
            <img
              src="../temp_images/{image_url3}" loading="lazy" style="margin: 0 auto 50px; width: 60%;"
              alt="강남구변기막힘"
            />
            <p>
              {desc28}{desc29}{desc30}{desc31}{desc32}{desc33}{desc34}{desc35}{desc36}{desc37}{desc38}{desc39}{desc40}
            </p>



            <h2 class="mb-4" id="section4" style="text-align: center;">결론</h2>
            <img
              src="../temp_images/{image_url4}" loading="lazy" style="margin: 0 auto 50px; width: 60%;"
              alt="강남구하수구막힘"
            />
            <p>
              {p_text} {desc41}{desc42}{desc43}{desc44}{desc45}{desc46}{desc47}{desc48}{desc49}{desc50}{desc51}{desc52}{desc52}
            </p>
          </div>

        <div class="container-fluid py-5">
      <div class="container p-0">
        <div class="text-center pb-2">
          <p class="section-title px-5">
            <span class="px-2">FAQ</span>
          </p>
          <h2>FAQ</h2>
          <h2>{sep_keyword1} 발생하는 이유?</h2>
          <p>{sep_keyword1}은 여러 가지 원인으로 발생할 수 있습니다.가장 흔한 원인은 이물질의 유입입니다.일반적으로 화장지, 물티슈, 여성 위생 용품과 같은 물에 잘 녹지 않는 물질이 변기로 흘러들어가 막힘을 유발합니다. {desc36}{desc38}</p>
          <br>
          <h2>{sep_keyword1} 예방법은?</h2>
          <p>{sep_keyword1} 예방법으로는 변기에는 화장지 이외의 이물질을 투입하지 않도록 합니다. {desc11}{desc32}{desc26}</p>
        </div>
      </div>

    </div>

        <table border="1" style="margin: 0 0 50px 0;">
            <tr>
                <th>{sep_keyword1}</th>
                <th>{sep_keyword2}</th>
                <th>강남구변기막힘</th>
            </tr>
            <tr>
                <td>{td_text}</td>
                <td>{td_text2}</td>
                <td>{td_text3}</td>
            </tr>
            <tr>
                <td>{td_text4}</td>
                <td>{td_text5}</td>
                <td>{td_text6}</td>
            </tr>
        </table>

        <div class="col-lg-4 mt-5 mt-lg-0">
          



          <!-- Tag Cloud -->
          <div class="mb-5">
            <h2 class="mb-4">Tag</h2>
            <div class="d-flex flex-wrap m-n1">
              <a href="https://gangnamgu.jianhomecare.com" class="btn btn-outline-primary m-1">{sep_keyword1}</a>
              <a href="https://gangnamgu.jianhomecare.com" class="btn btn-outline-primary m-1">{sep_keyword2}</a>
              <a href="https://jianhomecare.com" class="btn btn-outline-primary m-1">강남구변기막힘</a>
            </div>
          </div>

          
        </div>
      </div>
    </div>
    <!-- Detail End -->

     <!-- Footer Start -->
     <div
     class="container-fluid bg-secondary text-white mt-5 py-5 px-sm-3 px-md-5"
   >
     <div class="row pt-5">
       <div class="col-lg-3 col-md-6 mb-5">
         <a
           href=""
           class="navbar-brand font-weight-bold text-primary m-0 mb-4 p-0"
           style="font-size: 40px; line-height: 40px"
         >
           <span class="text-white">{keywords}</span>
         </a>
         <p>
           강남구변기막힘<br>
           100% 해결하는 업체
         </p>
       
       </div>
       
       <div class="col-lg-3 col-md-6 mb-5">
         <h3 class="text-primary mb-4">메뉴</h3>
         <div class="d-flex flex-column justify-content-start">
           <a class="text-white mb-2" href="/"
             ><i class="fa fa-angle-right mr-2"></i>홈</a
           >
          
           <a class="text-white mb-2" href="/서비스"
             ><i class="fa fa-angle-right mr-2"></i>서비스</a
           >
           <a class="text-white mb-2" href="/작업사진"
             ><i class="fa fa-angle-right mr-2"></i>작업사진</a
           >
           <a class="text-white mb-2" href="/블로그"
             ><i class="fa fa-angle-right mr-2"></i>블로그</a
           >
           <a class="text-white" href="tel:010-3463-4474"
             ><i class="fa fa-angle-right mr-2"></i>문의하기</a
           >
         </div>
       
     </div>
     <div
       class="container-fluid pt-5"
       style="border-top: 1px solid rgba(23, 162, 184, 0.2)"
     >
       <p class="m-0 text-center text-white">
         &copy; {keywords}
       </p>
     </div>
   </div>
   <!-- Footer End -->

    
   <a href="tel:010-3463-4474" class="back-to-top"
    ><img src="../img/call.png" width="80px" alt="강남구 변기막힘 상담"></a>


   <!-- JavaScript Libraries -->
   <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
   <script src="../lib/easing/easing.min.js"></script>
   <script src="../lib/owlcarousel/owl.carousel.min.js"></script>
   <script src="../lib/isotope/isotope.pkgd.min.js"></script>
   <script src="../lib/lightbox/js/lightbox.min.js"></script>

   <!-- Template Javascript -->
   <script src="../js/main.js"></script>
 </body>
</html>

"""

# 기본 URL 및 출력 폴더 설정
base_url = "https://gangnamgu.jianhomecare.com/"
output_folder = "output/"

# 출력 폴더 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 엑셀 파일에서 데이터를 읽어옴
keywords, column2_values, column3_values = read_keywords_from_excel("하수구_강남구.xlsx")



def get_n_different_random_values(values_list, n):
    if len(values_list) < n:
        return values_list[:n]  # 값이 n개 미만일 경우 가능한 만큼 반환
    return random.sample(values_list, n)  # 서로 다른 n 개 값을 랜덤으로 선택



def process_keywords(keywords, column2_values, column3_values):
    if not keywords:
        print("No keywords found.")
        return
    
    
    for keyword_string in keywords:
        # 키워드를 쉼표로 분리하여 리스트로 변환
        keyword_list = keyword_string.split(',')
        keyword_list = [keyword.strip() for keyword in keyword_list]

        # 변수에 각각의 키워드 저장
        seperate_keyword1 = keyword_list[0] if len(keyword_list) > 0 else None
        seperate_keyword2 = keyword_list[1] if len(keyword_list) > 1 else None
        seperate_keyword3 = keyword_list[2] if len(keyword_list) > 2 else None

        random_keywords = ["변기막힘", "싱크대막힘", "하수구막힘"]

        # 키워드들을 하이픈으로 연결
        keyword_str = '-'.join(keyword_list)

        # 키워드들을 공백으로 연결
        no_keyword_str = ' '.join(keyword_list)

        random_values = get_n_different_random_values(column2_values, 6)
        random_values2 = get_n_different_random_values(column3_values, 300)
        random_images = get_n_different_random_values(adjusted_images, 22)


        # HTML 콘텐츠 생성
        html_content = html_template.format(
            keywords=no_keyword_str,
            canonical_url=base_url + keyword_str,
            og_title=no_keyword_str,
            og_url=base_url + keyword_str,
            twitter_title=no_keyword_str,
            title=no_keyword_str,
            span_text=no_keyword_str,
            p_text=no_keyword_str,
            h1_text=no_keyword_str,
            alt_text=no_keyword_str,
            a_text=no_keyword_str,
            sep_keyword1=seperate_keyword1,
            sep_keyword2=seperate_keyword2,
            sep_keyword3=seperate_keyword3,
            random_keyword=random.choice(random_keywords),
            image_url=random_images[0],
            image_url2=random_images[1],
            image_url3=random_images[2],
            image_url4=random_images[3],
            image_url5=random_images[4],
            image_url6=random_images[5],
            image_url7=random_images[10],
            td_text=random_values[0],
            td_text2=random_values[1],
            td_text3=random_values[2],
            td_text4=random_values[3],
            td_text5=random_values[4],
            td_text6=random_values[5],
            desc=random.choice(random_values2),
            desc2=random.choice(random_values2),
            desc3=random.choice(random_values2),
            desc4=random.choice(random_values2),
            desc5=random.choice(random_values2),
            desc6=random.choice(random_values2),
            desc7=random.choice(random_values2),
            desc8=random.choice(random_values2),
            desc9=random.choice(random_values2),
            desc10=random.choice(random_values2),
            desc11=random.choice(random_values2),
            desc12=random.choice(random_values2),
            desc13=random.choice(random_values2),
            desc14=random.choice(random_values2),
            desc15=random.choice(random_values2),
            desc16=random.choice(random_values2),
            desc17=random.choice(random_values2),
            desc18=random.choice(random_values2),
            desc19=random.choice(random_values2),
            desc20=random.choice(random_values2),
            desc21=random.choice(random_values2),
            desc22=random.choice(random_values2),
            desc23=random.choice(random_values2),
            desc24=random.choice(random_values2),
            desc25=random.choice(random_values2),
            desc26=random.choice(random_values2),
            desc27=random.choice(random_values2),
            desc28=random.choice(random_values2),
            desc29=random.choice(random_values2),
            desc30=random.choice(random_values2),
            desc31=random.choice(random_values2),
            desc32=random.choice(random_values2),
            desc33=random.choice(random_values2),
            desc34=random.choice(random_values2),
            desc35=random.choice(random_values2),
            desc36=random.choice(random_values2),
            desc37=random.choice(random_values2),
            desc38=random.choice(random_values2),
            desc39=random.choice(random_values2),
            desc40=random.choice(random_values2),
            desc41=random.choice(random_values2),
            desc42=random.choice(random_values2),
            desc43=random.choice(random_values2),
            desc44=random.choice(random_values2),
            desc45=random.choice(random_values2),
            desc46=random.choice(random_values2),
            desc47=random.choice(random_values2),
            desc48=random.choice(random_values2),
            desc49=random.choice(random_values2),
            desc50=random.choice(random_values2),
            desc51=random.choice(random_values2),
            desc52=random.choice(random_values2),
            # image_url=selected_image_path
        )
        
        # HTML 파일명 생성
        output_filename = f"{keyword_str}.html"
        
        # 파일 저장
        try:
            with open(os.path.join(output_folder, output_filename), 'w', encoding='utf-8') as file:
                file.write(html_content)
        except Exception as e:
            print(f"Error saving HTML file: {e}")

# HTML 파일 생성 및 랜덤 값 출력
process_keywords(keywords, column2_values, column3_values)

print(f'HTML 파일이 {output_folder} 폴더에 저장되었습니다.')