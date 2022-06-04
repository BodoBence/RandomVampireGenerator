create_global_event_listener('input', 'manual_age_input_id', toggle_input_field, 'id')
create_global_event_listener('input', 'manual_name_input_id', toggle_input_field, 'id')
create_global_event_listener('input', 'manual_calculation_input_id', toggle_input_field, 'id')

create_global_event_listener("change", "manual_name_selection", input_sync, 'name')
create_global_event_listener("change", "manual_age_selection", input_sync, 'name')
create_global_event_listener("change", "manual_calculation_selection", input_sync, 'name')

create_global_event_listener("input", "slider", display_slider_value, "class")
create_global_event_listener("change", "selection_theme", toggle_character_style, "id")

create_global_event_listener("click", "button_input_contianer_visibility", accordion_motion, 'id')
create_global_event_listener("click", "button_load_defaults", load_default_input_values, 'id')

create_global_event_listener("change", "selection_clan_id", toogle_generation_options, 'id')

correct_overflow()

// Corrects overflow for the input container animation
function correct_overflow(){
    current_element = document.getElementById("input_container_id")

    current_element.addEventListener("transitionend", () => {
        if (current_element.classList.contains("animation_close") == false){
            current_element.style.overflow = "initial"
        }
    })
}

// Functions for the acordion motion of the input container

function accordion_motion(current_trigger){
    target_id = current_trigger.getAttribute("data-target-id")
    target_class_1 = current_trigger.getAttribute("data-target-class-1")
    target_element = document.getElementById(target_id)

    // Prepare for the animation
    target_element.classList.add("animation_pre_smooth")    

    // Toggle animation
    target_element.classList.toggle(target_class_1)
    target_element.style.overflow = "hidden"

    // Cleanup
    function remove_animation_ease(){
        target_element.classList.remove("animation_pre_smooth")
        target_element.removeEventListener("webkitTransitionEnd", remove_animation_ease)
        target_element.removeEventListener("transitionend", remove_animation_ease)
    }
    // Code for Chrome, Safari and Opera
    target_element.addEventListener("webkitTransitionEnd", remove_animation_ease)

    // Standard syntax
    target_element.addEventListener("transitionend", remove_animation_ease)
}

function toggle_input_field(current_driver){
    referred_element_id = current_driver.getAttribute("data-driver-reference")
    referred_element = document.getElementById(referred_element_id)
    referred_element.value = "Manual"
    referred_element.dispatchEvent(new Event('change', { bubbles: true }))
}

function input_sync(current_selector){
    connected_field_reference = current_selector.getAttribute("data-input-reference")
    connected_field = document.getElementById(connected_field_reference)
    connected_button_reference = current_selector.getAttribute("data-reference-id-button")
    connected_button = document.getElementById(connected_button_reference)
    case_1 = String(current_selector.getAttribute("data-input-focus"))

    switch (current_selector.value) {
        case case_1:
            // Update iput field value
            default_value = current_selector.getAttribute("data-input-default")
            connected_field.value = default_value

            // Update fake dropdown value
            connected_button.firstElementChild.innerHTML = case_1
            break

        case 'Manual':
            // Update fake dropdown value
            connected_button.firstElementChild.innerHTML = 'Manual'
            break
    }
}

// Functions for the Input sliders (generator_inputs.html)

function load_default_input_values(){
    // Dropdowns
    input_clan = document.getElementById('selection_clan_id')
    input_clan.value = 'Random'
    input_clan.parentElement.firstElementChild.innerHTML = 'Random'
    input_clan.dispatchEvent(new Event('change', { bubbles: true }))

    input_generation = document.getElementById('selection_generation_id')
    input_generation.value = 'Random'
    input_generation.parentElement.firstElementChild.innerHTML = 'Random'
    input_generation.dispatchEvent(new Event('change', { bubbles: true }))

    input_age = document.getElementById('selection_sex_id')
    input_age.value = 'Random'
    input_age.parentElement.firstElementChild.innerHTML = 'Random'
    input_age.dispatchEvent(new Event('change', { bubbles: true }))

    input_age = document.getElementById('selection_age_id')
    input_age.value = 'Random'
    input_age.parentElement.firstElementChild.innerHTML = 'Random'
    input_age.dispatchEvent(new Event('change', { bubbles: true }))

    input_name = document.getElementById('selection_name_id')
    input_name.value = 'Random'
    input_name.parentElement.firstElementChild.innerHTML = 'Random'
    input_name.dispatchEvent(new Event('change', { bubbles: true }))

    input_calculation = document.getElementById('selection_calculation_id')
    input_calculation.value = 'Algorithm'
    input_calculation.parentElement.firstElementChild.innerHTML = 'Random'
    input_calculation.dispatchEvent(new Event('change', { bubbles: true }))


    // Sliders
    input_discipline = document.getElementById('slider_discipline_id')
    input_discipline.value = 5
    document.getElementById('value_discipline_id').innerHTML = input_discipline.value
    input_discipline.dispatchEvent(new Event('change', { bubbles: true }))

    input_physical = document.getElementById('slider_physical_id')
    input_physical.value = 50
    document.getElementById('value_physical_id').innerHTML = input_physical.value
    input_physical.dispatchEvent(new Event('change', { bubbles: true }))

    input_mental = document.getElementById('slider_mental_id')
    input_mental.value = 50
    document.getElementById('value_mental_id').innerHTML = input_mental.value
    input_mental.dispatchEvent(new Event('change', { bubbles: true }))

    input_social = document.getElementById('slider_social_id')
    input_social.value = 50
    document.getElementById('value_social_id').innerHTML = input_social.value
    input_social.dispatchEvent(new Event('change', { bubbles: true }))


    // Input fields
    document.getElementById('manual_name_input_id').value = 'Fruzsi'
    document.getElementById('manual_age_input_id').value = 1
    document.getElementById('manual_calculation_input_id').value = 1
}

function display_slider_value(current_slider){
    target_id = current_slider.getAttribute('data-reference-id')
    target_element = document.getElementById(target_id)
    new_value = current_slider.value

    target_element.innerHTML = new_value
}

function toggle_character_style(stlye_selector){
    style_element = document.getElementById('link_character_color')

    switch (stlye_selector.value) {
        case 'Light':
            style_element.setAttribute("href", "/static/stylesheets/generated_character_color_light.css")
            break

        case 'Dark':
            style_element.setAttribute("href", "/static/stylesheets/generated_character_color_dark.css")
            break
    }
}

function toogle_generation_options(){
    // Special case for thin-bloods to only have 14 and higher generations
    console.log('thin blood selected')
    let selected_clan = document.getElementById('selection_clan_id').value
    let generations_ul_element = document.getElementById('generation_container_id')
    let generations_li_elements = generations_ul_element.children
    let thin_blood_minimum_generation = 14

    if (selected_clan == 'Thin-blood'){
        for (let index = 0; index < generations_li_elements.length; index++) {
            const element = generations_li_elements[index];
            const element_value = element.getAttribute('data-reference-option')
            
            if (element_value != 'Random' ){
                if (element_value < thin_blood_minimum_generation){
                    element.classList.add('disabled')
                }
            }   
        }

        // Modify the generation selsection input area
        let generation_input =  document.getElementById('selection_generation_id').value
        if (generation_input != 'Random' && generation_input < 14){
            generation_input = 14
            document.getElementById('button_generation_list_id').firstElementChild.innerHTML = 14
        }
        
    } else {
        for (let index = 0; index < generations_li_elements.length; index++) {
            const element = generations_li_elements[index];
            const element_value = element.getAttribute('data-reference-option')
            
            if (element_value != 'Random' ){
                if (element.classList.contains('disabled') == true){
                    element.classList.remove('disabled')
                }
            }   
        }
    } 
}