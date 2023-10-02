// [BOJ]_1759_암호만들기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <algorithm>
#include <vector>

//using namespace std;
//
//int main()
//{
//    int L, C;
//    cin >> L >> C;
//
//    vector<char> jaeum;
//    vector<char> moeum;
//
//    char vowels[] = { 'a', 'e', 'i', 'o', 'u' };
//
//    char *p = find(vowels, vowels + 5, 'b');
//    
//    for (int i = 0; i < L; i++) {
//        if (p == vowels + 5) {                  // 자음
//            cout << "여기" << endl;
//        }
//        else {                                  // 모음
//            cout << *p;
//        }
//    }
//    
//    
//
//    return 0;
//
//}

using namespace std;
typedef long long int ll;
int L, C;
vector<char> v;
vector<char> res;

bool check()
{
    int moum = 0;
    for (int i = 0; i < L; i++)
    {
        if (res[i] == 'a' ||
            res[i] == 'e' ||
            res[i] == 'i' ||
            res[i] == 'o' ||
            res[i] == 'u')
            moum++;
    }
    // 모음의 수 1개 이상, 자음의수 = 전체수 -모음의 수 . 2개이상.
    if (moum >= 1 && L - moum >= 2) return true;
    return false;
}
void dfs(int d) {
    if ((int)res.size() == L) {
        if (check()) { //check에서 조건 부합시 출력.
            for (int k = 0; k < L; k++)
            {
                cout << res[k];
            }
            cout << '\n';
        }
        return;
    }
    for (int i = d; i < C; i++)
    {
        res.push_back(v[i]); //들어갈때 하나씩 추가해주고
        dfs(i + 1);
        res.pop_back(); //나오면 하나 빼주고.
    }
    return;
}
int main(void)
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> L >> C;
    for (int i = 0; i < C; i++)
    {
        char temp;
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end()); //정렬하고 dfs(0)시작.
    dfs(0);
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
