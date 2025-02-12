from contextlib import nullcontext as does_not_raise

# url, expected_status_code, expectation
PARAMS_TEST_GET_EVENTS = [
    # positive case get all events
    (
        "/events",
        200,
        does_not_raise(),
    ),
]

# url, payload, expected_status_code, expectation
PARAMS_TEST_POST_EVENTS = [

    # positive case create one event
    (
        "/events",
        {
            "event_id": 4,
            "coefficient": "1.8",
            "deadline": 1799347012,
            "state": 1,
        },
        200,
        does_not_raise(),
    ),

    # negative case create  one event with exist id
    (
        "/events",
        {
            "event_id": 1,
            "coefficient": "1.8",
            "deadline": 1799347012,
            "state": 1,
        },
        400,
        does_not_raise(),
    ),
]


# url, expected_status_code, expectation
PARAMS_TEST_GET_ONE = [

    # positive case with exist id
    (
        "/events/1",
        200,
        does_not_raise(),
    ),

    # negative case with invalid id
    (
        "/events/10",
        404,
        does_not_raise(),
    ),
]


# url, params, expected_status_code, expectation
PARAMS_TEST_PATCH_ONE = [

    # positive case patch one event
    (
        "/events/1",
        {
            "state": 2,
        },
        200,
        does_not_raise(),
    ),

    # negative case patch one event with invalid id
    (
        "/events/10",
        {
            "state": 2,
        },
        404,
        does_not_raise(),
    ),
]
