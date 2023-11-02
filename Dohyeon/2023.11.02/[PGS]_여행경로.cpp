#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> answer;
bool visited[100000001];
bool check = false;


void dfs(string airport, vector<vector<string>> tickets, int count) {
    if (count == tickets.size()) {// 모두 사용
        check = true;
    }
    answer.push_back(airport);

    for (int i = 0; i < tickets.size(); i++) {
        if (!visited[i] and tickets[i][0] == airport) {//현재공항티켓 탐색
            visited[i] = true;
            dfs(tickets[i][1], tickets, count + 1);

            if (!check) {//모두 다 사용할수 없을경우
                answer.pop_back();
                visited[i] = false;
            }
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {

    sort(tickets.begin(), tickets.end());
    dfs("ICN", tickets, 0);
    return answer;
}