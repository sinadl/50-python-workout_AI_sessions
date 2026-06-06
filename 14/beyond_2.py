temps = {
    "2026-06-01": 22,
    "2026-06-02": 24,
    "2026-06-03": 21,
    "2026-06-04": 25,
    "2026-06-05": 23,
    "2026-06-06": 20,
    "2026-06-07": 26
}

date = input("Enter a date (YYYY-MM-DD): ")

if date in temps:
    dates = list(temps.keys())
    index = dates.index(date)

    print(f"Temperature on {date}: {temps[date]}°C")

    if index > 0:
        prev_date = dates[index - 1]
        print(f"Previous date: {prev_date}, Temperature: {temps[prev_date]}°C")

    if index < len(dates) - 1:
        next_date = dates[index + 1]
        print(f"Next date: {next_date}, Temperature: {temps[next_date]}°C")
else:
    print("Date not found.")