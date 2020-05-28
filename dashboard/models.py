from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text

    def user_give_opinion(self, user):
        """
        Returns False if user has already given opinion, else True
        """
        user_opinion = user.opinion_set.all()
        qs = user_opinion.filter(poll=self)
        if qs.exists():
            return False
        return True

    @property
    def num_opinion(self):
        return self.opinion_set.count()

    def get_results_dict(self):
        """
        Returns a list of objects in the form:
        [
            # for each related choice
            {
                'text': choice_text,
                'num_votes': number of votes on that choice
                'percentage': num_votes / poll.num_votes * 100
            }
        ]
        """
        res = []
        for choice in self.choice_set.all():
            d = {}
            d['text'] = choice.choice_text
            d['num_opinion'] = choice.num_opinion
            if not self.num_opinion:
                d['percentage'] = 0
            else:
                d['percentage'] = choice.num_opinion / self.num_opinion * 100
            res.append(d)
        return res


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.poll.text[:25], self.choice_text[:25])

    @property
    def num_opinion(self):
        return self.opinion_set.count()

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

