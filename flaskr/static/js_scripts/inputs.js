console.log("first line of generator.js")

// synchronize manual/random switch with manual input in the input field

create_global_event_listener("input", "selection_driver", toggle_input_field, 'class')
create_global_event_listener("change", "manual_name_selection", selection_based_sync, 'name')
create_global_event_listener("change", "manual_age_selection", selection_based_sync, 'name')
create_global_event_listener("click", "button_input_contianer_visibility", accordion_motion, 'id')
create_global_event_listener("click", "button_load_defaults", load_default_input_values, 'id')
create_global_event_listener("change", "slider", display_slider_value, "class")
correct_overflow()

// Corrects overflow for the input container animation
function correct_overflow(){
    current_element = document.getElementById("input_container_id")
    console.log(current_element.style.overflow)

    current_element.addEventListener("transitionend", () => {
        console.log("input container transitioned")
        if (current_element.classList.contains("animation_close") == false){
            current_element.style.overflow = "initial"
            console.log("chanegd overflow to:")
            console.log(current_element.style.overflow)
        }
    })
}


// Functions for the acordion motion of the input container

function accordion_motion(current_trigger){
    target_id = current_trigger.getAttribute("data-target-id")
    target_class_1 = current_trigger.getAttribute("data-target-class-1")
    target_element = document.getElementById(target_id)

    // Toggle animation
    target_element.classList.toggle(target_class_1)
    target_element.style.overflow = "hidden"
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

// Functions for the Input sliders (generator_inputs.html)

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


function display_slider_value(current_slider){
    console.log('slidering')
    console.log(current_slider)
    target_id = current_slider.getAttribute('data-reference-id')
    target_element = document.getElementById(target_id)
    new_value = current_slider.value

    target_element.innerHTML = new_value
}