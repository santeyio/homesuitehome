from rest_framework.exceptions import APIException


class HouseholdException(APIException):
    status_code = 400
    default_detail = 'This user is not associated with a household'
    default_code = 'household_not_set'
