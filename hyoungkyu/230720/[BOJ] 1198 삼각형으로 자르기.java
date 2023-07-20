// 실버2 / 128ms
import java.io.*;

class Main
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] dots = new int[N][2];

        for (int i=0; i<N; i++) {
            String[] line = br.readLine().split(" ");
            dots[i][0] = Integer.parseInt(line[0]);
            dots[i][1] = Integer.parseInt(line[1]);
        }

        double maxV = 0;
        for (int i=0; i<N-2; i++) {
            for (int j=i+1; j<N-1; j++) {
                for (int k=j+1; k<N; k++) {
                    int[][] lst = {dots[i], dots[j], dots[k], dots[i]};
                    double tmp = func(lst);
                    if (maxV < tmp) maxV = tmp;
                }
            }
        }
        System.out.println(maxV);
	}

    public static double func(int[][] lst) {
        int tmp = 0;
        for (int i=0; i<3; i++) {
            tmp += (lst[i][0] * lst[i + 1][1] - lst[i + 1][0] * lst[i][1]);
        }
        return Math.abs(tmp) * 1.0 / 2;
    }
}