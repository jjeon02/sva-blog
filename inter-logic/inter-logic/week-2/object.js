// Assignment 1
// Pick four objects in everyday life and represent them as a data type

//Object 1 = Arrays
let myTools = ['Macbook', 'Ipad', 'Iphone'];

//Object 2 // Assignment 2 // Create an object and verify it using [https://jsonlint.com/]
let myMusic = {
    "App" : "Spotify Premium", 
    "instrument" : "Bass Guitar",
    "Genre" : "Rock",
    "Hello" : "World"
};

//Object 3 = Numbers
let currentYear = new Date().getFullYear();
let myYearsLeftinSchool = parseFloat(2024 - currentYear).toFixed(1);

//Object 4 = Hours I sleep
let mySleep = 5;
let mySleepBoolean = Boolean(mySleep > 6)

var mySleepStatus = function (mySleep){
    if(mySleep < 6){
        return "I have slept less than 6 hours per day this week."
    }
    else{
        return "I have slept more than 6 hours per day this week."
    }
}

// Assignment 3
// Create your own story algorithm. You can modify an example from class (story maker) or create your own. Remember to comment your code and use examples of: - user inputs - variables (int or float, string, boolean) - concatenation

let myStatement = "I do my homework using my" + myTools[0] + ". I usually listen to music using " + myMusic["App"] + " and my favourite instrument is " + myMusic["instrument"] + ". I am " + myYearsLeftinSchool + " years away from graduating from Grad School. " + mySleepStatus(5.2) + " The statement that I slept more than 6 hours is " + mySleepBoolean + "."

console.log(myStatement)

// Assignment 
// What if different types of data can be represented with lego blocks? They're good for visualizing since they are color-coded and easy to build structure. They can be used to represent quantity of the data - especially number as well.