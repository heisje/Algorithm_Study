// [BOJ]_15686_치킨 배달.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>


using namespace std;

int homeToChicken[101][27]; // 다른 함수에서 사용하기 위해 전역변수로 설정
int minChicken = 10000;     // 최소 치킨거리
int homeIdx = 0;
int chickenIdx = 0;

//조합 함수
void generateCombinations(vector<int>& combination, int start, int n, int m) {
    // 조합이 완성된 경우 결과를 출력
    if (combination.size() == m) {
        int tmp = 0;

        for (int k = 0; k < homeIdx; k++) {
            int bestTmp = 150;
            for (int num : combination) {
                
                bestTmp = min(bestTmp, homeToChicken[k][num]);      // 살아남은 치킨집 중 가장 가까운곳 찾기
            }
            tmp += bestTmp;
        }
        /*for (int num : combination) {
            cout << num << " ";
            for (int k = 0; k < homeIdx - 1; k++) {
                tmp += homeToChicken[k][num];
            }
        }*/
        /*cout << endl;
        cout << tmp << endl;*/
        if (tmp < minChicken) {
            minChicken = tmp;
        }
        return;
    }

    // 조합 생성
    for (int i = start; i <= n; ++i) {
        combination.push_back(i);
        generateCombinations(combination, i + 1, n, m);
        combination.pop_back();
    }
}


int main()
{
    int N, M;
    int city[51][51];
    pair<int, int> home[101];
    pair<int, int> chicken[27];
    
    int p = 0;

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int tmp;
            p++;
            cin >> tmp;
            city[i][j] = tmp;
            if (tmp == 1) {
                home[homeIdx].first = i;
                home[homeIdx].second = j;
                homeIdx++;
            }
            if (tmp == 2) {
                chicken[chickenIdx].first = i;
                chicken[chickenIdx].second = j;
                chickenIdx++;
            }
        }
    }

    // 각 집별 각 치킨집까지의 거리를 저장
    for (int i = 0; i < homeIdx; i++) {
        for (int j = 0; j < chickenIdx; j++) {
            homeToChicken[i][j] = abs(home[i].first - chicken[j].first) + abs(home[i].second - chicken[j].second);

        }
    }

    vector<int> combination;
    generateCombinations(combination, 0, chickenIdx - 1, M);

    cout << minChicken;

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
