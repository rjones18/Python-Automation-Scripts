import shutil
du = shutil.disk_usage("/")
print(du)
print("The percentage of free disk space is below:")
print(du.free/du.total*100)