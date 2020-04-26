from django.contrib import admin

from qnaapi.models import Team, ArchTeamsQnaUser, Tag, Question, Answer, QuestionComment, AnswerComment, QuestionVote, \
    AnswerVote, QuestionView

admin.site.register(Team)
admin.site.register(ArchTeamsQnaUser)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
admin.site.register(QuestionVote)
admin.site.register(AnswerVote)
admin.site.register(QuestionView)
