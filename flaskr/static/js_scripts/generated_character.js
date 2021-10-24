generated_character_page_initial()

create_global_event_listener("click", "button_discipline_skills", toggle_discipline_skills, 'class')
create_global_event_listener("click", "button_download_vampire_id", convert_character_to_pdf, 'id')
create_global_event_listener("click", "dot", toggle_dot_filled_and_unfilled, 'class') // if the span elements are not selected with adifferent class, they trigger in a chain and first function always triggers teh second, so we cant put fill to unfill 
create_global_event_listener("click", "square", toggle_square_filled_and_unfilled, 'class')
create_global_event_listener("click", "skill_delete_button", skill_delete, "class")

// create_global_event_listener("click", "dot_unfilled", swap_dot_unfilled_to_filled, 'class')
// create_global_event_listener("click", "square_filled", swap_square_filled_to_unfilled, 'class')
// create_global_event_listener("click", "square_unfilled", swap_square_unfilled_to_filled, 'class')


function generated_character_page_initial(){
    replace_underscores_inner_htmls()
    var character_sheet = document.getElementById('generated_character_id')
    character_sheet.scrollIntoView(alignToTop=true)

}

function create_event_listener_for_skills(class_name, target_class_name){
    var selected_class_elements = document.getElementsByClassName(class_name)
    for (let index = 0; index < selected_class_elements.length; index++) {
        selected_class_elements[index].addEventListener("click", e =>{
            var reference = e.target.getAttribute("data-toggle-reference")
            var discipliine_skill_table = document.getElementsByClassName(target_class_name)[reference]
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
    var character_sheet = document.getElementById('generated_character_id')
    character_sheet.scrollIntoView(alignToTop=true)
    var character_sheet_width = character_sheet.offsetWidth
    var character_sheet_height = character_sheet.offsetHeight
    var pdf = new jsPDF('p', 'px', [character_sheet_width, character_sheet_height]);
    pdf.addHTML(character_sheet, 0, 0, function () {
        pdf.save('generated_vampire.pdf');
    });
}

function replace_underscores_inner_htmls(){
    console.log('replacing underscores')
    let elements_with_underscore = document.getElementsByClassName('underscore')
    for (let index = 0; index < elements_with_underscore.length; index++) {
        let original_string = elements_with_underscore[index].innerHTML
        elements_with_underscore[index].innerHTML = original_string.replaceAll('_', ' ')
    }
}

function toggle_dot_filled_and_unfilled(trigger) {
    /* change filled to unfilled on dot */
    trigger.classList.toggle('dot_filled')
    trigger.classList.toggle('dot_unfilled')
}

function toggle_square_filled_and_unfilled(trigger) {
    /* change filled to unfilled on square */
    trigger.classList.toggle('square_filled')
    trigger.classList.toggle('square_unfilled')
}

function skill_delete(trigger) {
    let container = trigger.parentElement
    container.parentNode.removeChild(container)
}