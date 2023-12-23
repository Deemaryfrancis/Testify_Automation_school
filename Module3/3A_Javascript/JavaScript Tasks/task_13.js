const book = {
    title : 'My Javascript Journey',
    description : 'This is throw more details into my one-month javascript training journey with TAS',
    numberOfPage : 15,
    author : 'Mary Francis',
    reading : true,
    toggleReadingStatus: function() {
        if(book.reading === true) {
            book.reading = false
        } else {
            book.reading = true
        }
    }
}

book.reading = false;
book.toggleReadingStatus();
console.log(book.reading);
