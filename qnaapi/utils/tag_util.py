from qnaapi.models import AnswerComment, Answer, ArchTeamsQnaUser, Tag
from qnaapi.serializers import QuestionSerializer, TagSerializer
from qnaapi.utils.question_util import is_question_accessible


def create_and_get_tag_ids(tags, team_id):
    new_tags = [tag for tag in tags if isinstance(tag, str)]
    existing_tags = [tag for tag in tags if not isinstance(tag, str)]
    for new_tag in new_tags:
        serializer = TagSerializer(data={'name': new_tag, 'team': team_id})
        serializer.is_valid(raise_exception=True)
        tag = serializer.save()
        existing_tags.append(tag.id)
    return existing_tags
