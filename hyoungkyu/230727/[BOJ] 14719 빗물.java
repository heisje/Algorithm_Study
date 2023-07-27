// 골드5 / 124ms
import java.io.*;

class Main_14719
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int W = Integer.parseInt(input[1]);
        String[] tmp_blocks = br.readLine().split(" ");
        int[] blocks = new int[W];
        for(int i=0; i<W; i++){
            blocks[i] = Integer.parseInt(tmp_blocks[i]);
        }
        
        int maxV = blocks[0];
        int tmp_maxV = 0;
        int tmp = 0;
        int answer = 0;
        int i=0;
        while(i<W-1){
            i++;
            // 뒤에 돌면서 고일 수 있는지 확인, 최대 높이가 바뀌면 break
            for(int j=i; j<W; j++){
                if(blocks[j] >= maxV){
                    answer += (j-i) * maxV - tmp;
                    i = j;
                    maxV = blocks[j];
                    tmp = 0;
                    tmp_maxV = 0;
                    break;
                } else if (blocks[j] > tmp_maxV){
                    tmp_maxV = blocks[j];
                    tmp += blocks[j];
                } else {
                    tmp += blocks[j];
                }
            }
            // 최대 높이가 안바꼈으면 작은 웅덩이 구하기
            if(tmp != 0){
                for(int j=W-1; j>=i; j--){
                    if(blocks[j] == tmp_maxV){
                        answer += (j-i+1) * tmp_maxV - tmp;
                        i = j;
                        maxV = tmp_maxV;
                        tmp = 0;
                        tmp_maxV = 0;
                        break;
                    } else {
                        tmp -= blocks[j];
                    }
                }
            }
            // System.out.printf("i: %d, answer: %d\n", i, answer);
        }
        System.out.println(answer);
    }
}
