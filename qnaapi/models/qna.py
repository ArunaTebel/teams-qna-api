from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    avatar = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def user_count(self):
        return self.archteamsqnauser_set.count()


class ArchTeamsQnaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    full_name = models.CharField(max_length=250, blank=False, null=False)
    avatar = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name + ' [user: ' + self.user.username + ']'


class Tag(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField(max_length=65000)
    owner = models.ForeignKey(ArchTeamsQnaUser, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def answer_count(self):
        return self.answer_set.count()

    def views(self):
        return self.questionview_set.count()

    def up_votes(self):
        return self.questionvote_set.filter(vote_type=QuestionVote.UP).count()

    def down_votes(self):
        return self.questionvote_set.filter(vote_type=QuestionVote.DOWN).count()


class QuestionView(models.Model):
    viewer = models.ForeignKey(ArchTeamsQnaUser, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.name + ' viewed by ' + self.viewer.full_name


class QuestionVote(models.Model):
    UP = 'up'
    DOWN = 'down'
    VOTE_TYPES = [(UP, 'Up Voted'), (DOWN, 'Down Voted')]

    voter = models.ForeignKey(ArchTeamsQnaUser, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=4, choices=VOTE_TYPES, default=UP)

    def __str__(self):
        return self.question.name + ' ' + self.vote_type + ' voted by ' + self.voter.full_name


class Comment(models.Model):
    content = models.TextField(max_length=65000)
    up_votes = models.IntegerField(default=0, blank=True)
    down_votes = models.IntegerField(default=0, blank=True)
    owner = models.ForeignKey(ArchTeamsQnaUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Answer(Comment):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class AnswerVote(models.Model):
    UP = 'up'
    DOWN = 'down'
    VOTE_TYPES = [(UP, 'Up Voted'), (DOWN, 'Down Voted')]

    voter = models.ForeignKey(ArchTeamsQnaUser, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=4, choices=VOTE_TYPES, default=UP)

    def __str__(self):
        return str(self.answer.id) + ' ' + self.vote_type + ' voted by ' + self.voter.full_name


class QuestionComment(Comment):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class AnswerComment(Comment):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
