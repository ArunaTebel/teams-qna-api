from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


def paginated_response(view, qs, serializer, request):
    queryset = view.filter_queryset(qs)

    page = view.paginate_queryset(queryset)
    if page is not None:
        serializer_obj = serializer(page, many=True, context={'request': request})
        return view.get_paginated_response(serializer_obj.data)

    serializer_obj = serializer(queryset, many=True, context={'request': request})
    return Response(serializer_obj.data)


def limit_offset_paginated_response(view, qs, serializer, request):
    queryset = view.filter_queryset(qs)
    paginator = LimitOffsetPagination()
    page = paginator.paginate_queryset(queryset, request)
    if page is not None:
        serializer_obj = serializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer_obj.data)

    serializer_obj = serializer(queryset, many=True, context={'request': request})
    return Response(serializer_obj.data)
