create_global_event_listener('click', 'DOM_link', go_to_citizen, 'class')
create_global_event_listener("click", "citizen_detail_header", accorian_details, "class")
create_global_event_listener("click", "svg_button_triangle", accorian_details, "class")
create_global_event_listener("mouseover", "relations", add_relationship_lines, "class")
// create_global_event_listener("mouseout", "relations", remove_relationship_lines, "class")

// Once per page load
replace_underscores_inner_htmls()
bring_city_into_view()

// document.onload = test_line_adding()

// Functions
function bring_city_into_view(){
    city = document.querySelector('.generated_city')
    city.scrollIntoView(true)
}

function go_to_citizen(e){
    /* Bring into view clicked citizen */
    citizens = document.getElementsByClassName('citizen_name')
    for (let index = 0; index < citizens.length; index++) {
        const element = citizens[index]
        if (element.innerHTML == e.innerHTML){
            my_target = element
            break
        }
    }
    my_target.scrollIntoView({block: 'center', inline: 'center'})
}

function accorian_details(current_button){
    let citizen_detail_elements = current_button.parentElement.getElementsByClassName('citizen_details')
    for (let index = 0; index < citizen_detail_elements.length; index++) {
        citizen_detail_elements[index].classList.toggle('dont_display')      
    }

    handle_indicator_animation(current_button, citizen_detail_elements)
}

function handle_indicator_animation(current_button, citizen_detail_elements){
    triangle = current_button.querySelector('.svg_button_triangle')
    triangle.classList.toggle('triangle_closed')
}

function replace_underscores_inner_htmls(){
    let elements_with_underscore = document.getElementsByClassName('underscore')
    for (let index = 0; index < elements_with_underscore.length; index++) {
        let original_string = elements_with_underscore[index].innerHTML
        elements_with_underscore[index].innerHTML = original_string.replaceAll('_', ' ')
    }
}

function connect_elements_with_svg_line(element_a, element_b, svg_style, parent){
    /* Adds an svg line, connecting element_a to element_b, it creates the svg line */
    // let x1 = element_a.offsetLeft + (element_a.offsetWidth/2);
    // let y1 = element_a.offsetTop + (element_a.offsetHeight/2);
    // let x2 = element_b.offsetLeft + (element_b.offsetWidth/2);
    // let y2 = element_b.offsetTop + (element_b.offsetHeight/2);

    let x1 = get_element_outline_point(element_a, 'center', 'bottom', 'x')
    let y1 = get_element_outline_point(element_a, 'center', 'bottom', 'y')
    let x2 = get_element_outline_point(element_b, 'center', 'bottom', 'x')
    let y2 = get_element_outline_point(element_b, 'center', 'top', 'y')

    // Create the svg element
    let new_svg = document.createElementNS('http://www.w3.org/2000/svg','svg')
    new_svg.classList.add(svg_style)
    new_svg.style.height = document.body.clientHeight
    new_svg.style.width = document.body.clientWidth

    // new_svg.classList.add(svg_class)
    let new_line = document.createElementNS('http://www.w3.org/2000/svg','line')
    // new_line.classList.add(line_class)
    new_line.setAttribute('x1',x1)
    new_line.setAttribute('y1',y1)
    new_line.setAttribute('x2',x2)
    new_line.setAttribute('y2',y2)
    new_line.setAttribute('stroke', 'red')
    new_line.setAttribute('stroke-width', '4px')
    new_svg.appendChild(new_line)
    parent.appendChild(new_svg)

}

function test_line_adding(){
    citizens = document.getElementsByClassName('citizen')
    connect_elements_with_svg_line(citizens[0], citizens[1], 'svg_layer', document.body)
    connect_elements_with_svg_line(citizens[0], citizens[2], 'svg_layer', document.body)
    connect_elements_with_svg_line(citizens[0], citizens[3], 'svg_layer', document.body)       
}

function get_element_outline_point(element, horizontal, vertical, output){
    /* gives coordinates for the element vertical (top, bottom, center) on horizontal (eft, right, center) */
    switch (horizontal) {
        case 'left':
            x = element.offsetLeft
            break;
        case 'right':
            x = element.offsetLeft + element.offsetWidth
            break;
        case 'center':
            x = element.offsetLeft + (element.offsetWidth / 2)
            break;
        default:
            console.log('invalid side_horizontal value')
            break;
    }

    switch (vertical) {      
        case 'top':
            y = element.offsetTop
            break;
        case 'bottom':   
            y = element.offsetTop + element.offsetHeight 
            break;  
        case 'center':   
            y = element.offsetTop + (element.offsetHeight/2)
            break;    
        default:
            console.log('invalid side_vertical value')
            break;
    }
    
    switch (output) {
        case 'x':
            return x
        case 'y':
            return y
        default:
            return console.log('output not well defined')
    }
}

function add_relationship_lines(e){
    console.log(e)
    related_elements = e.getAttribute('data-relations').slice(0, -1).slice(0, 0)
    console.log(related_elements)
}