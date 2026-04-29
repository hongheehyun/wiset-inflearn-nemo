---
marp: true
theme: default
paginate: true
header: "NemoApp 상가 데이터 분석 보고서 (Risograph Style)"
footer: "© 2026 NemoApp Data Analysis Team"
backgroundColor: #F7F2E8
style: |
  section {
    font-family: 'Space Mono', 'Apple SD Gothic Neo', sans-serif;
    color: #2D2D2D;
    background-color: #F7F2E8;
    background-image: url('https://www.transparenttextures.com/patterns/paper-fibers.png');
    padding: 50px;
  }
  h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 80px;
    letter-spacing: 4px;
    color: #E8344A;
    text-shadow: 4px 4px 0px rgba(13, 92, 158, 0.3);
    text-transform: uppercase;
    margin-bottom: 0px;
  }
  h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 45px;
    color: #0D5C9E;
    border-bottom: 3px dashed #F5D020;
    padding-bottom: 10px;
    margin-bottom: 30px;
  }
  .card {
    background-color: rgba(255, 255, 255, 0.5);
    border: 1px solid #2D2D2D;
    padding: 20px;
    mix-blend-mode: multiply;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    mix-blend-mode: multiply;
  }
  th {
    background-color: #F5D020;
    color: #2D2D2D;
    padding: 10px;
  }
  td {
    border-bottom: 1px solid #0D5C9E;
    padding: 10px;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2rem;
  }
  img {
    filter: sepia(0.2) contrast(1.1) brightness(0.9);
    mix-blend-mode: multiply;
    border: 1px solid #2D2D2D;
  }
  blockquote {
    border-left: 5px solid #E8344A;
    padding-left: 20px;
    font-style: italic;
    color: #E8344A;
  }
---

# NEMOAPP REPORT
### ANALOG DATA INSIGHTS

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
<div>

![w:400](images/viz1_deposit_dist.png)
**DEPOSIT**: PEAK AT 30M-50M
</div>
<div>

![w:400](images/viz2_rent_dist.png)
**RENT**: PEAK AT 2M-3M
</div>
</div>

---

## 4. SIZE VS RENT

<div class="columns">
<div>

![w:400](images/viz3_size_vs_rent.png)
**CORRELATION**: STRONG LINEAR RELATION
</div>
<div>

![w:400](images/viz4_cat_large_freq.png)
**CATEGORY**: F&B DOMINANT
</div>
</div>

---

## 5. FLOOR PREMIUM

<div class="columns">
<div>

![w:400](images/viz5_floor_vs_rent.png)
**FLOOR**: 1ST FLOOR PREMIUM IS HUGE
</div>
<div>

![w:400](images/viz6_dep_vs_rent.png)
**RELATION**: 0.948 (VERY STRONG)
</div>
</div>

---

## 6. EFFICIENCY

<div class="columns">
<div>

![w:400](images/viz7_area_price_dist.png)
**VALUE**: CONCENTRATED AT 125 MARK
</div>
<div>

![w:400](images/viz9_maint_vs_rent.png)
**MAINT**: HIDDEN COST ALERT
</div>
</div>

---

## 7. PREMIUM ANALYSIS

<div class="columns">
<div>

![w:350](images/viz10_premium_pie.png)
**PREMIUM**: 54% NO PREMIUM
</div>
<div>

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
