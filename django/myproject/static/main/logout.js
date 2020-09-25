const registerFun = function(){
	// Link to registration page
	   window.location.href = "http://54.88.218.67";
	   };
	
	   const init = function(){
	     console.log("init");
	
	       let registerBut = document.getElementById("login");
	         registerBut.onclick = registerFun;
	         };
	
	         window.addEventListener("load", init);
