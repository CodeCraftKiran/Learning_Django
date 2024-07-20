from django import forms
from .models import Review
# class reviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages= {
#         "required": "This field required a name.",
#         "max_length": "Please enter a valid name.",
#     } )
#     review_text = forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
    
class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ["user_name", "rating"] 
        # exclude = ["review_text"]
        
        labels = {
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating": "Your_Rating",
        }
        
        error_messages = {
            "user_name": {
                "required": "This field required a name.",
                "max_length": "Please enter a valid name.",
            }
        }