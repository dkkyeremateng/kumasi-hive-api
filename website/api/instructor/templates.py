def instructor_obj(instructor):
    instructor_obj = {
        "id": instructor.external_id,
        'email': instructor.email,
        'first_name': instructor.first_name,
        'last_name': instructor.last_name,
        'telephone': instructor.telephone,
        'gender': instructor.gender,
        'display_pic': instructor.display_pic,
        'interests': instructor.interests
    }
    return instructor_obj


def instructors_objs(instructors):
    instructors_obj = []
    for instructor in instructors:
        instructors_obj.append(instructor_obj(instructor))
    return instructors_obj
