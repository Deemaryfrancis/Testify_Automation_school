// const books = {
//     title : 'My Javascript Journey',
//     description : 'This is throw more details into my one-month javascript training journey with TAS',
//     numberOfPage : 15,
//     author : 'Mary Francis',
//     reading : true,
//     toggleReadingStatus : function (){
//         if(this.reading === false){
//             console.log(this.reading = true)
//         } else {
//             console.log(this.reading = false)
//         }
//     }
// }
// books.toggleReadingStatus()
// console.log(books.reading);
// console.log(books);

const books = [
    {
        title : 'My Javascript Journey',
        description : 'This is throw more details into my one-month javascript training journey with TAS',
        numberOfPage : 15,
        author : 'Mary Francis',
        reading : true
    },
    {
        title : 'My Python Journey',
        description : 'This is throw more details into my one-month python training journey with TAS',
        numberOfPage : 15,
        author : 'Mary Francis',
        reading : false
    },
    {
        title : 'My Switch to software testing Journey',
        description : 'This is throw more details into my three-month Switch to software testing training journey with TAS',
        numberOfPage : 20,
        author : 'Mary Francis',
        reading : true
    }
]
for (let i = 0; i <= books.length; i++){
    if(books[i].reading === true){
        console.log(books[i])
    }
}