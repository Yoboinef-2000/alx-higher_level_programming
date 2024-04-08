#!/usr/bin/env node
const firstargument = process.argv;
const firstInt = Number(firstargument[2]);
if (isNaN(firstInt))
{
    console.log("Missing number of occurences");
}
else
{
    for (let i = 0; i < firstInt; i++)
    {
        console.log("C is fun");
    }
}
