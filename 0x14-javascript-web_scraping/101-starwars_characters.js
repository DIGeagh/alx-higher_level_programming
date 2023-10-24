#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    const characters = [];

    // Create an array of promises for character data requests
    const characterPromises = characterUrls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const characterData = JSON.parse(charBody);
            characters.push(characterData.name);
            resolve();
          }
        });
      });
    });

    // Resolve all promises and print characters in order
    Promise.all(characterPromises)
      .then(() => {
        characters.forEach((characterName) => {
          console.log(characterName);
        });
      })
      .catch((err) => {
        console.error(err);
      });
  }
});
