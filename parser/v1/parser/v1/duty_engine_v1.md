FILE NAME:
HTS_DETERMINISTIC_ENGINE.md

---

# HTS DUTY ENGINE – DETERMINISTIC ARCHITECTURE

## 🎯 PURPOSE

This system builds a **deterministic import duty engine** based on U.S. HTS data.

The engine:

* Parses HTS duty structures (percent + specific)
* Integrates Chapter 99 (Section 301, additional duties)
* Produces **final_total_duty**
* Avoids any probabilistic or AI-based inference

---

## ⚠️ CORE PRINCIPLE (LOCKED)

> This system is **100% deterministic**

* No guessing
* No AI interpretation
* No fuzzy matching
* Only rule-based parsing and official data

---

## 🧱 DATA LAYERS

### 1. RAW LAYER (SOURCE OF TRUTH)

Table: `hts_final_v2`

* Direct import from official HTS dataset
* ~35,000 rows
* NEVER modified

Columns:

* code
* description
* general_raw
* special_raw
* other_raw
* level

---

### 2. PARSED DUTY LAYER

Derived fields:

* percent_duty (ad valorem)
* specific_duty (per unit)

Examples:

| general_raw | percent_duty | specific_duty |
| ----------- | ------------ | ------------- |
| 6.8%        | 6.8          | NULL          |
| 1¢/kg       | NULL         | 1.00          |
| 0.9¢ each   | NULL         | 0.90          |

---

### 3. ENGINE TABLE

Table: `hts_engine_prod_v1`

This is the **calculation layer (NOT raw data)**

Columns:

* code
* percent_duty
* specific_duty
* extra_percent
* requires_base
* base_total_duty
* final_total_duty
* calculation_status

---

## ⚙️ CALCULATION LOGIC

### BASE DUTY

```text
IF percent_duty exists → use percent_duty
ELSE IF specific_duty exists → use specific_duty
ELSE → 0
```

---

### CHAPTER 99 (ADDITIONAL DUTY)

Parsed from:

```text
"The duty provided in the applicable subheading + 25%"
```

Extracted fields:

* extra_percent
* requires_base

---

## 🔗 CHAPTER 99 MAPPING

Table: `chapter99_map_v3`

Columns:

* chapter99_code
* hts_code
* extra_percent

---

## 🧠 MATCHING STRATEGY (CRITICAL)

### Problem:

One HTS code can match multiple Chapter 99 rules:

```text
0101.29.00.10 matches:
- 0101
- 0101.29.00
- 0101.29.00.10
```

---

### Solution:

**Longest Prefix Match**

```sql
ORDER BY LENGTH(hts_code) DESC
LIMIT 1
```

---

### Matching Rule:

```sql
REPLACE(e.code, '.', '') 
LIKE REPLACE(c.hts_code, '.', '') || '%'
```

---

## 🚫 IMPORTANT DESIGN RULE

NO UPDATE-based logic

✔ Calculations are done via SELECT
✔ Engine is stateless
✔ No mutation of core data

---

## 📊 FINAL DUTY FORMULA

```text
final_total_duty = base_total_duty * (1 + extra_percent / 100)
```

Example:

```text
base = 68
extra = 25%

final = 68 * 1.25 = 85
```

---

## 🚨 CURRENT LIMITATION

Coverage:

```text
matched: 94
total: 28620
coverage: 0.33%
```

---

### Root Cause:

* Chapter 99 mapping incomplete
* HS6 / HS4 fallback missing
* Data issue, not engine issue

---

## 🔜 NEXT STEPS

* HS6 mapping layer
* Fallback hierarchy (HS6 → HS4 → HS2)
* Country-based logic (China / Section 301)
* Full coverage expansion

---

## 🧾 DISCLAIMER

All calculations are based on:

* Official HTS data
* Deterministic rules

No generative AI or probabilistic logic is used.

---

## 🧠 SUMMARY

✔ Engine logic complete
✔ Deterministic system established
❗ Remaining problem: DATA COVERAGE

---
