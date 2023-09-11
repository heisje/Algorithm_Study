// 실버3 / 128ms
import java.io.*;
import java.util.*;

class Main_17484
{
    static int N, M;
    static int[][] arr;
    static int[][][] dp;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        dp = new int[N][M][3];

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solution();
    }

    private static void solution()
    {
        // 첫째줄 초기화
        for(int j=0; j<M; j++) {
            for(int k=0; k<3; k++) {
                dp[0][j][k] = arr[0][j];
            }
        }

        // 3차원 dp 배열 채우기
        for(int i=1; i<N; i++) {
            for(int j=0; j<M; j++) {
                for(int n=-1; n<=1; n++) {
                    if(j+n >= 0 && j+n < M){
                        int tmp = fn(n, dp[i-1][j+n]);
                        
                        dp[i][j][n+1] = tmp + arr[i][j];
                    }
                }
            }
        }

        // for(int i=0; i<N; i++){
        //     for(int j=0; j<M; j++){
        //         System.out.print("[ ");
        //         for(int k=0; k<3; k++){
        //             System.out.print(dp[i][j][k]+" ");
        //         }
        //         System.out.print("], ");
        //     }
        //     System.out.println();
        // }

        // 최소값 구하기
        int answer = Integer.MAX_VALUE;
        for(int j=0; j<M; j++){
            for(int k=0; k<3; k++){
                int tmp = dp[N-1][j][k];
                if(tmp != 0 && answer > tmp){
                    answer = tmp;
                }
            }
        }
        System.out.println(answer);
    }

    // dp 배열 채우는 함수
    private static int fn(int n, int[] nums)
    {
        if(n == -1) {
            if(nums[2] == 0) return nums[1];
            return Math.min(nums[1], nums[2]);
        } else if (n == 0) {
            if(nums[0] == 0) return nums[2];
            else if(nums[2] == 0) return nums[0];
            return Math.min(nums[0], nums[2]);
        } else {
            if(nums[0] == 0) return nums[1];
            return Math.min(nums[0], nums[1]);
        }
    }
}
