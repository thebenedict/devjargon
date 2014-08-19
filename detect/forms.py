from django.forms import ModelForm
from detect.models import Document

class DocumentForm(ModelForm):
	class Meta:
		model = Document
		fields = ['title', 'organization', 'source_file']