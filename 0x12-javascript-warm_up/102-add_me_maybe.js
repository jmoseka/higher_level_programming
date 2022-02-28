#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  const sum = number + 1;
  theFunction(sum);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
