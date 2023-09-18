import java.io.*;
import java.util.*;

class Main_부대복귀
{
    static ArrayList<ArrayList<Integer>> adjL = new ArrayList<>();
    public static void main(String[] args) throws Exception
    {
        // 1번 예제
        // int n = 3;
        // int[][] roads = {{1, 2}, {2, 3}};
        // int[] resources = {2, 3};
        // int destination = 1;

        // 2번 예제
        int n = 5;
        int[][] roads = {{1, 2}, {1, 4}, {2, 4}, {2, 5}, {4, 5}};
        int[] resources = {1, 3, 5};
        int destination = 5;
        int[] answer;
        
        for(int[] road : roads) {
            // 당연히 입력이 a < b로 주어지는줄;;
            int a=Math.min(road[0], road[1])-1, b=Math.max(road[0], road[1])-1;
            while(adjL.size() < b){
                adjL.add(new ArrayList<>());
            }
        
            adjL.get(a).add(b);
            adjL.get(b).add(a);
        }
        answer = dijkstra(n, resources, destination);
        for(int i : answer) {
            System.out.print(i+" ");
        }
        return;
    }
    
    private static int[] dijkstra(int n, int[] sources, int destination) {
        int[] distances = new int[n];
        for(int i=0; i<n; i++){
            distances[i] = Integer.MAX_VALUE;
        }
        distances[destination-1] = 0;

        // 실수로 계속 a -> -a[0] 해서 젤 작은거 꺼내니까 시간초과뜸
        PriorityQueue<int[]> pque = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int[] start = {distances[destination-1], destination-1};
        pque.add(start);

        while(!pque.isEmpty()){
            int[] current = pque.poll();

            if(current[0] > distances[current[1]]) {
                continue;
            }

            for(int new_destination : adjL.get(current[1])) {
                int distance = current[0] + 1;
                if(distance < distances[new_destination]) {
                    distances[new_destination] = distance;
                    int[] next_destination = {distance, new_destination};
                    pque.add(next_destination);
                }
            }
        }

        int[] res = new int[sources.length];
        for(int i=0; i<n; i++){
            System.out.print(distances[i]==Integer.MAX_VALUE ? -1+" " : distances[i]+" ");
        }
        System.out.println();

        for(int i=0; i<sources.length; i++) {
            res[i] = distances[sources[i]-1] != Integer.MAX_VALUE ? distances[sources[i]-1] : -1;
        }
        return res;
    }
}