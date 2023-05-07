import java.io.*;
import java.util.*;

public class BOJ_2636_치즈 {
	static int[][] D = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};	// 상우하좌
	static int[][] arr;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]), M = Integer.parseInt(input[1]);
		arr = new int[N][M];
		
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int cnt = 0;
		int tmp = 0;
		int i = 0;
		
		while(true) {
			changeAir(0, 0, arr);
			tmp = findStart(arr);
			if (tmp != 0) {
				cnt = tmp;
			} else {
				System.out.println(i);
				System.out.println(cnt);
				return;
			}
			i++;
		}
	}
	
	// 공기를 5로 만들기
	public static void changeAir(int si, int sj, int[][] arr) {
		for(int i=si; i<arr.length; i++) {
			for(int j=sj; j<arr[0].length; j++) {
				if (arr[i][j] == 0) {
					BFS(i, j, arr);
					return;
				}
			}
		}
	}
	
	// BFS로 공기를 5로 만들기
	public static void BFS(int si, int sj, int[][] arr) {
		// visited 생성
		int[][] visited = new int[arr.length][arr[0].length];
		for(int i=0; i<arr.length; i++) {
			for(int j=0; j<arr[0].length; j++) {
				visited[i][j] = 0;
			}
		}
		
		// BFS
		Deque<int[]> queue = new ArrayDeque<int[]>();
		int[] pos = {si, sj};
		visited[si][sj] = 1;
		arr[si][sj] = 5;
		queue.add(pos);
		while(queue.size() > 0) {
			int[] cpos = queue.poll();
			int ci=cpos[0], cj=cpos[1];
			for (int d=0; d<4; d++) {
				int ni=ci+D[d][0], nj=cj+D[d][1];
				if (0<=ni && ni<arr.length && 0<=nj && nj<arr[0].length && (arr[ni][nj] == 0 || arr[ni][nj] == 5) && visited[ni][nj] == 0) {
					visited[ni][nj] = 1;
					arr[ni][nj] = 5;
					int[] npos = {ni, nj};
					queue.addLast(npos);
				}
			}
		}
	}
	
	// 치즈 조각 찾아서 녹이기
	public static int findStart(int[][] arr) {
		// visited 생성
		int[][] visited = new int[arr.length][arr[0].length];
		for(int i=0; i<arr.length; i++) {
			for(int j=0; j<arr[0].length; j++) {
				visited[i][j] = 0;
			}
		}
		
		int cnt = 0;
		for(int i=0; i<arr.length; i++) {
			for(int j=0; j<arr[0].length; j++) {
				if (arr[i][j] == 1 && visited[i][j] == 0) {
					cnt += DFS(i, j, arr, visited);
				}
			}
		}
		return cnt;
	};
	
	// DFS로 치즈 녹이기
	public static int DFS(int si, int sj, int[][] arr, int[][] visited) {
		
		visited[si][sj] = 1;
		arr[si][sj] = 0;
		Stack<int[]> stack = new Stack<int[]>();
		stack.push(new int[] {si, sj});
		int ci = si, cj = sj;
		int cnt = 1;
		
		while(true) {
			// for else 구문이 없어서 flag로 판단하기
			boolean flag = false;
			for(int d=0; d<4; d++) {
				int ni = ci+D[d][0], nj = cj+D[d][1];
				if (0<=ni && ni<arr.length && 0<=nj && nj<arr[0].length && arr[ni][nj] == 1 && visited[ni][nj] == 0) {
					boolean check = false;
					// for else 구문이 없어서 만약 녹는 부분이라면 check 변수로 체크하기
					for (int k=0; k<4; k++) {
						int nni = ni+D[k][0], nnj = nj+D[k][1];
						if (0<=nni && nni<arr.length && 0<=nnj && nnj<arr[0].length && arr[nni][nnj] == 5) {
							check = true;
							break;
						}
					}
					// 녹는 부분이라면 녹이기
					if (check == true) {
						arr[ni][nj] = 0;
						cnt += 1;
					}
					// 방문 체크 후 다음 점으로 이동
					visited[ni][nj] = 1;
					stack.push(new int[] {ni, nj});
					ci = ni;
					cj = nj;
					flag = true;
					break;
				}
			}
			
			// 되돌아가기 or 끝내기
			if (flag == false) {
				if (stack.size() > 0) {
					int[] cpos = stack.pop();
					ci = cpos[0];
					cj = cpos[1];
				} else {
					return cnt;
				}
			}
		}
		
	}
}
