var dragItem = document.querySelector("#draggable_id");
var dragRegion = document.querySelector("#drag_region_id");
var container = dragItem;
//Declare Variables
var active = false;
var currentX;
var currentY;
var initialX;
var initialY;
var xOffset = 0;
var yOffset = 0;

//Add Event Listeners for Touchscreens
container.addEventListener("touchstart", dragStart, false);
container.addEventListener("touchend", dragEnd, false);
container.addEventListener("touchmove", drag, false);

//Add Event Listeners for Mouse
container.addEventListener("mousedown", dragStart, false);
container.addEventListener("mouseup", dragEnd, false);
container.addEventListener("mousemove", drag, false);


function dragStart(e) { //when the drag starts
  if (e.type === "touchstart") { //if its a touchscreen
    initialX = e.touches[0].clientX - xOffset; //set initial x-cordinate to where it was before drag started
    initialY = e.touches[0].clientY - yOffset; //set initial y-cordinate to where it was before drag started
  } else { //if its not a touchscreen (mouse)
    initialX = e.clientX - xOffset; //set initial x-cordinate to where it was before drag started
    initialY = e.clientY - yOffset; //set initial y-cordinate to where it was before drag started
  }
  if (e.target === dragItem) { //if user is dragging circle
    active = true; //the drag is active
  }
}

function dragEnd(e) { //when the drag ends
  const dragRegionSize = dragRegion.getBoundingClientRect(); //the size of dragRegion
  const elementSize = dragItem.getBoundingClientRect(); //the size of the circle
  if (elementSize.left >= dragRegionSize.left && elementSize.right <= dragRegionSize.right && elementSize.top >= dragRegionSize.top && elementSize.bottom <= dragRegionSize.bottom) { //if the circle is in dragRegion
    initialX = currentX; //set the initial x-cordinate to where it is now
    initialY = currentY; //set the initial y-cordinate to where it is now
  } 
  
  active = false; //the drag is no longer active
}
function drag(e) { //when the circle is being dragged
  if (active) { //if the drag is active
    e.preventDefault(); //the user cant do anything else but drag
  
    if (e.type === "touchmove") { //if its a touchscreen
      currentX = e.touches[0].clientX - initialX; //set current x-cordinate to where it is now
      currentY = e.touches[0].clientY - initialY; //set current y-cordinate to where it is now
    } else { //if its not a touchscreen (mouse)
      currentX = e.clientX - initialX; //set current x-cordinate to where it is now
      currentY = e.clientY - initialY; //set current y-cordinate to where it is now
    }
    
    //Im not sure what this does but it dosnt work without it
    xOffset = currentX;
    yOffset = currentY;
    setTranslate(currentX, currentY, dragItem);
  }
}

function setTranslate(xPos, yPos, el) { //Im not sure what this does but it dosnt work without it
  el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}