console.log("first line of navigation.js")

window.onload = start_logo_load_animation

// Navigaiton Functions

// Logo load animation

function start_logo_load_animation() {
    logo_elements = document.getElementsByClassName("logo_element")
    
    create_random_aniamtion_time()

    for (let index = 0; index < logo_elements.length; index++) {
        const element = logo_elements[index];

        // only calculate random time one per iteration
        if (element == logo_elements[0]){
            element.addEventListener('animationiteration', create_random_aniamtion_time)
            element.addEventListener('animationend', loop_standy_animation)
        }

        // start the animation by addig the animation class
        element.classList.add('animation_logo_load')
    }
}


function create_random_aniamtion_time(){
    base_time = get_css_variable('--load_animation_time')
    // console.log('base time:' + base_time)

    // get rid of "s" in the end
    base_time_corrected = parseFloat(base_time.slice(0, -1))

    random_component = (Math.random()) * 0.5
    // console.log('random:' + random_component)

    calculated_time = base_time_corrected + random_component + 's'
    // console.log('calculated time:' + calculated_time)
    
    // return the value to CSS
    set_css_variable('--load_animation_time_randomized', calculated_time)

}


function loop_standy_animation(){
    logo_elements = document.getElementsByClassName("logo_element")

    for (let index = 0; index < logo_elements.length; index++) {
        const element = logo_elements[index];

        // remove the load animation by addig the animation class
        element.classList.remove('animation_logo_load')

        // start the animation by addig the animation class
        element.classList.add('animation_logo_pulse')
    }

}
