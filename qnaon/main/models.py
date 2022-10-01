from django.db import models


class Question(models.Model):
    question_text = models.TextField('Текст вопроса', max_length=10000)
    question_title = models.CharField('Заголовок вопроса', max_length=200)
    question_pub_date = models.DateTimeField('Дата публикации вопроса')
    question_author = models.CharField('Автор вопроса', max_length=200)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField('Текст ответа', max_length=10000)
    answer_pub_date = models.DateTimeField('Дата публикации ответа')
    answer_author = models.CharField('Автор ответа', max_length=200)

    def __str__(self):
        return self.answer_text[:10]
