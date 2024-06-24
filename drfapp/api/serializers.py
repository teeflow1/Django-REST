from rest_framework import serializers
from drfapp.models import Account, Cinema

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = '__all__'
        
    
    
    
class CinemaSerializer(serializers.ModelSerializer):
    
    class Meta:
         model = Cinema
         fields = '__all__'
        
         
        
        
    
   
    
