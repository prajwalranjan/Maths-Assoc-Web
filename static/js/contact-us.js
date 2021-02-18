const submitButton = document.querySelector(".submit-contact");

function congratulations(e){
	alert("Your response has been submitted");
}


submitButton.addEventListener("click", congratulations);