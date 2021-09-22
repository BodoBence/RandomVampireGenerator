create_checkboxes()
add_svg_to_dice()

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

    if (tracker_stat.name == 'dice_meter'){
        add_svg_to_dice()
    }
}

function add_tracker(current_target, chosen_class_name) {
    new_tracker = document.createElement('div')
    new_tracker.className = chosen_class_name
    current_target.appendChild(new_tracker)

    if (chosen_class_name === 'dice'){
        new_tracker.innerHTML = '0'
    }
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

// Connected to Dire rolling

function roll_the_dice(roll_button) {
    // creates random numbers between 1 and 10 for each dice respective of the roll button
    let dice = roll_button.parentElement.querySelectorAll(".dice")
    let roll = []

    for (let index = 0; index < dice.length; index++) {
        roll.push((Math.floor(Math.random() * 10)) + 1) // random gives values between 0 and 1, to have it go from 1 to 10, we add 1
    }

    roll.sort((a, b) => a - b)

    roll = replace_10s_with_0s(roll)

    write_roll_numbers(roll, dice)

    allocate_hunger(dice, roll_button)
    
    add_svg_to_dice()
}

function replace_10s_with_0s(pool){
    for (let index = 0; index < pool.length; index++) {
        if (pool[index] == 10){
            pool[index] = 0
        }
    }
    
    return pool
}

function write_roll_numbers(roll, dice) {
    for (let index = 0; index < roll.length; index++) {
        dice[index].innerHTML = roll[index]  
    }
}

function allocate_hunger(dice, roll_button) {
    let hunger_value = roll_button.parentElement.querySelector("input[name='hunger_meter']").value

    if (hunger_value == 0) {
    } else {

        // get rid of current hunger dice
        dice.forEach(e => {
            if (e.classList.contains('dice_hunger'))
            e.classList.remove('dice_hunger')
        })

        // assign new hunger dice
        hunger_dice = array_sampler(Array.from(dice), hunger_value) // defined in general.js
        for (let index = 0; index < hunger_dice.length; index++) {
            hunger_dice[index].classList.add('dice_hunger')
        }
    }
}

function add_svg_to_dice(){
    let svg_type = document.querySelector('.svg_dice')
    let dice = document.querySelectorAll('.dice')

    dice.forEach(e => {
        if (e.children.length == 0){
            let svg_token = svg_type.cloneNode(true)
            e.appendChild(svg_token)
            e.querySelector('.svg_dice').style.visibility = 'initial'
        }
    })
}