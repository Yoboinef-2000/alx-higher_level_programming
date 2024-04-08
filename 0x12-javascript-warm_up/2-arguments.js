#!/usr/bin/env node
const numArgs = process.argv.length - 2;
if (numArgs < 2)
{
    console.log("No argument");
}
else if (numArgs === 3)
{
    console.log("Argument found");
}
else
{
    console.log("Arguments found");
}
