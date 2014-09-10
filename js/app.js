var app = app || {};

var ROOT = 'http://api.devjargon.org'

$(function() {
	new app.AppView();

    $('#submit-file').click(function(){
        var formData = new FormData($('form')[0]);
        $.ajax({
            url: 'http://api.devjargon.org/documents/',
            data: formData,
            type: 'POST',
            xhr: function() {
                return $.ajaxSettings.xhr();
            },
            beforeSend: function() {
                $('#submit-file').prop('disabled', true);
                $('#submit-file').prop('value', 'Finding jargon...')
            },
            success: function(data) {
                destination = "#/documents/" + data['id']
                window.location.href = destination;
            },
            error: function() {
                $('#submit-file').prop('value', 'An error occurred')
                setTimeout(function() { 
                    window.location.href = "/";
                }, 2000);
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

    $(document).on('click', '#start-over', function() {
        window.location.href = "/";
    });    
});