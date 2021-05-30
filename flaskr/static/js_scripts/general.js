console.log("first line of general.js")
// Global functions

window.addEventListener('resize', (event) => {
    resize_to_window_width("svg_city_1")
    console.log('page is resized');
  });


function resize_to_window_width(target_element_id) {
    
    target_element = document.getElementById(target_element_id)

    element_width = target_element.offsetWidth
    window_width = window.innerWidth

    calculated_scale_ratio =  window_width / element_width

    console.log(target_element)
    console.log(element_width)
    console.log(window_width)
    console.log(calculated_scale_ratio)

    document.documentElement.style.setProperty('--screen_scale', calculated_scale_ratio)
}



function get_last_url_segment(input_url){
    var parts = input_url.split("/")
    var last_segment = parts.pop() || parts.pop();  // handle potential trailing slash
    return last_segment
}

function create_global_event_listener(type, selector, callback, element_type){
    console.log("creating global event listerner")
    document.addEventListener(type, e => {
        // console.log(e.target)

        switch (element_type) {
            case 'name':
                console.log('in case name')
                if (e.target.getAttribute('name') == selector){
                    console.log(e.target)
                    callback(e.target)
                }
                break

            case 'class':
                console.log('in case class')
                if (e.target.classList.contains(selector)){
                    console.log(e.target)
                    callback(e.target)
                }
                break

            case 'id':
                console.log('in case id')
                if (e.target.id == selector){
                    console.log(e.target)
                    callback(e.target)
                }
                break

        }
    })
}

function toggle_visibility(element_in_focus){
    // console.log("inside toggle visibility function")
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
        console.log(target_element)
        console.log(target_class)
        console.log(id_based)
        console.log(my_target)
        my_target.classList.toggle(target_class)
    }

    if (id_based == false) {
        my_targets = document.getElementsByClassName(target_element)
        
        for (let index = 0; index < my_targets.length; index++) {
            my_targets[index].classList.toggle(target_class)
        }
    }
}