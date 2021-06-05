
create_global_event_listener('click', 'custom_dropdown_button', handle_custom_select, 'class')
create_global_event_listener('click', 'fake_option', update_select_with_custom, 'class')

function handle_custom_select(activated_custom_select){
  // Reveal/Hide the custom select options
  custom_options_containter_id = activated_custom_select.getAttribute('data-reference-id')
  custom_options_container = document.getElementById(custom_options_containter_id)
  custom_options_container.classList.toggle("show");

  // Close the dropdown menu if user clicks outside
  window.onclick = function(event) {
    if (!event.target.matches('.custom_dropdown_button')) {
      custom_options_container.classList.toggle("show")
    }
  }
}

function update_select_with_custom(my_trigger) {
    // console.log('in the code driven select option change function')
    target_select_id = my_trigger.getAttribute('data-reference-id')
    target_select = document.getElementById(target_select_id)
    target_option_value = my_trigger.getAttribute('data-reference-option')
    target_select.value = target_option_value

    // Set fake dropdown select elemet's text to match the chosen selection
    set_dropdown_text(my_trigger)
}

function set_dropdown_text(chosen_option){
  new_value = chosen_option.innerHTML
  target_id = chosen_option.getAttribute('data-reference-id-button')
  target = document.getElementById(target_id)
  
  target.innerHTML = new_value
}