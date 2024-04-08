#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const numero = number + 1;
  theFunction(numero);
};
