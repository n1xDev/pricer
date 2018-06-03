var analyze = {
	result: 0,

	start: function() {
		document.getElementById("analyzer-main-block").style.display = "none";
		document.getElementById("analyzer-wait-block").style.display = "block";
        var mycategory = "";
        if(document.getElementById("radio_smarts").checked) mycategory = "smarts";
        else if(document.getElementById("radio_phones").checked) mycategory = "phones";
        else if(document.getElementById("radio_pads").checked) mycategory = "pads";
        $.ajax({
            url: '/analyze_data',
            data: 'category=' + mycategory,
            type: 'POST',
            success: function(response) {
                console.log("Success: " + response[0]);
                analyze.result = response;
                analyze.view(response);
            },
            error: function(error) {
                console.log("Error: " + error);
            }
        });
	},
	getRand: function() {
		return Math.random();
	},
	view: function(res) {
		this.result = res;
		this.result = JSON.parse(res);
		document.getElementById("analyzer-wait-block").style.display = "none";
		document.getElementById("analyzer-result-block").style.display = "block";
		if(res != "err") {
			document.getElementById("result-there").innerHTML = "данные скоро будут...";
			var html_result = "";
			var rnd = 0;
			for(var i = 0; i < this.result[0].length - 1; i++) {
				if(this.result[1][i] != "err") {
					if(this.result[0][i].indexOf("iPhone") < 0) html_result += '<p class="lead">' + this.result[0][i] + " -- " + this.result[1][i].toString() + '</p>';
				}
			}
			document.getElementById("result-there").innerHTML = html_result;
			document.getElementById("analyzer-result-block").style.marginBottom = "0";
			document.getElementById("analyzer-result-block").style.marginTop = "25%";
		}
		else  document.getElementById("result-there").innerHTML = "Извините, возникла ошибка, попробуйте ещё раз";
	},
}

window.onload = {

}