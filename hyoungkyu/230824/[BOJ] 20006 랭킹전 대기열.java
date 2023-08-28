// 실버2 / 180ms
import java.io.*;
import java.util.*;

class Main_20006
{
    static int p, m;
    static List<Room> rooms = new ArrayList<>();
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] input = br.readLine().split(" ");
        p = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        // 방에 집어 넣기
        for(int i=0; i<p; i++){
            input = br.readLine().split(" ");
            getRoom(Integer.parseInt(input[0]), input[1]);
        }
        // 방에 있는 사람들 출력하기
        for(Room room : rooms){
            if(room.members.size() == m){
                bw.write("Started!\n");
            } else {
                bw.write("Waiting!\n");
            }
            // 같은 방 안에서 이름 순으로 정렬
            Collections.sort(room.members, (x1, x2) -> x1.nickname.compareTo(x2.nickname));
            for(Member member : room.members){
                bw.write(member.level+" "+ member.nickname+"\n");
            }
        }
        bw.flush();
        bw.close();
    }

    // 방에 집어넣기
    private static void getRoom(int level, String nickname){
        // 들어갈 방이 있으면 집어넣기
        for(Room room : rooms){
            if(room.members.size() < m && Math.abs(room.masterLevel - level) <= 10){
                room.members.add(new Member(level, nickname));
                return;
            }
        }
        // 새로운 방 파기
        List<Member> tmpMembers = new ArrayList<>();
        tmpMembers.add(new Member(level, nickname));
        rooms.add(new Room(level, tmpMembers));
        return;
    }

    static class Member
    {
        int level;
        String nickname;

        Member(int level, String nickname){
            this.level = level;
            this.nickname = nickname;
        }
    }

    static class Room
    {
        int masterLevel;
        List<Member> members;

        Room(int level, List<Member> members){
            this.masterLevel = level;
            this.members = members;
        }
    }
}