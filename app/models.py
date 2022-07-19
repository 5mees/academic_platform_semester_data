from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=30)

    @property
    def sheets(self):
        subject = Subject.objects.get(name=self)
        sheets = subject.sheet_set.all()

        data = [{"pk": sheet.id,
                "name": sheet.name,
                 "content": sheet.content.url}
                for sheet in sheets]

        return data

    @property
    def references(self):
        subject = Subject.objects.get(name=self)
        references = subject.reference_set.all()

        data = [{"pk": reference.id,
                "name": reference.name,
                 "content": reference.content.url}
                for reference in references]

        return data

    @property
    def tutorials(self):
        subject = Subject.objects.get(name=self)
        tutorials = subject.tutorial_set.all()

        data = [{"pk": tutorial.id,
                "name": tutorial.name,
                 "content": tutorial.content.url}
                for tutorial in tutorials]

        return data

    @property
    def exams(self):
        subject = Subject.objects.get(name=self)
        exams = subject.exam_set.all()

        data = [{"pk": exam.id,
                "name": exam.name,
                 "content": exam.content.url}
                for exam in exams]

        return data

    def __str__(self):
        return self.name


class Sheet(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name


class Reference(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.FileField()

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.FileField()

    def __str__(self):
        return self.name


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.FileField()

    def __str__(self):
        return self.name
