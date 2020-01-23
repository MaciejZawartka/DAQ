	var g1, g2, g3, g4;
	document.addEventListener("DOMContentLoaded", function(event) {
	    g1 = new JustGage({
		id: "g1",
		value: {{temp}},
		valueFontColor: "black",
		min: -10,
		max: 50,
		title: "Temperatura",
		label: "Celciuszy"
	});
	    g2 = new JustGage({
		id: "g2",
		value: {{press}},
		valueFontColor: "black",
		min: 900,
		max: 1100,
		title: "Cisnienie",
		label: "%"
	});
	    g3 = new JustGage({
		id: "g3",
		value: {{temp2}},
		valueFontColor: "black",
		min: -10,
		max: 50,
		title: "Temperatura",
		label: "Celciuszy"
	});
	    g4 = new JustGage({
		id: "g4",
		value: {{press2}},
		valueFontColor: "black",
		min: 900,
		max: 1100,
		title: "Cisnienie",
		label: "%"
	});
  });
