#!/usr/bin/env python3
import psutil

if __name__ == '__main__':
    perc_cpu = psutil.cpu_percent(interval=1, percpu=True)
    mem_virt = int(psutil.virtual_memory().used / (1024 ** 2))
    avail_mem = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print(f'''Estat actual del PC:
Els cores estan al {perc_cpu}%
Utilitzant {mem_virt} Mb de memòria
Queda un {avail_mem}% de memòria lliure''')