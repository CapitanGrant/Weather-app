$(function() {
    $("#city").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "https://api.opencagedata.com/geocode/v1/json",
                data: {
                    q: request.term,
                    key: "08cd053b55a64895a3435d7dc7264d56"
                },
                success: function(data) {
                    response(data.results.map(function(item) {
                        return item.formatted;
                    }));
                }
            });
        },
        minLength: 2
    });
});