# HTS Deterministic Duty Engine — Status & Handoff

## 🎯 PURPOSE

Build a **fully deterministic import duty engine** using U.S. HTS data.

**Rules:**

* ❌ No DELETE
* ❌ No UPDATE
* ❌ No OVERWRITE of raw data
* ✔ Read-only / SELECT-based logic
* ✔ 100% rule-based (no AI guessing)

---

## 🧱 DATA LAYERS

### 1. RAW (SOURCE OF TRUTH)

* `hts_2026_raw` → official HTS dataset (~35k rows)
* `chapter_99_raw` → official Chapter 99 dataset

👉 NEVER modified

---

### 2. WORKING TABLE

* `hts_final_v2`
* cleaned / structured HTS copy (still no destructive ops)

---

### 3. PARSE LAYER

* `hts_parsed_v6_1`

✔ duty parsed into JSON components:

```json
[
  { "type": "percent", "value": 6.8 },
  { "type": "specific", "value": 1.2, "unit": "kg" }
]
```

✔ supports:

* percent
* specific
* mixed
* multi-component
* units (kg, liter, dozen, pf liter, etc.)

❗ no calculation here

---

## ⚙️ ENGINE (WORKING)

### ✔ BASE DUTY

From parsed components:

* percent → value-based
* specific → quantity-based

---

### ✔ CHAPTER 99 (TEMP SOLUTION)

* using: `v_ch99_resolved_full`
* logic:

  * exact match
  * prefix match
  * HS6 fallback

✔ works but LIMITED

---

### ✔ CHINA (SECTION 301)

```text
if country = china → apply extra_percent
```

---

### ✔ MPF (CONFIRMED CBP)

```text
rate: 0.003464
min: 33.58
max: 651.50
base: product value only
```

---

### ✔ HMF (CONFIRMED CBP)

```text
rate: 0.00125
only if transport_mode = ocean
```

---

## 🧮 FINAL ENGINE FUNCTION

`fn_landed_cost(...)`

Inputs:

* code
* value
* quantity
* country
* mode (ocean/air)

Outputs:

* base_duty
* extra_percent
* duty_total
* mpf
* hmf
* total_landed_cost

✔ FULLY WORKING

---

## 📊 CURRENT STATUS

| Component   | Status |
| ----------- | ------ |
| HTS Parse   | ✅ DONE |
| Base Duty   | ✅ DONE |
| China Logic | ✅ DONE |
| MPF         | ✅ DONE |
| HMF         | ✅ DONE |
| Landed Cost | ✅ DONE |

---

## 🚨 CURRENT BLOCKER

### ❌ CHAPTER 99 COVERAGE

```text
coverage ≈ 0.3%
```

### ROOT CAUSE:

Current system:

```text
hts_code → chapter99_code mapping
```

BUT real Chapter 99:

```text
RULE-BASED (NOT DIRECT MAPPING)
```

Examples:

* "applies to goods of headings 0101–0106"
* "products of China"
* "except ..."

````

---

## ❗ PROBLEM TYPE

```text
NOT SQL problem
NOT engine problem

→ DATA MODEL problem
````

---

## 🎯 REQUIRED FIX

### NEW MODEL:

Create:

```text
chapter99_rules_v1
```

Columns:

* chapter99_code
* extra_percent
* country
* hs_from
* hs_to
* exclusion_text

---

## 🚀 NEXT STEPS

### STEP 1

Parse Chapter 99 raw:

* extract % (e.g. +25%)
* extract country (china)

### STEP 2

Extract HS ranges:

* "0101–0106" → hs_from / hs_to

### STEP 3

Replace matching logic:

```sql
hs6 BETWEEN hs_from AND hs_to
```

---

## 💡 KEY INSIGHT

```text
HTS = structured
Chapter 99 = text rules
```

---

## 🧠 SUMMARY

✔ Engine logic is correct
✔ Calculations are correct
✔ System is deterministic

❗ Only missing piece:

```text
REAL Chapter 99 rule parsing
```

---

## 🔒 FINAL PRINCIPLE

> "We do not fix data with SQL tricks.
> We fix the model and let deterministic logic work."

---
