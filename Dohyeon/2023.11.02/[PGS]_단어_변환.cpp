// [PGS]_단어_변환.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int answer = 50;
bool visited[50];

//다른 문자가 1개인지 확인하는 함수
bool check_diff(string a, string b) {
    int dif_cnt = 0;

    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            dif_cnt++;
        }
    }

    if (dif_cnt == 1) {
        return true;
    }
    
    return false;
}

void dfs(string begin, string target, vector<string>words, int step) {
   
    if (answer <= step)
        return;

    if (begin == target) {
        answer = min(answer, step);
        return;
    }

    for (int i = 0; i < words.size(); i++) {
        // 한개의 문자만 다르고 방문 하지 않은 단어이면 탐색 시작

        if (check_diff(begin, words[i]) && !visited[i]) {
            visited[i] = true;
            // 그 단어부터 탐색을 다시 시작한다. 단계가 하나 추가되었으므로 step+1을 인자로 넘긴다.
            dfs(words[i], target, words, step + 1);
            // dfs 재귀 호출하여 종료되어 여기로 돌아오면, 백트래킹 (방문 표시 해제) 하여 다음분기점부터 다시 탐색을 시작한다.
            visited[i] = false;
        }
    }

    return;
}

int solution(string begin, string target, vector<string> words) {
    dfs(begin, target, words, 0);

    // 탐색후 target문자열을 만나지 못했을 때
    if (answer == 50)
        return 0;

    return answer;
}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
