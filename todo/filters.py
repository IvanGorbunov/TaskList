# from utils.filterset import SearchFilterSet
from django_filters import rest_framework as filters


# class ApprovalListFilter(SearchFilterSet):
#     search_fields = ()
#     view = filters.CharFilter(method='filter_view')
#
#     class Meta:
#         model = Approval
#         fields = (
#             'user',
#             'status',
#         )
#
#     def filter_view(self, qs, name, values):
#         filters = Q()
#         for item in values.split(','):
#             if item == ApprovalListViewChoices.INFO:
#                 filters |= Q(info_message_id__isnull=False)
#             elif item == ApprovalListViewChoices.ARTICLE:
#                 filters |= Q(article__type=ArticleType.ARTICLE)
#             elif item == ApprovalListViewChoices.PROJECT:
#                 filters |= Q(article__type=ArticleType.PROJECT)
#             else:
#                 return qs.none()
#         return qs.filter(filters)
