// create_event_listener_for_skills("button_discipline_skills", "discipline_skills");
create_global_event_listener("click", "button_discipline_skills", toggle_discipline_skills, false)

create_global_event_listener("click", "print_vampire", print_character, true)

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

function toggle_discipline_skills (pressed_button){
    animating_class = pressed_button.getAttribute("data-toggle-animation-class")
    selection_class = pressed_button.getAttribute("data-toggle-selection-class")
    target_reference = pressed_button.getAttribute("data-toggle-reference")

    target_element = document.getElementsByClassName(selection_class)[target_reference]
    target_element_id = target_element.getAttribute("id")

    toggle_class_based_animation(target_element_id, animating_class, true)

}


function print_character(){
    console.log("hi")
    window.print()
}
