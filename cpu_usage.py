import psutil
print(f'The current amount of CPU being used is {psutil.cpu_percent(0.1)}')
