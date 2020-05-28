from django.contrib.auth.models import User


class EmailBackend(object):

	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(email=username)
		except User.MultipleObjectsReturned:
			user = User.objects.filter(email=username).order_by('id').first()
		except User.DoesNotExist:
			return None

		if getattr(user, 'is_active') and user.check_password(password):
			return user
		return None

	#if django user model is to be ignored(custom check)
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None