var app = app || {};

var DocumentList = Backbone.Collection.extend({
  model: app.Document,
  url: '/documents'
})