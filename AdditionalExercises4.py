print("Exercise 1")

SEED_NUM = 1  
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "ARTHUR NERY"
LOCAL_HAZARD = "TYPHOON"
CONTROL_NUM = max(3, SEED_NUM)

from collections import defaultdict, Counter

stream = [
("TUP Manila", "BSECE"),
("TUP Taguig", f"BSME_v{CONTROL_NUM}"),
("TUP Manila", f"BSME_v{CONTROL_NUM}"),
("TUP Manila", "BSECE"),
("TUP Visayas", STUDENT_MAJOR),
("TUP Taguig", "BSECE"),
("TUP Manila", "BSECE")
]



stream.extend([
    ("TUP Manila", "BSME"),
    ("TUP Taguig", "BSME"),
    ("TUP Visayas", "BSME"),
    ("TUP Manila", "BSECE"),
    ("TUP Cavite", "BSEE"),
    ("TUP Taguig", "BSECE")
])

print(len(stream))



campus_programs = defaultdict(list)

for campus, program in stream:
    campus_programs[campus].append(program)

for campus, programs in campus_programs.items():
    print(f"{campus}: {programs}")



campus_counters = {}

for campus in campus_programs:
    campus_counters[campus] = Counter(campus_programs[campus])
    print(f"{campus}: {campus_counters[campus]}")



top_program, frequency = campus_counters["TUP Manila"].most_common(1)[0]

print("Top Requested Program at TUP Manila:", top_program)
print("Exact Frequency of Top Program:", frequency)





print("Exercise 2")

from collections import Counter

festival = {
    "BEN&BEN", "SB19", "BINI", "ERASERHEADS",
    FAVORITE_ARTIST, "ZILD", f"INDIE ARTIST {CONTROL_NUM}"
}

user_a = {
    "BEN&BEN", "BINI", "MAKI", "DIONELA", FAVORITE_ARTIST
}

user_b = {
    "SB19", "ERASERHEADS", "ZILD",
    f"INDIE ARTIST {CONTROL_NUM}",
    "PAROKYA NI EDGAR"
}



festival.update({
    "ARTHUR NERY",
    "ADIE",
    "JOLIANNE"
})



def jaccard(set_a, set_b):
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return (len(intersection) / len(union)) * 100, intersection, union



a_score, a_intersection, a_union = jaccard(user_a, festival)

b_score, b_intersection, b_union = jaccard(user_b, festival)

dealbreakers = user_a.difference(festival)



print("Total Artists in Expanded Festival:", len(festival))

print("Length of Intersection (User A & Festival):", len(a_intersection))
print("Length of Union (User A & Festival):", len(a_union))
print("User A Jaccard Similarity (%):", round(a_score, 2))
print("User B Jaccard Similarity (%):", round(b_score, 2))
print("User A Dealbreaker Artists:", dealbreakers)





print("Exercise 3")

from collections import deque, Counter


window = deque(maxlen=5)


burst = [
    (CONTROL_NUM, "WEATHER"),
    (CONTROL_NUM + 1, "TRAFFIC"),
    (CONTROL_NUM + 2, "WEATHER"),
    (CONTROL_NUM + 3, "WEATHER"),   # CHECK THIS EVENT
    (CONTROL_NUM + 4, LOCAL_HAZARD),
    (CONTROL_NUM + 5, "WEATHER"),
    (CONTROL_NUM + 6, "TRAFFIC")
]


start_time = CONTROL_NUM + 7

burst.extend([
    (start_time, "SPORTS"),
    (start_time + 1, "WEATHER"),
    (start_time + 2, "TRAFFIC"),
    (start_time + 3, "NEWS"),
    (start_time + 4, "WEATHER")
])


weather_at_c3_appended = False
local_hazard_appended = False


for timestamp, category in burst:

    categories = [item[1] for item in window]
    counts = Counter(categories)

    # Spam rule: reject if already appears 2+ times
    if counts[category] >= 2:
        continue

    window.append((timestamp, category))

    # tracking conditions
    if (CONTROL_NUM + 3, "WEATHER") in window:
        weather_at_c3_appended = True

    if category == LOCAL_HAZARD:
        local_hazard_appended = True


total_burst_size = len(burst)
final_deque_length = len(window)
timestamp_sum = sum(item[0] for item in window)


print("LOCAL_HAZARD Used:", LOCAL_HAZARD)
print("Total Burst Size (After adding custom alerts):", total_burst_size)
print("Did WEATHER at CONTROL_NUM+3 append? (Y/N):",
      "Y" if weather_at_c3_appended else "N")
print("Did LOCAL_HAZARD append? (Y/N):",
      "Y" if local_hazard_appended else "N")
print("Final Deque Length:", final_deque_length)
print("Final Sum of Timestamps in Deque:", timestamp_sum)
print("Exact Final Deque Output:", list(window))