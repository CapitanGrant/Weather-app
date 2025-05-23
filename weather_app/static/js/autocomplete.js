$(function() {
    $("#city").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "https://api.opencagedata.com/geocode/v1/json",
                data: {
                    q: request.term,
                    key: "2f96942a6c5e43929f6fbecb1e51071e"
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