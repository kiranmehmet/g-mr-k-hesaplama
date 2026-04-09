# HTS Parser v1 — Pipeline

## Amaç
Raw HTS verisini deterministic şekilde parse ederek structured duty component üretmek.

---

## STEP 001 — BASE PARSE

Kaynak:
hts_2026_raw

Yapılanlar:
- htsno → code
- hs_numeric üretildi
- hs6 üretildi
- raw kolonlar korundu

Output:
hts_parsed_v1

---

## STEP 001.1 — CODE VALIDATION

Yapılanlar:
- geçerli HTS code flag’i eklendi

Kolon:
is_valid_code

Output:
hts_parsed_v1_1

---

## STEP 002 — SPLIT

Yapılanlar:
- general_raw → general_parts
- "+" üzerinden parçalama

Output:
hts_parsed_v2

---

## STEP 003 — CLASSIFICATION

Yapılanlar:
- percent (%)
- specific (¢ / $)
- free
- text

Component JSON üretildi

Output:
hts_parsed_v3

---

## STEP 003.1 — NULL FIX

Yapılanlar:
- NULL raw için component üretimi engellendi

Output:
hts_parsed_v3_2

---

## STEP 004 — UNIT EXTRACTION

Yapılanlar:
- kg, liter, each, head gibi unitler çıkarıldı

Output:
hts_parsed_v4

---

## STEP 005 — ORDER FIX

Yapılanlar:
- component sırası korundu (WITH ORDINALITY)

Output:
hts_parsed_v5

---

## STEP 006 — ADVANCED PARSE

Yapılanlar:
- pf liter
- per X
- divisor
- multi-word unit

Output:
hts_parsed_v6

---

## STEP 006.1 — PF LITER FIX

Yapılanlar:
- "pf.liter" gibi formatlar düzeltildi

Output:
hts_parsed_v6_1

---

## FINAL OUTPUT

hts_parsed_v6_1

---

## Parser Scope

Parser sadece:
- extraction yapar
- classification yapar

Parser şunları yapmaz:
- calculation
- unit conversion
- threshold logic
- parametric logic

---

## Next Step

ENGINE layer:
- duty calculation
- unit conversion
- total duty
- landed cost
