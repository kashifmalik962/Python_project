function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/location"; // Adjust the URL as per your Flask route
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data && data.locations) {
            var locations = data.locations;
            for (var i = 0; i < locations.length; i++) {
                var opt = '<option>' + locations[i].split("_")[1] + '</option>'; // Corrected line
                console.log(opt)
                $('#uiLocations').append(opt);
            }
        }
    });
     
}
window.onload = onPageLoad;