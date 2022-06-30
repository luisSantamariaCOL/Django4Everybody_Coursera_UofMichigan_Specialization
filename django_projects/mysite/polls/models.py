from django.db import models

class Question(models.Model):
    # Django automaticamente genera una llave primaria, por eso
    # no se necesita crearla.
    question_text = models.CharField(max_length=255) # CharField = Varchar
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    # CASCADE: Cuando se borre una pregunta, se borraran todas las choices que esa pregunta tenga
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
