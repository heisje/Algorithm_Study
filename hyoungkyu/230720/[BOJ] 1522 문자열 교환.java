// 실버1 / 136ms
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// StringBuilder sb = new StringBuilder();				// 다 모아서 한번에 출력 => 이거 안하면 시간초과;;
		String S = br.readLine();
        int lenA = (int) S.chars().filter(i -> String.valueOf((char) i).equals("a")).count();
        S = S + S;
        int minV = S.length();
        for (int i=0; i<S.length()-lenA; i++) {
            int tmp = (int) S.substring(i, i+lenA).chars().filter(j -> String.valueOf((char) j).equals("b")).count();
            minV = Math.min(minV, tmp);
        }
        System.out.println(minV);
	}
}