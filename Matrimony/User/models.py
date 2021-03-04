from django.db import models

#Personal Chat Model
class Chat_Box(models.Model):
    To_id = models.IntegerField()
    From_id = models.IntegerField()
    Message = models.TextField()
    def __str__(self):
        return 'Message'+str(self.id)

#Contact Us Model

class Contact_Us(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    Details = models.TextField()
    When = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Express Interest table model

class Express_Interest(models.Model):
    To_id = models.IntegerField()
    From_id = models.IntegerField()
    Message = models.TextField()

    def __str__(self):
        return self.Message

#feedback models

class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    Comment = models.TextField()
    When = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
#Image Gallery Model

class Image_Gallery(models.Model):
    Images = models.URLField()
    Pro_id = models.IntegerField()

    def __str__(self):

        id =str(self.id)
        return "Image"+id

class Created_For(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name
class Mariatal_Status(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name
class Body_Type(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Physical_Status(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Mother_Tongues(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Religions(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Castes(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Gothrams(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Zodiacs(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Stars(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Eating_Habits(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Drinking_Habits(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Smoking_Habits(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name


class Countries(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Cities(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class States(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Education_Table(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Occupations(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name
class Salary_Range(models.Model):
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name
class Kundla_Details(models.Model):
    Name = models.CharField(max_length=15)

# Profile Table Models

class Profile(models.Model):
    Pro_id = models.IntegerField()
    Profile_Creator_id = models.ForeignKey(Created_For, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Mariatal_Status_id = models.ForeignKey(Mariatal_Status , on_delete=models.CASCADE)
    Body_Type_id = models.ForeignKey(Body_Type,on_delete=models.CASCADE)
    Age = models.IntegerField()
    Physical_Status_id = models.ForeignKey(Physical_Status,on_delete=models.CASCADE)
    Height = models.FloatField()
    Weight = models.FloatField()
    Mother_Tongue_id = models.ForeignKey(Mother_Tongues,on_delete=models.CASCADE)
    Religion_id = models.ForeignKey(Religions,on_delete=models.CASCADE)
    Caste_id = models.ForeignKey(Castes,on_delete=models.CASCADE)
    Gothram_id = models.ForeignKey(Gothrams,on_delete=models.CASCADE)
    Zodiac = models.ForeignKey(Zodiacs,on_delete=models.CASCADE)
    Star = models.ForeignKey(Stars,on_delete=models.CASCADE)
    Eating_habit = models.ForeignKey(Eating_Habits,on_delete=models.CASCADE)
    Drinking_habit = models.ForeignKey(Drinking_Habits,on_delete=models.CASCADE)
    Smoking_habit = models.ForeignKey(Smoking_Habits,on_delete=models.CASCADE)
    Country = models.ForeignKey(Countries,on_delete=models.CASCADE)
    City = models.ForeignKey(Cities,on_delete=models.CASCADE)
    State = models.ForeignKey(States,on_delete=models.CASCADE)
    Education = models.ForeignKey(Education_Table,on_delete=models.CASCADE)
    Occupation = models.ForeignKey(Occupations,on_delete=models.CASCADE)
    Employeed_in = models.CharField(max_length=50)
    Salary = models.ForeignKey(Salary_Range,on_delete=models.CASCADE)
    Mobile_No = models.CharField(max_length=15)
    Images = list(models.ImageField)
    About_Me =  models.TextField()
    Required_Details = models.TextField()
    Membership = models.CharField(max_length=20)
    Paid_Status = models.BooleanField(default=False)
    Start_Date= models.DateTimeField()
    End_Date = models.DateTimeField()
    Email_ID = models.CharField(max_length=100)
    Profession = models.CharField(max_length=20)
    Address = models.TextField()
    Pincode = models.CharField(max_length=10)
    Phone_No = models.CharField(max_length=15)
    Paid_Date = models.DateTimeField()
    Login_Status = models.CharField(max_length=10)










    
