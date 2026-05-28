#!/usr/bin/env python3
"""
Turkish Morphology Test Comparison Script
Usage: python main.py turkish_expected.txt turkish_output.txt

Parses both files as alternating tag/form pairs and reports
matches, mismatches, and missing entries.

Expected file format (turkish_expected.txt):
    araba+Noun+Sg+Nom
    araba

    araba+Noun+Sg+Acc
    arabayı
    ...

Output file format (turkish_output.txt, produced by xfst apply down):
    araba+Noun+Sg+Nom
    araba

    araba+Noun+Sg+Acc
    arabayı
    ...
"""

import sys


def parse_pairs(path):
    """Parse a file of tag/form pairs, returning an ordered list of (tag, form)
    and a dict mapping tag -> form. Blank lines are ignored."""
    pairs = []
    seen = {}
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\r\n") for l in f]

    # Strip blank lines and collect non-empty lines
    tokens = [l for l in lines if l.strip()]

    # Lines alternate: tag, form, tag, form ...
    i = 0
    while i + 1 < len(tokens):
        tag  = tokens[i].strip()
        form = tokens[i + 1].strip()
        pairs.append((tag, form))
        seen[tag] = form
        i += 2

    return pairs, seen


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} expected.txt output.txt")
        sys.exit(1)

    expected_path = sys.argv[1]
    output_path   = sys.argv[2]

    expected_pairs, expected = parse_pairs(expected_path)
    output_pairs,  output   = parse_pairs(output_path)

    total    = len(expected_pairs)
    correct  = 0
    wrong    = []
    missing  = []

    for tag, exp_form in expected_pairs:
        if tag not in output:
            missing.append(tag)
        else:
            got = output[tag]
            if got == exp_form:
                correct += 1
            else:
                wrong.append((tag, exp_form, got))

    # Extra tags produced by output but not in expected
    extra = [tag for tag in output if tag not in expected]

    # ----------------------------------------------------------------
    # Report
    # ----------------------------------------------------------------
    print("=" * 60)
    print("TURKISH MORPHOLOGY TEST RESULTS")
    print("=" * 60)
    print(f"  Total expected:  {total}")
    print(f"  Correct:         {correct}  ({100*correct/total:.1f}%)")
    print(f"  Wrong:           {len(wrong)}")
    print(f"  Missing:         {len(missing)}")
    print(f"  Extra (in output only): {len(extra)}")
    print()

    if wrong:
        print("-" * 60)
        print("MISMATCHES:")
        for tag, exp, got in wrong:
            print(f"  {tag}")
            print(f"    expected : {exp}")
            print(f"    got      : {got}")
        print()

    if missing:
        print("-" * 60)
        print("MISSING FROM OUTPUT:")
        for tag in missing:
            print(f"  {tag}")
        print()

    if extra:
        print("-" * 60)
        print("EXTRA (in output but not expected):")
        for tag in extra:
            print(f"  {tag}  ->  {output[tag]}")
        print()

    print("=" * 60)
    if correct == total and not missing:
        print("ALL TESTS PASSED!")
    else:
        print(f"FAILED: {len(wrong) + len(missing)} issue(s) remaining.")
    print("=" * 60)

    # Exit code: 0 = all pass, 1 = failures
    sys.exit(0 if (correct == total and not missing) else 1)


if __name__ == "__main__":
    main()
