// 실버2 / 236ms
import java.io.*;

class Main_15990
{
    static int N;
    static long[][] DP = new long[100001][3];
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        // 초기화
        for(int i=0; i<2; i++){
            for(int j=0; j<3; j++){
                DP[i][j] = 0;
            }
        }
        DP[1][0] = 1;
        DP[2][1] = 1;
        DP[3][0] = 1;
        DP[3][1] = 1;
        DP[3][2] = 1;
        int maxV = 4;

        for(int i=0; i<T; i++){
            N = Integer.parseInt(br.readLine());
            if(maxV <= N){
                for(int j=maxV; j<N+1; j++){
                    DP[j][0] = (DP[j-1][1]+DP[j-1][2])%1000000009;
                    DP[j][1] = (DP[j-2][0]+DP[j-2][2])%1000000009;
                    DP[j][2] = (DP[j-3][0]+DP[j-3][1])%1000000009;
                }
                maxV = N;
            }
            System.out.println((DP[N][0]+DP[N][1]+DP[N][2])%1000000009);
        }
    }
}
// 3 - 3
// 1+2
// 2+1
// 3

// 4 - 3
// 1+2+1
// 1+3
// 3+1

// 5 - 4
// 1+3+1
// 2+1+2
// 2+3
// 3+2

// 6 - 8
// 1+2+1+2
// 1+2+3
// 1+3+2
// 2+1+2+1
// 2+1+3
// 2+3+1
// 3+1+2
// 3+2+1

// 7 - 9

// 10 - 27