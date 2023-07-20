// 188ms
function main() {
  let maxi = 0;
  for (let i = 0; i < arr.length; i++) {
    const p1X = arr[i][0];
    const p1Y = arr[i][1];
    for (let j = i + 1; j < arr.length; j++) {
      const p2X = arr[j][0];
      const p2Y = arr[j][1];
      for (let k = j + 1; k < arr.length; k++) {
        const p3X = arr[k][0];
        const p3Y = arr[k][1];

        const result = Math.abs(
          p1X * p2Y + p2X * p3Y + p3X * p1Y - p2X * p1Y - p3X * p2Y - p1X * p3Y
        );
        if (maxi < result) {
          maxi = result;
        }
      }
    }
  }
  console.log(maxi / 2);
}

const fs = require("fs");
const [n, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = input.map((i) => {
  return i.split(" ").map(Number);
});

main();
