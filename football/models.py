from django.db import models

#dummy trans
_ = lambda x: x

class Season(models.Model):
    """
    """
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)

    def __unicode__(self):
        return self.name


class Club(models.Model):
    """
    """
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)

    def __unicode__(self):
        return self.name


class Competition(models.Model):
    """
    """
    TYPES = (
        ('LEA', _('League')),
        ('CUP', _('Cup')),
    )

    season = models.ForeignKey(Season)
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    type = models.CharField(max_length=3, choices=TYPES)

    def __unicode__(self):
        return self.name


class Round(models.Model):
    """
    """
    competition = models.ForeignKey(Competition)
    number = models.IntegerField()
    name = models.CharField(max_length=60, null=True, blank=True)

    def __unicode__(self):
        return 'ROUND %d Competition %s' % (self.number, self.competition)


class Match(models.Model):
    """
    """
    round = models.ForeignKey(Round)
    home_team = models.ForeignKey(Club, related_name='home_matches')
    away_team = models.ForeignKey(Club, related_name='away_matches')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    time = models.DateTimeField()

    def __unicode__(self):
        return '' % ()


#############


class LeagueTableRow(models.Model):
    position = models.IntegerField(default=1)
    club = models.ForeignKey(Club)
    wins = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
