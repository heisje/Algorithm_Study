function solution(alp, cop, problems) {
  // 2차원 배열 dp
  let maxA = 0;
  let maxC = 0;

  for (let i = 0; i < problems.length; i++) {
    const [alp_req, cop_req, alp_rwd, cop_rwd, cost] = problems[i];
    maxA = Math.max(alp_req, maxA);
    maxC = Math.max(cop_req, maxC);
  }

  const dp = Array.from(Array(maxA + 1), () => Array(maxC + 1).fill(10000000));
  dp[Math.min(alp, maxA)][Math.min(cop, maxC)] = 0;

  for (let a = Math.min(alp, maxA); a <= maxA; a++) {
    for (let c = Math.min(cop, maxC); c <= maxC; c++) {
      if (a + 1 <= maxA) dp[a + 1][c] = Math.min(dp[a + 1][c], dp[a][c] + 1);

      if (c + 1 <= maxC) dp[a][c + 1] = Math.min(dp[a][c + 1], dp[a][c] + 1);

      for (let i = 0; i < problems.length; i++) {
        const [alp_req, cop_req, alp_rwd, cop_rwd, cost] = problems[i];

        if (alp_req <= a && cop_req <= c) {
          let goA = Math.min(a + alp_rwd, maxA);
          let goC = Math.min(c + cop_rwd, maxC);

          dp[goA][goC] = Math.min(dp[goA][goC], dp[a][c] + cost);
        }
      }
    }
  }

  return dp[dp.length - 1][dp[dp.length - 1].length - 1];
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.53ms, 33.5MB)
// 테스트 2 〉	통과 (0.79ms, 33.5MB)
// 테스트 3 〉	통과 (0.37ms, 33.5MB)
// 테스트 4 〉	통과 (0.45ms, 33.4MB)
// 테스트 5 〉	통과 (0.72ms, 33.7MB)
// 테스트 6 〉	통과 (0.48ms, 33.6MB)
// 테스트 7 〉	통과 (0.59ms, 33.5MB)
// 테스트 8 〉	통과 (0.48ms, 33.5MB)
// 테스트 9 〉	통과 (0.39ms, 33.5MB)
// 테스트 10 〉	통과 (0.36ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (14.53ms, 38.7MB)
// 테스트 2 〉	통과 (22.23ms, 39.7MB)
// 테스트 3 〉	통과 (4.37ms, 35MB)
// 테스트 4 〉	통과 (19.48ms, 39.8MB)
// 테스트 5 〉	통과 (27.44ms, 39.9MB)
// 테스트 6 〉	통과 (20.39ms, 39.9MB)
// 테스트 7 〉	통과 (30.01ms, 39.9MB)
// 테스트 8 〉	통과 (20.21ms, 38.8MB)
// 테스트 9 〉	통과 (38.12ms, 39.9MB)
// 테스트 10 〉	통과 (11.49ms, 38.7MB)
