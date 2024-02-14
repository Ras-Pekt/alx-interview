#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require("request");

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function printCharactersInOrder() {
  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    for (const characterUrl of movieResponse.characters) {
      const characterResponse = await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body));
          }
        });
      });
      console.log(characterResponse.name);
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

printCharactersInOrder();
