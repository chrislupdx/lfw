let dropdown = document.querySelector('#dropdownselector')
let clframe = document.getElementById("clframe");
let iframe = document.getElementById("coverletter_window");

let jobapps = null
let jobapp = null 

dropdown.addEventListener('change',
  function() {
    let jobappID = parseInt(dropdown.value)
    if (!jobapps) {
    	console.log('first and only fetch for jobapps')
		fetch('http://localhost:8000/jobapp_loader/')
		  
		  .then(function(response) {
		  	return response.json()
		  })
		  .catch(function(error) {
		  	console.log(error)
		  })
		  .then(function(response){
		  	jobapps = JSON.parse(response)
		  	urldisplay(jobappID)
		  })
	} else {
		console.log('finding jobapp from eiframeisting jobapps')
	  	urldisplay(jobappID)
	}
});

function urldisplay(jobappID){
	jobapp = findJobapp(jobappID)
	console.log(jobapp)
	console.log(jobapp.fields.url)
	if (jobapp.fields.url) {
		console.log('url exists: ' + jobapp.fields.url)
		if (window.getComputedStyle(clframe).display === 'none') {
	  		console.log('display is none')
	      	clframe.style.display = "block";
	      	iframe.src = jobapp.fields.url;
	  	} else {
	      clframe.style.display = "none";
	  	}	
	} else {
	    clframe.style.display = "none";
	}	

// i don't think this logic is floipping the switch
	
}


function findJobapp(id) {
	return jobapps.find(item => item.pk == id)
}