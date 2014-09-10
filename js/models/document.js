var app = app || {};

app.Document = Backbone.Model.extend({
  defaults: {
    title: '',
    organization: '',
    words: 0,
    word_counts: [],
  },
  urlRoot: ROOT + '/documents'
});