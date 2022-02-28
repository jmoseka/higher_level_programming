#!/usr/bin/node
const myArgs = process.argv[2];
if (myArgs === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
