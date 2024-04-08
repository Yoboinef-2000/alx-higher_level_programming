#!/usr/bin/node
const numArgs = process.argv.length;
if (numArgs < 2)
{
    console.log("Not a number");
}
else
{
    const firstArgument = parseInt(process.argv[2]);
    if (isNaN(firstArgument))
    {
        console.log("Not a number");
    }
    else
    {
        console.log("My number: " + firstArgument)
    }
}
