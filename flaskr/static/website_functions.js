let current_url = window.location.href;
let current_location = get_last_url_segment(current_url);
let root_url = location.pathname;

// Functinoality spereation for the different pages

if (root_url == "/" || current_location === "result"){
    let button_complex_sliders = document.getElementById("button_complex_sliders_visibility");
    let button_input_container = document.getElementById("button_input_contianer_visibility");
    // console.log(button_complex_sliders);
    // console.log(button_input_container);

    button_complex_sliders.addEventListener("click", e => {
        console.log("inside the complex sliders event listener");
        // console.log(button_complex_sliders);
        var reference = button_complex_sliders.getAttribute("data-toggle-reference")
        // console.log(reference);
        toggle_visibility(document.getElementById(reference))
        e.stopPropagation()
    });
    
    button_input_container.addEventListener("click", e => {
        console.log("inside the input container event listener")
        // console.log(button_input_container);
        var reference = button_input_container.getAttribute("data-toggle-reference")
        // console.log(reference);
        toggle_visibility(document.getElementById(reference))
        e.stopPropagation()
    });

    if (current_location === "result"){
        create_event_listener_for_skills("button_discipline_skills", "discipline_skills");
        // let button_download = document.getElementById("button_download");
        // button_download.addEventListener("click", e => {})

        create_global_event_listener("click", "print_vampire", print_character, true)
    };
}

if (current_location === "encounter_tracker"){
    create_checkboxes()
    create_global_event_listener("click", "tracker", toggle_filled, false)
    create_global_event_listener("input", "health_meter", update_value, true)
    create_global_event_listener("input", "willpower_meter", update_value, true)
    create_global_event_listener("click", "add", add_encounter, true)
    create_global_event_listener("click", "remove", remove_encounter, true)
}

// Global functions

function get_last_url_segment(input_url){
    var parts = input_url.split("/")
    var last_segment = parts.pop() || parts.pop();  // handle potential trailing slash
    return last_segment
}

function create_global_event_listener(type, selector, callback, use_name){
    document.addEventListener(type, e => {

        if (use_name == true) {
            if (e.target.getAttribute('name') == selector){
                callback(e.target)
            }
        }

        if (use_name == false) {
            if (e.target.className == selector){
                callback(e.target)
            }
        }
    })
}

function toggle_visibility(element_in_focus){
    console.log("inside toggle visibility function")
    if (element_in_focus.style.visibility === "collapse") {
        element_in_focus.style.visibility = "visible";
        console.log("visibility changed to visible")
    } else {
        element_in_focus.style.visibility = "collapse";
        console.log("visibility changed to collapse")
    }
}

// Functions for the Input sliders (generator_inputs.html)

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

function drive_complex_ranges(currnet_slider){
    // console.log("hi on change");

    var new_value = currnet_slider.value;
    // console.log(new_value);

    var modifiend_slider_name_1 = currnet_slider.getAttribute("data-referenced-name-1");
    var modifiend_slider_name_2 = currnet_slider.getAttribute("data-referenced-name-2");
    
    subject_1 = document.getElementsByName(modifiend_slider_name_1)[0];
    subject_2 = document.getElementsByName(modifiend_slider_name_2)[0];

    subject_1.value = new_value;
    subject_2.value = new_value;
}

function toggle_visibility_skills(button_id) {
    console.log("hi skills visibility toggle")
    var skill_tables = document.getElementsByClassName("discipline_skills")
    var specific_disciplines_skills = skill_tables[button_id]
    console.log(skill_tables)
    console.log(specific_disciplines_skills)
    // var specific_disciplines_skills = document.getElementById("Dominate");
    if (specific_disciplines_skills.style.visibility === "collapse") {
        specific_disciplines_skills.style.visibility = "visible"
    } else {
        specific_disciplines_skills.style.visibility = "collapse"
    }
}

// Functions for the generated character (generated_characters_designed.html)

function create_event_listener_for_skills(class_name, target_class_name){
    // console.log(class_name)
    var selected_class_elements = document.getElementsByClassName(class_name)
    // console.log(selected_class_elements)
    for (let index = 0; index < selected_class_elements.length; index++) {
        // console.log("loooop")
        // console.log(selected_class_elements[index])
        selected_class_elements[index].addEventListener("click", e =>{
            // console.log("inside the class based event listener creation")
            var reference = e.target.getAttribute("data-toggle-reference")
            var discipliine_skill_table = document.getElementsByClassName(target_class_name)[reference]
            // console.log(discipliine_skill_table.style.visibility)
            toggle_visibility(discipliine_skill_table)
        })
    }
}

function print_character(){
    console.log("hi")
    window.print()
}

// Functinos for the Encounter Tracker (encounter_tracker.hmtl)

// Connected to checkboxes

function create_checkboxes(element_in_focus){
    healths = document.getElementsByName("health_meter")
    willpowers = document.getElementsByName("willpower_meter")
    for (let index = 0; index < healths.length; index++) {
        update_value(healths[index])
    }
    for (let index = 0; index < willpowers.length; index++) {
        update_value(willpowers[index])
    }
}

function update_value(tracker_stat){
    current_tracker_stat = tracker_stat.value
    console.log(current_tracker_stat)
    current_parent = tracker_stat.parentElement
    current_trackers = current_parent.nextElementSibling.getElementsByClassName("tracker")

    if (current_tracker_stat == current_trackers.length) {return}

    if (current_tracker_stat > current_trackers.length){
        while (current_tracker_stat > current_trackers.length){
            add_tracker(current_trackers[0].parentElement)
        }
    }

    if (current_tracker_stat < current_trackers.length) {
        while (current_tracker_stat < current_trackers.length) {
            current_trackers[current_trackers.length-1].remove()
        }
    }
}

function add_tracker(current_target){
    new_tracker = document.createElement("td")
    new_tracker.className = "tracker"
    new_tracker.style.backgroundColor = 'var(--grey)'
    current_target.appendChild(new_tracker)
}

function toggle_filled(element_in_focus){
    if (element_in_focus.style.backgroundColor == 'var(--bg)') {
        element_in_focus.style.backgroundColor = 'var(--grey)';
    } else {
        element_in_focus.style.backgroundColor = 'var(--bg)';
    }
}

// Connected to encounters

function add_encounter(){
    encounters = document.getElementsByClassName("encounter")
    number_of_encounters = encounters.length

    if (number_of_encounters < 10){
        last_encounter = encounters[encounters.length-1]
        encounter_cloned = last_encounter.cloneNode(true)
        last_encounter.parentElement.appendChild(encounter_cloned)
    }
}

function remove_encounter(current_button){
    number_of_encounters = document.getElementsByClassName("encounter").length
    
    if (number_of_encounters > 1){
        current_encounter = current_button.parentElement.parentElement
        current_encounter.remove()
    }
}