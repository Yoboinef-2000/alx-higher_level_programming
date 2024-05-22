#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  for (const characterUrl of characters) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
