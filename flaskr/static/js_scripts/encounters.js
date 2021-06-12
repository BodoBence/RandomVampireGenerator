
create_checkboxes()
create_global_event_listener("click", "tracker", toggle_filled, "class")
create_global_event_listener("input", "health_meter", update_value, "name")
create_global_event_listener("input", "willpower_meter", update_value, "name")
create_global_event_listener("input", "custom_meter", update_value, "name")
create_global_event_listener("click", "add_encounter", add_encounter, "name")
create_global_event_listener("click", "remove_encounter", remove_encounter, "name")

// Connected to checkboxes

function create_checkboxes(){
    healths = document.getElementsByName("health_meter")
    willpowers = document.getElementsByName("willpower_meter")
    customs = document.getElementsByName("custom_meter")
    // console.log(customs)
    // console.log(healths)
    // console.log(willpowers)

    for (let index = 0; index < healths.length; index++) {
        console.log("updating health boxes")
        console.log(healths[index])
        update_value(healths[index])
    }
    
    for (let index = 0; index < willpowers.length; index++) {
        console.log("updating willpower boxes")
        update_value(willpowers[index])
    }

    for (let index = 0; index < customs.length; index++) {
        console.log("updating custom boxes")
        update_value(customs[index])
    }

}

function update_value(tracker_stat){
    current_tracker_stat = tracker_stat.value
    // console.log("updating value")
    // console.log(current_tracker_stat)
    current_parent = tracker_stat.nextElementSibling
    // console.log(current_parent)

    current_trackers = current_parent.getElementsByClassName("tracker")

    if (current_tracker_stat == current_trackers.length) {return}

    if (current_tracker_stat > current_trackers.length){
        while (current_tracker_stat > current_trackers.length){
            add_tracker(current_parent)
        }
    }

    if (current_tracker_stat < current_trackers.length) {
        while (current_tracker_stat < current_trackers.length) {
            current_trackers[current_trackers.length-1].remove()
        }
    }
}

function add_tracker(current_target){
    new_tracker = document.createElement("div")
    new_tracker.className = "tracker"
    current_target.appendChild(new_tracker)
}

function toggle_filled(element_in_focus){
    element_in_focus.classList.toggle('tracker_clicked')
}

// Connected to encounters

function add_encounter(){
    console.log("adding encounter")
    encounters = document.getElementsByClassName("div_encounter_card")
    number_of_encounters = encounters.length

    if (number_of_encounters < 10){
        last_encounter = encounters[encounters.length-1]
        encounter_cloned = last_encounter.cloneNode(true)
        last_encounter.parentElement.appendChild(encounter_cloned)
    }
}

function remove_encounter(current_button){
    number_of_encounters = document.getElementsByClassName("div_encounter_card").length
    console.log(number_of_encounters)

    if (number_of_encounters > 1){
        current_encounter = current_button.parentElement.parentElement
        console.log(current_encounter)
        current_encounter.remove()
    }
}