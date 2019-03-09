clush -a "free && sync && echo 3 > /proc/sys/vm/drop_caches && free"

maprcli node services -action restart -name collectd -nodes mapr01.wired.carnoustie mapr02.wired.carnoustie mapr03.wired.carnoustie mapr04.wired.carnoustie mapr05.wired.carnoustie
