
create_checkboxes()
create_global_event_listener("click", "tracker", toggle_filled, false)
create_global_event_listener("input", "health_meter", update_value, true)
create_global_event_listener("input", "willpower_meter", update_value, true)
create_global_event_listener("click", "add", add_encounter, true)
create_global_event_listener("click", "remove", remove_encounter, true)


// Connected to checkboxes

function create_checkboxes(element_in_focus){
    healths = document.getElementsByName("health_meter")
    willpowers = document.getElementsByName("willpower_meter")
    for (let index = 0; index < healths.length; index++) {
        update_value(healths[index])
    }
    for (let index = 0; index < willpowers.length; index++) {
        update_value(willpowers[index])
    }
}

function update_value(tracker_stat){
    current_tracker_stat = tracker_stat.value
    console.log(current_tracker_stat)
    current_parent = tracker_stat.parentElement
    current_trackers = current_parent.nextElementSibling.getElementsByClassName("tracker")

    if (current_tracker_stat == current_trackers.length) {return}

    if (current_tracker_stat > current_trackers.length){
        while (current_tracker_stat > current_trackers.length){
            add_tracker(current_trackers[0].parentElement)
        }
    }

    if (current_tracker_stat < current_trackers.length) {
        while (current_tracker_stat < current_trackers.length) {
            current_trackers[current_trackers.length-1].remove()
        }
    }
}

function add_tracker(current_target){
    new_tracker = document.createElement("td")
    new_tracker.className = "tracker"
    new_tracker.style.backgroundColor = 'var(--grey)'
    current_target.appendChild(new_tracker)
}

function toggle_filled(element_in_focus){
    if (element_in_focus.style.backgroundColor == 'var(--bg)') {
        element_in_focus.style.backgroundColor = 'var(--grey)';
    } else {
        element_in_focus.style.backgroundColor = 'var(--bg)';
    }
}

// Connected to encounters

function add_encounter(){
    encounters = document.getElementsByClassName("encounter")
    number_of_encounters = encounters.length

    if (number_of_encounters < 10){
        last_encounter = encounters[encounters.length-1]
        encounter_cloned = last_encounter.cloneNode(true)
        last_encounter.parentElement.appendChild(encounter_cloned)
    }
}

function remove_encounter(current_button){
    number_of_encounters = document.getElementsByClassName("encounter").length
    
    if (number_of_encounters > 1){
        current_encounter = current_button.parentElement.parentElement
        current_encounter.remove()
    }
}