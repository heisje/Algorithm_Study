package algo;

import java.util.*;
import java.io.*;

public class BOJ_10844_쉬운계단수 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		long cnt = 9;
		// 초기값 세팅
		long[] check = new long[10];
		for (int i=1; i<10; i++) {
			check[i] = 1;
		}
		
		for (int n=1; n<N; n++) {			
			// 다음 수들을 담을 임시 배열
			cnt = 0;
			long[] tmp = new long[10];
			for (int i=0; i<10; i++) {
				if (i == 0) {
					tmp[i+1] += check[i]%1000000000;
					cnt += check[i]%1000000000;
				} else if (i == 9) {
					tmp[i-1] += check[i]%1000000000;
					cnt += check[i]%1000000000;
				} else {
					tmp[i-1] += check[i]%1000000000;
					tmp[i+1] += check[i]%1000000000;
					cnt += (check[i]%1000000000) * 2;
				}
			}
			check = Arrays.copyOf(tmp, 10);
		}
		
		System.out.println((long) (cnt%1000000000));
	}
}

// N = 1 : 9
// N = 2 : (9*2)-1 = 17
// N = 3 : ((9*2)-1)*2-2 = 32


// 1 - 10, 12 - 101, 121, 123
// 2 - 21, 23 - 210, 212, 232, 234
// 3 - 32, 34 - 
// 4 - 43, 45
// 5 - 54, 56
// 6 - 65, 67
// 7 - 76, 78
// 8 - 87, 89 - 876, 878, 898
// 9 - 98	  - 987, 989
