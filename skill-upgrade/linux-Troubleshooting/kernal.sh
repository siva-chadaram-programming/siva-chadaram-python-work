## Linux Kernal 
1.Linux employs monolithic kernel.The core OS services like File system, device drivers, network protocals and memory managment 
run in kernel space.
2.Linux supports loadable kernel modules allowing synamic insertion and removal of features from the kernel.
3.Kernel Space: This is where kernel runs and have complete control over the system.it operates with high level of privileges and can directly interact with hardware.
4.User Space: This is where user applications run in.User space can't directly access the hardware or kernel memory.It does through system calls.

##Kernel is responsible for:
  * Process Management 
  * Memory Management 
  * File System 
  * Device Drivers 
  * Network stack 
  * System Calls Interface 
  * Security 
  * IPC (Inter process communication) 

# Loading a Kernel module:
Loading kernel module is a straght process.it should only possible with right privileges to load module suhc as root.
Module compatibility with your kernel version and hardware is necessary.
Commands to load and remove kernel modules
insmode
modprobe
lsmod 

ex: sudo insmode /lib/modules/$(uname -r )/kernel/drivers/dummy

sudo modprobe dummy

Removig modules:
sudo rmmod dummy
sudo modprobe -r dummy 
