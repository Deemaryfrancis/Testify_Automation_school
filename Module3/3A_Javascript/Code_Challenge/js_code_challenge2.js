
//Create a length converter function
function lengthConverter(number,converter){
    let result=0;
        var unit = {
            'cm': 100,
            'km': 0.001,
            'mm': 1000,
        }
        for(var key in unit){
            result = number * unit[converter];
        }
        return result;
    }
    console.log(lengthConverter(27, 'cm'));