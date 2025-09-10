temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def is_hot_temperature(temperature):
    return temperature > 28


hot_temperatures = list(filter(is_hot_temperature, temperatures))

min_temperature = min(hot_temperatures)

max_temperature = max(hot_temperatures)

avg_temperature = round(sum(hot_temperatures) / len(hot_temperatures), 2)

print(f"""
Minimum temperature: {min_temperature}
Maximum temperature: {max_temperature}
Average temperature: {avg_temperature}
""")
