import json
import os

from STRAPI.settings import MSG_LOCALE


def create_message(data, status_code=None):
    """Create message utility for creating responses

    Args:
        data ([list]): [List of objects]
        status ([int], mandatory): [Internal system status code for the
                                    response defined in module locale]
                                    Defaults to None.

    Returns:
        [dict]: [Dict with status, message and data keys for client]
    """

    return {
        # internal system codes
        "status": status_code,
        # locale message in the system codes
        "message": get_message(status_code),
        "data": data,
    }


def get_message(msg_code=None):
    """Get localized message according to the given code.
    Locale used is configured in settings

    Args:
        msg_code ([int], mandatory): [Message code described in module locale]
    """

    # msg_code not provided
    if not msg_code:
        raise ValueError("msg_code not provided")

    try:

        # Open locale messages

        with open(
            os.path.dirname(os.path.realpath(__file__)) + "/message.json", "r"
        ) as locale_file:
            message_dict = json.load(locale_file)

            return message_dict[str(msg_code)]["msg"][MSG_LOCALE]

    except Exception as ex:
        return "Message not found against code " + str(msg_code)
