# -*- encoding: utf-8 -*-

import jsonschema

from functools import wraps

from werkzeug.exceptions import BadRequest


def json_expected(schema=None, allowed_methods=('POST', 'PUT')):
    def wrapper(func):
        @wraps(func)
        def _decorator():
            if request.method in allowed_methods:
                json_data = json.loads(request.get_data().decode('utf-8'))
                if schema is not None:
                    try:
                        jsonschema.validate(json_data, schema)
                    except jsonschema.SchemaError:
                        raise BadRequest()
                return func(json_data)
            else:
                raise BadRequest()
        return _decorator
    return wrapper

