// 골드5 / 128ms
import java.io.*;
import java.util.*;

class Main_2565
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<int[]> lines = new ArrayList<>();
        for(int i=0; i<N; i++){
            String[] tmp = br.readLine().split(" ");
            int[] lst = {Integer.parseInt(tmp[0]), Integer.parseInt(tmp[1])};
            lines.add(lst);
        }
        Collections.sort(lines, (e1, e2) -> e1[0] - e2[0]);
        
        List<Integer> LIS = new ArrayList<>();
        LIS.add(0);
        for(int i=0; i<lines.size(); i++){
            int n = lines.get(i)[1];
            if(LIS.get(LIS.size()-1) < n){
                LIS.add(n);
            } else {
                int left=0, right=LIS.size();
                while(left<right){
                    int mid = (left+right)/2;
                    if(LIS.get(mid) < n){
                        left = mid + 1;
                    } else{
                        right = mid;
                    }
                }
                LIS.remove(right);
                LIS.add(right, n);
            }
        }
        System.out.println(lines.size()-LIS.size()+1);
    }
}

// 교차가 젤 많이 되는 선부터 제거 -> 틀림

// boolean flag = true;
// int answer = 0;
// while(flag){
//     flag = false;
//     int n = lines.size();
//     int[] tmp = new int[n];
//     Arrays.fill(tmp, 0, n, 0);
//     for(int i=0; i<n; i++){
//         for(int j=i+1; j<n; j++){
//             if(lines.get(i)[1] > lines.get(j)[1]){
//                 tmp[i]++;
//                 tmp[j]++;
//                 flag = true;
//             }
//         }
//     }
//     if(flag){
//         int idx = 0;
//         int maxV = 0;
//         for(int i=0; i<n; i++){
//             // System.out.print(tmp[i]+" ");
//             if(maxV < tmp[i]){
//                 idx = i;
//                 maxV = tmp[i];
//             }
//         }
//         System.out.println("remove: "+lines.get(idx)[0]+" "+lines.get(idx)[1]);
//         lines.remove(idx);
//         answer++;
//     }
// }
// System.out.println(answer);

// 5
// 1 3
// 3 1
// 2 5
// 4 6
// 6 4