// scripts here:
function submitQuiz(myform) {
  "use strict";
  var errMsg = [];
  var hasError = false;
  if (!myform.rad1.value) {
    errMsg.push('Input Question 1');
    myform.rad1[0].focus();//focus 1st option
    hasError = true;
  }
  if (myform.prior.value === 'none') {
    errMsg.push('Input Question 2');
    hasError || myform.prior.focus();
    hasError = true;
  }
  if (!myform.rad2.value) {
    errMsg.push('Input Question 3');
    hasError || myform.rad2[0].focus();
    hasError = true;
  }
  if (myform.tx1.value.toLowerCase() !== 'yes' && myform.tx1.value.toLowerCase() !== 'no') {
    errMsg.push('Please enter Yes or No');
    hasError || myform.tx1.focus();
    hasError = true;
  }
  if (hasError) {
    alert(errMsg.join('\n'));
    return false;
  }
  //return false for debug purpose. In production return true
  alert('Submitting form');
 // return false;
}