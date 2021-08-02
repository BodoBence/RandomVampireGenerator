create_global_event_listener('click', 'custom_checkbox', update_input_checkbox, 'class')

function update_input_checkbox(current_trigger){
    input_checkbox_id = current_trigger.getAttribute('data-reference-id')
    input_checkbox_element = document.getElementById(input_checkbox_id)
    
    current_trigger.classList.toggle("custom_checkbox_clicked")

    if (input_checkbox_element.checked == true) {
        input_checkbox_element.checked = false
    } else {
        input_checkbox_element.checked = true
    }

    input_checkbox_element.dispatchEvent(new Event('change', { bubbles: true }))
}