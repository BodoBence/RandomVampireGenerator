
create_global_event_listener("change", "slider", display_slider_value, "class")

create_global_event_listener("click", "button_input_contianer_visibility", accordion_motion, 'id')
create_global_event_listener("click", "button_load_defaults", load_default_input_values, 'id')

correct_overflow()
load_default_input_values()
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

function display_slider_value(current_slider){
    let target_id = current_slider.getAttribute('data-reference-id')
    let target_element = document.getElementById(target_id)
    let new_value = current_slider.value
    target_element.innerHTML = new_value
}

function load_default_input_values(){
    /* Sets the values of the inputs to the defaults form default_city_input_values which gets server_functions through main_city_generator.html inline script and main.py */

    // Sliders
    input_discipline = document.getElementById('slider_camarilla_id')
    input_discipline.value = default_city_input_values['faction_ratio_camarilla']
    input_discipline.dispatchEvent(new Event('change', { bubbles: true }))

    input_physical = document.getElementById('slider_anarch_id')
    input_physical.value = default_city_input_values['faction_ratio_anarch']
    input_physical.dispatchEvent(new Event('change', { bubbles: true }))

    input_mental = document.getElementById('slider_sabbath_id')
    input_mental.value = default_city_input_values['faction_ratio_sabbath']
    input_mental.dispatchEvent(new Event('change', { bubbles: true }))

    input_social = document.getElementById('slider_independent_id')
    input_social.value = default_city_input_values['faction_ratio_independent']
    input_social.dispatchEvent(new Event('change', { bubbles: true }))
    
    input_social = document.getElementById('slider_average_age_id')
    input_social.value = default_city_input_values['age_average']
    input_social.dispatchEvent(new Event('change', { bubbles: true }))

    input_social = document.getElementById('slider_age_deviation_id')
    input_social.value = default_city_input_values['age_standard_deviation']
    input_social.dispatchEvent(new Event('change', { bubbles: true }))

    input_social = document.getElementById('slider_sireing_age_gap_id')
    input_social.value = default_city_input_values['minimum_sireing_gap']
    input_social.dispatchEvent(new Event('change', { bubbles: true }))

    input_social = document.getElementById('slider_male_to_female_id')
    input_social.value = default_city_input_values['favor_males']
    input_social.dispatchEvent(new Event('change', { bubbles: true }))

    input_social = document.getElementById('slider_n_vampires_id')
    input_social.value = default_city_input_values['number_of_vampires']
    input_social.dispatchEvent(new Event('change', { bubbles: true }))
}
