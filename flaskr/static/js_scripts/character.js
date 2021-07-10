create_global_event_listener("click", "button_discipline_skills", toggle_discipline_skills, 'class')
create_global_event_listener("click", "button_download_vampire", convert_character_to_pdf, 'id')

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
    selection_class = pressed_button.getAttribute("data-toggle-selection-class")
    target_reference = pressed_button.getAttribute("data-toggle-reference")

    target_element = document.getElementsByClassName(selection_class)[target_reference]

    toogle_max_height(target_element)
}

function convert_character_to_pdf(){
    console.log("in saving the character locally")
    
    // compenstating for the long run time
    cursor_to_wait()

    //  JSPDF + HTML2CANVAS SOLUTION

    var character_sheet = document.getElementById('generated_character_id')

    var character_sheet_width = character_sheet.offsetWidth / 2
    var character_sheet_height = character_sheet.offsetHeight / 2

    console.log(character_sheet_width)
    console.log(character_sheet_height)

    var pdf = new jsPDF('p', 'px', [character_sheet_width, character_sheet_height])

    pdf.addHTML(character_sheet, 0, 0, function () {
        pdf.save('generated_vampire.pdf');
    });

    // getting back to normal mode on completion
    cursor_to_default()
}