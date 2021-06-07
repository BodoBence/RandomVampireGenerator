console.log("first line of custom_select.js")

create_global_event_listener('click', 'dropdown_button', handle_custom_select, 'class')
create_global_event_listener('click', 'fake_option', update_select_with_custom, 'class')

function handle_custom_select(activated_custom_select){
  console.log("Handling custom dropdown")

  // Reveal/Hide the custom select options
  let custom_options_containter_id = activated_custom_select.getAttribute('data-reference-id')
  let custom_options_container = document.getElementById(custom_options_containter_id)

  custom_options_container.classList.toggle("show");

  // Trigeer cusotm arrow animaiton
  toggle_arrow_animation(activated_custom_select)

  // Add close listener
  add_close_listener(custom_options_container, activated_custom_select)
}

function update_select_with_custom(my_trigger) {
  console.log('updating the hidden select field with the fake selects manual input')

  let target_select_id = my_trigger.getAttribute('data-reference-id')
  let target_select = document.getElementById(target_select_id)
  let target_option_value = my_trigger.getAttribute('data-reference-option')

  target_select.value = target_option_value

  // Set fake dropdown select elemet's text to match the chosen selection
  set_dropdown_text(my_trigger)

  // Close the dropdown
  my_trigger.parentElement.classList.toggle("show")

  // Trigeer cusotm arrow animaiton
  toggle_arrow_animation(my_trigger)

}

function set_dropdown_text(chosen_option){
  let new_value = chosen_option.innerHTML
  let target_id = chosen_option.getAttribute('data-reference-id-button')
  let target = document.getElementById(target_id).firstElementChild
  console.log(target)

  target.innerHTML = new_value
}

function add_close_listener(open_dropdown, button){
  window.addEventListener('click', e => {
    if (e.target != button) {
      // Clsoe the dropdown menu
      open_dropdown.classList.remove("show")
      
      // Trigeer cusotm arrow animaiton
      toggle_arrow_animation(button)
    }
  })
}

function toggle_arrow_animation(current_trigger){
  // console.log('getting animation target')
  let current_target_id = current_trigger.getAttribute("data-reference-id-arrow")
  let current_target = document.getElementById(current_target_id)

  current_target.classList.toggle("animation_rotate")
  // console.log('the animation target is')
  // console.log(current_target)
}
