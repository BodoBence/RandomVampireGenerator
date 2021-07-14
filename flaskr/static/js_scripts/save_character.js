function convert_character_to_pdf(){
    //  JSPDF ONLY RECREATE SOLUTION

    // let character_sheet = document.getElementById('generated_character_id')
    // let character_sheet_width = character_sheet.offsetWidth / 2
    // let character_sheet_height = character_sheet.offsetHeight / 2
     
    // PDF Measurements
    var pdf_width = 1200
    var pdf_height = 3000

    var pdf = new jsPDF('p', 'px', [pdf_width, pdf_height]);

    // PDF-Text placement measuremesnts

    var left_margin = 40
    var top_margin = 40
    var unit_height = 20
    var circle_radius = 5
    var circle_spacing = 5
    var number_of_columns = 3
    var number_of_sections = 6

    // Calculated Measurements
    var circle_with_space = circle_radius * 2 + circle_spacing
    var column_width = (pdf_width - (left_margin * 2 )) / number_of_columns
    var unit_width = column_width / 2
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

    pdf_place_names_and_text_from_dictionary(
        current_dictionary = basic_info, 
        column_number = 1, 
        section_number = 1,
        measure_section = true,
        shape_type = 'rectangle',
        placement_direction = 'horizontal')
    
    section_heights[0] = section_heights[0] + unit_height

    pdf_place_names_and_text_from_dictionary(
        current_dictionary = trackers, 
        column_number = 1, 
        section_number = 2,
        measure_section = true,
        shape_type = 'rectangle',
        placement_direction = 'horizontal')
    
    section_heights[1] = section_heights[1] + unit_height

    pdf_place_names_and_text_from_dictionary(
        current_dictionary = attributes_physical, 
        column_number = 1, 
        section_number = 3,
        measure_section = true,
        shape_type = 'circle',
        placement_direction = 'vertical')

    section_heights[2] = section_heights[2] + unit_height

    pdf_place_names_and_text_from_dictionary(
        current_dictionary = attributes_social, 
        column_number = 2, 
        section_number = 3,
        measure_section = false,
        shape_type = 'circle',
        placement_direction = 'vertical')

        pdf_place_names_and_text_from_dictionary(
        current_dictionary = attributes_mental, 
        column_number = 3, 
        section_number = 3,
        measure_section = false,
        shape_type = 'circle',
        placement_direction = 'vertical')

    pdf_place_names_and_text_from_dictionary(
        current_dictionary = skills_physical, 
        column_number = 1, 
        section_number = 4,
        measure_section = true,
        shape_type = 'circle',
        placement_direction = 'vertical')

    section_heights[3] = section_heights[3] + unit_height

    pdf_place_names_and_text_from_dictionary(
        current_dictionary = skills_social, 
        column_number = 2, 
        section_number = 4,
        measure_section = false,
        shape_type = 'circle',
        placement_direction = 'vertical')

        pdf_place_names_and_text_from_dictionary(
        current_dictionary = skills_mental, 
        column_number = 3, 
        section_number = 4,
        measure_section = false,
        shape_type = 'circle',
        placement_direction = 'vertical')

    section_heights[4] = section_heights[4] + unit_height

    // pdf_iterate_dictionary_and_place_items(
    //     current_dictionary = disciplines_clan, 
    //     column_number = 1, 
    //     section_number = 5,
    //     measure_section = false,
    //     shape_type = 'circle',
    //     placement_direction = 'vertical')

    // pdf_iterate_dictionary_and_place_items(
    //     current_dictionary = disciplines_non_clan, 
    //     column_number = 2, 
    //     section_number = 5,
    //     measure_section = false,
    //     shape_type = 'circle',
    //     placement_direction = 'vertical')

    pdf.save('generated_vampire.pdf')

    // Inner Functions

    function pdf_place_names_and_text_from_dictionary(current_dictionary, column_number, section_number, shape_type, placement_direction){

        let baseline_horizontal = pdf_calculate_base_horizontal(section_number)
        let baseline_vertical = pdf_calculate_base_vertical(column_number)
        let iteration_number = 1
        let horizontal_offset = 0

        for (var key in current_dictionary) {
            if (!current_dictionary.hasOwnProperty(key)) {
                continue;
            }
            
            // Key
            let stat_name = String(key)
            let stat_name_split = pdf.splitTextToSize(stat_name, unit_width)

            pdf.text(baseline_vertical, baseline_horizontal + horizontal_offset, stat_name_split)
            
            let stat_name_height = stat_name_split.length * unit_height

            // Value
            // For text
            if (typeof current_dictionary[key] == 'string'){

                if (key != 'Derangement'){
                    let stat_value_split = pdf.splitTextToSize(current_dictionary[key], unit_width)
                    pdf.text(baseline_vertical + unit_width, baseline_horizontal + horizontal_offset, stat_value_split)

                    stat_value_height = stat_value_split.lengh * unit_height

                } else {
                    let stat_value_split = pdf.splitTextToSize(current_dictionary[key], (unit_width * 5))
                    pdf.text(baseline_vertical +  unit_width, baseline_horizontal  + horizontal_offset, stat_value_split)

                    stat_value_height = stat_value_split.lengh * unit_height
                }
            }

            // For numbers
            if (typeof current_dictionary[key] == 'number'){
                // Exclude Generation, Age
                if (key == 'Generation' || key == 'Age'){
                    let stat_value_split =  pdf.splitTextToSize(String(current_dictionary[key]), unit_width)
                    pdf.text(baseline_vertical + unit_width, baseline_horizontal, stat_value_split)

                    stat_value_height = stat_value_split.lengh * unit_height

                } else {
                    // add circles
                    fill_with_shapes(baseline_vertical, baseline_horizontal, current_dictionary[key], shape_type)

                    stat_value_height = unit_height
                }
            }
            
            // Do only once per line
            stat_height = Math.max(stat_name_height, stat_value_height)
            switch (placement_direction){
                case 'vertical':
                    baseline_horizontal = baseline_horizontal + stat_height
                    
                    if (measure_section){
                        section_heights[section_number-1] = section_heights[section_number-1] + stat_height
                    }

                    break;
                    
                case 'horizontal':
                    if (iteration_number % 3 != 0){
                        baseline_vertical = baseline_vertical + column_width

                        if (measure_section){
                            section_heights[section_number-1] = section_heights[section_number-1] + stat_height - unit_height
                        }
                        
                    } else {
                        baseline_vertical = baseline_vertical - (column_width * 2)
                        baseline_horizontal = baseline_horizontal + stat_height

                        if (measure_section){
                            section_heights[section_number-1] = section_heights[section_number-1] + stat_height 
                        }
                    }
                    break;

                default:
                    console.log('did not recieve a valid placement_direction')
                    break;
            }
        }
    }

    function pdf_iterate_dictionary_and_place_items(
        current_dictionary, column_number, section_number, measure_section, shape_type, placement_direction){

        let baseline_horizontal = pdf_calculate_base_horizontal(section_number)
        let baseline_vertical = pdf_calculate_base_vertical(column_number)
        let iteration_number = 1

        for (var key in current_dictionary) {
            if (!current_dictionary.hasOwnProperty(key)) {
                continue;
            }
            
            // Key
            let stat_key = String(key)
            let stat_key_split = pdf.splitTextToSize(stat_key, unit_width)

            pdf.text(baseline_vertical, baseline_horizontal, stat_key_split)         

            // Value
            let text_height_based_vertical_offset = unit_height

            // For strings
            if (typeof current_dictionary[key] == 'string'){

                if (key != 'Derangement'){
                    let stat_value_split = pdf.splitTextToSize(current_dictionary[key], unit_width)
                    pdf.text(baseline_vertical + unit_width, baseline_horizontal, stat_value_split)
                    text_height_based_vertical_offset = stat_value_split.length * unit_height

                } else {
                    let stat_value_split = pdf.splitTextToSize(current_dictionary[key], (unit_width * 5))
                    pdf.text(baseline_vertical +  unit_width, baseline_horizontal, stat_value_split)
                    text_height_based_vertical_offset = stat_value_split.length * unit_height
                }
            }

            // For numbers
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
                console.log('baseline horizontal at' +String(key) + ': ' + baseline_horizontal)
                fill_with_shapes(baseline_vertical, baseline_horizontal, current_dictionary[key], 'Level', shape_type)

                // Move to the row below
                baseline_horizontal = baseline_horizontal + unit_height
                let skill_iteration_number = 0
                
                for (var skill in current_dictionary[key]['Skills']){
                    skill_iteration_number++

                    if (!current_dictionary[key]['Skills'].hasOwnProperty(skill)) {
                        continue;
                    }

                    let skill_name = String(skill)
                    let skill_name_split = pdf.splitTextToSize(skill_name, unit_width)
                    let discipliine_skill_value = current_dictionary[key]['Skills'][skill]
                    let discipline_skill_value_split = pdf.splitTextToSize(discipliine_skill_value, unit_width)

                    pdf.text(baseline_vertical, baseline_horizontal, skill_name_split)
                    pdf.text(baseline_vertical + unit_width, baseline_horizontal, discipline_skill_value_split)

                    if (skill_iteration_number != current_dictionary[key]['Skills'].length){
                        text_height_based_vertical_offset = Math.max(skill_name_split.length,  discipline_skill_value_split.length) * unit_height
                        baseline_horizontal = baseline_horizontal + text_height_based_vertical_offset

                        if (measure_section){
                            section_heights[section_number-1] = section_heights[section_number-1] + text_height_based_vertical_offset 
                        }
                    }
                }
            }

            // Do only once per line
            switch (placement_direction){
                case 'vertical':
                    // For not disciplines
                    if (typeof current_dictionary[key] != 'object'){
                        baseline_horizontal = baseline_horizontal + text_height_based_vertical_offset
                    }
                    
                    if (measure_section){
                        section_heights[section_number-1] = section_heights[section_number-1] + text_height_based_vertical_offset 
                    }

                    break;
                    
                case 'horizontal':
                    if (iteration_number % 3 != 0){
                        baseline_vertical = baseline_vertical + column_width

                        if (measure_section){
                            section_heights[section_number-1] = section_heights[section_number-1] + text_height_based_vertical_offset - unit_height
                        }
                       
                    } else {
                        baseline_vertical = baseline_vertical - (column_width * 2)
                        baseline_horizontal = baseline_horizontal + text_height_based_vertical_offset

                        if (measure_section){
                            section_heights[section_number-1] = section_heights[section_number-1] + text_height_based_vertical_offset 
                        }
                    }
                    break;

                default:
                    console.log('did not recieve a valid placement_direction')
                    break;
            }
            console.log('')
            console.log('section height at ' + String(key) + ': ' + String(section_heights[section_number-1]))
            iteration_number++
        }
    }

    function fill_with_shapes(baseline_vertical, baseline_horizontal, number_of_shapes, shape_type){
        
        // Filled
        for (let index_filled = 1; index_filled <= number_of_shapes; index_filled++) {
            switch(shape_type) {
                case 'circle':
                    pdf.ellipse(
                        (baseline_vertical + unit_width + (index_filled * circle_with_space) ), 
                        baseline_horizontal, 
                        circle_radius, -circle_radius, 'F')

                    break;

                case 'rectangle':
                    pdf.rect(
                        (baseline_vertical + unit_width + (index_filled * circle_with_space) ), 
                        baseline_horizontal, 
                        circle_radius * 2, -(circle_radius * 2), 'F')

                    break;

                default:
                    console.log('did not recieve a valid shape name')
                    break;
            } 
        }

        // Empty
        for (let index_empty = 1; index_empty <= max_level -number_of_shapes; index_empty++) {
            switch(shape_type) {
                case 'circle':
                    pdf.ellipse(
                        (baseline_vertical + unit_width + number_of_shapes * circle_with_space) + (index_empty * circle_with_space), 
                        baseline_horizontal, 
                        circle_radius, -circle_radius)

                    break;
                case 'rectangle':
                    pdf.rect(
                        (baseline_vertical + unit_width + number_of_shapes * circle_with_space) + (index_empty * circle_with_space), 
                        baseline_horizontal, 
                        circle_radius * 2, -circle_radius * 2)

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