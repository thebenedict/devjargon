var app = app || {};

app.DocumentView = Backbone.View.extend({
  tagName: 'div',
  el: '.content',
  template: _.template( $('#document-template').html() ),

  initialize: function() {
    this.model.on('change', this.render, this);
    this.model.on('change', this.renderWordCounts, this);
  },

  renderWordCounts: function() {
    var bubble = d3.layout.pack()
      .sort(null)
      .size([400, 400])
      .children(function(d) { return d })
      .value(function(d) { return d.count })
      .padding(1.5);

    var svg = d3.select("svg");

    var node = svg.selectAll(".node")
        .data(bubble.nodes(this.model.get('word_counts'))
        .filter(function(d) { return !d.children; }))
      .enter().append("g")
        .attr("class", "node")
        .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
      
    node.append("circle")
      .attr("r", function(d) { return d.r })
      .style("fill", "indianred");

    node.append("title")
        .text(function(d) { return d.word__display + ": " + d.value; });

    node.append("text")
        .attr("dy", ".3em")
        .style("text-anchor", "middle")
        .style("font", "11px sans-serif")
        .text(function(d) { 
          if ((d.r / 4) > d.word__display.length) { return d.word__display + ": " + d.value; } 
        });
  },

  render: function() {
    this.$el.html( this.template( this.model.attributes ) );
    return this;
  },
});