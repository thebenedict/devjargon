var app = app || {};

app.WordCount = Backbone.Model.extend({
  defaults: {
    word__display: '',
    count: 0
  },
});