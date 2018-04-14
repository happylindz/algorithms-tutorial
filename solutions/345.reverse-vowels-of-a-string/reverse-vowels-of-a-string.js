/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {

    var array = s.split("");
    var len = array.length;
    var index = len - 1;
    for (var i = 0; i < len; i++) {

        if (array[i].toUpperCase() == "A" || array[i].toUpperCase() == "E" || array[i].toUpperCase() == 'I' || array[i].toUpperCase() == "O" || array[i].toUpperCase() == "U") {

            for (var j = index; j >= 0; j--) {


                if (j <= i) {
                    return array.join("");
                }

                if (array[j].toUpperCase() == "A" || array[j].toUpperCase() == "E" || array[j].toUpperCase() == 'I' || array[j].toUpperCase() == "O" || array[j].toUpperCase() == "U") {
                    index = j - 1;
                    var temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;


                    break;
                }
            }
        }
    }

    return array.join("");

};
