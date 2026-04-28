# Nemo Insight - 상권 분석 대시보드

네모(Nemo) 앱 데이터를 활용한 역삼역 주변 상권 분석 프로젝트입니다.

## 주요 기능
- **실시간 대시보드**: 월세 구간별 분포, 자본 투입 규모, 업종별 구성, 층수별 임대 가치 시각화
- **전략적 리포트**: 20년차 데이터 분석가 관점의 상권 생존 및 성장 전략 제언
- **데이터 파이프라인**: 네모 API를 통한 데이터 수집 및 자동 가공

## 기술 스택
- **Frontend**: HTML5, CSS3, JavaScript (Chart.js)
- **Backend/Data**: Python (Pandas, SQLite, Scikit-learn)
- **Deployment**: GitHub Pages

## 프로젝트 구조
- `index.html`: 메인 대시보드 페이지
- `dashboard_data.json`: 시각화용 가공 데이터
- `nemo_eda_report.md`: 상세 EDA 분석 리포트
- `src/`: 데이터 수집 및 분석 스크립트
- `docs/`: 프로젝트 관련 문서 및 프롬프트

## 분석 결과 요약
- **분석 데이터**: 역삼역 반경 1km 이내 매물 698개
- **주요 발견**: 전체 매물의 54.2%가 '무권리' 상태로, 공격적인 방어 전략이 필요한 시장 상황임을 확인.
