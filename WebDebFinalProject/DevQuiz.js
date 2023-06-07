//form validation
function validateForm() 
{
    //creating variables
    var radio1 = document.quiz.rad1;
    var radio2 = document.quiz.rad2;
    var valOps = document.quiz.prior;
    var radio3 = document.quiz.rad3;
    var radio4 = document.quiz.rad4;
    var tx1 = document.quiz.text1;
    //calling functions
    vWebRes(radio1, radio2);
    valOps(prior);
    vData(radio3, radio4);
    vLength(tx1);
    vCheck2(Text);
    
        if (vWebRes(radio1, radio2, radio3, radio4)) {
            if (valOps(prior)) {
                if (vData(radio3, radio4)) {
                    if (vLength(tx1)) {
                        if (vCheck2(tx1)) {
                        return false;
                    }
                }
            }
        }
    }
    //validating radio buttons
    function vWebRes(radio1, radio2)
    {
        x=0;
        if ((radio1.checked) || (radio2.checked)) {
            x++;
        }
        if (x==0) {
            alert('You forgot a question!')
            radio1.focus();
            return false;
        }
        else {
            return true;
        }
    }
    //validating checkbox options
    function valOps(prior) {
        if (prior.value == "Default") {
            alert('Select an option from the drop-down menu');
            prior.focus();
            return false;
        }
        else {
            return true;
        }
    }
    //validation question 3
    function vData(radio3, radio4) {
        z=0;
        if ((radio3.checked) || (radio4.checked)) {
            z++;
        }
        if (z==0){
            alert('You forgot a question!')
            radio3.focus();
            return false;
        }
        else {
            return true;
        }
    }
    //validating text length
    function vLength(tx1) {
        var txLength = tx1.value.length;
        if (txLength > 3) {
            alert("That is an incorrect entry, try again.");
            tx1.focus();
            return false;
        }
        else {
            return true;
        }
    }
    //validating text entry
    function vCheck2(tx1) {
        if ((tx1 == "Yes" || tx1 == "yes") || (tx1 == "No" || tx1 == "no")) {
            tx1.focus();
            return true;
        }
        else {
            alert('You entered an incorrect value, try again')
            tx1.focus();
            return false;
        }
    }
}
