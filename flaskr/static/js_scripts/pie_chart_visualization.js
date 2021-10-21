create_global_event_listener('change', 'pie_input', update_pie, 'class')

function update_pie() {
    let pie_input_elements = document.getElementsByClassName('pie_input')
    let sum_of_inputs = get_sum_of_inputs(pie_input_elements)
    let list_of_degrees = []

    for (let index = 0; index < pie_input_elements.length; index++) {
        let target_percentage = pie_input_elements[index].value / sum_of_inputs
        list_of_degrees.push(target_percentage * 360)
        let pie_segment_id = pie_input_elements[index].getAttribute('data-reference-pie-id')
        let pie_segment = document.getElementById(pie_segment_id)
        set_pie_sector_length(pie_segment, target_percentage)   
        set_pie_sector_rotation(pie_segment, index, list_of_degrees)

    }
}

function get_sum_of_inputs(pie_input_elements) {
    let sum_of_inputs = 0
    for (let index = 0; index < pie_input_elements.length; index++) {
        sum_of_inputs = sum_of_inputs + parseInt(pie_input_elements[index].value)
    }
    return sum_of_inputs
}

function set_pie_sector_length(pie_segmnet, target_percentage) {
    let perimeter = pie_segmnet.getAttribute("r") * 2 * Math.PI
    pie_segmnet.style.strokeDasharray =  perimeter
    pie_segmnet.style.strokeDashoffset =  perimeter * (1 - target_percentage)
}

function set_pie_sector_rotation(pie_segment, current_pie_input_index, list_of_degrees) {
    let degree = 0
    for (let index = 0; index < current_pie_input_index; index++) {
        degree = degree + list_of_degrees[index]
    }
    pie_segment.style.transform = "rotateZ(" + degree.toString() + "deg)"
    return
}