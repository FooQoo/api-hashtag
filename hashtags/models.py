import uuid
from django.db import models

class Hashtag(models.Model):
    tag_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=140, db_index=True)

    def __str__(self):
        return self.name

class SearchTask(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    WAITING = "waiting"
    PROCESSING = "processing"
    FINISHED = "finished"
    STATUS_SET = (
        (WAITING, "待ち"),
        (PROCESSING, "処理中"),
        (FINISHED, "完了"),
    )
    hashtag = models.ForeignKey(Hashtag, on_delete=models.PROTECT)
    since_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(choices=STATUS_SET, default=WAITING, max_length=10, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hashtag.name