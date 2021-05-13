let button_complex_sliders = document.getElementById("button_complex_sliders_visibility");
let button_input_container = document.getElementById("button_input_contianer_visibility");

// console.log(button_complex_sliders);
// console.log(button_input_container);

button_complex_sliders.addEventListener("click", function(){
    console.log("inside the addition of the event listener");
    // console.log(button_complex_sliders);
    var reference = button_complex_sliders.getAttribute("data-toggle-reference");
    // console.log(reference);
    toggle_visibility(reference);
});

button_input_container.addEventListener("click", function(){
    console.log("inside the addition of the event listener");
    // console.log(button_input_container);
    var reference = button_input_container.getAttribute("data-toggle-reference");
    // console.log(reference);
    toggle_visibility(reference);
});

function toggle_visibility(target_id){
    var target = document.getElementById(target_id);
    console.log("inside toggle visibility function")
    console.log(target);
    if (target.style.visibility === "collapse") {
        target.style.visibility = "visible";
        console.log("visibility changed to visible")
    } else {
        target.style.visibility = "collapse";
        console.log("visibility changed to collapse")
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
    var skill_tables = document.getElementsByClassName("discipline_skills");
    var specific_disciplines_skills = skill_tables[button_id];
    console.log(skill_tables);
    console.log(specific_disciplines_skills);
    // var specific_disciplines_skills = document.getElementById("Dominate");
    if (specific_disciplines_skills.style.visibility === "collapse") {
        specific_disciplines_skills.style.visibility = "visible";
    } else {
        specific_disciplines_skills.style.visibility = "collapse";
    }
}

function print_character(){
    window.print();
}