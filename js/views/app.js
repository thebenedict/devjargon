var app = app || {};

app.AppView = Backbone.View.extend({
  el: '#devjargon-app',

  initialize: function() {
    // this.render();
    // this.loadData();
    // app.Bins.loadHistogram();

    // this.renderDocument(6);
    // var circle = d3.selectAll("circle");
    // circle.data([10, 20, 40]);
    // circle.attr("r", function(d) { return d; });
  },

  // events: {
  //   'mouseenter .filenode-row': 'toggleNode',
  //   'mouseleave .filenode-row': 'toggleNode'
  // },

  // toggleNode: function(e) {
  //   currentNode = app.FileNodes.findWhere({'name': $(e.currentTarget).data('filenode-name')})
  //   $('tr[data-filenode-name=' + currentNode.get('name') + ']').toggleClass('selected');

  //   var c = this.$histogram.highcharts();
  //   c.series[0].data[currentNode.bin().get('id')].select();
  // },

  // renderDocument: function( id ) {
  //   var doc = new app.Document({'id': id});
  //   doc.fetch();
  //   var view = new app.DocumentView({ model: doc });
  // },

  // addFile: function( file ) {
  //   var view = new app.FileView({ model: file });
  //   $('.file-table-body').append( view.render().el );
  // },

  // loadData: function() {
  //   this.$('.filenode-table-body, .file-table-body').html('');
  //   app.FileNodes.each(this.addFileNode, this);
  //   app.Files.each(this.addFile, this);
  // },

  // render: function() {
  //   //placeholder
  // }
});