// 실버2 / 492ms
import java.io.*;
import java.util.*;

class Main_1406
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        Stack<Character> leftStack = new Stack<Character>();
        Stack<Character> rightStack = new Stack<Character>();
        for(int i=0; i<input.length(); i++){
            leftStack.add(input.charAt(i));
        }
        int M = Integer.parseInt(br.readLine());
        for(int i=0; i<M; i++){
            String command = br.readLine();
            switch(command.charAt(0)){
                case 'L':
                    if(!leftStack.isEmpty()){
                        rightStack.add(leftStack.pop());
                    }
                    break;
                case 'D':
                    if(!rightStack.isEmpty()){
                        leftStack.add(rightStack.pop());
                    }
                    break;
                case 'B':
                    if(!leftStack.isEmpty()){
                        leftStack.pop();
                    }
                    break;
                case 'P':
                    leftStack.add(command.charAt(2));
                    break;
                default:
                    break;
            }
        }
        for(char c : leftStack){
            bw.write(c);
        }
        for(int i=rightStack.size()-1; i>=0; i--){
            bw.write(rightStack.get(i));
        }
        bw.flush();
        bw.close();
    }
}

// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
// String input = br.readLine();
// List<Character> lst = new LinkedList<Character>();
// int N = input.length();
// for(int i=0; i<N; i++){
//     lst.add(input.charAt(i));
// }
// int pointer = N;
// int M = Integer.parseInt(br.readLine());
// for(int i=0; i<M; i++){
//     String command = br.readLine();
//     if (command.charAt(0) == 'L' && pointer != 0){
//         pointer--;
//     } else if (command.charAt(0) == 'D' && pointer != N){
//         pointer++;
//     } else if (command.charAt(0) == 'B' && pointer != 0){
//         pointer--;
//         lst.remove(pointer);
//         N--;
//     } else if (command.charAt(0) == 'P'){
//         char s = command.charAt(2);
//         lst.add(pointer, s);
//         pointer++;
//         N++;
//     }
// }
// for(char s : lst){
//     bw.write(s);;
// }
// bw.flush();
// bw.close();