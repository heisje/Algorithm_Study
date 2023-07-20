// 골드5 / 288ms
import java.io.*;
import java.util.*;

class Solution_15686
{
    static int M;
    static int N;
    static List<Integer[]> lst_1;
    static List<Integer[]> lst_2;
    
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        lst_1 = new ArrayList<>();   
        lst_2 = new ArrayList<>();   
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int tmp;
            for (int j=0; j<N; j++) {
                tmp = Integer.parseInt(st.nextToken());
                if (tmp == 1) {
                    lst_1.add(new Integer[]{i, j});
                } else if (tmp == 2) {
                    lst_2.add(new Integer[]{i, j});
                }
            }
        }

        int answer = func();
        System.out.println(answer);
    }

    // 거리 구하기
    public static int get_distance(Integer[] lst) {
        return Math.abs(lst[0]-lst[2]) + Math.abs(lst[1]-lst[3]);
    }

    // 조합 구하기
    public static void combinations(List<Integer> elements, List<List<Integer>> result, List<Integer> combination, int start, int r) {
        if (r == 0) {
            result.add(new ArrayList<>(combination));
            return;
        } else {
            for (int i=start; i<elements.size(); i++) {
                combination.add(elements.get(i));
                combinations(elements, result, combination, i+1, r-1);
                combination.remove(combination.size() - 1);
            }
        }
    }

    // 각 조합별 거리 계산 후 비교
    public static int func() {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> elements = new ArrayList<>();
        for (int i=0; i<lst_2.size(); i++) {
            elements.add(i);
        }
        combinations(elements, result, new ArrayList<>(), 0, M);
        int minV = Integer.MAX_VALUE;
        for (List<Integer> comb : result){
            int[] visited = new int[lst_1.size()];
            Arrays.fill(visited, Integer.MAX_VALUE);
            for (int i : comb) {
                for (int j=0; j<lst_1.size(); j++) {
                    Integer[] lst = {lst_2.get(i)[0], lst_2.get(i)[1], lst_1.get(j)[0], lst_1.get(j)[1]};
                    visited[j] = Math.min(visited[j], get_distance(lst));
                }
            }
            int sum = 0;
            for (int k=0; k<lst_1.size(); k++) {
                sum += visited[k];
            }
            minV = Math.min(minV, sum);
        };
        return minV;
    }
}