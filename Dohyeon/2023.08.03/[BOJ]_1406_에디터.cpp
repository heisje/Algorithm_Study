// [BOJ]_1406_에디터.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>


using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string word;
    int M;
    int N;
    cin >> word;
    cin >> M;
    N = word.size();
    int cursor_idx = word.size();
    for (int i = 0; i < M; i++) {
        char tmp1;
        cin >> tmp1;

        if (tmp1 == 'L') {          // ""은 안됨 조심하자
            if (cursor_idx >= 1) {
                cursor_idx--;
            }
            else {
                cursor_idx = 0;
            }
            continue;
        }
        
        if (tmp1 == 'D') {
            if (cursor_idx < N) {
                cursor_idx++;
            }
            else {
                cursor_idx = N;
            }
            continue;
        }
        if (tmp1 == 'B') {
            if (cursor_idx != 0) {
                word.erase(cursor_idx - 1, 1);
                N--;
                cursor_idx--;
            }
            continue;
        }

        if (tmp1 == 'P') {
            
            if (cursor_idx == N) {
                char tmp2;
                cin >> tmp2;
                word.append(1, tmp2);
                cursor_idx++;
                
            }
            else {
                string tmp2;
                cin >> tmp2;
                word.insert(cursor_idx, tmp2);
                cursor_idx++;
            }
            N++;
            continue;

        }
    }
    cout << word;
    return 0;
}

/*
#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string s = "";
    cin >> s;
    stack<char> l;
    stack<char> r;
    for (int i = 0; i < s.size(); i++) {
        l.push(s[i]);
    }
    int num;
    cin >> num;
    while (num--) {
        char tmp;
        cin >> tmp;
        if (tmp == 'P') {
            char c;
            cin >> c;
            l.push(c);
        }
        else if (tmp == 'L') {
            if (l.empty()) continue;
            else {
                r.push(l.top());
                l.pop();
            }
        }
        else if (tmp == 'B') {
            if (l.empty()) continue;
            else l.pop();
        }
        else if (tmp == 'D') {
            if (r.empty()) continue;
            else {
                l.push(r.top());
                r.pop();
            }
        }
    }
    while (!l.empty()) {
        r.push(l.top());
        l.pop();
    }
    while (!r.empty()) {
        cout << r.top();
        r.pop();
    }
    return 0;
}

*/


// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
