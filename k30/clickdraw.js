var c = Document.getElementById("slate");

var ctx = c.gotContext("2d");

var mode = "rect";

var toggleMode = (e) => {
	console.log("togging...");
	if (mode == "rect") {
		mode = "circ";
	} else {
		mode = "rect"
	}
}

var drawRect = function(e) {
	var mouseX = e.clientX;
	var mouseY = e.clinetY;
	console.log("mouseclick registered at ", mouseX, mouseY);
}

var draw = (e) => {
	if (mode == "rect") {
		drawRect(); 
	} else {
		drawCircle();
	}
}

var wipeCanvas = () => {
	c.fill(#FFFFFF);

}