console.log("first line of generator.js")

// synchronize manual/random switch with manual input in the input field

create_global_event_listener("input", "selection_driver", toggle_input_field, 'class')
create_global_event_listener("change", "manual_name_selection", selection_based_sync, 'name')
create_global_event_listener("change", "manual_age_selection", selection_based_sync, 'name')
create_global_event_listener("click", "button_input_contianer_visibility", accordion_motion, 'id')
create_global_event_listener("click", "button_load_defaults", load_default_input_values, 'id')
create_global_event_listener("change", "dropdown_selectors", animation_rotate_element, 'class')
create_global_event_listener("click", "dropdown_selectors", animation_rotate_element, 'class')

// Functions for the dropdown selectors

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

// Functions for the Input sliders (generator_inputs.html)

function accordion_motion(current_trigger){
    target_id = current_trigger.getAttribute("data-target-id")
    target_class_1 = current_trigger.getAttribute("data-target-class-1")

    toggle_class_based_animation(target_id, target_class_1, true)    

    // target_class_2 = current_trigger.getAttribute("data-target-class-2")
    // target_class_3 = current_trigger.getAttribute("data-target-class-3")
}


function toggle_input_field(current_driver){
    console.log("manual / random switch triggered")
    referred_element_id = current_driver.getAttribute("data-driver-reference")
    referred_element = document.getElementById(referred_element_id)
    referred_element.value = "Manual"
}

function selection_based_sync(current_selector){
    console.log("doing selection based sync to default value")

    focused_value = current_selector.getAttribute("data-input-focus")
    default_value = current_selector.getAttribute("data-input-default")

    conencted_field_reference = current_selector.getAttribute("data-input-reference")
    conencted_field = document.getElementById(conencted_field_reference)

    if (current_selector.value == focused_value){
        conencted_field.value = default_value
    }

}

function load_default_input_values(){
    console.log('changing input values to defaults')
    // Dropdowns
    document.getElementById('selection_clan').value = 'Malkavian'
    document.getElementById('selection_generation').value = 'Random'
    document.getElementById('selection_age').value = 'Random'
    document.getElementById('selection_name').value = 'Random'

    // Sliders
    document.getElementById('slider_discipline').value = 20
    document.getElementById('slider_physical').value = 50
    document.getElementById('slider_mental').value = 50
    document.getElementById('slider_social').value = 50

    // Input fields
    document.getElementById('manual_name_input_id').value = 'Fruzsi'
    document.getElementById('manual_age_input_id').value = 300

}
