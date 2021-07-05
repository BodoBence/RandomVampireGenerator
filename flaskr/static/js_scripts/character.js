create_global_event_listener("click", "button_discipline_skills", toggle_discipline_skills, 'class')
create_global_event_listener("click", "button_download_vampire", print_character, 'id')

function create_event_listener_for_skills(class_name, target_class_name){
    // console.log(class_name)
    var selected_class_elements = document.getElementsByClassName(class_name)
    // console.log(selected_class_elements)
    for (let index = 0; index < selected_class_elements.length; index++) {
        // console.log("loooop")
        // console.log(selected_class_elements[index])
        selected_class_elements[index].addEventListener("click", e =>{
            // console.log("inside the class based event listener creation")
            var reference = e.target.getAttribute("data-toggle-reference")
            var discipliine_skill_table = document.getElementsByClassName(target_class_name)[reference]
            // console.log(discipliine_skill_table.style.visibility)
            toggle_visibility(discipliine_skill_table)
        })
    }
}

function toggle_discipline_skills (pressed_button){
    selection_class = pressed_button.getAttribute("data-toggle-selection-class")
    target_reference = pressed_button.getAttribute("data-toggle-reference")

    target_element = document.getElementsByClassName(selection_class)[target_reference]

    toogle_max_height(target_element)
}

function print_character(){
    console.log("in saving the character locally")
    // window.print()

    // HTML2CANVAS SOLUTION
    // html2canvas(document.getElementById('generated_character_id'), {
    //     onrendered: function(canvas) {
    //         // document.body.appendChild(canvas);
    //         return Canvas2Image.saveAsPNG(canvas);
    //     }
    // });

    // JSPDF SOLUTION:

    // var output_pdf = new jsPDF()
    // var character_sheet = document.getElementById('generated_character_id')

    // output_pdf.fromHTML(character_sheet, 20, 20, {
    //     'width': 1000
    // })

    // output_pdf.save('test.pdf')


    // JSPDF SOLUTION 2


    // var output_pdf = new jsPDF()
    // var character_sheet = document.getElementById('generated_character_id')

    // output_pdf.html(character_sheet, {
    //     callback: function (output_pdf) {
    //         output_pdf.save();
    //     }
            
    // })

    // JSPDF + HTML2CANVAS SOLUTION:
    
    // var character_sheet = document.getElementById('generated_character_id')
    
    // html2canvas(character_sheet, {
    //     onrendered: function(canvas) {

    //         var image = canvas.toDataURL("image/png")
    //         var output_pdf = new jsPDF()
    //         console.log('got this far')
    //         output_pdf.addImage(image, 'JPEG', 0, 0, 1000)
    //         output_pdf.save('test.pdf')
    //     }
    // })

    //  JSPDF + HTML2CANVAS SOLUTION 2

    var character_sheet = document.getElementById('generated_character_id')
    // var pdf = new jsPDF('p', 'px', [1000, 3000]);
    var pdf = new jsPDF('p', 'px');
    pdf.addHTML(character_sheet, function () {
        console.log('generating pdf')
        pdf.save('Test.pdf');
    });

}
