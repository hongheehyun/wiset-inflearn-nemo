---
marp: true
theme: default
paginate: true
header: "NemoApp 상가 데이터 분석 보고서 (Neo-Brutalism)"
footer: "© 2026 NemoApp Data Analysis Team"
backgroundColor: #F5F500
style: |
  section {
    font-family: 'Space Mono', 'Courier New', 'Apple SD Gothic Neo', sans-serif;
    color: #000000;
    padding: 40px;
    border: 5px solid #000000;
    box-shadow: 15px 15px 0px 0px #000000;
    margin: 20px;
  }
  h1 {
    font-family: 'Impact', 'Arial Black', sans-serif;
    color: #000000;
    font-size: 70px;
    text-transform: uppercase;
    background-color: #FFFFFF;
    border: 4px solid #000000;
    padding: 20px;
    box-shadow: 10px 10px 0px 0px #000000;
    display: inline-block;
  }
  h2 {
    font-family: 'Impact', sans-serif;
    color: #000000;
    font-size: 45px;
    background-color: #CCFF00;
    border: 3px solid #000000;
    padding: 10px 20px;
    box-shadow: 8px 8px 0px 0px #000000;
    display: inline-block;
    margin-bottom: 30px;
  }
  table {
    border: 4px solid #000000;
    border-collapse: collapse;
    background-color: #FFFFFF;
    box-shadow: 10px 10px 0px 0px #000000;
  }
  th, td {
    border: 2px solid #000000;
    padding: 15px;
  }
  th {
    background-color: #FF2D55;
    color: #FFFFFF;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2rem;
  }
  .card {
    background-color: #FFFFFF;
    border: 3px solid #000000;
    padding: 15px;
    box-shadow: 8px 8px 0px 0px #000000;
  }
  blockquote {
    background-color: #0000FF;
    color: #FFFFFF;
    border: 3px solid #000000;
    padding: 15px;
    box-shadow: 8px 8px 0px 0px #000000;
    margin-top: 20px;
  }
---

# NEMOAPP REPORT
### EXPERT EDA REPORT

**SPEAKER:** GEMINI CLI
**DATE:** 2026-04-29

---

## 1. DATA OVERVIEW

<div class="card">

- **TOTAL ROWS**: 698
- **TOTAL COLUMNS**: 40
- **MAIN VARS**: DEPOSIT, RENT, SIZE, PREMIUM
- **TARGET AREA**: GANGNAM(YEOKSAM)
</div>

---

## 2. KEY STATISTICS

| METRIC | DEPOSIT | RENT | SIZE |
| :--- | :--- | :--- | :--- |
| **AVERAGE** | 67.6M KRW | 5.25M KRW | 126.8 ㎡ |
| **MEDIAN** | 40.0M KRW | 3.30M KRW | 100.0 ㎡ |
| **MAX** | 1.08B KRW | 90.0M KRW | 1,225 ㎡ |

> **INSIGHT**: EXTREME MARKET POLARIZATION DETECTED.

---

## 3. DISTRIBUTION

<div class="columns">
<div class="card">

![w:400](images/viz1_deposit_dist.png)
**DEPOSIT**: PEAK AT 30M-50M
</div>
<div class="card">

![w:400](images/viz2_rent_dist.png)
**RENT**: PEAK AT 2M-3M
</div>
</div>

---

## 4. SIZE VS RENT

<div class="columns">
<div class="card">

![w:400](images/viz3_size_vs_rent.png)
**CORRELATION**: STRONG LINEAR RELATION
</div>
<div class="card">

![w:400](images/viz4_cat_large_freq.png)
**CATEGORY**: F&B DOMINANT
</div>
</div>

---

## 5. FLOOR PREMIUM

<div class="columns">
<div class="card">

![w:400](images/viz5_floor_vs_rent.png)
**FLOOR**: 1ST FLOOR PREMIUM IS HUGE
</div>
<div class="card">

![w:400](images/viz6_dep_vs_rent.png)
**RELATION**: 0.948 (VERY STRONG)
</div>
</div>

---

## 6. EFFICIENCY

<div class="columns">
<div class="card">

![w:400](images/viz7_area_price_dist.png)
**VALUE**: CONCENTRATED AT 125 MARK
</div>
<div class="card">

![w:400](images/viz9_maint_vs_rent.png)
**MAINT**: HIDDEN COST ALERT
</div>
</div>

---

## 7. PREMIUM ANALYSIS

<div class="columns">
<div class="card">

![w:350](images/viz10_premium_pie.png)
**PREMIUM**: 54% NO PREMIUM
</div>
<div class="card">

![w:450](images/viz11_tfidf_keywords.png)
**KEYWORDS**: STATION-AREA, MAIN ROAD
</div>
</div>

---

## 8. STRATEGY (1)

### SPACE STRATEGY
<div class="card">

- USE **UPPER FLOORS / BASEMENT**
- REINVEST SAVED RENT INTO **DIGITAL MARKETING**
- TARGET CUSTOMERS VIA **SNS & INTERIOR**
</div>

---

## 9. STRATEGY (2)

### HYBRID MODEL
<div class="card">

- OFFICE DISTRICT LIMITATION -> **DAY & NIGHT MIX**
- CAFE(DAY) + PUB(NIGHT)
</div>

### FIXED COST
<div class="card">

- CONTROL **TOTAL FIXED COST** INCLUDING MAINT.
</div>

---

## 10. CONCLUSION

<div class="card">

- **DATA-DRIVEN** DECISION MAKING
- VERIFY **NO PREMIUM** TRAPS
- TARGETED STRATEGY FOR **YEOKSAM MARKET**
</div>

# THANK YOU!
