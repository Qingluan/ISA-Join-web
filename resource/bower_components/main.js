
$("div#new-user").hover(
    function(){
	var checked = $(this).attr("moved");
	if (checked == "un"){	
            $(this).animate({
	        'left' :"-=30%"
	    },1000,function(){
	        $("div#user-panel").collapse('toggle').attr("moved","ok");
	    }).attr("moved","ok");
	}
    }
);
