import uuid
from django.db import models


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=100)
  
    def __str__(self):
        return self.username
    
class DocumentsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_name = models.CharField(max_length=255)
    userid = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # FK to Django's User model.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document_name
    