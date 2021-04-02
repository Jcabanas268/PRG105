"""
program accumulates rainfall per month to total rainfall for twelve months.
"""


def main():
    file_doc = open('rainfall-totals.txt', 'r')
    read_lines = file_doc.readlines()
    total_rainfall = 0
    whole_place = 0
    dec_place = 0
    for ln in read_lines:
        ln_rstrip = ln.rstrip('\n')
        ln_rain_value = (ln_rstrip.split())[1]
        print(ln_rain_value)
        ln_rain_value_split = ln_rain_value.split(".")
        whole_place += int(ln_rain_value_split[0])
        print(int(ln_rain_value_split[0]))
        print(ln_rain_value_split[1])   # have to convert to int
    print("whole_place", whole_place)   # correct
    print("dec_place", dec_place)       # incorrect
    print("total_rainfall", total_rainfall)


main()

"""
    lines = []
    for ln in read_lines:
        ln_rstrip = ln.rstrip('\n')
        print(ln_rstrip)
        ln_split = ln_rstrip.split()
        print(ln_split[1])
        print(ln_split[1][0])
        lines += ln_split[1][0]
    print(tuple(lines))
    tuple_lines = tuple(lines)
------
    print("file_doc:", file_doc)
    read_line = file_doc.readline()
    print("read_line", read_line)
    read_lines = file_doc.readlines()
    print("read_lines", read_lines)
    split_line = read_line.split
    print("split_line", split_line)
----
    total_rain = ""
    for ln in read_lines:
        ln_rstrip = ln.rstrip('\n')
        print("ln_rstrip", ln_rstrip)
        rain_fall = (ln_rstrip.split())[1]
        print(rain_fall)
        total_rain += rain_fall
    print(total_rain)
    print(rain_fall.astype(int))
------
    total_rain = 0
    for ln in read_lines:
        ln_rstrip = ln.rstrip("\n")
        print("ln_rstrip", ln_rstrip)
        rain_fall = (ln_rstrip.split())[1]
        print(rain_fall)
        total_rain += format(rain_fall, ',.0f')
----
    ln_count = 0
    rain_per_month = 0
    for ln in read_lines:
        ln_count += 1
        ln_strip = ln.rstrip()
        for ch in ln:
            print("ch.split", ch.split())
        print("ln_strip", ln_strip)
        print(ln_strip.split())
        ln_split = ln_strip.split()
        print("ln_split1", ln_split[1])                 # rain per month
        print("ln_split.index(1)", ln_split.index())
        ln_val = format(ln_split[1], ',.0f')
        ln_val_int = ln_val
        print("ln_val", ln_val)
----
    ln_count = 0
    rain_per_month = 0
    for ln in read_lines:
        ln_count += 1
        ln_strip = ln.rstrip()
        for ch in ln:
            print("ch.split", ch.split())
        print("ln_strip", ln_strip)
        print(ln_strip.split())
        ln_split = ln_strip.split()
        print("ln_split1", ln_split[1])                 # rain per month
        print("ln_split.index(1)", ln_split.index())
        ln_val = format(ln_split[1], ',.0f')
        ln_val_int = ln_val
        print("ln_val", ln_val)
----
    ln_count = 0
    rain_per_month = 0
    for ln in read_lines:
        ln_count += 1
        ln_strip = ln.rstrip()
        for ch in ln:
            print("ch.split", ch.split())
        print("ln_strip", ln_strip)
        print(ln_strip.split())
        ln_split = ln_strip.split()
        print("ln_split1", ln_split[1])                 # rain per month
        ln_val = format(ln_split[1], ',.0f')
        ln_val_int = ln_val
        print("ln_val", ln_val)
-----
    for ln in read_lines:
        ln_count += 1
        for ch in ln:
            print("ch.split", ch.split())
        print("ln", ln)
        print("tuple(ln[1])", tuple(ln[1]))
        print(ln.split())
        ln_split = ln.split()
        print("ln_split1", ln_split[1])                 # rain per month
        ln_val = tuple(ln_split[1])
        print("ln_val", ln.split())
-----
        ln_split_str = str(ln_split[1])
        ln_split_format = format(ln_split_str, ',.2f')
        print("ln_split_format", ln_split_format)
        rain_per_month += ln_split_format
        print("rain_per_month", rain_per_month)
------
    ln_count = 0
    for ln in read_lines:
        ln_count += 1
        for ch in ln:
            print("ch.split", ch.split())
        print("ln", ln)
-------
    user_phrase = "input (\"Enter phrase: \") addon input"
    users_phrase_split = user_phrase.split()
    print("user split:", users_phrase_split)
    acronym = ""
    for ln in users_phrase_split:
        acronym += ln[0]
        print("ln:", ln)
        print("first letter:", ln[0])
    print(acronym.upper())
"""
"""
    for ln in users_phrase_split:
        print("ln:", ln)
        print(ln[0])
        for id in range(len(users_phrase_split)):
            print("id:", id)
    print(users_phrase_split[0], users_phrase_split[0][0])


def main():
    user_phrase = "input (\"Enter phrase: \") addon input"
    users_phrase_split = user_phrase.split()
    print("user split:", users_phrase_split)
    acronym = ""
    for ln in users_phrase_split:
        acronym += ln[0]
        print("ln:", ln)
        print("first letter:", ln[0])
    print(acronym.upper())


main()
"""
