generated_character_page_initial()

create_global_event_listener("click", "button_discipline_skills", toggle_discipline_skills, 'class')
create_global_event_listener("click", "button_download_vampire_id", convert_character_to_pdf, 'id')
create_global_event_listener("click", "dot", toggle_dot_filled_and_unfilled, 'class') // if the span elements are not selected with adifferent class, they trigger in a chain and first function always triggers teh second, so we cant put fill to unfill 
create_global_event_listener("click", "square", toggle_square_filled_and_unfilled, 'class')
create_global_event_listener("click", "skill_delete_button", skill_delete, "class")
create_global_event_listener("click", "skill_add_button", skill_add, "class")

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
    target_element.classList.toggle('dont_show')
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
    /* Create a list of skills to choose one to add to the current discipline
    the lsit is created programatically here and removed upon choosing one of its items */

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
    // let skill_options_list = trigger.parentElement.querySelector('.skill_options')
    // let skill_options_list_item_first = skill_options_list.children[0]

    // Create options list container and children
    let skill_options_list = document.createElement('ul')   
    let skill_option_none = document.createElement('li')
    skill_options_list.classList.add('skill_options')
    skill_options_list.appendChild(skill_option_none)
    let skill_option_p = document.createElement('p')
    skill_option_none.appendChild(skill_option_p)
    skill_option_p.innerHTML = 'None'
    skill_option_p.style.gridColumn = '1/-1'
    document.body.appendChild(skill_options_list)

    // Add to the list the potential skills
    for (const skill_tpye in discipline_dict[current_discipline]) {
        for (const skill_level in discipline_dict[current_discipline][skill_tpye]) {
            if (skill_level <= current_discipline_level) {
                let skill_keys = Object.keys(discipline_dict[current_discipline][skill_tpye][skill_level])
                skill_keys.forEach(key => {
                    if (owned_skills.includes(key) == false) {
                        let skill_options_list_item = document.createElement('li')
                        let skil_options_list_item_p1 = document.createElement('p')
                        let skil_options_list_item_p2 = document.createElement('p')
                        let skil_options_list_item_p3 = document.createElement('p')

                        skill_options_list_item.appendChild(skil_options_list_item_p1)
                        skill_options_list_item.appendChild(skil_options_list_item_p2)
                        skill_options_list_item.appendChild(skil_options_list_item_p3)
                        skil_options_list_item_p1.innerHTML = skill_tpye
                        skil_options_list_item_p2.innerHTML =  key
                        skil_options_list_item_p3.innerHTML =  discipline_dict[current_discipline][skill_tpye][skill_level][key]['Description']
                        skill_options_list.appendChild(skill_options_list_item)
                    }
                });  
            }
        }        
    }

    // Create event listeners for pop-up the list options
    // for (let index = 0; index < skill_options_list.children.length; index++) {
    //     skill_options_list.children[index].addEventListener('click', choose_option)
    // }

    document.addEventListener('click', choose_option)

    // Hide the options list when an option is clicked and add te skill
    function choose_option(event) {
        if (event.composedPath().includes(skill_options_list) == true) {    // Check if the list is clicked
            // The list is clicked
            // Unify the input for future operatios to be the LI element
            switch (event.target.tagName) {
                case 'LI':
                    chosen_option_element = event.target
                    break;

                case 'P':
                    chosen_option_element = event.target.parentElement
                    break;
            
                default:
                    console.log('The clicked element is not of the right kind, should be li or p')
                    break;
            }

            if (chosen_option_element.children[0].innerHTML != 'None') {
                // Create the chosen element as a discipline skill (skillname, description, clsoe button) and append them
                let new_skill_container = document.createElement('div')
                trigger.parentElement.insertBefore(new_skill_container, trigger)
                new_skill_container.classList.add('discipline_skill')

                let new_skill_name = document.createElement('p')
                let new_skill_description = document.createElement('p')
                let new_skill_delete_button = document.createElement('button')
                new_skill_delete_button.setAttribute('type', 'button')
                new_skill_delete_button.classList.add('skill_delete_button')
            
                // Append created elements
                new_skill_container.appendChild(new_skill_name)
                new_skill_container.appendChild(new_skill_description)
                new_skill_container.appendChild(new_skill_delete_button)

                // set the text of the new skill according to the chosen element
                new_skill_name.innerHTML =chosen_option_element.children[0].innerHTML
                new_skill_description.innerHTML = chosen_option_element.children[1].innerHTML
                new_skill_delete_button.innerHTML = 'X'
            }   

            // Remove Items
            skill_options_list.parentElement.removeChild(skill_options_list)    // Remove the list
            document.removeEventListener('click', choose_option)    // Remove event listener
        } else {
            // Click outside the list
            // Remove Items
            skill_options_list.parentElement.removeChild(skill_options_list)    // Remove the list
            document.removeEventListener('click', choose_option)    // Remove event listener
        }
    }
}
