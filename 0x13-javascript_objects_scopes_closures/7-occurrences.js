#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (const nb of list) {
    if (nb === searchElement) {
      occ++;
    }
  }
  return occ;
};
