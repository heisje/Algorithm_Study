// 132 ms

// 슬라이딩 윈도우로 풀어래요..
// 1. a의 연속된 갯수는 a의 개수와 같다.
// 2. a의 연속된 갯수만큼 문자열을 잘라서 b가 몇 개인지 센다.
// 3. 최소 b가 나온 숫자가 최소 변경 횟수이다.

const main = (st) => {
  const arr = [...st];
  const aCount = arr.reduce((before, current) => {
    if (current === "a") {
      return before + 1;
    }
    return before;
  }, (before = 0));

  let minC = 1000000000000000;

  for (let i = aCount; i > 0; i--) {
    const newArr = [...arr.slice(arr.length - i, arr.length), ...arr.slice(0, aCount - i)];
    let c = aCount;
    for (let n of newArr) {
      if (n === "a") {
        c--;
      }
    }

    if (c < minC) {
      minC = c;
    }
  }

  for (let i = 0; i + aCount - 1 < arr.length; i++) {
    const newArr = arr.slice(i, aCount + i);
    let c = aCount;
    for (let n of newArr) {
      if (n === "a") {
        c--;
      }
    }

    if (c < minC) {
      minC = c;
    }
  }

  console.log(minC);
};

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
main(input);
