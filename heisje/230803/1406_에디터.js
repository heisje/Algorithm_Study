// 764ms

class Editor {
  constructor(string, N, obInputs) {
    this.lStack = [...string];
    this.rStack = [];
    this.N = N;
    this.inputs = obInputs;
    this.go = {
      L: this.l.bind(this),
      D: this.d.bind(this),
      B: this.b.bind(this),
      P: this.p.bind(this),
    };
  }

  run() {}

  l() {
    if (this.lStack.length > 0) {
      this.rStack.push(this.lStack.pop());
    }
  }

  d() {
    if (this.rStack.length) {
      this.lStack.push(this.rStack.pop());
    }
  }

  b() {
    this.lStack.pop();
  }

  p(char) {
    this.lStack.push(char);
  }
}

function main(editor) {
  editor.run();
  editor.inputs.forEach((element) => {
    editor.go[element[0]](element[1]);
  });
  console.log(editor.lStack.join("") + editor.rStack.reverse().join(""));
}

const raw = `abc
9
L
L
L
L
L
P x
L
B
P y`;
// let fs = require("fs");
// const raw = fs.readFileSync("/dev/stdin");
const [string, N, ...inputs] = raw.toString().trim().split("\n");
const obInputs = inputs.map((a) => {
  return a.split(" ");
});
const editor = new Editor(string, parseInt(N), obInputs);
main(editor);
