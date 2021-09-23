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
create_global_event_listener("click", "button_roll", accorian_dice_roller_button, "class")
create_global_event_listener("click", "svg_roll_triangle", accorian_dice_roller_triangle, "class")

create_global_event_listener("animationend", "animation_roll_svg", remove_animation_roll_svg, "class")
create_global_event_listener("animationend", "animation_roll_path", remove_animation_roll_path, "class")
create_global_event_listener("animationend", "animation_roll_div", remove_animation_roll_div, "class")

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
    let current_tracker_stat = tracker_stat.value
    let target_container = get_tracker_container(tracker_stat)
    let added_class = tracker_stat.getAttribute('data-class-name')
    let current_trackers = target_container.getElementsByClassName(added_class)

    if (current_tracker_stat == current_trackers.length) { return }

    if (current_tracker_stat > current_trackers.length) {
        while (current_tracker_stat > current_trackers.length) {
            add_tracker(target_container, added_class)
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
        new_tracker.innerHTML = String(generate_n_random_number(1)[0])
    }
}

function get_tracker_container(tracker){
    switch (tracker.name) {
        case 'health_meter':
            return tracker.nextElementSibling
        case 'willpower_meter':
            return tracker.nextElementSibling
        case 'custom_meter':
            return tracker.nextElementSibling            
        case 'dice_meter':
            return tracker.parentElement.querySelector('.dice_container')        
        default:
            break;
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
    let roll = generate_n_random_number(dice.length)

    roll.sort((a, b) => a - b)

    roll = replace_10s_with_0s(roll)

    write_roll_numbers(roll, dice)

    allocate_hunger(dice, roll_button)
    
    add_svg_to_dice()

    add_animation_roll_load(dice)
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
            e.querySelector('.svg_dice').style.display = 'block'
        }
    })
}

function generate_n_random_number(n){
    let generated_numbers = []

    for (let index = 0; index <n; index++) {
        generated_numbers.push((Math.floor(Math.random() * 10)) + 1) // random gives values between 0 and 1, to have it go from 1 to 10, we add 1
    }
    return generated_numbers
}

function add_animation_roll_load(target_elements){
    target_elements.forEach(e => {
        let time_random_component = Math.random()

        e.classList.add('animation_roll_div')
        add_random_time_component(e, time_random_component)

        let target_svgs = e.getElementsByClassName('svg_dice')
        target_svgs[0].classList.add('animation_roll_svg')
        add_random_time_component(target_svgs[0], time_random_component)

        let target_paths = target_svgs[0].getElementsByClassName('path_dice')
        target_paths[0].classList.add('animation_roll_path')
        add_random_time_component(target_paths[0], time_random_component)
    })
}

function remove_animation_roll_svg(finished_element){
    finished_element.classList.remove('animation_roll_svg')
}

function remove_animation_roll_path(finished_element){
    finished_element.classList.remove('animation_roll_path')
}

function remove_animation_roll_div(finished_element){
    finished_element.classList.remove('animation_roll_div')
}

function add_random_time_component(target_element, time){
    target_element.style.animationDuration = String(1.2 + (time * 0.5)) + 's'
}

function accorian_dice_roller_button(current_button){
    let dice_roller_elements = current_button.parentElement.getElementsByClassName('dire_roller_element')
    for (let index = 0; index < dice_roller_elements.length; index++) {
        dice_roller_elements[index].classList.remove('dont_display')      
    }

    current_button.value = 'ROLL'
    handle_indicator_animation(current_button, dice_roller_elements)
}

function accorian_dice_roller_triangle(current_triangle){
    let dice_roller_elements = current_triangle.parentElement.getElementsByClassName('dire_roller_element')
    for (let index = 0; index < dice_roller_elements.length; index++) {
        dice_roller_elements[index].classList.toggle('dont_display')      
    }

    if (dice_roller_elements[0].classList.contains('dont_display')){
        current_triangle.previousElementSibling.value = 'SHOW DICE ROLLER'
    } else {
        current_triangle.previousElementSibling.value = 'ROLL'
    }

    handle_indicator_animation(current_triangle.previousElementSibling, dice_roller_elements)
}

function handle_indicator_animation(current_button, dice_roller_elements){
    if (dice_roller_elements[0].classList.contains('dont_display')){
        current_button.nextElementSibling.classList.add('triangle_closed')
    } else {
        current_button.nextElementSibling.classList.remove('triangle_closed')
    }
}