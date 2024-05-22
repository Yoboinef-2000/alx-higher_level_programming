#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.error(err);
    } else {
      console.log(`Successfully saved contents of ${url} to ${filePath}`);
    }
  });
});
