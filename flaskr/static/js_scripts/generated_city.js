create_global_event_listener('click', 'DOM_link', go_to_citizen, 'class')

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