from rest_framework.pagination import PageNumberPagination


class UserProfilePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_query_param = "page_size"


class FollowersPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_query_param = "page_size"
