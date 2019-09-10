import uuid
from django.db import models


class Word(models.Model):
    word_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)
    char_string = models.CharField(max_length=140, db_index=True)

    def __str__(self):
        return self.char_string


class Biterm(models.Model):
    biterm_id = models.CharField(
        max_length=72, primary_key=True, editable=False)
    word_i = models.ForeignKey(
        Word, on_delete=models.PROTECT, related_name='word_i')
    word_j = models.ForeignKey(
        Word, on_delete=models.PROTECT, related_name='word_j')

    def __str__(self):
        return self.word_i.char_string + ',' + self.word_j.char_string


class Hashtag(models.Model):
    tag_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)
    WAITING = "waiting"
    PROCESSING = "processing"
    FINISHED = "finished"
    STATUS_SET = (
        (WAITING, "待ち"),
        (PROCESSING, "処理中"),
        (FINISHED, "完了"),
    )
    name = models.CharField(max_length=140, db_index=True)
    since_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(
        choices=STATUS_SET, default=WAITING, max_length=10, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    tweet_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)

    WAITING = "waiting"
    PROCESSING = "processing"
    FINISHED = "finished"
    STATUS_SET = (
        (WAITING, "待ち"),
        (PROCESSING, "処理中"),
        (FINISHED, "完了"),
    )
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    text = models.CharField(max_length=140, db_index=True)
    status = models.CharField(
        choices=STATUS_SET, default=WAITING, max_length=10, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class CoOccurrence(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.PROTECT)
    biterm = models.ForeignKey(Biterm, on_delete=models.PROTECT)
    frequency = models.IntegerField()

    def __str__(self):
        return "({0},{1}) = {2}".format(self.biterm.word_i.char_string, self.biterm.word_j.char_string, self.hashtag.name)
