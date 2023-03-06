from django import forms
from admissions.models import Student

# def check_contact(value): #1 method
#     if len(str(value))!=10:
#         raise forms.ValidationError(['Invalid number'])
#     return value

class StudentModelForm(forms.ModelForm):
    # contact=forms.IntegerField(validators=[check_contact])
    class Meta:
        model = Student
        fields='__all__'
    def clean_contact(self): #2 method
        contact = self.cleaned_data['contact']
        if len(str(contact))!=10:
            raise forms.ValidationError(['Invalid number'])
        return contact
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len((name))<3:
            raise forms.ValidationError(["minimum 3 characters required"])
        return name
    
    def clean_fathername(self):
        fathername = self.cleaned_data['fathername']
        if len(fathername)<3:
            raise forms.ValidationError(["Invalid father name"])
        return fathername
    
    def clean_classname(self):
        classname = self.cleaned_data['classname']
        if (classname)>10:
            raise forms.ValidationError(["not school student"])
        return classname
    
    
    # 3def clean(self): #3 method
    #     cleaned_data=super().clean()
        
    #     name =self.cleaned_data['name' ]
    #     fathername =self.cleaned_data['fathername' ]
    #     classname = self.cleaned_data['classname' ]
    #     contact = self.cleaned_data['contact' ]
    #     if len(name)<3:
    #         raise forms.ValidationError(["minimum 3 characters required"])
    #     if len(fathername)< 7:
    #         raise forms.ValidationError(['Post Should Contain a minimum of 10 characters'])
    #     if len(classname)>10:
    #         raise forms.ValidationError([' not studie in school'])
    #     if len(contact)==10:
    #         raise forms.ValidationError(['Invalid number'])
        
            
    

class VendorForm(forms.Form):
    name=forms.CharField()
    address=forms.CharField()
    contact=forms.CharField()
    item=forms.CharField()