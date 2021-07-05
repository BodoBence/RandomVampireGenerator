$('.cmd').click(function () {  
  var pdf = new jsPDF();
  var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
  };
  
  var $addr = $(this).closest('.res').find('.content');
  var $temp = $('.content-template');
  $temp.find('h3').text($addr.find('h3').text());
  pdf.fromHTML($temp.html(), 15, 15, {
        'width': 170,
        'elementHandlers':specialElementHandlers
	    }
  );
  pdf.save('sample-file.pdf');
});