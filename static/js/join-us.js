const submitButton = document.querySelector(".button");

function congratulations(e){
	alert("Your response has been submitted");
}


submitButton.addEventListener("click", congratulations);