generated_character_page_initial()

create_global_event_listener('click', 'button_discipline_skills', toggle_discipline_skills, 'class')
create_global_event_listener('click', 'button_download_vampire_static_id', convert_character_to_pdf, 'id') // Convert to pdf
create_global_event_listener('click', 'button_download_vampire_interactive_id', create_character_interactive_pdf, 'id') // Create interactive pdf
create_global_event_listener('click', 'button_download_vampire_csv_id', convert_character_to_csv, 'id') // Create CSV 
create_global_event_listener('click', 'dot', toggle_dot_filled_and_unfilled, 'class') // if the span elements are not selected with a different class, they trigger in a chain and first function always triggers teh second, so we cant put fill to unfill 
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

function create_character_interactive_pdf(){
    /* Setup values */
    // Size
    let page_width = 1000
    let page_height = 2000
    let page_margin = 50
    let text_area = page_width - (page_margin * 2)
    let thee_column_layout_column_width = text_area / 3
    let three_column_layout = [page_margin, page_margin + (text_area / 3), page_margin + ((text_area / 3) *2) ]
    let subcolumn_start = 150
    let rows_start = [130, 200, 400, 800]
    let line_height = 30

    // Data
    let max_skill_level = 10

    // PDF
    var doc = new jsPDF('p', 'pt', [page_height, page_width]); // create pdf

    /* Populating the empty PDF with Data */

    doc.text(500, 50, 'Vampire'); // Title
    doc.text(500, 65, 'The Masquerade'); // SubTitle
    doc.text(500, 80, 'Created by AutoFeed'); // SubTitle 2

    /* Basic info */
    doc.text(three_column_layout[0], rows_start[0], "Name")
    create_text_field(pos_x=three_column_layout[0] + subcolumn_start, pos_y=rows_start[0], text=String(character_sheet["Character_Details"]["Basic_Information"]["Name"], field_name="text_field_name", is_multiline=false))

    doc.text(three_column_layout[1], rows_start[0], "Age")
    create_text_field(pos_x=three_column_layout[1] + subcolumn_start, pos_y=rows_start[0], text=String(character_sheet["Character_Details"]["Basic_Information"]["Age"]), field_name="text_field_age", is_multiline=false)


    doc.text(three_column_layout[2], rows_start[0], "Clan")
    create_combo_box(pos_x=three_column_layout[2] + subcolumn_start, pos_y=rows_start[0], list_options=clans, list_value=String(character_sheet["Character_Details"]["Basic_Information"]["Clan"]), field_name="list_field_clan")

    doc.text(three_column_layout[0], rows_start[0] + 30, "Sire")
    create_text_field(pos_x=three_column_layout[0] + subcolumn_start, pos_y=rows_start[0] + 30, text=String(character_sheet["Character_Details"]["Basic_Information"]["Sire"], field_name="text_field_sire", is_multiline=false))

    doc.text(three_column_layout[1], rows_start[0] + 30, "Sex")
    create_combo_box(pos_x=three_column_layout[1] + subcolumn_start, pos_y=rows_start[0] + 30, list_options=["Male", "Female"], list_value=String(character_sheet["Character_Details"]["Basic_Information"]["Sex"]), field_name="list_field_sex")

    doc.text(three_column_layout[2], rows_start[0] + 30, "Generation")
    create_combo_box(pos_x=three_column_layout[2] + subcolumn_start, pos_y=rows_start[0] + 30, list_options=["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"], list_value=String(character_sheet["Character_Details"]["Basic_Information"]["Generation"]), field_name="list_field_sex")

    /* Trackers */

    /* Attributes */
    let keys_physical_attributes = []
    Object.keys(character_sheet['Attributes']['Physical_Attributes']).forEach(function(key) {
        keys_physical_attributes.push(key)
     });

    let keys_social_attributes = []
    Object.keys(character_sheet['Attributes']['Social_Attributes']).forEach(function(key) {
        keys_social_attributes.push(key)
    });

    let keys_mental_attributes = []
    Object.keys(character_sheet['Attributes']['Mental_Attributes']).forEach(function(key) {
        keys_mental_attributes.push(key)
    });

    create_column_with_boxes(column_item_keys=keys_physical_attributes, column_items=character_sheet['Attributes']['Physical_Attributes'], pos_x=three_column_layout[0], pos_y=rows_start[1], offset_x=subcolumn_start, offset_y=30)
    create_column_with_boxes(column_item_keys=keys_social_attributes, column_items=character_sheet['Attributes']['Social_Attributes'], pos_x=three_column_layout[1], pos_y=rows_start[1], offset_x=subcolumn_start, offset_y=30)
    create_column_with_boxes(column_item_keys=keys_mental_attributes, column_items=character_sheet['Attributes']['Mental_Attributes'], pos_x=three_column_layout[2], pos_y=rows_start[1], offset_x=subcolumn_start, offset_y=30)
    
    /* Skills */
    let keys_physical_skills = []
    Object.keys(character_sheet['Skills']['Physical_Skills']).forEach(function(key) {
        keys_physical_skills.push(key)
     });

    let keys_social_skills = []
    Object.keys(character_sheet['Skills']['Social_Skills']).forEach(function(key) {
        keys_social_skills.push(key)
    });

    let keys_mental_skills = []
    Object.keys(character_sheet['Skills']['Mental_Skills']).forEach(function(key) {
        keys_mental_skills.push(key)
    });

    create_column_with_boxes(column_item_keys=keys_physical_skills, column_items=character_sheet['Skills']['Physical_Skills'], pos_x=three_column_layout[0], pos_y=rows_start[2], offset_x=subcolumn_start, offset_y=30)
    create_column_with_boxes(column_item_keys=keys_social_skills, column_items=character_sheet['Skills']['Social_Skills'], pos_x=three_column_layout[1], pos_y=rows_start[2], offset_x=subcolumn_start, offset_y=30)
    create_column_with_boxes(column_item_keys=keys_mental_skills, column_items=character_sheet['Skills']['Mental_Skills'], pos_x=three_column_layout[2], pos_y=rows_start[2], offset_x=subcolumn_start, offset_y=30)

    /* Disciplines */
    let keys_clan_disciplines = []
    Object.keys(character_sheet['Disciplines']['Clan_Disciplines']).forEach(function(key) {
        keys_clan_disciplines.push(key)
    });

    let keys_non_clan_disciplines = []
    Object.keys(character_sheet['Disciplines']['Non-Clan_Disciplines']).forEach(function(key) {
        keys_non_clan_disciplines.push(key)
    });

    /* Clan */
    let clan_disciplines_current = clan_discipline_dict[character_sheet["Character_Details"]["Basic_Information"]["Clan"]]
    for (let discipline_index = 0; discipline_index < clan_disciplines_current.length; discipline_index++) {
        // Discipline name and level
        if (keys_clan_disciplines.includes(clan_disciplines_current[discipline_index])){
            doc.text(three_column_layout[discipline_index], rows_start[3], String(clan_disciplines_current[discipline_index]))
            create_n_checkbox(max_skill_level, character_sheet["Disciplines"]["Clan_Disciplines"][String(keys_clan_disciplines[discipline_index])]["Level"], three_column_layout[discipline_index] + subcolumn_start, rows_start[3], box_offset=15)

            // Discipline skills
            let current_discipline_skill_keys = []
            Object.keys(character_sheet["Disciplines"]["Clan_Disciplines"][String(keys_clan_disciplines[discipline_index])]["Skills"]).forEach(function(key) {
                current_discipline_skill_keys.push(key)
            });

            let current_discipline_skill_values = []
            Object.values(character_sheet["Disciplines"]["Clan_Disciplines"][String(keys_clan_disciplines[discipline_index])]["Skills"]).forEach(function(value) {
                current_discipline_skill_values.push(value)
            });

            create_column_with_text(column_items=current_discipline_skill_keys, pos_x=three_column_layout[discipline_index], pos_y=rows_start[3] + line_height, offset_y=line_height)

            create_column_with_text(column_items=current_discipline_skill_values, pos_x=three_column_layout[discipline_index] + subcolumn_start, pos_y=rows_start[3] + line_height, offset_y=line_height)
                
        } else {
            doc.text(three_column_layout[discipline_index], rows_start[3], String(clan_disciplines_current[discipline_index]))
            create_n_checkbox(max_skill_level, 0, three_column_layout[discipline_index] + subcolumn_start, rows_start[3], box_offset=15)
        }
    }

    /* Non-Clan */





    // create_n_checkbox(4, 4, 100, 100, 15)
    // create_dropdownlist(["1", "2", "3"], "1", "1", 200, 100, 100, 15)

    doc.save('Test.pdf');

    // Internal functions
    function create_combo_box(pos_x, pos_y, list_options, list_value, field_name){
        let comboBox = new ComboBox();
        comboBox.fieldName = field_name;
        comboBox.topIndex = 1;
        comboBox.Rect = [pos_x, pos_y - 10, 100, 20];
        comboBox.setOptions(list_options);
        comboBox.value = list_value;
        comboBox.defaultValue = list_value;
        doc.addField(comboBox);
    }

    function create_text_field(pos_x, pos_y, text, field_name, is_multiline){
        let textField_name = new TextField();
        textField_name.Rect = [pos_x, pos_y - 10, 100, 20]
        textField_name.multiline = is_multiline;
        textField_name.value = text
        textField_name.fieldName = field_name;
        doc.addField(textField_name);
    }

    function create_column_with_boxes(column_item_keys, column_items, pos_x, pos_y, offset_x, offset_y){
        for (let index = 0; index < column_item_keys.length; index++) {
            doc.text(pos_x, pos_y + (offset_y * index), String(column_item_keys[index]), align="left")
            create_n_checkbox(max_skill_level, column_items[column_item_keys[index]], pos_x + offset_x, pos_y + (offset_y * index), 15)
        }
    }

    function create_column_with_text(column_items, pos_x, pos_y, offset_y){
        for (let index = 0; index < column_items.length; index++) {
            doc.text(pos_x, pos_y + (offset_y * index), String(column_items[index]), align="left", maxWidth=String(thee_column_layout_column_width-subcolumn_start))
        }
    }

    function create_n_checkbox(n, n_filled, pos_x, pos_y, box_offset){
        n_filled -= 1 // indexes later start with 0 not 1
        let boxes = []
        let box_baseline_correction = 10

        for (let index = 0; index < n; index++) {
            boxes[index] = new CheckBox()
            boxes[index].fieldName = "field" + String(index);
            boxes[index].Rect = [pos_x + (box_offset * index), pos_y - box_baseline_correction, 10, 10];
            if (index <= n_filled){
                boxes[index].appearanceState = 'On' //checked
            } else {
                boxes[index].appearanceState = 'Off' //unchecked
            }
            doc.addField(boxes[index])
        }
    }
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

function convert_character_to_csv(){
   
    //  create CSV file data in an array
    var csvFileData = []
    console.log('hi')
    let stats = document.getElementsByClassName("stat_name")

    // Stats
    for (let i = 0; i < stats.length; i++) {
        let item = []
        // stat name
        item.push(stats[i].innerHTML)

        // stat value
        let statValue = 0
        let statValueSource = stats[i].nextElementSibling
        if (statValueSource.children.length == 0) {
            // stat value is a text, or number, but is not indicated with dots
            statValue = statValueSource.innerHTML
        } else {
            // stat vlaie is indicated visually with dots, etc.
            if (statValueSource.firstElementChild.classList.contains('square')){
                statValue = statValueSource.getElementsByClassName('square_filled').length
            }
            if (statValueSource.firstElementChild.classList.contains('dot')){
                statValue = statValueSource.getElementsByClassName('dot_filled').length
            }
        }

        item.push(statValue)
        csvFileData.push(item)

        // Gather discipline skills
        if (stats[i].classList.contains("discipline_name")){
            console.log(stats[i].innerHTML)
            let discipline_skill_data = stats[i].parentElement.lastElementChild.getElementsByClassName("discipline_skill")
        
            let discipline_name = String(stats[i].innerHTML + " skills")
            let discipline_skills = []

            for (let i = 0; i < discipline_skill_data.length - 1; i++) {

                if (discipline_skill_data[i].children > 0){
                    discipline_skills.push(discipline_skill_data[i].firstElementChild)
                }
            }

            csvFileData.push([discipline_name, discipline_skills])
            
        }
    }

    

    //  define the heading for each row of the data  
    var csv = 'Stat name,Stat value\n';  
    
    //  merge the data with CSV  
    csvFileData.forEach(function(row) {  
            csv += row.join(',');  
            csv += "\n";  
    });  

    //  Creating a hidden element - needed so that the downloaded file will have a name
    var hiddenElement = document.createElement('a');  
    hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);  
    hiddenElement.target = '_blank';  
        
    //  provide the name for the CSV file to be downloaded  
    hiddenElement.download = 'RandomGeneratedVampireData.csv';  
    hiddenElement.click();  

    // Cleanup
    document.removeChild('a')
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