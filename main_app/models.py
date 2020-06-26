from django.db import models
from django.urls import reverse

# Create your models here.
VILLAINS = (
    ('Cheetah', 'Cheetah'),
    ('Lex Luther', 'Lex Luther'),
    ('Green Gobblin', 'Green Gobblin'),
    ('Joker', 'Joker'),
    ('Mystic', 'Mystic')
)

class Power(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse ('powers_detail', kwargs={'pk': self.id})

class Hero(models.Model):
    heroname = models.CharField(max_length=100)
    realname = models.CharField(max_length=100)
    superpower = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.heroname
   
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hero_id': self.id})

class Fighting(models.Model):
    date = models.DateField()
    villain = models.CharField(max_length=50,
    choices=VILLAINS,
    default=VILLAINS [0][0]
    )

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_villain_display()} on {self.date}"

    class Meta:
        ordering = ['date']