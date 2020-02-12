from flask import jsonify

response_message = {200: 'success',
                    204: 'not login',
                    400: 'data format error',
                    401: 'data content error',
                    403: 'forbidden',
                    404: 'page not found',
                    500: 'undefined error',
                    504: 'timeout'}


def response(status_code, message=None, response_data=None):
    if status_code == StatusCode().DATA_CONTENT_ERROR and not message:
        raise ValueError('[ERROR - Response] data content error must have message to tell which content is wrong')

    result = {'message': response_message[status_code] if not message else message,
              'data': response_data if response_data else []}

    return jsonify(result), status_code


class StatusCode:
    def __init__(self):
        self.OK = self.SUCCESS = 200
        self.NOT_LOGIN = 204
        self.DATA_FORMAT_ERROR = 400
        self.DATA_CONTENT_ERROR = 401
        self.FORBIDDEN = 403
        self.NOT_FOUND = 404
        self.UNDEFINED = 500
        self.TIMEOUT = 504
