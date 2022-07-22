# We will examine it in 3 steps. Follow me step-by-step

## 0.1 start the machine and connect.

## 0.2 we need information, so use gobuster, dirb and nmap tools 
	We use the gobuster tool to find subdirectories
	- /uploads 
	- /secret 
![gobuster](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-1.png)
	That's it was found with dirb
![dirb](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-2.png)
	These were found with nmap
	- The -sV parameter gives us "Probe open ports to determine service/version info"
	- The -sO parameter scan to ports with ping,
	- The -A parameter gives us "server OS, OS version and traceroute"
![nmap](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-3.png)

## elimizde olan verileri inceliyoruz.


![](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-4.png)
![](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-5.png)
![](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-6.png)
![](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-7.png)
![](https://github.com/Onur-TURAN/THM/blob/main/gamingserver/img/e_1-8.png)
