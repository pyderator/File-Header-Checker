import os
for f in os.listdir():
    print(os.system(f'hexyl {f} -c 16'))
