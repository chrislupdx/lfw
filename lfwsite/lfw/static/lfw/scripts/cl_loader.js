let dropdown = document.querySelector('#dropdownselector')

dropdown.addEventListener('change',
  function() {
    alert(dropdown.value)
})