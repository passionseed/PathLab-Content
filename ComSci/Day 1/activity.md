# DAY 1 "แก้ bug ก่อนระบบพัง"

- *คุณได้รับรายงานมาว่า

```
เวลา 08:47 น. ระบบ REGISTRATION ล่ม นิสิตปี 1 กว่า 200 คนลงทะเบียนไม่ได้ อาจารย์ที่ปรึกษาโทรถามทุก 10 นาที คุณคือ dev คนเดียวที่ออนไลน์อยู่ตอนนี้
```

คุณกลับมาดูโค้ด backend ระบบ :

```python
students = ["Big", "Nutt", "Angpao"]
max_courses = 3

def register(student, course_list):
    if len(course_list) => max_courses:
        print(f"{student} ลงทะเบียนเกิน limit")
        return False
    print(f"{student} ลงทะเบียนสำเร็จ")
    return True

register("Angpao", ["Math", "CS", "Eng", "Art"])
```

> อ่าน error message ให้ครบ — มันบอกอะไร บรรทัดไหน?
> 

# 1.วิเคราะห์ก่อนแก้

- Error บอกว่าอะไรผิด?
- บรรทัดไหนที่น่าสงสัยที่สุด?

# 2.แก้และทดสอบ

แก้ bug แล้วรัน test cases ต่อไปนี้ให้ผ่านทั้งหมด:

```python
register("Angpao", ["Math", "CS", "Eng", "Art"]) -> ควร print "ลงทะเบียนเกิน limit"
register("Big", ["Math", "CS", "Eng"])           -> ควร print "ลงทะเบียนสำเร็จ"
register("Nutt", ["Math"])                       -> ควร print "ลงทะเบียนสำเร็จ"
```

*แล้วถ้า....*

```python
register("Big", [])  # -> ควรเกิดอะไร? ระบบรับ 0 วิชาได้ไหม?
```

# 3.**Post-mortem** เขียนตอบ 3 ข้อนี้ ข้อละ 1 บรรทัด

- พังเพราะอะไร?
- แก้ยังไง?
- ถ้าเป็นระบบจริงจะเพิ่ม safeguard อะไรได้อีก?

## Constraint

> **ใช้เวลารวมไม่เกิน 25 นาที**  หากขั้นตอนที่ 3 ใช้เกิน 10 นาที ให้หยุดทันที แล้วเขียนว่า “ติดตรงไหน และเพราะอะไร” ซึ่งถือเป็นผลลัพธ์ที่ใช้ได้เช่นกัน

