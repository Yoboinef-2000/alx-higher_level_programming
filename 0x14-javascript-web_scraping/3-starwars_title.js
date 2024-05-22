#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.error('Error: Request failed with status code', response.statusCode);
  }
});
