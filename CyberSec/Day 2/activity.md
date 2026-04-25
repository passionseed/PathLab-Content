# DAY 2 — "Hunt หา Attacker ก่อนโดนรอบสอง"

### **Goal:** ตัดสินใจว่า attacker ยังอยู่ในระบบไหม โดยใช้ข้อมูลที่ไม่ครบ

## **Situation** :

```
เมื่อคืน incident ถูก contain แล้ว — IP โดน block, session ถูก kill, logs preserve ไว้แล้ว

แต่ทีม security เชื่อว่า attacker อาจฝัง backdoor ไว้ก่อนออกไป และยังสามารถกลับเข้ามาได้
```

**คุณได้รับไฟล์ 4 ชุดจากเซิร์ฟเวอร์เพื่อตรวจสอบ**
#### FILE 1 — `netstat_output.txt`

> **netstat คืออะไร?** คำสั่งที่แสดงรายการ "การเชื่อมต่อเครือข่าย" ที่เซิร์ฟเวอร์กำลังมีอยู่ตอนนี้ เหมือนดูว่าประตูบ้านไหนเปิดอยู่บ้าง และมีใครยืนอยู่หน้าประตูนั้นไหม

### คำอธิบาย :
	Proto = ประเภทการเชื่อมต่อ (tcp = ปกติ)
	Local Address = IP:port ของเซิร์ฟเวอร์เรา
	Foreign Address = IP:port ของคนที่เชื่อมต่อมา
	State = สถานะ — ESTABLISHED = เชื่อมต่ออยู่, LISTEN = รอรับ, TIME_WAIT = กำลังปิด
### Internal IPs ของระบบ :
- `10.0.0.5` = IT admin workstation
- `10.0.0.8` = Hospital app server
- `10.0.0.12` = Reporting server
- `10.0.2.15` = Hospital database server

```
Proto  Local Address          Foreign Address         State
tcp    0.0.0.0:22             0.0.0.0:*               LISTEN
tcp    0.0.0.0:80             0.0.0.0:*               LISTEN
tcp    0.0.0.0:443            0.0.0.0:*               LISTEN
tcp    0.0.0.0:3306           0.0.0.0:*               LISTEN
tcp    10.0.2.15:22           203.154.12.88:61002     ESTABLISHED
tcp    10.0.2.15:22           10.0.0.5:52341          ESTABLISHED
tcp    10.0.2.15:443          171.96.80.14:44210      ESTABLISHED
tcp    10.0.2.15:443          171.96.80.14:44211      ESTABLISHED
tcp    10.0.2.15:443          171.96.80.14:44212      ESTABLISHED
tcp    10.0.2.15:3306         10.0.0.8:53291          ESTABLISHED
tcp    10.0.2.15:3306         10.0.0.12:55019         ESTABLISHED
tcp    10.0.2.15:443          <redacted>:443          ESTABLISHED
tcp    10.0.2.15:22           <redacted>:51422        ESTABLISHED
tcp    10.0.2.15:80           52.86.214.10:38800      TIME_WAIT
tcp    10.0.2.15:80           52.86.214.10:38801      TIME_WAIT
```

>  หมายเหตุ: 2 rows นี้ถูก export ออกมาไม่สมบูรณ์ ทำให้ไม่เห็น IP ปลายทาง แต่ยังเห็นว่า connection ยัง ESTABLISHED อยู่


#### **FILE 2 — `crontab_root.txt`**

> **crontab คืออะไร?** รายการ "งานอัตโนมัติ" ที่ตั้งเวลาให้เซิร์ฟเวอร์ทำเองโดยไม่ต้องมีคนสั่ง เหมือน alarm ที่ตั้งไว้ล่วงหน้า

### **คำอธิบาย format:**
	`นาที ชั่วโมง วัน เดือน วันในสัปดาห์ คำสั่ง` 
	เช่น `0 2 * * *` = ทุกคืนตี 2

```
# /var/spool/cron/crontabs/root  
# last modified: Apr 23 18:44  
# captured by IT during incident review  
  
0 2 * * * /usr/local/bin/db_health_check.sh  
30 3 * * * /usr/local/bin/backup_patients.sh  
0 */6 * * * /usr/local/bin/log_rotate.sh  
15 8 * * 1 /usr/local/bin/weekly_report.sh
```

### FILE 3 — `new_files_24h.txt`

> **ไฟล์นี้คืออะไร?** รายการไฟล์ทั้งหมดที่ถูกสร้างใหม่ใน 24 ชั่วโมงล่าสุด
### คำอธิบาย :
	Permissions = สิทธิ์การเข้าถึง — `rwx` = อ่าน/เขียน/รัน
	Owner = เจ้าของไฟล์
	Size = ขนาดไฟล์
	Date/Time= วันเวลาที่สร้าง
    Name = ชื่อไฟล์ ไฟล์ที่ชื่อขึ้นต้นด้วย `.` จะเป็นไฟล์ซ่อนใน Linux

```
Permissions   Owner    Group    Size    Date/Time       Name
-rw-r--r--    root     root     2.1K    Apr 24 07:15    /var/log/syslog.1
-rw-r--r--    www-data www-data 512     Apr 24 08:02    /var/www/html/index.html
-rw-r--r--    root     root     847M    Apr 24 02:13    /tmp/patients_2024.tar.gz
-rw-r--r--    root     adm      4.2K    Apr 24 09:31    /var/log/auth.log.1
-rwxr-x---    root     root     18K     Apr 24 03:07    /tmp/.sys_update
-rw-r--r--    root     root     128     Apr 24 03:07    /tmp/.sys_update.lock
-rw-r-----    mysql    mysql    1.1K    Apr 24 06:45    /var/lib/mysql/ib_logfile0
-rw-r--r--    root     root     334     Apr 24 03:09    /etc/cron.d/sys-maintenance
```
#### ลองมองหา :
- ไฟล์ที่ถูกสร้างใกล้เวลาเกิดเหตุ  
- ไฟล์ซ่อน (ไฟล์ที่ขึ้นด้วย "." จะซ่อนอยู่ใน Linux)
- ไฟล์บีบอัด (eg. .zip, .tar.gz)
- งานอัตโนมัติ
- ไฟล์ที่มีสิทธิ์รันได้(executable)
### FILE 4 — `sys-maintenance.txt`
  
> **ไฟล์นี้คืออะไร?**  
> นี่คือเนื้อหาของไฟล์ `/etc/cron.d/sys-maintenance`  
> ไฟล์ใน `/etc/cron.d/` ใช้ตั้ง “งานอัตโนมัติ” ให้ระบบรันคำสั่งตามเวลาที่กำหนด

``` 
File contents :
*/10 * * * * root /tmp/.sys_update >/dev/null 2>&1
```

ลองถามตัวเองว่า:  
- คำสั่งนี้รันบ่อยแค่ไหน?  
- รันด้วยสิทธิ์ของใคร?  
- ไฟล์ที่ถูกรันอยู่ตรงไหน?  
- ทำไมชื่อไฟล์ขึ้นต้นด้วย `.`  
- ทำไมต้องซ่อน output/error ด้วย `>/dev/null 2>&1`

## Step 1 )  แยก evidence

#### จาก 4 ไฟล์ด้านบน แยก items ทั้งหมดออกเป็น 3 กอง

### **Example :**

| ยืนยันว่าโดน | น่าสงสัย | ปกติดี |
| ------------ | -------- | ------ |
|              |          |        |

## Step 2 ) วาด Attack Timeline
#### สามารถทำได้หลายแบบ เช่น วาดลงกระดาษ, whiteboard, iPad, FigJam, Miro, หรือโปรแกรมอื่น ๆ ที่ถนัด ขอแค่ให้เห็นลำดับเหตุการณ์ชัดเจนว่า “เกิดอะไรขึ้นก่อนหลัง”

ไม่ต้องถูกทุกอย่าง สิ่งสำคัญคือ **reasoning ว่าทำไมถึงเรียงแบบนั้น**

### Step 3 )  2 Hypotheses

#### **เขียน 2 ข้อนี้**

**Hypothesis A:** Attacker ยังมีช่องทางกลับเข้าระบบ / มี persistence อยู่

- Evidence ที่ support: ...
- Evidence ที่ขัดแย้ง: ...

**Hypothesis B:** Attacker ออกไปแล้ว และยังไม่มีหลักฐานว่ากลับเข้ามาได้

- Evidence ที่ support: ...
- Evidence ที่ขัดแย้ง: ...

### Step 4 ) ตัดสินใจ

> หมายเหตุ: “ยังอยู่ในระบบ” อาจหมายถึงยังมี active connection หรือมี persistence/backdoor ที่ทำให้กลับเข้ามาได้

#### **เลือก 1 hypothesis แล้วตอบ:**

1. คุณเลือก Hypothesis ใด?
2. Confidence Level: `High` / `Medium` / `Low`
3. เหตุผลที่เลือก (2-3 ประโยค)
# Output ที่ต้องส่ง

1. Evidence table (3 กอง)
2. Attack timeline (รูปหรือข้อความก็ได้)
3. Hypothesis ที่เลือก + Confidence Level + เหตุผล
