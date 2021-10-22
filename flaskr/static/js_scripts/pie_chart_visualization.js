create_global_event_listener('change', 'pie_input', pie_update, 'class')

function pie_update() {
    /* Updates the angle of an svg pie chart's sections so as to they match the relations of input element values */
    // the script behaves welll, if it fires up on page load, meaning e.g. default values are set through scipt
    // also requires 'change' events to fire on part of the values when they change, even if it happens through a script

    // It works in unision with a css file for pie segments and the html document set up properly
    
    // Set upt variables:
    let pie_input_elements = document.getElementsByClassName('pie_input') // the inputs that influence the pie chart must have the smae unique class in the document
    let sum_of_inputs = pie_get_sum_of_inputs(pie_input_elements)
    let list_of_degrees = []

    // Adjsut the pie chart pieces per input value:
    for (let index = 0; index < pie_input_elements.length; index++) {
        // base values:
        let target_percentage = pie_input_elements[index].value / sum_of_inputs // This system works with a changing sum of input values
        list_of_degrees.push(target_percentage * 360) // Each section will be roatated taking into consideration the rotations of the previous ones
        // get the relevent pie section:
        let pie_segment_id = pie_input_elements[index].getAttribute('data-reference-pie-id') // the 'data-reference-pie-id' attribute has to be present on the input DOM element
        let pie_segment = document.getElementById(pie_segment_id)
        // Actual changes:
        pie_set_sector_length(pie_segment, target_percentage)   
        pie_set_sector_rotation(pie_segment, index, list_of_degrees)
    }

    function pie_get_sum_of_inputs(pie_input_elements) {
        // Sums the elements of the inpuut collection/list
        let sum_of_inputs = 0
        for (let index = 0; index < pie_input_elements.length; index++) {
            sum_of_inputs = sum_of_inputs + parseInt(pie_input_elements[index].value) // important to parse, input.value is not integer by default
        }
        return sum_of_inputs
    }
    
    function pie_set_sector_length(pie_segment, target_percentage) {
        /* Creates a perimeter long dash for the stroke of the svg circle element 
        and offests it so that it does not display
        and offests it again so as to cover only the given percentage
        of the perimeter of the circle --> giviing the illusion of a circle segment */
        let perimeter = parseInt(pie_segment.getAttribute("r")) * 2 * Math.PI
        let seperator_length = perimeter * 0.035  // make the sections shorter uniformly than their percentage so as to seperate them
        pie_segment.style.strokeDasharray =  perimeter
        pie_segment.style.strokeDashoffset =  (perimeter * (1 - target_percentage)) + seperator_length // Offset is calcualte in the opposite direction so we have to go with 1- target_percentage
    }
    
    function pie_set_sector_rotation(pie_segment, current_pie_input_index, list_of_degrees) {
        /* Rotates each pie segment to visually begin where the previous oen finishes */
        let degree = 0
        for (let index = 0; index < current_pie_input_index; index++) { // for the first segment the codes does not get into this loop, this is by design as the first segment shouldn't rotate
            degree = degree + list_of_degrees[index]
        }
        pie_segment.style.transform = "rotateZ(" + degree.toString() + "deg)" // be carefull with the string phrasing
        return
    }
}