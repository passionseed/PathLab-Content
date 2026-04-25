students = ["Big", "Nutt", "Angpao"]
max_courses = 3 # maxiumum course

def register(student, course_list):
    if len(course_list) >=  max_courses:  
        print(f"{student} ลงทะเบียนเกิน limit")
        return False
    print(f"{student} ลงทะเบียนสำเร็จ")
    return True

register("Angpao", ["Math", "CS", "Eng", "Art"])
