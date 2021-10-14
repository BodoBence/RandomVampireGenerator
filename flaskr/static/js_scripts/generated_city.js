create_global_event_listener('click', 'DOM_link', go_to_citizen, 'class')
create_global_event_listener("click", "citizen_detail_header", accorian_details, "class")
create_global_event_listener("click", "svg_button_triangle", accorian_details, "class")

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