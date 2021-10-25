generated_character_page_initial()

create_global_event_listener("click", "button_discipline_skills", toggle_discipline_skills, 'class')
create_global_event_listener("click", "button_download_vampire_id", convert_character_to_pdf, 'id')
create_global_event_listener("click", "dot", toggle_dot_filled_and_unfilled, 'class') // if the span elements are not selected with adifferent class, they trigger in a chain and first function always triggers teh second, so we cant put fill to unfill 
create_global_event_listener("click", "square", toggle_square_filled_and_unfilled, 'class')
create_global_event_listener("click", "skill_delete_button", skill_delete, "class")
create_global_event_listener("click", "skill_add_button", skill_add, "class")

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

function skill_add(trigger) {
    /* Creat a list of skills to choose whic to add to the current discipline
    the options come from a JSON dictionary read in in main_character_generator.html
    the list's DOM objects are created in the code */
    console.log(discipline_dict)

    let current_discipline = trigger.parentElement.getAttribute('id')
    // Get current discipline level
    let current_discipline_level_container = trigger.parentElement.parentElement.querySelector('.discipline_level')
    let current_discipline_level = current_discipline_level_container.querySelectorAll('.dot_filled').length

    // Get already owned rituals
    let skill_containers = trigger.parentElement.querySelectorAll('.discipline_skill')
    let owned_skills = []
    for (let index = 0; index < skill_containers.length; index++) {
        owned_skills.push(skill_containers[index].children[0].innerHTML)
    }

    // Get Options list container and first child
    let skill_options_list = trigger.parentElement.querySelector('.skill_options')
    let skill_options_list_item_first = skill_options_list.children[0]

    for (const skill_level in discipline_dict[current_discipline]['skill']) {
        if (skill_level <= current_discipline_level) {
            let skill_keys = Object.keys(discipline_dict[current_discipline]['skill'][skill_level])
            skill_keys.forEach(key => {
                if (owned_skills.includes(key) == false) {
                    let skill_options_list_item = skill_options_list_item_first.cloneNode(true)
                    skill_options_list_item.children[0].innerHTML = key
                    skill_options_list_item.children[1].innerHTML =  discipline_dict[current_discipline]['skill'][skill_level][key]['Description']
                    skill_options_list.appendChild(skill_options_list_item)
                }
            });  
        }
    }

    // Dispaly options
    skill_options_list.classList.remove('dont_show')

    for (let index = 0; index < skill_options_list.children.length; index++) {
        skill_options_list.children[index].addEventListener('click', choose_option)
    }

    // Hide the options list when an option is clicked and add te skill
    function choose_option(event) {
        console.log(event.target.children)
        let new_skill_container = document.createElement('div')
        Node.trigger.target.parentElement.insertBefore(new_skill_container, Node.trigger)
        new_skill_container.classList.add('discipline_skill')

        let new_skill_name = document.createElement('p')
        let new_skill_description = document.createElement('p')

        new_skill_container.appendChild(new_skill_name)
        new_skill_container.appendChild(new_skill_description)

        new_skill_name.innerHTML = event.target.children[0].innerHTML
        new_skill_description.innerHTML = event.target.children[1].innerHTML
             

        // maybe a li p no pointer events kne hoyg leygen hoyg minid g a li legyen az event.target
        
       
        skill_options_list.classList.add('dont_show')
    }
}
