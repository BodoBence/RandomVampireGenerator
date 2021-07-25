window.onload = start_logo_load_animation

function start_logo_load_animation() {
    logo_elements = document.getElementsByClassName("logo_element")    
    create_random_aniamtion_time()

    for (let index = 0; index < logo_elements.length; index++) {
        const element = logo_elements[index];

        if (element == logo_elements[0]){
            element.addEventListener('animationiteration', create_random_aniamtion_time)
            element.addEventListener('animationend', loop_standby_animation)
        }
        element.classList.add('animation_logo_load')
    }
}

function create_random_aniamtion_time(){
    base_time = get_css_variable('--load_animation_time')
    base_time_corrected = parseFloat(base_time.slice(0, -1))
    random_component = (Math.random()) * 0.5
    calculated_time = base_time_corrected + random_component + 's'
    set_css_variable('--load_animation_time_randomized', calculated_time)
}

function loop_standby_animation(){
    logo_elements = document.getElementsByClassName("logo_element")

    for (let index = 0; index < logo_elements.length; index++) {
        const element = logo_elements[index];
        element.classList.remove('animation_logo_load')

        // Do animation pulsation only on powerful phones / desktop
        if (window.innerWidth > 400){
            element.classList.add('animation_logo_pulse')
        }
    }

}
