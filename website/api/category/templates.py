def category_obj(category):
    category_obj = {
        'category_name': category.category_name
    }

    return category_obj


def categories_objs(categories):
    categories_objs = []

    for category in categories:
        courses_obj.append(category_obj(category))

    return categories_objs
