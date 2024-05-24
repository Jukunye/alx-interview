#!/usr/bin/node

const request = require('request');

const args = process.argv;
const movieUrlBase = 'https://swapi-api.hbtn.io/api/films/';
// Define URL for movie API endpoint using command-line argument
const movieUrl = `${movieUrlBase}${args[2]}/`;

let characterIndex = 0;
let characterUrls = [];

function getMovieDetails() {
  request(movieUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movieDetails = JSON.parse(body);
      characterUrls = movieDetails.characters;
      if (characterUrls.length > 0) {
        getCharacterDetails();
      }
    } else {
      console.log(error);
    }
  });
}

// Function to fetch character details from API
function getCharacterDetails() {
  if (characterIndex < characterUrls.length) {
    request(characterUrls[characterIndex], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const characterDetails = JSON.parse(body);
        console.log(characterDetails.name);
        characterIndex++;
        getCharacterDetails();
      } else {
        console.error('error:', error);
      }
    });
  }
}

getMovieDetails();
