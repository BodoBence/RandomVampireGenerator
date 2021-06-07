console.log("first line of custom_select.js")

create_global_event_listener('click', 'dropdown_button', handle_custom_select, 'class')
create_global_event_listener('click', 'fake_option', update_select_with_custom, 'class')

function handle_custom_select(activated_custom_select){
  // Reveal/Hide the custom select options
  custom_options_containter_id = activated_custom_select.getAttribute('data-reference-id')
  custom_options_container = document.getElementById(custom_options_containter_id)
  custom_options_container.classList.toggle("show");

  current_custom_arrow = activated_custom_select.parentElement.children.getElementsByClass("custom_arrow")
  console.log(current_custom_arrow)
  animation_rotate_element(current_custom_arrow[0])

  add_close_listener(custom_options_container, activated_custom_select)
}

function update_select_with_custom(my_trigger) {
    console.log('updating the hidden select field with the fake selects manual input')
    target_select_id = my_trigger.getAttribute('data-reference-id')
    target_select = document.getElementById(target_select_id)
    target_option_value = my_trigger.getAttribute('data-reference-option')
    
    target_select.value = target_option_value
    console.log("the new selcetion value is:")
    console.log(target_select.value)

    // Set fake dropdown select elemet's text to match the chosen selection
    set_dropdown_text(my_trigger)
    // Close the dropdown
    my_trigger.parentElement.classList.toggle("show")
}

function set_dropdown_text(chosen_option){
  new_value = chosen_option.innerHTML
  target_id = chosen_option.getAttribute('data-reference-id-button')
  target = document.getElementById(target_id).firstElementChild
  console.log(target)

  target.innerHTML = new_value
}

function add_close_listener(open_dropdown, button){
  window.addEventListener('click', e => {
    if (e.target != button) {
      open_dropdown.classList.remove("show")
    }
  })
}

function animation_rotate_element(current_trigger){
  console.log(current_trigger)
  animation_target = current_trigger.nextElementSibling
  console.log(animation_target)
  
  if (animation_target.getAttribute('class') == 'custom_arrow') {

      if (animation_target.style.transform == "rotate(225deg)") {
          animation_target.style.transform = "rotate(45deg)"
      } else {
          animation_target.style.transform = "rotate(225deg)"
      }
  }
}
