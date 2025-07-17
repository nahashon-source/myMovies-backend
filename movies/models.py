from django.db import models

CATEGORY_CHOICES = [
    ('movie', 'Movie'),
    ('series', 'Series'),
]

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    release_year = models.PositiveIntegerField()
    poster = models.URLField()  # Placeholder; upgrade to ImageField later
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
