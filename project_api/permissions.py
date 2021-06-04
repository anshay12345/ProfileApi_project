from rest_framework import permissions


# this will provide us with a base class that we can use to create custom permission class

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            # this is only for the request which involves only reading but no changing
        # SAFE_METHOD is for checking if the request if only of reading if the method being used is a HTTP GET then
        # it will be in the safe method,therefore it will return true and allow the request

        return obj.id == request.user.id  # when the user make a request, we are gonna check  if the reques is in the
        # safe method IF THE REQUEST IS IN THE SAFE_METHOD(CHECKED BY THE IF CONDITION). SAFE_METHOD MEANS GET
        # REQUEST THEN IT RETURNS TRUE AND THE REQUEST IS MADE, IF THE CONDITION IS FALSE THAT MEANS THE REQUES IS NOT
        # IN SAFE MODE, THAT IS THE REQUEST IS POST OR ANYTHING THEN IT WILL RETURN TRUE IF THE USER IS AUTHENTICATE
        # (WHICH MEANS THE USER IS TRYING TO UPDATE IT'S OWN PROFILE NOT ) AND WILL RETURN FALSE IF THE USER IS NOT
        # AUTHENTICATED
