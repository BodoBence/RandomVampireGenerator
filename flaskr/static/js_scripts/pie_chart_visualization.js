initialize_pie_chart('circle_pie_sector', 'pie_input')

function initialize_pie_chart(class_name_sectors, class_name_inputs) {
    var pie_chart_sectors = document.getElementsByClassName(class_name_sectors)
    var pie_chart_inputs = document.getElementsByClassName(class_name_inputs)
    var pie_svg = pie_chart_sectors[0].parentElement
    // Create as many pie sector as there are inputs
    // Guard check
    if ((pie_chart_inputs.length - pie_chart_sectors.length) <= 0){
        console.log('Too many circle_pie_sector elements in the doc')
    } else {
        while ((pie_chart_inputs.length - pie_chart_sectors.length) > 0) {
            let clone = pie_chart_sectors[pie_chart_sectors.length - 1].cloneNode(true)
            pie_svg.appendChild(clone)
        }
    }
    // set circle sector values
    console.log('---------')
    console.log(pie_chart_sectors)
    console.log('---------')

    // check if the nubmers match
    if (pie_chart_inputs.length == pie_chart_sectors.length){
        let sector_degrees = []
        for (let index = 0; index < pie_chart_inputs.length; index++) {
            let perimeter = pie_chart_sectors[index].getAttribute("r") * 2 * 3.14
            let percentage = calculate_pie_input_sum(pie_chart_inputs) / pie_chart_inputs[index].value
            let degree = 360 * percentage
            sector_degrees.push(degree)
            let accumulated_degrees = sum_sector_degrees(sector_degrees, index)
            pie_chart_sectors[index].style.strokeDasharray =  perimeter
            pie_chart_sectors[index].setAttribute('data-pie_percentage', percentage)
            pie_chart_sectors[index].style.strokeDashoffset =  perimeter * (1 - percentage)
            pie_chart_sectors[index].style.zIndex = index
            pie_chart_sectors[index].style.transform = "rotateZ(" + accumulated_degrees + "deg)"
        }
    }

    function sum_sector_degrees(sector_degrees, input_index) {
        sum = 0
        if (input_index == 0) {
            return sum
        } else {
            for (let index = 0; index < input_index; index++) {
                sum = sum + sector_degrees[index] 
            }
            return sum
        }    
    }

    function calculate_pie_input_sum(pie_inputs) {
        sum = 0
        for (let index = 0; index < pie_inputs.length; index++) {
            sum = sum + pie_inputs[index].value
        }
        return sum
    }
}



