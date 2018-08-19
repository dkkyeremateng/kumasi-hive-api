schema = {
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'duration': {'type': 'string'},
        'starting_date': {
            'type': 'string',
            'pattern': '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$'
        },
        'ending_date': {
            'type': 'string',
            'pattern': '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$'
        },
        'user_id': {'type': 'string'},
        'display_picture': {
            'type': 'string',
            'format': 'uri'
        },
        'requirements': {'type': 'array'},
        'what_you_will_learn': {'type': 'array'},
        'curriculum': {'type': 'object'},
        'target_audience': {'type': 'array'}
    },
    'required': [
        'title',
        'description',
        'ending_date',
        'user_id',
        'display_picture',
        'requirements',
        'what_you_will_learn',
        'curriculum',
        'duration',
        'starting_date',
        'target_audience'
    ]
}
