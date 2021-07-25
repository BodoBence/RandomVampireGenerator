create_global_event_listener('click', 'dropdown_button', handle_custom_select, 'class')
create_global_event_listener('click', 'fake_option', update_input_field_with_customs_value, 'class')
document.addEventListener('click', close_dropdowns)

function close_dropdowns(e){
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

function handle_custom_select(activated_custom_select){
  let custom_options_containter_id = activated_custom_select.getAttribute('data-reference-id')
  let custom_options_container = document.getElementById(custom_options_containter_id)

  custom_options_container.classList.toggle("show");

  if (window.innerHeight/2 < custom_options_container.offsetHeight){
    console.log('found phone')
    custom_options_container.classList.add('phone_custom_select_menu')
  }

  toggle_arrow_animation(activated_custom_select)
}

function update_input_field_with_customs_value(my_trigger) {

  let target_input_id = my_trigger.getAttribute('data-reference-id')
  let target_input = document.getElementById(target_input_id)
  let target_option_value = my_trigger.getAttribute('data-reference-option')
  let target_button_id = my_trigger.getAttribute('data-reference-id-button')
  let target_button = document.getElementById(target_button_id)

  target_input.value = target_option_value
  

  target_input.dispatchEvent(new Event('change', { bubbles: true }))

  set_dropdown_text(my_trigger)

  my_trigger.parentElement.classList.toggle("show")

  toggle_arrow_animation(target_button)
}

function set_dropdown_text(chosen_option){
  let new_value = chosen_option.innerHTML
  let target_id = chosen_option.getAttribute('data-reference-id-button')
  let target = document.getElementById(target_id).firstElementChild

  target.innerHTML = new_value
}

function toggle_arrow_animation(current_trigger){

  let current_target_id = current_trigger.getAttribute("data-reference-id-arrow")
  let current_target = document.getElementById(current_target_id)

  current_target.classList.toggle("animation_rotate")
}
