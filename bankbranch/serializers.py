from rest_framework import serializers
from . models import BankBranch

class BranchSearchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BankBranch
		#fields = ('id', 'url', 'bank', 'state', 'location', 'address', 'email', 'phone' )
		fields = '__all__'
