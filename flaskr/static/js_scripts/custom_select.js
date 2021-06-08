console.log("first line of custom_select.js")

create_global_event_listener('click', 'dropdown_button', handle_custom_select, 'class')
create_global_event_listener('click', 'fake_option', update_select_with_custom, 'class')
window.addEventListener('click', close_dropdowns)

function close_dropdowns(e){
  // by definition addEventListener first passes over the event as a parameter
  
  console.log('window click')
  console.log(e.target)
  // Quit in favour of other click tied functionality
  if (e.target.classList.contains('dropdown_button')){
    return
  }

  if (e.target.classList.contains('dropdown_content')){
    return
  }

  let dropdowns = document.getElementsByClassName('dropdown_content')
  
  if (dropdowns.length == 0){
    return
  }

  for (let index = 0; index < dropdowns.length; index++) {
    const element = dropdowns[index];
    if (element.classList.contains('show')){
      element.classList.remove('show')
      let respective_button = document.getElementById(element.getAttribute('data-reference-id-button'))
      toggle_arrow_animation(respective_button)
    }
  }
}

// window.addEventListener('click', close_dropdown)

// function handle_outside_clock(trigger_button, dropdown_container){
//   console.log("inside handle outside click function")
//   window.addEventListener('click', close_dropdown)

//   function close_dropdown(){
//     console.log('trigger:' + this + ' is activated')

//     if (this == trigger_button){
//       window.removeEventListener('click', close_dropdown)
//       console.log('returned because the button was clicked')
//       return
//     }

//     if (this == dropdown_container){
//       window.removeEventListener('click', close_dropdown)
//       console.log('returned because the dropdown was clicked')
//       return
//     }

//     dropdown_container.classList.remove("show")
//     toggle_arrow_animation(trigger_button)
//     console.log('closed:' + dropdown_container)
//     window.removeEventListener('click', close_dropdown)
//   }
// }

function handle_custom_select(activated_custom_select){
  console.log("Handling custom dropdown")

  // Reveal/Hide the custom select options
  let custom_options_containter_id = activated_custom_select.getAttribute('data-reference-id')
  let custom_options_container = document.getElementById(custom_options_containter_id)

  custom_options_container.classList.toggle("show");
  console.log("opened the dropdown")

  // Trigeer cusotm arrow animaiton
  toggle_arrow_animation(activated_custom_select)

  // Add close listener
  // handle_outside_clock(activated_custom_select, custom_options_container)
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
  console.log(my_trigger.parentElement)
  my_trigger.parentElement.classList.toggle("show")

  // Trigeer cusotm arrow animaiton
  toggle_arrow_animation(my_trigger)

  // Remove outside event listneer
  // window.removeEventListener('click', close_dropdown)
}

function set_dropdown_text(chosen_option){
  let new_value = chosen_option.innerHTML
  let target_id = chosen_option.getAttribute('data-reference-id-button')
  let target = document.getElementById(target_id).firstElementChild
  console.log(target)

  target.innerHTML = new_value
}

function toggle_arrow_animation(current_trigger){
  // console.log('getting animation target')
  let current_target_id = current_trigger.getAttribute("data-reference-id-arrow")
  let current_target = document.getElementById(current_target_id)

  current_target.classList.toggle("animation_rotate")
  // console.log('the animation target is')
  // console.log(current_target)
}
