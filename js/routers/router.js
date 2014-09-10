var app = app || {};

var JargonRouter = Backbone.Router.extend({
    routes: {
        "documents/:id": "getDocument",
    },

    getDocument: function(id) {
        var doc = new app.Document({'id': id});
        doc.fetch();
        var view = new app.DocumentView({ model: doc });
    }
})

app.TodoRouter = new JargonRouter();
Backbone.history.start();