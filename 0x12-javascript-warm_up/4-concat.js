#!/usr/bin/node
const arguments = process.argv;
const numArgs = process.argv.length;
let firstargument;
let secondargument;
if (numArgs < 2)
{
    firstargument = "undefined";
    secondargument = "undefined";
}
else if (numArgs === 3)
{
    firstargument = arguments[2];
    secondargument = "undefined";
}
else
{
    firstargument = arguments[2];
    secondargument = arguments[3];
}
console.log(firstargument + " is " + secondargument);
