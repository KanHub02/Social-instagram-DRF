from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_query_param = "page_size"


class CommentsPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 1000
    page_query_param = "page_size"


class LikePaginatioin(PageNumberPagination):
    page_size = 10
    max_page_size = 1000
    page_query_param = "page_size"
