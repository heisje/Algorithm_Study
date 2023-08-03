// 500ms
function find(status, n){
    let left = 0
    let right = status.length - 1
    while(left <= right){
        const idx = parseInt((left + right) / 2)
        if(status[idx][0] < n){
            left = idx + 1
        }else{
            right = idx - 1
        }
    }
    return status[left][1]
}

function main(input){
    const [N, M] = input[0].split(' ').map((inp)=>parseInt(inp))
    const status = []
    let answer = ''
    const set = {}
    let i = 1 
    for (; i < N + 1 ; i++){
        const [name, stat] = input[i].split(' ')
        if (set[stat] == undefined){
            status.push([(parseInt(stat)), name])
            set[stat] = 1
        }
    }
    
    for (; i < M + N + 1 ; i++){
        const n = parseInt(input[i])
        answer = answer + find(status, n) + '\n'
    }
    console.log(answer.trim())
}

const input = `3 8
WEAK 10000
NORMAL 100000
STRONG 1000000
0
9999
10000
10001
50000
100000
500000
1000000`.trim().split('\n')
// const input = require('fs').readFileSync("/dev/stdin").toString().trim().split('\n')
main(input)