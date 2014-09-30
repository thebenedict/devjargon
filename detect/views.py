import json
from django.core import serializers
from django.views.generic import DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from braces.views import JSONResponseMixin, CsrfExemptMixin
from detect.models import Document
from detect.forms import DocumentForm

class DocumentView(JSONResponseMixin, DetailView):
    model = Document

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        counts = self.object.wordcount_set.all().values('word__display', 'count')

        context_dict = {
            u"id": self.object.id,
            u"words": self.object.total_word_count,
            u"source_file": self.object.source_file.url,
            u"word_counts": list(counts),
        }

        return self.render_json_response(context_dict)

class DocumentListView(JSONResponseMixin, CsrfExemptMixin, ListView):
    model = Document

    def get(self, request, *args, **kwargs):
        return self.render_json_object_response(self.get_queryset())

    def post(self, request, *args, **kwargs):
        form_data = DocumentForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        print form_data
        print form_data.errors
        d = form_data.save(commit=False)
        d.total_word_count = 0
        try:
            d.save()
            context_dict = {
                u"id": d.id,
                u"words": d.total_word_count,
                u"source_file": d.source_file.url,
            }
            return self.render_json_response(context_dict)
        except Exception as e:
            msg = "document could not be saved: %s" % e
            context_dict = {
                u"status": 400,
                u"error": msg,
            }            
            return self.render_json_response(context_dict, status=400)