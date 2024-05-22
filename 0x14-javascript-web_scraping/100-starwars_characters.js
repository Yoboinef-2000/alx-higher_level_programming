#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);

  const fetchCharacterInfo = (url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  };

  film.characters.forEach((characterUrl) => {
    fetchCharacterInfo(characterUrl);
  });
});
