from Tkinter import *

from django.db import models


class firstCity(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class secondCity(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    from Tkinter import *

    master = Tk()

    def makeentry(parent, caption, width=None):
        Label(parent, text=caption).pack(side=LEFT)
        entry = Entry(parent)
        if width:
            entry.config(width=width)
        entry.pack(side=LEFT)
        return entry

    parent = master

    user = makeentry(parent, "First City:", 30)
    password = makeentry(parent, "Second City:", 30)
    content = StringVar()

    text = content.get()
    content.set(text)
    mainloop()


    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
