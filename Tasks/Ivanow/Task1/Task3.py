speed_kmh = float(input('Input speed in km/h: '))

kmh_to_ms = 0.27778
speed_ms = round(speed_kmh * kmh_to_ms, 1)

print(f'Speed in m/s: {speed_ms}')