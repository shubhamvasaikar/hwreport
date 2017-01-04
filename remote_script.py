import psutil

def main():
    with open("/root/remote/report.txt", 'w') as report:
        #string = "CPU Percentage: " + psutil.cpu_percent(interval = 0.2)
        report.write("CPU Percentage: " + str((psutil.cpu_percent(interval=0.2))) + "\n")
        report.write("CPU Count: " + str((psutil.cpu_count())) + "\n")

        virt_mem = psutil.virtual_memory()

        report.write("Total Memory:  " + str(virt_mem.total) + "\n")
        report.write("Availale Memory " + str(virt_mem.available) + "\n")
        report.write("Used Memory " + str(virt_mem.used) + "\n")
        report.write("Free Memory " + str(virt_mem.free) + "\n")
        report.write("% Memory " + str(virt_mem.percent) + "\n")

        disks = psutil.disk_partitions()      
        mounts = []
        for disk in disks:
            mounts.append(disk.mountpoint)

        for mount in mounts:
            report.write(mount + ": " + str(psutil.disk_usage(mount)) + "\n")

if __name__ == '__main__':
    main()
