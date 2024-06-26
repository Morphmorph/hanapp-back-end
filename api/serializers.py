from rest_framework import serializers
from .models import *



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16,min_length=8)

    class Meta:
        model = User
        fields = ['id','usertype','email','password']
    
 
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class VerifyOtp(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class AddressSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Address
        fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
    # street = serializers.ALL_FIELDS(source='user')
    # user = serializers.PrimaryKeyRelatedField(queryset=User.object.all())

    class Meta:
        model = UserDetails
        fields = '__all__'

class ProfileAddressSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=False,many=True,source = 'user.address_set')
    # userdetails = UserDetailsSerializer()
    class Meta:
        model = UserDetails
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guardian
        fields = '__all__'

class EducationBGSerializer(serializers.ModelSerializer):
      class Meta:
        model = EducationBg
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    # email = serializers.CharField(source='user.email')
    # first_name = serializers.CharField(source = 'userdetails.first_name')

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # post = PostSerializer(read_only=True,many=True)
    # user_profile = UserDetailsSerializer
    
    class Meta:
        model = User
        fields = '__all__'


class ApplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Apply
        fields = '__all__'

class BookmarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'

class UserDetailsSerializer2(serializers.ModelSerializer):
    # user = UserSerializer()
    # post = PostSerializer(many = True,read_only=True, source='user.post_set')
    # class Meta:
    #     model = UserDetails
    #     fields = ['post','first_name','last_name','mid_name']
    profile = UserDetailsSerializer(read_only=True,many=True,source = 'user.userdetails_set')
    company = CompanySerializer(read_only=True,many=True,source='user.company_set')
    applies = ApplySerializer(read_only=True,many=True,source='apply_set')
    bookmark = BookmarSerializer(read_only=True,many=True,source='bookmark_set')
    address = AddressSerializer(read_only=True,many=True,source='user.address_set')

    class Meta:
        model = Post
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    # profile = UserDetailsSerializer(read_only=True,many=True,source = 'user.userdetails_set')
    company = CompanySerializer(read_only=True,many=True,source = 'user.company_set')
    address = AddressSerializer(read_only=True,many=True,source = 'user.address_set')

    class Meta:
        model=  UserDetails
        fields = '__all__'
    
    
    # Edit profile with addresse Serializer I dont what Im doing murag wla no ge gamit
class UserDetailsAddressSerializer(serializers.Serializer):
    user_details = UserDetailsSerializer()
    address = AddressSerializer()

    def update(self, instance, validated_data):
        user_details_data = validated_data.get('user_details')
        address_data = validated_data.get('address')

        user_details = instance.get('user_details')
        address = instance.get('address')

        user_details_serializer = UserDetailsSerializer(user_details, data=user_details_data)
        if user_details_serializer.is_valid():
            user_details_serializer.save()

        address_serializer = AddressSerializer(address, data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()

        return instance

class EditProfilePicture(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['profile']




class AppliedSerializer(serializers.ModelSerializer):

    userdetails = UserDetailsSerializer(read_only=True,many=True,source = 'user.userdetails_set')
    address = AddressSerializer(read_only=True,many=True,source = 'user.address_set')
    guardian = GuardianSerializer(read_only=True,many=True,source = 'user.guardian_set')
    school = EducationBGSerializer(read_only=True,many=True,source = 'user.educationbg_set')
    user = UserSerializer()
    # post = PostSerializer()
    class Meta:
        model = Apply
        fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):
    userdetails = UserDetailsSerializer(read_only=True,many=True,source = 'userdetails_set')
    address = AddressSerializer(read_only=True,many=True,source = 'address_set')
    guardian = GuardianSerializer(read_only=True,many=True,source = 'guardian_set')
    school = EducationBGSerializer(read_only=True,many=True,source = 'educationbg_set')
    class Meta:
        model = User
        fields = '__all__'

class BookmarkUserPostSerializer(serializers.ModelSerializer):
    post = UserDetailsSerializer2()
    class Meta:
        model = Bookmark
        fields = '__all__'
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    post = UserDetailsSerializer2()
    user = StudentProfileSerializer()
    applicant = ApplicantSerializer(read_only=True,many=True,source = 'applicant_set')
    class Meta:
        model = Apply
        fields = '__all__'



class WebProfileSerializer(serializers.ModelSerializer):
    userdetails = UserDetailsSerializer(read_only=True,many=True,source = 'userdetails_set')
    address = AddressSerializer(read_only=True,many=True,source = 'address_set')
    guardian = GuardianSerializer(read_only=True,many=True,source = 'guardian_set')
    company = CompanySerializer(read_only=True,many=True,source = 'company_set')
    educationbg = EducationBGSerializer(read_only=True,many=True,source = 'educationbg_set')

    class Meta:
        model = User
        fields = '__all__'
