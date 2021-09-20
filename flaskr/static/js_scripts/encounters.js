
create_checkboxes()

create_global_event_listener("click", "tracker", toggle_filled, "class")

create_global_event_listener("input", "health_meter", update_value, "name")
create_global_event_listener("input", "willpower_meter", update_value, "name")
create_global_event_listener("input", "custom_meter", update_value, "name")
create_global_event_listener("input", "dice_meter", update_value, "name")

create_global_event_listener("click", "add_encounter", add_encounter, "name")
create_global_event_listener("click", "remove_encounter", remove_encounter, "name")

create_global_event_listener("click", "button_roll", roll_the_dice, "class")

// Connected to checkboxes

function create_checkboxes() {
    let healths = document.getElementsByName("health_meter")
    let willpowers = document.getElementsByName("willpower_meter")
    let customs = document.getElementsByName("custom_meter")
    let dice = document.getElementsByName("dice_meter")

    for (let index = 0; index < healths.length; index++) {
        update_value(healths[index])
    }

    for (let index = 0; index < willpowers.length; index++) {
        update_value(willpowers[index])
    }

    for (let index = 0; index < customs.length; index++) {
        update_value(customs[index])
    }

    for (let index = 0; index < dice.length; index++) {
        update_value(dice[index])
    }
}

function update_value(tracker_stat) {
    current_tracker_stat = tracker_stat.value
    current_parent = tracker_stat.nextElementSibling
    added_class = tracker_stat.getAttribute('data-class-name')
    current_trackers = current_parent.getElementsByClassName(added_class)

    if (current_tracker_stat == current_trackers.length) { return }

    if (current_tracker_stat > current_trackers.length) {
        while (current_tracker_stat > current_trackers.length) {
            add_tracker(current_parent, added_class)
        }
    }

    if (current_tracker_stat < current_trackers.length) {
        while (current_tracker_stat < current_trackers.length) {
            current_trackers[current_trackers.length - 1].remove()
        }
    }
}

function add_tracker(current_target, chosen_class_name) {
    new_tracker = document.createElement('div')
    new_tracker.className = chosen_class_name
    current_target.appendChild(new_tracker)
}

function toggle_filled(element_in_focus) {
    element_in_focus.classList.toggle('tracker_clicked')
}

// Connected to encounters

function add_encounter() {
    encounters = document.getElementsByClassName('div_encounter_card')
    number_of_encounters = encounters.length

    if (number_of_encounters < 10) {
        last_encounter = encounters[encounters.length - 1]
        encounter_cloned = last_encounter.cloneNode(true)
        last_encounter.parentElement.appendChild(encounter_cloned)
    }
}

function remove_encounter(current_button) {
    number_of_encounters = document.getElementsByClassName("div_encounter_card").length

    if (number_of_encounters > 1) {
        current_encounter = current_button.parentElement.parentElement
        console.log(current_encounter)
        current_encounter.remove()
    }
}

function roll_the_dice(roll_button) {
    let difficulty = roll_button.parentElement.querySelector("input[name='diffculty_meter']").value
    let number_of_dice = roll_button.parentElement.querySelector("input[name='dice_meter']").value
    let hunger = roll_button.parentElement.querySelector("input[name='hunger_meter']").value
    let dice = roll_button.parentElement.querySelectorAll(".dice")
    let critical = 0
    let bestial_faliure = 0
    let messy_critical = 0 
    let succes = 0
    let faliure = 0

    if (hunger > 0) {
        for (let index = 0; index < hunger; index++) {
            dice[index].classList.append('hunger')
        }
    }

    // roll each die
    dice.forEach(element => {
        if (element.classList.contains('hunger') == true){
            let die_type = 'hunger'
        }  

        let roll = Math.floor(Math.random() * 10)
        if (1 == roll) {
            faliure = faliure + 1
        }
        if (6 <= roll && roll <= 9) {
            succes = succes + 1
        }
        if (0 == roll) {
            critical = critical + 1
        }
        console.log(roll)
    })

    // calcualte result
    if (critical % 2 == 0 && critical != 0) {
        critical = critical * 2
    }

    if (faliure < succes) {
        succes = succes - faliure
    } 

    let roll_result = succes + critical 
    if (roll_result >= difficulty) {
        console.log('succes, with a margin of: ' + String(roll_result - difficulty))
    } else {
        console.log('failue with a margin of: ' + String(difficulty - roll_result))
    }



}