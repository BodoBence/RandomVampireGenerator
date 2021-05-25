console.log("first line of generator.js")

// synchronize manual/random switch with manual input in the input field

create_global_event_listener("input", "selection_driver", toggle_input_field, false)
create_global_event_listener("change", "manual_name_selection", selection_based_sync, true)
create_global_event_listener("change", "manual_age_selection", selection_based_sync, true)
create_global_event_listener("click", "button_general", accordion_motion, false)

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

function load_default_slider_values(){
    document.getElementsByName("Attributes")[0].value="{{ default_input_weights['Attributes'] }}";
    document.getElementsByName("Skills")[0].value="{{ default_input_weights['Skills'] }}";
    document.getElementsByName("Disciplines")[0].value="{{ default_input_weights['Disciplines'] }}";
    document.getElementsByName("Physical_Attributes")[0].value="{{ default_input_weights['Physical_Attributes'] }}";
    document.getElementsByName("Social_Attributes")[0].value="{{ default_input_weights['Social_Attributes'] }}";
    document.getElementsByName("Mental_Attributes")[0].value="{{ default_input_weights['Mental_Attributes'] }}";
    document.getElementsByName("Physical_Skills")[0].value="{{ default_input_weights['Physical_Skills'] }}";
    document.getElementsByName("Social_Skills")[0].value="{{ default_input_weights['Social_Skills'] }}";
    document.getElementsByName("Mental_Skills")[0].value="{{ default_input_weights['Mental_Skills'] }}";
    document.getElementsByName("Clan_Disciplines")[0].value="{{ default_input_weights['Clan_Disciplines'] }}";
    document.getElementsByName("Non-Clan_Disciplines")[0].value="{{ default_input_weights['Non-Clan_Disciplines'] }}";
}
