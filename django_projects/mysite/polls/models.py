from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    # Django automaticamente genera una llave primaria, por eso
    # no se necesita crearla.
    question_text = models.CharField(max_length=255) # CharField = Varchar
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        # Deterimna si la pregunta como maximo un dia de antiguedad
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # CASCADE: Cuando se borre una pregunta, se borraran todas las choices que esa pregunta tenga
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text
