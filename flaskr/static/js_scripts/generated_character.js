generated_character_page_initial()

create_global_event_listener('click', 'button_discipline_skills', toggle_discipline_skills, 'class')
create_global_event_listener('click', 'button_download_vampire_id', convert_character_to_pdf, 'id')
create_global_event_listener('click', 'dot', toggle_dot_filled_and_unfilled, 'class') // if the span elements are not selected with adifferent class, they trigger in a chain and first function always triggers teh second, so we cant put fill to unfill 
create_global_event_listener('click', 'square', toggle_square_filled_and_unfilled, 'class')
create_global_event_listener('click', 'skill_delete_button', delete_container, 'class')
create_global_event_listener('click', 'skill_add_button', skill_add, 'class')
create_global_event_listener('click', 'discipline_delete_button', delete_container, 'class')
create_global_event_listener('click', 'discipline_add_button', discipline_add, 'class')

function generated_character_page_initial(){
    replace_underscores_inner_htmls()
    var character_sheet = document.getElementById('generated_character_id')
    character_sheet.scrollIntoView(alignToTop=true)
}

function toggle_discipline_skills (pressed_button){
    selection_class = pressed_button.getAttribute('data-toggle-selection-class')
    target_reference = pressed_button.getAttribute('data-toggle-reference')

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

function delete_container(trigger) {
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
                        console.log(skill_tpye)
                        skil_options_list_item_p1.innerHTML = ((skill_tpye != 'blood_sorcery_ritual') ? ((skill_tpye != 'ceremony') ? 'Skill' : 'Ceremony') :'Ritual')
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
                // chosen_option_element.children[0] is the skill type (e.g. skill, ritual, etc.)
                // chosen_option_element.children[1] is the skill name (e.g. rapid reflexes, hightened senes, etc.)
                // chosen_option_element.children[2] is the skill description (e.g. be able to see ghosts etc.)
                new_skill_name.innerHTML = chosen_option_element.children[1].innerHTML
                new_skill_description.innerHTML = chosen_option_element.children[2].innerHTML
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

function discipline_add(trigger_event) {
    /* Create a list of disciplines to choose one to add
    the lsit is created programatically here and removed upon choosing one of its items */
    let current_discipline_elements = Array.from(document.querySelectorAll('.discipline_name'))
    let owned_discipline_names = []

    //  Collect the currently owned disciplines
    for (let index = 0; index < current_discipline_elements.length; index++) {
        owned_discipline_names.push(current_discipline_elements[index].innerHTML)
    }

    // Create the discipline options menu with a first none element
    // Do basic formatting that is extra to those in csss
    let discipline_options = document.createElement('ul')
    discipline_options.classList.add('discipline_options')  
    let discipline_option_none = document.createElement('li')
    let discipline_option_none_p1 = document.createElement('p')
    discipline_options.appendChild(discipline_option_none)
    discipline_options.style.gridTemplateColumns = '1fr'
    discipline_option_none.appendChild(discipline_option_none_p1)
    discipline_option_none_p1.innerHTML = 'None'
    discipline_option_none_p1.style.gridColumn = '1/-1'

    //  Create discipline options li item for not-owned disciplins
    for (const discipline in discipline_dict) {
        if (owned_discipline_names.includes(discipline) == false) {
            let discipline_option = document.createElement('li')
            let discipline_option_p1 = document.createElement('p')

            discipline_option.appendChild(discipline_option_p1)
            discipline_option_p1.innerHTML = discipline
            discipline_options.appendChild(discipline_option)
        }
    }

    document.body.appendChild(discipline_options)
    document.addEventListener('click', choose_discipline)

    function choose_discipline(click_event) {
        if (click_event.composedPath().includes(discipline_options) == true) {    // Check if the list is clicked
            // The list is clicked
            // Unify the input for future operatios to be the LI element
            switch (click_event.target.tagName) {
                case 'LI':
                    chosen_option_element = click_event.target
                    break;

                case 'P':
                    chosen_option_element = click_event.target.parentElement
                    break;
            
                default:
                    console.log('The clicked element is not of the right kind, should be li or p')
                    break;
            }

            if (chosen_option_element.children[0].innerHTML != 'None') {
                // Create the chosen element as a discipline  (skillname, description, clsoe button) and append them
                let last_discipline = Array.from(Array.from(document.querySelectorAll('.discipline_container')).at(-1).children).at(-1)
                let new_discipline = last_discipline.cloneNode(true)
                let discipline_name = chosen_option_element.children[0].innerHTML

                // Setup new Discipline values
                new_discipline.children[0].innerHTML = discipline_name
                let new_discipline_dots = new_discipline.querySelectorAll('.dot_filled')

                // Set disciplin dots to one filled, rest unfilled
                for (let index = 0; index < new_discipline_dots.length; index++) {
                    new_discipline_dots[index].classList.remove('dot_filled')
                    new_discipline_dots[index].classList.add('dot_unfilled')
                }
                new_discipline_dots[0].classList.remove('dot_unfilled')
                new_discipline_dots[0].classList.add('dot_filled')

                let visibility_button = new_discipline.querySelector('.button_discipline_skills')
                visibility_button.setAttribute('data-toggle-reference', discipline_name)

                new_discipline.querySelector('.discipline_skills').setAttribute('id', discipline_name)
                
                let skills = Array.from(new_discipline.querySelectorAll('.discipline_skill'))
                for (let index = 0; index < skills.length; index++) {
                    skills[index].parentElement.removeChild(skills[index])
                }

                // Append te completed disciplin to the discipline list
                last_discipline.parentElement.appendChild(new_discipline)   
            }         

            // Remove Items
            discipline_options.parentElement.removeChild(discipline_options)    // Remove the list
            document.removeEventListener('click', choose_discipline)    // Remove event listener
        } else {
            // Click outside the list
            // Remove Items
            discipline_options.parentElement.removeChild(discipline_options)    // Remove the list
            document.removeEventListener('click', choose_discipline)    // Remove event listener
        }
    }
}