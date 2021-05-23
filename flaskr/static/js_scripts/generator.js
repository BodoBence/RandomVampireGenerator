console.log("first line of generator.js")

// synchronize manual/random switch with manual input in the input field

create_global_event_listener("input", "selection_driver", toggle_input_field, false)
create_global_event_listener("selectionchange", selection_based_sync,  false)
create_global_event_listener("click", "button_general", trigger_animation, false)

// Functions for the Input sliders (generator_inputs.html)

function trigger_animation(current_trigger){
    
    target_id = current_trigger.getAttribute("data-target-id")
    target_class_1 = current_trigger.getAttribute("data-target-class-1")
    target_class_2 = current_trigger.getAttribute("data-target-class-2")
 
    target_element = document.getElementById(target_id)
    current_class = target_element.className

    // console.log("initial class")
    // console.log(current_class)

    target_element.classList.toggle(target_class_2)
    
    // console.log("final class")
    // console.log( target_element.getAttribute("class"))
}
    


function toggle_input_field(current_driver){
    // console.log("triggered")
    referred_element_id = current_driver.getAttribute("data-driver-reference")
    referred_element = document.getElementById(referred_element_id)
    referred_element.value = "Manual"
}

function selection_based_sync(current_selector, focused_value, conencted_field, default_value){
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
