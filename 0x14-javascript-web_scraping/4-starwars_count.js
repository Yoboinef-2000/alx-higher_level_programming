#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const wedgeAntillesId = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(wedgeAntillesId)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.error('Error: Request failed with status code', response.statusCode);
  }
});
