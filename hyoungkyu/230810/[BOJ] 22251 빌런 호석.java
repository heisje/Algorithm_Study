// 골드5 / 356ms
import java.io.*;
import java.util.*;

class Main_22251
{
    // N : 최대 층, K : 디스플레이 자리수, P : 바꿀 LED 최대수, X : 현재 층
    // 0: 1111110
    // 1: 0110000
    // 2: 1101101
    // 3: 1111001
    // 4: 0110011
    // 5: 1011011
    // 6: 1011111
    // 7: 1110000
    // 8: 1111111
    // 9: 1111011

    static int N, K, P, X;
    static Map<Integer, int[]> countMap = new HashMap<>();
    static Map<Integer, String> changeNumMap = new HashMap<>();
    static Set<Integer> answer = new HashSet<>();
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        K = Integer.parseInt(input[1]);
        P = Integer.parseInt(input[2]);
        X = Integer.parseInt(input[3]);

        setChangeNumMap();  // 숫자 -> 시계 변환
        setCountMap();      // 숫자별 변환 횟수 테이블 만들기
        solution(0, P, 0);
        System.out.println(answer.size());
    }

    // 숫자 -> 시계 변환 함수
    private static void setChangeNumMap(){
        changeNumMap.put(0, "1111110");
        changeNumMap.put(1, "0110000");
        changeNumMap.put(2, "1101101");
        changeNumMap.put(3, "1111001");
        changeNumMap.put(4, "0110011");
        changeNumMap.put(5, "1011011");
        changeNumMap.put(6, "1011111");
        changeNumMap.put(7, "1110000");
        changeNumMap.put(8, "1111111");
        changeNumMap.put(9, "1111011");
    }

    // 숫자별 변환 횟수 테이블 만드는 함수
    private static void setCountMap(){
        for(int i=0; i<10; i++){
            countMap.put(i, new int[10]);
            for(int j=0; j<10; j++){
                countMap.get(i)[j] = getCnt(i, j);
            }
        }
    }

    // 숫자 변환 횟수 구하는 함수
    private static int getCnt(int i, int j){
        String s1 = changeNumMap.get(i);
        String s2 = changeNumMap.get(j);
        int tmp = 0;
        for(int idx=0; idx<7; idx++){
            if(s1.charAt(idx) != s2.charAt(idx)){
                tmp++;
            }
        }
        return tmp;
    }

    // 재귀 돌면서 각 변환 가능한 숫자들 구하는 함수
    private static void solution(int idx, int cnt, int num){
        if (cnt < 0 || num > N) return;
        else if(idx == K){
            // num > 0;;;; 0층은 없다고!!!!
            if(num != X && num > 0){
                answer.add(num);
            }
            return;
        } 
        for(int i=0; i<10; i++){
            solution(idx+1, cnt-countMap.get(X%(int)Math.pow(10, K-idx)/(int)Math.pow(10, K-idx-1))[i], num+i*(int)Math.pow(10, K-idx-1));
        }
    }
}