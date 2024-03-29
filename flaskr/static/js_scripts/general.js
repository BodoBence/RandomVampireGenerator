window.onload = visualize_current_page()

function visualize_current_page(){
    current_path = window.location.pathname

    switch (current_path) {
        case '/':
            document.getElementById('nav_link_character').classList.add('current_page_link')
            break
        case '/result_character':
            document.getElementById('nav_link_character').classList.add('current_page_link')
            break
        case '/encounter_tracker':
            document.getElementById('nav_link_tracker').classList.add('current_page_link')
            break
        case '/city_generator':
            document.getElementById('nav_link_city').classList.add('current_page_link')
            break
        case '/result_city':
            document.getElementById('nav_link_city').classList.add('current_page_link')
            break
        case '/about':
            document.getElementById('nav_link_about').classList.add('current_page_link')
            break 
    }
}

function set_css_variable(variable_name, new_value) {
    let r = document.querySelector(':root');
    r.style.setProperty(variable_name, new_value);
}

function get_css_variable(variable_name){
    // Get the root element
    let r = document.querySelector(':root');
    requested_value = getComputedStyle(r).getPropertyValue(variable_name)
    return requested_value

}

function get_last_url_segment(input_url){
    var parts = input_url.split("/")
    var last_segment = parts.pop() || parts.pop();  // handle potential trailing slash
    return last_segment
}

function create_global_event_listener(type, selector, callback, element_type){
    // console.log("creating global event listerner")
    document.addEventListener(type, e => {
        // console.log(e.target)

        switch (element_type) {
            case 'name':
                // console.log('in case name')
                if (e.target.getAttribute('name') == selector){
                    // console.log(e.target)
                    callback(e.target)
                }
                break

            case 'class':
                // console.log('in case class')
                if (e.target.classList.contains(selector)){
                    // console.log(e.target)
                    callback(e.target)
                }
                break

            case 'id':
                // console.log('in case id')
                if (e.target.id == selector){
                    // console.log(e.target)
                    callback(e.target)
                }
                break
        }

        e.stopPropagation()
    })
}

function toggle_visibility(element_in_focus){
    if (element_in_focus.style.visibility === "collapse") {
        element_in_focus.style.visibility = "visible";
        console.log("visibility changed to visible")
    } else {
        element_in_focus.style.visibility = "collapse";
        console.log("visibility changed to collapse")
    }
}

function toggle_class_based_animation(target_element, target_class, id_based){
    if (id_based == true) {
        my_target = document.getElementById(target_element)
        my_target.classList.toggle(target_class)
    }

    if (id_based == false) {
        my_targets = document.getElementsByClassName(target_element)
        
        for (let index = 0; index < my_targets.length; index++) {
            my_targets[index].classList.toggle(target_class)

        }
    }
}

function toogle_max_height(target_element){
    if (target_element.style.maxHeight) {
        target_element.style.maxHeight = null;
      } else {
        target_element.style.maxHeight = target_element.scrollHeight + "px";
    }
}

function cursor_to_wait(){
    console.log('changed cursor to wait')
    document.body.style.cursor='wait'
}

function cursor_to_default(){
    console.log('changed cursor to default')
    document.body.style.cursor='default'
}

function array_sampler(pool, sample_size){
    // returns n random elements from my_array
    if (sample_size == 0) {
        return console.log('Error: give non 0 sample size')
    }

    let samples = []
    for (let index = 0; index < sample_size; index++) {
        let sample_element = pool[Math.floor(Math.random() * pool.length)];
        samples.push(sample_element)
        pool.splice(sample_element.index, 1)        
    }

    return samples
}
