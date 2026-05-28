# Turkish Inflectional Morphology — Finite-State Analyser

A finite-state morphological analyser and generator for Turkish,
implemented using lexc and xfst (Beesley & Karttunen, 2003).

## Coverage
- Nominal case inflection (7 cases)
- Number (singular/plural)
- Possessive suffixes
- Nominal copula (present/past)
- Verbal TAM: present progressive, simple past, evidential past,
  future, conditional, necessitative, aorist
- Negation, passive, causative
- Adjectival copula
- Four vowel harmony classes (VHA, VHE, VHO, VHU)

## Requirements
- xfst (PARC Finite-State Tool)
- Python 3

## How to Run
```bash
python run.py
```
Or directly with xfst:
```bash
xfst -f turkish.script
python main.py turkish_expected.txt turkish_output.txt
```

## Test Results
133/133 test cases passing (100%)

## References
- Beesley & Karttunen (2003). Finite State Morphology. CSLI.
- Oflazer (1994). Two-level description of Turkish morphology.
- Göksel & Kerslake (2005). Turkish: A Comprehensive Grammar.
