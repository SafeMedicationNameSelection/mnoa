# Test Case 1: Detailed Output Logs

This file contains the complete, detailed output from running the `Test 1.txt` dataset through the MNOA tool.

---

## Final Cleaned List (43 Names)
!fluticasone
#fluticasone#
(ferrous sulfate)
heparin sodium
123hyzaar4
<heparin><sodium>
[ezetimibe]
advair
aug mentin
benicar
conjugated estrogens
ethinyl estradiol
ezetimibe
ezetimibe[]
ezetimibe{}
famotidine
fenofibrate
fent-anyl
ferrous sulfate
ferrous"sulfate"
ferrous'sulfate'
ferrous,sulfate
ferrous-sulfate
ferrous:sulfate
ferrous;sulfate
ferrous_sulfate
ferrous~sulfate
fioricet
fioricet()
fluticasone propionate
fluticasone@propionate
heparin sodium
heparin&&sodium
heparin.sodium
heparin/sodium
heparin\sodium
heparin^sodium
heparinsodium&
heparin|sodium
hyzaar
lotrisone
night time
{exetimibe}


---

## Round by Round Stats

| Round | Characters | Unresolved | Disambiguated | KPraw | %KP    |
|-------|------------|------------|---------------|-------|--------|
| 1     | 16         | 31         | 12            | 15    | 34.88% |
| 2     | 10         | 26         | 17            | 6     | 13.95% |
| 3     | 6          | 26         | 17            | 1     | 2.33%  |
| 4     | 7          | 24         | 19            | 1     | 2.33%  |
| 5     | 5          | 24         | 19            | 0     | 0.00%  |
| 6     | 5          | 24         | 19            | 0     | 0.00%  |
| 7     | 5          | 24         | 19            | 0     | 0.00%  |
| 8     | 20         | 7          | 36            | 15    | 34.88% |
| 9     | 3          | 5          | 37            | 1     | 2.33%  |
| 10    | 3          | 2          | 39            | 2     | 4.65%  |
| 11    | 1          | 2          | 39            | 0     | 0.00%  |
| 12    | 2          | 0          | 41            | 1     | 2.33%  |

---

## All Overlaps by Round

### Round 1
- Prefix "!" resolved: !fluticasone
- Prefix "#" resolved: #fluticasone#
- Prefix "(" resolved: (ferrous sulfate)
- Prefix "*" resolved: **heparin sodium**
- Prefix "1" resolved: 123hyzaar4
- Prefix "<" resolved: <heparin><sodium>
- Prefix "[" resolved: [ezetimibe]
- Prefix "a" matched multiple: advair, aug mentin
- Prefix "b" resolved: benicar
- Prefix "c" resolved: conjugated estrogens
- Prefix "e" matched multiple: ethinyl estradiol, ezetimibe, ezetimibe[], ezetimibe{}
- Prefix "f" matched multiple: famotidine, fenofibrate, fent-anyl, ferrous sulfate, ferrous"sulfate", ferrous'sulfate', ferrous,sulfate, ferrous-sulfate, ferrous:sulfate, ferrous;sulfate, ferrous_sulfate, ferrous~sulfate, fioricet, fioricet(), fluticasone propionate, fluticasone@propionate
- Prefix "h" matched multiple: heparin sodium, heparin&&sodium, heparin.sodium, heparin/sodium, heparin\sodium, heparin^sodium, heparinsodium&, heparin|sodium, hyzaar
- Prefix "l" resolved: lotrisone
- Prefix "n" resolved: night time
- Prefix "{" resolved: {exetimibe}

### Round 2
- Prefix "fe" matched multiple: ferrous;sulfate, ferrous-sulfate, ferrous_sulfate, ferrous sulfate, ferrous~sulfate, ferrous:sulfate, fent-anyl, fenofibrate, ferrous'sulfate', ferrous"sulfate", ferrous,sulfate
- Prefix "he" matched multiple: heparin sodium, heparin\sodium, heparinsodium&, heparin/sodium, heparin|sodium, heparin^sodium, heparin.sodium, heparin&&sodium
- Prefix "fi" matched multiple: fioricet, fioricet()
- Prefix "et" resolved: ethinyl estradiol
- Prefix "fl" matched multiple: fluticasone@propionate, fluticasone propionate
- Prefix "hy" resolved: hyzaar
- Prefix "au" resolved: aug mentin
- Prefix "ez" matched multiple: ezetimibe[], ezetimibe, ezetimibe{}
- Prefix "ad" resolved: advair
- Prefix "fa" resolved: famotidine

### Round 3
- Prefix "fer" matched multiple: ferrous;sulfate, ferrous sulfate, ferrous~sulfate, ferrous-sulfate, ferrous_sulfate, ferrous:sulfate, ferrous'sulfate', ferrous"sulfate", ferrous,sulfate
- Prefix "hep" matched multiple: heparin sodium, heparin\sodium, heparinsodium&, heparin^sodium, heparin/sodium, heparin&&sodium, heparin.sodium, heparin|sodium
- Prefix "fio" matched multiple: fioricet, fioricet()
- Prefix "eze" matched multiple: ezetimibe[], ezetimibe{}, ezetimibe
- Prefix "flu" matched multiple: fluticasone@propionate, fluticasone propionate
- Prefix "fen" matched multiple: fent-anyl, fenofibrate

### Round 4
- Prefix "ferr" matched multiple: ferrous;sulfate, ferrous sulfate, ferrous~sulfate, ferrous-sulfate, ferrous_sulfate, ferrous:sulfate, ferrous'sulfate', ferrous"sulfate", ferrous,sulfate
- Prefix "hepa" matched multiple: heparin sodium, heparin\sodium, heparinsodium&, heparin^sodium, heparin/sodium, heparin&&sodium, heparin.sodium, heparin|sodium
- Prefix "fior" matched multiple: fioricet, fioricet()
- Prefix "ezet" matched multiple: ezetimibe{}, ezetimibe[], ezetimibe
- Prefix "flut" matched multiple: fluticasone@propionate, fluticasone propionate
- Prefix "fent" resolved: fent-anyl
- Prefix "feno" resolved: fenofibrate

### Round 5
- Prefix "ferro" matched multiple: ferrous;sulfate, ferrous sulfate, ferrous~sulfate, ferrous-sulfate, ferrous_sulfate, ferrous:sulfate, ferrous'sulfate', ferrous"sulfate", ferrous,sulfate
- Prefix "hepar" matched multiple: heparin sodium, heparin\sodium, heparinsodium&, heparin^sodium, heparin/sodium, heparin&&sodium, heparin.sodium, heparin|sodium
- Prefix "fiori" matched multiple: fioricet, fioricet()
- Prefix "ezeti" matched multiple: ezetimibe{}, ezetimibe[], ezetimibe
- Prefix "fluti" matched multiple: fluticasone@propionate, fluticasone propionate

### Round 6
- Prefix "ferrou" matched multiple: ferrous;sulfate, ferrous sulfate, ferrous~sulfate, ferrous-sulfate, ferrous_sulfate, ferrous:sulfate, ferrous'sulfate', ferrous,sulfate, ferrous"sulfate"
- Prefix "hepari" matched multiple: heparin sodium, heparin\sodium, heparinsodium&, heparin^sodium, heparin/sodium, heparin&&sodium, heparin.sodium, heparin|sodium
- Prefix "fioric" matched multiple: fioricet, fioricet()
- Prefix "ezetim" matched multiple: ezetimibe{}, ezetimibe[], ezetimibe
- Prefix "flutic" matched multiple: fluticasone@propionate, fluticasone propionate

### Round 7
- Prefix "ferrous" matched multiple: ferrous;sulfate, ferrous sulfate, ferrous~sulfate, ferrous-sulfate, ferrous_sulfate, ferrous:sulfate, ferrous'sulfate', ferrous,sulfate, ferrous"sulfate"
- Prefix "heparin" matched multiple: heparin sodium, heparin\sodium, heparinsodium&, heparin^sodium, heparin/sodium, heparin&&sodium, heparin.sodium, heparin|sodium
- Prefix "fiorice" matched multiple: fioricet, fioricet()
- Prefix "ezetimi" matched multiple: ezetimibe{}, ezetimibe[], ezetimibe
- Prefix "flutica" matched multiple: fluticasone@propionate, fluticasone propionate

### Round 8
- Prefix "ferrous;" resolved: ferrous;sulfate
- Prefix "heparin " resolved: heparin sodium
- Prefix "ferrous " resolved: ferrous sulfate
- Prefix "ferrous~" resolved: ferrous~sulfate
- Prefix "heparin\\" resolved: heparin\sodium
- Prefix "ferrous-" resolved: ferrous-sulfate
- Prefix "ferrous_" resolved: ferrous_sulfate
- Prefix "fioricet" matched multiple: fioricet, fioricet()
- Prefix "heparins" resolved: heparinsodium&
- Prefix "ferrous:" resolved: ferrous:sulfate
- Prefix "ezetimib" matched multiple: ezetimibe{}, ezetimibe[], ezetimibe
- Prefix "fluticas" matched multiple: fluticasone@propionate, fluticasone propionate
- Prefix "heparin^" resolved: heparin^sodium
- Prefix "ferrous'" resolved: ferrous'sulfate'
- Prefix "heparin/" resolved: heparin/sodium
- Prefix "ferrous," resolved: ferrous,sulfate
- Prefix "ferrous\"" resolved: ferrous"sulfate"
- Prefix "heparin&" resolved: heparin&&sodium
- Prefix "heparin." resolved: heparin.sodium
- Prefix "heparin|" resolved: heparin|sodium

### Round 9
- Prefix "ezetimibe" matched multiple: ezetimibe{}, ezetimibe[], ezetimibe
- Prefix "fluticaso" matched multiple: fluticasone@propionate, fluticasone propionate
- Prefix "fioricet(" resolved: fioricet()

### Round 10
- Prefix "ezetimibe{" resolved: ezetimibe{}
- Prefix "fluticason" matched multiple: fluticasone@propionate, fluticasone propionate
- Prefix "ezetimibe[" resolved: ezetimibe[]

### Round 11
- Prefix "fluticasone" matched multiple: fluticasone@propionate, fluticasone propionate

### Round 12
- Prefix "fluticasone " resolved: fluticasone propionate
- Prefix "fluticasone@" resolved: fluticasone@propionate