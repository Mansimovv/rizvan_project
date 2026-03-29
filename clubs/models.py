from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Membership(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	joined_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'club')

	def __str__(self):
		return f"{self.user.username} - {self.club.name}"
