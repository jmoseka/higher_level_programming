#!/usr/bin/node
const myNumber = parseInt(process.argv[2]);
if (isNaN(myNumber)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < myNumber; i++) {
  console.log('C is fun');
}
