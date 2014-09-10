var app = app || {};

var ROOT = 'http://api.devjargon.org'

$(':button').click(function(){
    var formData = new FormData($('form')[0]);
    $.ajax({
        url: 'http://api.devjargon.org/documents/',
        data: formData,
        type: 'POST',
        xhr: function() {
            return $.ajaxSettings.xhr();
        },
        success: function(data) {
        	destination = "/documents/" + data['id']
        	window.location.href = destination;
        },
        error: function(e) {
        	//TODO
        	console.log('error')
        },
        cache: false,
        contentType: false,
        processData: false
    });
});

$(function() {
	new app.AppView();
});