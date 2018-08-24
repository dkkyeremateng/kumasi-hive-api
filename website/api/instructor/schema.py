instructor_schema = {
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "pattern": "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        },
        "first_name": {
            "type": "string"
        },
        "last_name": {
            "type": "string"
        },
        "password": {
            "type": "string",
            "minLength": 6
        },
        'display_pic': {
            'type': 'string'
        },
        'courses': {
            'type': 'array'
        },
        'interests': {
            'type': 'array'
        },
        'gender': {
            'type': 'string',
            'oneOf': [{'type': 'string', 'enum': ['Male', 'Female']}]
        },
        'telephone': {
            'type': 'string',
            'pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}'
        }
    },
    "required": ["email", "password", 'first_name', 'last_name', 'display_pic', 'gender', 'telephone']
}