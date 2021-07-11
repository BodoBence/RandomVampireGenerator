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
    //  JSPDF ONLY RECREATE SOLUTION

    // let character_sheet = document.getElementById('generated_character_id')
    // let character_sheet_width = character_sheet.offsetWidth / 2
    // let character_sheet_height = character_sheet.offsetHeight / 2

    let pdf = new jsPDF('p', 'px', [1200, 3000]);

    // PDF Measurements

    var left_margin = 40
    var top_margin = 40
    var unit_height = 20
    var unit_width_desired = 150
    var circle_radius = 5
    var circle_spacing = 5
    var number_of_sections = 6

    // Calculated Measurements
    var circle_with_space = circle_radius * 2 + circle_spacing
    var unit_width = Math.max(unit_width_desired, (max_level * circle_with_space))
    var column_width = unit_width * 2
    var section_heights = []
    for (let section_filler = 1; section_filler <= number_of_sections; section_filler++) {
        section_heights.push(0);
    }

    // Dictionary Parts

    let basic_info = vampire['Character_Details']['Basic_Information']
    let trackers = vampire['Character_Details']['Trackers']
    let attributes_physical = vampire['Attributes']['Physical_Attributes']
    let attributes_social = vampire['Attributes']['Social_Attributes']
    let attributes_mental = vampire['Attributes']['Mental_Attributes']
    let skills_physical = vampire['Skills']['Physical_Skills']
    let skills_social = vampire['Skills']['Social_Skills']
    let skills_mental = vampire['Skills']['Mental_Skills']
    let disciplines_clan = vampire['Disciplines']['Clan_Disciplines']
    let disciplines_non_clan = vampire['Disciplines']['Non-Clan_Disciplines']

    // Fill iup the pdf

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = basic_info, 
        column_number = 1, 
        section_number = 1,
        measure_section = true,
        shape_type = 'rectangle')
    
    section_heights[0] = section_heights[0] + unit_height

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = trackers, 
        column_number = 1, 
        section_number = 2,
        measure_section = true,
        shape_type = 'rectangle')
    
    section_heights[1] = section_heights[1] + unit_height

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = attributes_physical, 
        column_number = 1, 
        section_number = 3,
        measure_section = true,
        shape_type = 'circle')

    section_heights[2] = section_heights[2] + unit_height

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = attributes_social, 
        column_number = 2, 
        section_number = 3,
        measure_section = false,
        shape_type = 'circle')

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = attributes_mental, 
        column_number = 3, 
        section_number = 3,
        measure_section = false,
        shape_type = 'circle')

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = skills_physical, 
        column_number = 1, 
        section_number = 4,
        measure_section = true,
        shape_type = 'circle')

    section_heights[3] = section_heights[3] + unit_height

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = skills_social, 
        column_number = 2, 
        section_number = 4,
        measure_section = false,
        shape_type = 'circle')

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = skills_mental, 
        column_number = 3, 
        section_number = 4,
        measure_section = false,
        shape_type = 'circle')

    section_heights[4] = section_heights[4] + unit_height

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = disciplines_clan, 
        column_number = 1, 
        section_number = 5,
        measure_section = true,
        shape_type = 'circle')

    pdf_iterate_dictionary_and_place_items(
        current_dictionary = disciplines_non_clan, 
        column_number = 1, 
        section_number = 6,
        measure_section = true,
        shape_type = 'circle')

    pdf.save('generated_vampire.pdf')

    // Inner Functions

    function pdf_iterate_dictionary_and_place_items(
        current_dictionary, column_number, section_number, measure_section, shape_type){

        let baseline_horizontal = pdf_calculate_base_horizontal(section_number)
        let baseline_vertical = pdf_calculate_base_vertical(column_number)

        for (var key in current_dictionary) {
            if (!current_dictionary.hasOwnProperty(key)) {
                continue;
            }
            
            // Key
            pdf.text(baseline_vertical, baseline_horizontal, String(key))         

            // Value
            if (typeof current_dictionary[key] == 'string'){
                pdf.text(baseline_vertical + unit_width, baseline_horizontal, current_dictionary[key])
            }

            if (typeof current_dictionary[key] == 'number'){
                // Exclude Generation, Age
                if (key == 'Generation' || key == 'Age'){
                    pdf.text(baseline_vertical + unit_width, baseline_horizontal, String(current_dictionary[key]))

                } else {
                    // add circles
                    fill_with_shapes(baseline_vertical, baseline_horizontal, current_dictionary, key, shape_type)
                }
            }
            
            // For Disciplines
            if (typeof current_dictionary[key] == 'object'){

                fill_with_shapes(baseline_vertical, baseline_horizontal, current_dictionary[key], 'Level', shape_type)
                measure_section_height(measure_section)

                for (var skill in current_dictionary[key]['Skills']){
                    if (!current_dictionary[key]['Skills'].hasOwnProperty(skill)) {
                        continue;
                    }

                    baseline_horizontal = baseline_horizontal + unit_height
                    measure_section_height(measure_section)                    
                    pdf.text(baseline_vertical, baseline_horizontal, skill)
                    pdf.text(baseline_vertical + unit_width, baseline_horizontal, current_dictionary[key]['Skills'][skill])
                }

                baseline_horizontal = baseline_horizontal + unit_height
            }

            // Do only once per line
            baseline_horizontal = baseline_horizontal + unit_height
            measure_section_height(measure_section)
        }
    }

    function measure_section_height(measure_section){
        if (measure_section){
            section_heights[section_number-1] = section_heights[section_number-1] + unit_height 
        }
    }

    function fill_with_shapes(baseline_vertical, baseline_horizontal, current_dictionary, key, shape_type){
        
        // Filled
        for (let index_filled = 1; index_filled <= current_dictionary[key]; index_filled++) {
            switch(shape_type) {
                case 'circle':
                    pdf.ellipse(
                        (baseline_vertical + unit_width + (index_filled * circle_with_space) ), 
                        baseline_horizontal, 
                        circle_radius, 
                        -circle_radius, 
                        'F')

                    break;

                case 'rectangle':
                    pdf.rect(
                        (baseline_vertical + unit_width + (index_filled * circle_with_space) ), 
                        baseline_horizontal, 
                        circle_radius * 2, 
                        -(circle_radius * 2), 
                        'F')

                    break;

                default:
                    console.log('did not recieve a valid shape name')
                    break;
            } 
        }

        // Empty
        for (let index_empty = 1; index_empty <= max_level - current_dictionary[key]; index_empty++) {
            switch(shape_type) {
                case 'circle':
                    pdf.ellipse(
                        (baseline_vertical + unit_width + (current_dictionary[key] * circle_with_space) + (index_empty * circle_with_space)), 
                        baseline_horizontal, 
                        circle_radius, 
                        -circle_radius)

                    break;
                case 'rectangle':
                    pdf.rect(
                        (baseline_vertical + unit_width + (current_dictionary[key] * circle_with_space) + (index_empty * circle_with_space)), 
                        baseline_horizontal, 
                        circle_radius * 2, 
                        -circle_radius * 2)

                    break;
                default:
                    console.log('did not recieve a valid shape name')
                    break;

            }              
        }
    }

    function pdf_calculate_base_horizontal(section_number) {
        let section_distance = 0

        if (section_number == 1) {
            section_distance = 0
        } else {
            for (let index = 0; index < (section_number -  1); index++) {
                section_distance = section_distance + section_heights[index]
            }
        }

        let distance = top_margin + section_distance

        return distance
    }

    function pdf_calculate_base_vertical(column_number) {
        let distance = left_margin + (column_width * (column_number - 1))
        return distance
    }
}