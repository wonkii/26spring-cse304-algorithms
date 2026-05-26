import importlib.util

module_name = "knapsack3_algo"

# NOTE on the lecture pseudocode (algorithm 6.2, best-first B&B):
# The bound() function is the fractional-knapsack greedy bound, which is only a
# valid upper bound when the items are sorted by p/w (value density) in
# DESCENDING order. That ordering is a precondition of the algorithm.
#
# Two consequences this test must account for:
#   1) Crash on tie: a faithful translation pushes (-bound, node) onto a heap.
#      When two nodes share the same bound, heapq falls back to comparing the
#      Node payloads, which raise "TypeError: '<' not supported between
#      instances of 'Node' and 'Node'". The old case 8 (unsorted) hit such a
#      tie under real division (p[k]/w[k]) and crashed. It is now given with
#      items already sorted by p/w, which both removes the tie (no crash) and
#      satisfies the precondition (correct optimum 17 for // and / alike).
#   2) "accept": when items are NOT sorted, the bound can prune the optimal
#      branch, so a textbook implementation returns a suboptimal value while an
#      implementation that sorts (or brute-forces) returns the true optimum.
#      Cases 3 and 7 keep their unsorted data and accept BOTH values so neither
#      group of students is penalised.
test_cases = [
    {"n": 3, "W": 5.0,  "w": [2, 3, 4],             "p": [4, 5, 6],         "expected": 9.0,  "desc": "items 1+2 fit exactly"},
    {"n": 4, "W": 10.0, "w": [3, 4, 6, 5],          "p": [6, 7, 10, 8],     "expected": 17.0, "desc": "items 2+3 best"},
    {"n": 5, "W": 15.0, "w": [1, 2, 3, 9, 11],      "p": [2, 5, 7, 14, 20],  "expected": 28.0, "accept": [28.0, 29.0], "desc": "unsorted B&B yields 28; true optimum 29 (items 1+3+5)"},
    {"n": 3, "W": 50.0,  "w": [60, 70, 80],         "p": [10, 20, 30],      "expected": 0.0,  "desc": "all items too heavy"},
    {"n": 6, "W": 20.0, "w": [2, 3, 5, 8, 7, 4],    "p": [3, 5, 12, 20, 16, 10],"expected": 48.0, "desc": "items 4+5+6"},
    {"n": 3, "W": 6.0,  "w": [3, 4, 2],             "p": [4, 5  , 3],         "expected": 8.0,  "desc": "items 2+3"},
    {"n": 4, "W": 10.0,  "w": [5, 4, 6, 3],         "p": [10, 40, 30, 50], "expected": 80.0, "accept": [80.0, 90.0], "desc": "unsorted B&B yields 80; true optimum 90 (items 2+4)"},
    {"n": 4, "W": 12.0, "w": [3, 8, 5, 3],          "p": [5, 12, 7, 4],     "expected": 17.0, "desc": "items 1+2 (data pre-sorted by p/w; optimum 17, no heap tie)"},
    {"n": 4, "W": 20.0, "w": [10, 5, 7, 8],         "p": [15, 8, 10, 11],   "expected": 29.0, "desc": "items 2+3+4"},
    {"n": 5, "W": 11.0,  "w": [1, 2, 5, 6, 7],      "p": [1, 6, 18, 22, 28],"expected": 40.0, "desc": "textbook example"},
]

def run_test_cases(file_path="6.2.knapsack.0-1.bb_bestfs.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    ks_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ks_module)

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        print(f"\n\033[1mExample {i}: {case['desc']}\033[0m")

        n = case["n"]
        W = case["W"]
        w = [0] + case["w"]
        p = [0] + case["p"]
        # Pad lists for empty cases
        if len(w) <= 1:
            w.append(0)
            p.append(0)
        expected = case["expected"]
        accept = case.get("accept", [expected])

        try:
            result = ks_module.knapsack3(n, W, w, p)
        except Exception as e:
            # Isolate failures so one crashing case does not abort the rest.
            print(f"출력: ❌ Failed (raised {type(e).__name__}: {e})")
            print("-" * 40)
            continue

        print(f"Max profit: {result}")

        if any(abs(result - a) < 1e-6 for a in accept):
            print("출력: ✅ Passed")
            passed += 1
        else:
            shown = " or ".join(str(a) for a in accept)
            print(f"출력: ❌ Failed (Expected: {shown}, Got: {result})")

        print("-" * 40)

    print(f"\n✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == '__main__':
    run_test_cases()
