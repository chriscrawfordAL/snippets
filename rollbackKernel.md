2. List the Kernel Entries as per GRUB2 file:

# >awk -F\\' '$1=="menuentry " {print $2}' /etc/grub2.cfg
```Oracle Linux Server, with Unbreakable Enterprise Kernel 3.8.13-94.el7uek.x86_64
Oracle Linux Server, with Unbreakable Enterprise Kernel 3.8.13-94.el7uek.x86_64 with debugging
Oracle Linux Server 7.1, with Linux 3.10.0-229.el7.x86_64
Oracle Linux Server 7.1, with Unbreakable Enterprise Kernel 3.8.13-55.1.6.el7uek.x86_64
Oracle Linux Server 7.1, with Linux 0-rescue-441e86c9ff854310a306bd33e56aae2b
```
**NOTE: The first entry is denoted as Zero. So currently the Server is booted to 0th entry as per the above `uname -a` command output.**

3. Let us modify the Kernel Version to 3.8.13-55.1.6.el7uek.x86_64 which is at line number 4 but denoted as entry 3.

# >grub2-set-default 3
4. Changes to /etc/default/grub require rebuilding the grub.cfg file as follows:

# >grub2-mkconfig -o /boot/grub2/grub.cfg
```Generating grub configuration file ...
Found linux image: /boot/vmlinuz-3.10.0-229.el7.x86_64
Found initrd image: /boot/initramfs-3.10.0-229.el7.x86_64.img
Found linux image: /boot/vmlinuz-3.8.13-94.el7uek.x86_64
Found initrd image: /boot/initramfs-3.8.13-94.el7uek.x86_64.img
Found linux image: /boot/vmlinuz-3.8.13-55.1.6.el7uek.x86_64
Found initrd image: /boot/initramfs-3.8.13-55.1.6.el7uek.x86_64.img
Found linux image: /boot/vmlinuz-0-rescue-441e86c9ff854310a306bd33e56aae2b
Found initrd image: /boot/initramfs-0-rescue-441e86c9ff854310a306bd33e56aae2b.img
done```

Reboot the Server and it will boot with Kernel Version 3.8.13-55.1.6.el7uek.x86_64.

# shutdown -r now
