# HTS Duty Parser v1

## Amaç
HTS duty stringlerini structured JSON component’lere çevirmek.

---

## Ne Yapar

Parser aşağıdaki duty tiplerini tanır:

- Percent (ad valorem)
- Specific ($ / ¢)
- Mixed duty (örn: 57¢/kg + 1.4%)
- Multi-component duty
- Free

---

## Unit Coverage

Parser aşağıdaki unitleri tanır:

- kg, g, lb
- liter, l
- each, unit, no.
- head
- dozen
- gross
- pair
- set
- case
- pf liter (proof liter)

---

## Advanced Support

- per X (örn: per 100 kg)
- divisor (per 100, per 1000)
- multi-word units (pf liter)
- order preservation

---

## Output Format

Her duty şu formatta döner:

[
  { "type": "specific", "value": 1.104, "unit": "kg" },
  { "type": "percent", "value": 14.9 }
]

---

## Önemli Kurallar

- Calculation yapılmaz
- Unit conversion yapılmaz
- Condition logic çözülmez
- Chapter 99 burada işlenmez

Bunların hepsi engine katmanında yapılır.

---

## Pipeline

001_base_parse  
002_split  
003_classification  
004_unit_extraction  
005_order_fix  
006_advanced_units  

---

## Sonuç

Final tablo:

hts_parsed_v6_1

---

## Not

Bu parser production-ready v1 seviyesindedir.

Geri kalan logic engine katmanında çözülecektir.
