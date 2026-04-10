FILE NAME:
HTS_FULL_SYSTEM_STATUS.md

---

# HTS DUTY ENGINE — FULL SYSTEM STATUS

## 🎯 PURPOSE

Build a **deterministic import duty engine** using:

* HTS (01–97)
* Section 301 (China tariffs)
* Chapter 99 (additional duty rules)

---

# 🧱 SYSTEM ARCHITECTURE

```text
HTS RAW → PARSER → STRUCTURED HTS
                 ↓
            SECTION 301
                 ↓
            CHAPTER 99
                 ↓
         RULE EXTRACTION
                 ↓
         (NEXT: CALCULATION ENGINE)
```

---

# ✅ COMPLETED (CONFIRMED WORKING)

---

## 1. HTS PARSER PIPELINE (V1)

Final Table:
`hts_parsed_v6_1`

### Steps Completed:

```text
001_base_parse
001.1_code_validation
002_split
003_classification
003.1_null_fix
004_unit_extraction
005_order_fix
006_advanced_parse
006.1_pf_liter_fix
```

---

## 2. PARSER CAPABILITIES

### ✔ Supported Types

* Percent (ad valorem)
* Specific ($ / ¢)
* Mixed duty
* Multi-component
* Free

---

### ✔ Unit Coverage

* kg, g, lb
* liter
* each / unit / no
* head
* dozen / pair / set
* case
* pf liter

---

### ✔ Advanced Support

* per X (per 100kg, etc)
* divisor logic
* multi-word units
* order preservation

---

### ✔ Output Format

```json
[
  { "type": "specific", "value": 1.104, "unit": "kg" },
  { "type": "percent", "value": 14.9 }
]
```

---

### ❗ Parser Scope

Parser ONLY:

* extraction
* classification

Parser DOES NOT:

* calculation
* unit conversion
* threshold logic
* parametric logic

---

## 3. SECTION 301 INTEGRATION

Table: `section_301`

### ✔ What works

* Official dataset used
* hts8 → chapter99 mapping exists
* Direct join established

### ✔ Critical Fix

```text
HTS10 → normalize → HTS8 → join
```

---

## 4. CHAPTER 99 CONNECTION

Table: `chapter_99_raw`

### ✔ What works

* chapter99 linked successfully
* general_raw pulled
* description available

---

## 5. RULE CLASSIFICATION (CHAPTER 99)

### ✔ Types Detected

* percent_only → "25%"
* parametric → "base + X%"
* mixed → contains "+"
* text_rule → fallback

---

## 6. PERCENT EXTRACTION

### ✔ Implemented

```text
"The duty provided ... + 7.5%"
→ 7.5
```

✔ Regex extraction works
✔ Numeric value ready

---

## 7. STRUCTURE LAYER

Single query provides:

* HTS base duty
* Section 301 mapping
* Chapter 99 rule
* Rule type
* Extracted percent

---

# ❌ NOT COMPLETED (REAL GAPS)

---

## 1. BASE DUTY → NUMERIC

❌ general_raw not converted to numeric

Examples:

```text
68¢/head
0.9¢ each
```

---

## 2. SPECIFIC DUTY ENGINE

❌ no unit normalization
❌ no quantity handling

---

## 3. FINAL CALCULATION

❌ no final_total_duty

---

## 4. PARAMETRIC EXECUTION

✔ detection exists
❌ execution missing

---

## 5. MULTI-COMPONENT RESOLUTION

✔ parsed
❌ not combined

---

## 6. TEXT RULE HANDLING

❌ not resolved
❌ no flag system

---

# ⚠️ WRONG / DEAD APPROACHES (LOCKED OUT)

* ❌ Parsing Chapter 99 descriptions for mapping
* ❌ Direct HTS ↔ Chapter99 join attempts
* ❌ Assuming mapping missing
* ❌ UPDATE-based system logic

---

# 🔴 CORE TRUTHS (LOCKED)

---

## 1.

> Section 301 = mapping layer

---

## 2.

> Chapter 99 = rule layer (NOT numeric)

---

## 3.

> Duty model:

```text
base duty + additional rule
```

---

## 4.

> System is NOT a flat % engine

---

# 🎯 NEXT PHASE (ENGINE)

---

## Step 1

Base duty → numeric extraction

---

## Step 2

Unit normalization layer

---

## Step 3

Deterministic calculation engine

---

## Step 4

Total duty output

---

# 🧠 FINAL STATUS

---

✔ Parser → DONE
✔ Mapping → DONE
✔ Section 301 → DONE
✔ Chapter 99 → DONE
✔ Classification → DONE
✔ Extraction → DONE

---

❗ Remaining:

> Calculation Engine

---

# 🧾 DISCLAIMER

All logic:

* uses official HTS data
* is deterministic
* contains no AI inference

---
