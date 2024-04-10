#!/usr/bin/node
const fs = require('fs');

function concatFiles (file1, file2, destination) {
  const data1 = fs.readFileSync(file1, 'utf8');
  const data2 = fs.readFileSync(file2, 'utf8');
  const cleanedData2 = data2.replace(/\n|\r/g, '');
  const concatenatedData = data1 + cleanedData2;
  fs.writeFileSync(destination, concatenatedData);
  console.log(concatenatedData);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

concatFiles(file1, file2, destination);
