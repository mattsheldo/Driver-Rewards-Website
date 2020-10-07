const registerFun = function(){
	//Link to registration page
	window.location.href = "logout/";
};
	
const init = function(){
	console.log("init");
	
	let registerBut = document.getElementById("logout");
	registerBut.onclick = registerFun;
};
	
window.addEventListener("load", init);
