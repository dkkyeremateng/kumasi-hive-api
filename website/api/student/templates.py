def student_obj(student):
    student_obj = {
        "id": student.external_id,
        'email': student.email,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'telephone': student.telephone,
        'gender': student.gender,
        'display_pic': student.display_pic,
        'interests': student.interests
    }
    return student_obj


def students_objs(students):
    students_objs = []
    for student in students:
        print(student)
        students_objs.append(student_obj(student))
    return students_objs
