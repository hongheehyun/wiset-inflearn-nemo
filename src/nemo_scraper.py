import requests
import sqlite3
import json
import os
import time

def scrape_nemo():
    # 1. 설정 및 경로 준비
    base_url = "https://www.nemoapp.kr/api/store/search-list"
    params = {
        "Subway": "222",
        "Radius": "1000",
        "CompletedOnly": "false",
        "NELat": "37.51140055648316",
        "NELng": "127.03456544361883",
        "SWLat": "37.498879807111344",
        "SWLng": "127.02080817937446",
        "Zoom": "15",
        "SortBy": "29",
        "PageIndex": 0
    }
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }
    
    data_dir = "data"
    db_path = os.path.join(data_dir, "nemo_stores.db")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    total_count = 0
    page = 0
    table_created = False

    while True:
        params["PageIndex"] = page
        print(f"페이지 {page} 수집 중...")
        
        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(f"페이지 {page} 요청 실패: {e}")
            break

        items = data.get("items", [])
        if not items:
            print(f"페이지 {page}에 데이터가 없습니다. 수집을 종료합니다.")
            break

        print(f"페이지 {page}: {len(items)}개의 아이템 발견")

        # 테이블 스키마 동적 생성 (최초 1회)
        if not table_created:
            sample_item = items[0]
            columns = []
            for key, value in sample_item.items():
                if isinstance(value, int):
                    col_type = "INTEGER"
                elif isinstance(value, float):
                    col_type = "REAL"
                else:
                    col_type = "TEXT"
                columns.append(f'"{key}" {col_type}')

            column_defs = ", ".join(columns)
            cursor.execute(f"CREATE TABLE IF NOT EXISTS stores ({column_defs})")
            table_created = True
            
            # 삽입 쿼리 미리 준비
            keys = list(sample_item.keys())
            col_names = ", ".join([f'"{k}"' for k in keys])
            placeholders = ", ".join(["?" for _ in keys])
            insert_query = f"INSERT INTO stores ({col_names}) VALUES ({placeholders})"

        # 데이터 삽입
        for item in items:
            values = []
            for key in keys:
                val = item.get(key)
                if isinstance(val, (list, dict)):
                    val = json.dumps(val, ensure_ascii=False)
                values.append(val)
            
            try:
                cursor.execute(insert_query, values)
                total_count += 1
            except Exception as e:
                print(f"데이터 삽입 오류 (ID: {item.get('id')}): {e}")

        conn.commit()
        page += 1
        time.sleep(1)  # 서버 부하 방지를 위한 지연

    conn.close()
    print(f"총 {total_count}개의 데이터를 {db_path}에 저장했습니다.")

if __name__ == "__main__":
    scrape_nemo()
