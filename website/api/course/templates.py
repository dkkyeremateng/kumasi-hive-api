def course_obj(course):
    course_obj = {
        'title': course.title,
        'description': course.description,
        'duration': course.duration,
        'starting_date': str(course.starting_date.isoformat()[:19]) + "Z",
        'ending_date': str(course.ending_date.isoformat()[:19]) + "Z",
        'display_picture': course.display_picture,
        'user_id': course.user_id,
        'what_you_will_learn': course.what_you_will_learn,
        'curriculum_for_course': course.curriculum,
        'requirements': course.requirements,
        'external': course.external_id,
        'target_audience': course.target_audience,
        "links": [
            {"rel": "self", "href": f"/api/courses/{course.external_id}"}
        ]
    }

    return course_obj


def courses_obj(courses):
    courses_obj = []

    for course in courses:
        courses_obj.append(course_obj(course))

    return courses_obj
