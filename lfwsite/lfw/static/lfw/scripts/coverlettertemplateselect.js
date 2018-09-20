let templatedropdown = document.querySelector('#coverletterselector')
let textarea = document.getElementsByName('coverlettercopy')[0];

let coverletters = null
let coverletter = null

templatedropdown.addEventListener('change',
  function() {
    let coverletterID = parseInt(templatedropdown.value)
    if (!coverletters) {
    	console.log('first and only fetch for jobapps')
		fetch('http://localhost:8000/coverlettertext_loader/')
		  
		  .then(function(response) {
		  	return response.json()
		  })
		  .catch(function(error) {
		  	console.log(error)
		  })
		  .then(function(response){
		  	coverletters = JSON.parse(response)
			coverletter = coverletters.find((cl) => cl.pk == coverletterID)
			console.log(coverletter)
			textarea.innerText = coverletter.fields.coverlettertext
		  })
	} else {
	}

});
