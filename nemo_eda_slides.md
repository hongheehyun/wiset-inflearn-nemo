---
marp: true
theme: default
paginate: true
header: "NemoApp 상가 데이터 분석 보고서 (EDA)"
footer: "© 2026 NemoApp Data Analysis Team"
backgroundColor: #ffffff
style: |
  section {
    font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
  }
  h1 {
    color: #2c3e50;
  }
  h2 {
    color: #34495e;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# NemoApp 상가 데이터 분석 보고서
### 20년차 데이터 분석가의 전문 EDA 리포트

**발표자:** Gemini CLI
**날짜:** 2026년 4월 29일

---

## 1. 데이터 탐색 개요

- **전체 데이터 수**: 698행
- **전체 변수 수**: 40개
- **주요 변수**: 보증금, 월세, 관리비, 면적, 권리금, 업종, 지하철역 거리 등
- **데이터 특징**: 서울 강남(역삼역) 상권에 고도로 집중된 데이터셋

---

## 2. 수치형 데이터 기술 통계

| 지표 | 보증금 (deposit) | 월세 (monthlyRent) | 면적 (size) |
| :--- | :--- | :--- | :--- |
| **평균** | 약 6,764만 원 | 약 525만 원 | 126.8 ㎡ |
| **중위값** | 4,000만 원 | 330만 원 | 100.0 ㎡ |
| **최대값** | 10.8억 원 | 9,000만 원 | 1,225 ㎡ |

> **분석 의견**: 매물 간 격차가 매우 큰 양극화 시장 (Right-skewed 분포)

---

## 3. 보증금 및 월세 분포 분석

<div class="columns">
<div>

![w:450](images/viz1_deposit_dist.png)
**보증금**: 3,000~5,000만 원 구간 집중
</div>
<div>

![w:450](images/viz2_rent_dist.png)
**월세**: 200~300만 원 정점 (소형 상가 중심)
</div>
</div>

---

## 4. 면적 vs 월세 및 업종 분석

<div class="columns">
<div>

![w:450](images/viz3_size_vs_rent.png)
**상관계수**: 선형적 관계 확인
</div>
<div>

![w:450](images/viz4_cat_large_freq.png)
**업종**: 기타업종 및 F&B(음식점) 압도적
</div>
</div>

---

## 5. 층수 및 보증금-월세 상관성

<div class="columns">
<div>

![w:450](images/viz5_floor_vs_rent.png)
**층수**: 1층 임대료 압도적 (가시성 프리미엄)
</div>
<div>

![w:450](images/viz6_dep_vs_rent.png)
**상관성**: 0.948 (매우 강한 양의 상관관계)
</div>
</div>

---

## 6. 단위 면적당 효율 및 고정비 분석

<div class="columns">
<div>

![w:450](images/viz7_area_price_dist.png)
**가성비**: 특정 가격대(125) 밀집
</div>
<div>

![w:450](images/viz9_maint_vs_rent.png)
**관리비**: 층수/빌딩 규모별 '숨은 월세' 주의
</div>
</div>

---

## 7. 권리금 및 키워드 분석

<div class="columns">
<div>

![w:400](images/viz10_premium_pie.png)
**권리금**: 무권리(54%) 비중 높음 (시장 변화 시사)
</div>
<div>

![w:500](images/viz11_tfidf_keywords.png)
**키워드**: 무권리, 역세권, 대로변 등 마케팅 포인트
</div>
</div>

---

## 8. 종합 비즈니스 인사이트 (1)

### 🚀 공간 전략의 전환 (목적형 소비 공략)
- 1층의 살인적인 임대료 대신 **2층 이상/지하** 매물 활용
- 절감된 고정비를 **디지털 마케팅 및 인테리어**에 재투자
- SNS 기반 목적형 방문 고객 유도로 수익성 극대화

---

## 9. 종합 비즈니스 인사이트 (2)

### 💡 하이브리드 모델 도입
- 오피스 상권의 한계(특정 시간 집중)를 극복하기 위한 **Day & Night 믹스**
- 낮(브런치/카페) + 밤(와인바/펍) 형태의 공간 가동률 극대화

### ⚠️ 숨은 고정비(관리비) 통제
- 관리비 포함 **'총 고정비용'** 기준의 보수적 재무 계획 필수

---

## 10. 결론: 데이터 기반 의사결정

- "감"이 아닌 **"데이터"**에 기반한 입지 선정
- 무권리 매물의 함정(상권 쇠퇴 여부) 현장 검증 필수
- 역삼 상권의 양극화를 기회로 삼는 **타겟 맞춤형 전략** 수립

# 감사합니다!
