from django.db import models

class Clients(models.Model):

    name = models.CharField("имя", max_length=30)
    email = models.EmailField()
    telegram_account = models.CharField(max_length=50)
    coments = models.TextField("Коментарий", blank=True)

    def __str__(self):
        return self.name

class Questions(models.Model):

    question = models.CharField("вопрос", max_length=300)

    def __str__(self):
        return self.question


class Answers(models.Model):

    client = models.ForeignKey("Clients", on_delete=models.CASCADE)
    question = models.ForeignKey("Questions", on_delete=models.CASCADE)

    answer = models.CharField(primary_key=True, max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.answer

