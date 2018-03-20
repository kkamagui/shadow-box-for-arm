```bash      
 ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗      ██████╗  ██████╗ ██╗  ██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║      ██╔══██╗██╔═══██╗╚██╗██╔╝
 ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║█████╗██████╔╝██║   ██║ ╚███╔╝ 
 ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║╚════╝██╔══██╗██║   ██║ ██╔██╗ 
 ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝      ██████╔╝╚██████╔╝██╔╝ ██╗
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝       ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
      
                       ARM TrustZone-Based Kernel Protector
```

# 1. Notice
Shadow-box v2 (for ARM) is a next generation of Shadow-box v1 (for x86). If you want to know about Shadow-box for x86, please visit [Shadow-box for x86 project](https://github.com/kkamagui/shadow-box-for-x86).

We have been doing our best to publish our source code and will publish it soon.
Please give a star and watch our project!!!

# 1.1. Presentation
Shadow-box for ARM is a lightweight and practical kernel protector, and it was introduced at security conferences below.
 - [Black Hat Asia 2018](https://www.blackhat.com/asia-18/briefings.html#shadow-box-v2-the-practical-and-omnipotent-sandbox-for-arm): Shadow-box v2: The Practical and Omnipotent Sandbox for ARM
 
 You can watch the demo videos below.
 - [Demo](https://youtu.be/mhS3ujH6yyA): If you use kernel-level protection mechanism with Shadow-box v2, then rootkits cannot neutralize it and cannot work. 

# 1.2. Contributions
We always welcome your contributions. Issue report, bug fix, new feature implementation, anything is alright. Feel free to send us. 

# 1.3. License
Shadow-box v2 has MIT license and other parts follow their own license.

# 2. Introduction of Shadow-Box v2 for ARM
Shadow-box v2, using virtualization technologies of x86 and ARM processor. Shadow-box v2 inherits a novel architecture inspired by a shadow play from Shadow-box v1, and we made Shadow-box v2 from scratch. Shadow-box v2 for ARM utilizes OP-TEE (Open Platform Trusted Execution Environment) which follows GlobalPlatform TEE system architecture specification. Qualcomm and Samsung also follow the specification. Moreover, OP-TEE supports more than eleven manufacturers including Broadcom and NXP, therefore Shadow-box v2 can be ported many ARM-based devices easily. 

Shadow-box v2 also utilizes integrity measurement architecture (IMA). IMA can verify signatures of executable files from kernel. Therefore Shadow-box v2 provides strict integrity of executable files. Shadow-box v2 has additional features such as hash-based kernel integrity monitor, workload-concerned monitoring, and remote attestation in comparison with Shadow-box v1. 

# 2.1. Architecture of Shadow-Box for ARM
We explain how we resigned the Light-box and the Shadow-watcher. It is designed to support a lightweight and practical security monitoring framework using ARM TrustZone technology.

<center> <img src="document/images/architecture.png" width="600"> </center>

If you want to know more about Shadow-box, please see my presentation at [Black Hat Asia 2018](https://www.blackhat.com/asia-18/briefings.html#shadow-box-v2-the-practical-and-omnipotent-sandbox-for-arm).

# 3. We Are Preparing to Publish Our Source Code!
We have been doing our best to publish our source code and will publish it soon.
Please give a star and watch our project!!!
