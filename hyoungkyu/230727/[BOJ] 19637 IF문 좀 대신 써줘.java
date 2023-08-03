// 실버3 / 548ms
import java.util.*;
import java.io.*;

class Main_19637
{
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String[] titles = new String[N];
        int[] powers = new int[N];
        
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            String title = st.nextToken();
            int power = Integer.parseInt(st.nextToken());
            titles[i] = title;
            powers[i] = power;
        }

        for(int i=0; i<M; i++){
            int power = Integer.parseInt(br.readLine());
            get_title(power, powers, titles);
        }
        System.out.println(sb);
    }

    public static void get_title(int power, int[] powers, String[] titles){
        int s = 0;
        int e = powers.length-1;
        while(s<e){
            int m = (s+e)/2;
            if(powers[m] < power){
                s = m+1;
            } else {
                e = m;
            }
        }
        sb.append(titles[e]+"\n");
    }
}