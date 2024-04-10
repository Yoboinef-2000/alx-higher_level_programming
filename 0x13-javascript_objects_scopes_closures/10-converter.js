#!/usr/bin/node
exports.converter = function (base) {
  function convert (num) {
    if (num < base) {
      return num.toString(base);
    }
    return convert(Math.floor(num / base)) + (num % base);
  }
  return convert;
};
