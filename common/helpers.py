def get_default_query_param(request, key, default):
    """

    @param request: request object
    @type request: request
    @param key: key to get data from
    @type key: str
    @param default: default variable to return if key is empty or doesn't exist
    @type default: str/None
    @return: key
    @rtype: str/None
    """
    if key in request.query_params:
        key = request.query_params.get(key)
        if key:
            return key
    return default


def verify_user_in_request(request, obj):
    if not obj or (request.user.id == obj.app.user.id):
        return True
    return False
