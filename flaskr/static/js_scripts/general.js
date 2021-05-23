console.log("first line of general.js")
// Global functions

function get_last_url_segment(input_url){
    var parts = input_url.split("/")
    var last_segment = parts.pop() || parts.pop();  // handle potential trailing slash
    return last_segment
}

function create_global_event_listener(type, selector, callback, use_name){
    console.log("creating global event listerner")
    document.addEventListener(type, e => {
        if (use_name == true) {
            if (e.target.getAttribute('name') == selector){
                callback(e.target)
            }
        }

        if (use_name == false) {
            if (e.target.className == selector){
                callback(e.target)
            }
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
    // console.log(id_based)
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