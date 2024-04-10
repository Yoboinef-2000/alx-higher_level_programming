#!/usr/bin/node
exports.esrever = function (list) {
  const listLength = list.length - 1;
  for (let i = 0; i < listLength / 2; i++) {
    const temp = list[i];
    list[i] = list[listLength - i];
    list[listLength - i] = temp;
  }
  return (list);
};
