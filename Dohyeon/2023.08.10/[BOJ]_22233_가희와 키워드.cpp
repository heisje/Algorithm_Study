
// [BOJ]_가희와 키워드.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <cstring>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int n, m, total;
    string s = "", temp = "", k = "";
    
    unordered_set<string>st;

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s;
        st.insert(s);
    }
    
    while (m--) {
        cin >> temp;
        int pos = 0;
        while (pos < temp.length()) {   // . 나누기
            auto it = temp.find(',', pos);  // "" 쓰면 안됨
            if (it == temp.npos) {          // 없을 경우 npos를 반환하기 때문
                k = temp.substr(pos);
                if (st.find(k) != st.end()) {   // 찾는데 없으면 .end()를 반환하기 때문
                    st.erase(k);
                }
                break;  // 한 단어 였으니 탈출
            }
            else {
                k = temp.substr(pos, it - pos);
                if (st.find(k) != st.end()) {
                    st.erase(k);
                }
                pos = it + 1;

            }
            
        }
        cout << st.size() << "\n";
    }
    return 0;
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
