import base64
import os
import re

# index.html 경로
html_path = 'index.html'
# 이미지 폴더 경로
images_dir = 'images'

def embed_images(html_content):
    # images/ 폴더의 모든 파일 목록 가져오기
    image_files = os.listdir(images_dir)
    
    for filename in image_files:
        if filename.endswith('.png'):
            img_path = os.path.join(images_dir, filename)
            with open(img_path, 'rb') as img_file:
                # 이미지를 base64로 인코딩
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                data_url = f'data:image/png;base64,{encoded_string}'
                
                # HTML 내의 이미지 경로를 data URL로 치환
                # Marp가 생성한 HTML에서 &quot;images/filename&quot; 또는 images/filename 형태를 찾음
                pattern = re.compile(re.escape(f'images/{filename}'))
                html_content = pattern.sub(data_url, html_content)
                
                # HTML 이스케이프된 경로(&quot;images/filename&quot;)도 처리
                escaped_pattern = re.compile(re.escape(f'images/{filename}'))
                html_content = escaped_pattern.sub(data_url, html_content)
                
    return html_content

if __name__ == '__main__':
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = embed_images(content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully embedded images into {html_path}")
