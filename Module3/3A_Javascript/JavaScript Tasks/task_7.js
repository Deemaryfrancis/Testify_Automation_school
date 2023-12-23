const typeOfTriangle = (x,y,z) => {
    const side1 = x;
    const side2 = y;
    const side3 = z;
    if(side1===side2 && side1===side3 && side2===side3) {
        console.log('Equilateral Triangle');
    } else if(side1===side2 || side1===side3 || side2===side3) {
        console.log('Isosceles Triangle');
    } else {
        console.log('Scalene Triangle');
    }
}

typeOfTriangle(1,2,4);
