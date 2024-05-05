const fs = require('fs');
const csv = require('csvtojson');

(async () => {
  const cot = await csv().fromFile('D:/과학/과고/수행/지학/preview/examples/simple-viewer/cot.csv').then((jsonArray) => {
    // 여기서 jsonArray는 CSV 파일을 JSON 형식으로 변환한 배열입니다.
    return jsonArray;
  });

  const cth = await csv().fromFile('D:/과학/과고/수행/지학/preview/examples/simple-viewer/cth.csv').then((jsonArray) => {
    // 여기서 jsonArray는 CSV 파일을 JSON 형식으로 변환한 배열입니다.
    return jsonArray;
  });

  var convertedCot = cot.map(function(row) {
    return Object.values(row).map(function(element) {
      return parseFloat(element, 10);
    });
  });
  var convertedCth = cth.map(function(row) {
    return Object.values(row).map(function(element) {
      return parseFloat(element, 10);
    });
  });
  console.log(convertedCot);
  console.log(convertedCth);
})();