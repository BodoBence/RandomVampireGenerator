create_global_event_listener('input', 'pie_input', pie_update, 'class')
window.onload = pie_update()

function pie_update() {
    /* Adjust the percentage css variable of the pie_chart div -->
    this will make the conic gradient display the percentages */

    // It works in unision with a css file for pie and the html document set up properly
    
    // Set upt variables:
    let pie_input_elements = document.getElementsByClassName('pie_input')
    let sum_of_inputs = pie_get_sum_of_inputs(pie_input_elements)
    let pie_class_string = pie_input_elements[0].getAttribute('data-reference-pie-class')
    let pies = document.getElementsByClassName(pie_class_string)

    // Adjsut the pie chart css variables per input value:
    for (let index = 0; index < pie_input_elements.length; index++) {
        // base values:
        let target_percentage = 100 * (pie_input_elements[0].value / sum_of_inputs)
        for (let i = 1; i <= index; i++) {
            target_percentage = target_percentage + (100 * (pie_input_elements[i].value / sum_of_inputs))
        }
        let css_variable_name = pie_input_elements[index].getAttribute('data-reference-pie-variable')      
        for (let index = 0; index < pies.length; index++) {
            pies[index].style.setProperty(css_variable_name, (target_percentage.toString() + '%'))            
        }
    }

    function pie_get_sum_of_inputs(pie_input_elements) {
        // Sums the elements of the inpuut collection/list
        let sum_of_inputs = 0
        for (let index = 0; index < pie_input_elements.length; index++) {
            sum_of_inputs = sum_of_inputs + parseInt(pie_input_elements[index].value) // important to parse, input.value is not integer by default
        }
        return sum_of_inputs
    }
}