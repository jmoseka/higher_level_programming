#!/usr/bin/node
let value = 0;
exports.logMe = function (item) {
  console.log(`${value++}: ${item}`);
};
