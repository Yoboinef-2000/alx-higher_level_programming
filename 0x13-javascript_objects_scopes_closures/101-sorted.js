#!/usr/bin/node

const { dict } = require('./101-data');

const listenBaby = Object.entries(dict).reduce((run, [key, value]) => {
  run[value] = run[value] ? [...run[value], key] : [key];
  return (run);
}, {});

console.log(listenBaby);
