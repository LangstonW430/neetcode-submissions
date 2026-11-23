# Blind 75 problem log

One row per problem, added the day it's solved. Code lives in `Data Structures & Algorithms/` (synced from NeetCode).
Anything not solved unaided gets a redo date 7 days out.

Targets: 25 by 2026-12-17 · 75 by 2027-05-15 (one a day ≈ 75 by late Jan).

| # | Date | Problem | Pattern | Time / Space | Min | Unaided / Hint / Looked up | What tripped me | Redo |
|---|------|---------|---------|--------------|-----|----------------------------|-----------------|------|
| 1 | 2026-11-16 | Two Sum | Complement lookup | O(n) / O(n) | 10 | Unaided | First used index as the dict key; key must be what you look up by | — |
| 2 | 2026-11-16 | Valid Anagram | Counting map | O(n) / O(1) (26-letter alphabet) | 3 | Unaided | — (polish: length early-exit, `Counter`) | — |
| 3 | 2026-11-18 | Contains Duplicate | Seen set | O(n) / O(n) | 2 | Unaided | NA | — |
| 4 | 2026-11-18 | Group Anagrams | Canotical Key | O(nmlogm) / O(nm) | 14 | Hint | getting counter dict into a good key for the larger dict | — |
| 5 | 2026-11-19 | Top K Frequent Elements | Counting map | O(nlogn) / O(n) | 7 | Hint | converting from the counter into the keys witht the highest values| — |
| 6 | 2026-11-20 | Encode and Decode Strings | Length-Prefix Serialization | both O(nm) / O(nm) | 17 | Unaided | forgot the chr() funciton | — |
| 7 | 2026-11-23 | Products of Array Except Self| Prefix Product | O(n) / O(n) | 10 | hint | concept hint| - |
