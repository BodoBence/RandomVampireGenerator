create_global_event_listener("mouseover", "rectangle_input_container", rectangle_input,"class")

function rectangle_input(e){
    let mousePosition;
    let offset = [0,0];
    let isDown = false;
    let div = e.querySelector('.rectange_input_cursor')
    let container = e

    // input tracking values:
    let left_top = [div.offsetLeft / container.offsetWidth, div.offsetTop / container.offsetHeight]
    let right_top = [(div.offsetLeft + container.offsetWidth) / container.offsetWidth, div.offsetTop / container.offsetHeight]
    let left_bottom = [div.offsetLeft / container.offsetWidth, (div.offsetTop + container.offsetHeight)/ container.offsetHeight]
    let right_bottom = [(div.offsetLeft + container.offsetWidth) / container.offsetWidth, (div.offsetTop + container.offsetHeight)/ container.offsetHeight]

    div.addEventListener('mousedown', function(e) {
        isDown = true;
        offset = [
            div.offsetLeft - e.clientX,
            div.offsetTop - e.clientY
        ];
    }, true);
    
    document.addEventListener('mouseup', function() {
        isDown = false;
        console.log('---------------------------')
        console.log('left_top' + left_top)
        console.log('right_top' + right_top)
        console.log('left_bottom' + left_bottom)
        console.log('right_bottom' + right_bottom)
    }, true);
    
    document.addEventListener('mousemove', function(event) {
        if (isDown) {
            mousePosition = {
                x : Math.min(Math.max(event.clientX, container.offsetLeft), (container.offsetLeft + container.offsetWidth)),
                y : Math.min(Math.max(event.clientY, container.offsetTop), (container.offsetTop + container.offsetHeight))
            };
            div.style.left = (mousePosition.x + offset[0]) + 'px';
            div.style.top  = (mousePosition.y + offset[1]) + 'px';
        }
    }, true);
}
