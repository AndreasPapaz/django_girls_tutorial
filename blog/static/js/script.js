// $(document).ready(function(){
//   var i=1;
//
//   var table = document.getElementById('tab_logic');
//   var row = document.getElementById('addr0');
//
//   $("#add_row").click(function(){
//       var lastRow = i - 1;
//       var appendRow = document.getElementById('addr' + lastRow);
//       var copyRow = row.cloneNode(true);
//       copyRow.id = 'addr'+i;
//       appendRow.after(copyRow);
//       i++;
//
//     });
//
//     $("#delete_row").click(function(){
//       if(i > 1){
//       $("#addr"+(i-1)).html('');
//         i--;
//     }
//   });
//
//   $('.file_upload').click(function(){
//     var inputs = $('.img_input');
//
//     Array.prototype.forEach.call( inputs, function(input) {
//
//       var label = input.nextElementSibling,
//       labelVal = label.innerHTML;
//
//       input.addEventListener('change', function(e){
//         var fileName = '';
//         if (this.files && this.files.length > 1){
//             fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
//         }
//         else{
//             fileName = e.target.value.split('\\').pop();
//         }
//
//         if (fileName){
//             label.innerHTML = fileName
//         }
//         else{
//             label.innerHTML = labelVal;
//         }
//       });
//     });
//   });
//
// });
