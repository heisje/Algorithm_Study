import java.io.*;
import java.util.*;


public class BOJ_암기왕 {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();				// 다 모아서 한번에 출력 => 이거 안하면 시간초과;;
		
        int T = Integer.parseInt(br.readLine());
		// 테스트케이스
		for (int tc=0; tc<T; tc++) {			
			// 입력 받기
			int N = Integer.parseInt(br.readLine());
			HashSet<Integer> set = new HashSet<Integer>();	// HashSet 생성
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				set.add(Integer.parseInt(st1.nextToken()));	// HashSet에 한개씩 넣기
			}
			
			int M = Integer.parseInt(br.readLine());
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int i=0; i<M; i++) {
				int m = Integer.parseInt(st2.nextToken());
				boolean tmp = set.contains(m);				// 해당 값이 set에 있는지 확인
				if (tmp) {
					sb.append(1+"\n");					
				} else {					
					sb.append(0+"\n");
				}
				
			}
		}
    System.out.println(sb);
	}
}
