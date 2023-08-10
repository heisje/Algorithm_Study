// 실버2 / 3388ms
import java.io.*;
import java.util.*;

class Main_22233
{
    static int N, M;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        Map<String, Integer> keywords = new HashMap<>();

        // map에 키워드 추가
        for(int i=0; i<N; i++){
            String tmp = br.readLine();
            if(!keywords.containsKey(tmp)){
                keywords.put(tmp, 1);
            }
        }

        // 글에 쓴 것들 메모장에서 지우고 출력
        for(int i=0; i<M; i++){
            String[] tmp_lst = br.readLine().split(",");
            for(String keyword : tmp_lst){
                if(keywords.containsKey(keyword)){
                    keywords.remove(keyword);
                }
            }
            System.out.println(keywords.keySet().size());
        }
    }
}