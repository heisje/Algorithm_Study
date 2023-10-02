// [BOJ]_17484_진우의_달_여행.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <algorithm>

using namespace std;

int cost[8][8];
int dp[8][8][3]; 
int N, M;

int solve(int x, int y, int dir)
{
    if (x == N) // 범위 밖
    {
        return 0;
    }

    if (dp[x][y][dir] != 4000)              // 6 * 6 * 100 을 넘을수없음
    {
        return dp[x][y][dir];
    }

    // 왼쪽
    if (dir != 0 && y - 1 >= 0)         // 이전이 왼쪽이 아니면
    {
        dp[x][y][dir] = solve(x + 1, y - 1, 0) + cost[x][y];
    }

    // 중앙 
    if (dir != 1)                       // 이전이 중앙이 아니면
    {
        dp[x][y][dir] = min(dp[x][y][dir], solve(x + 1, y, 1) + cost[x][y]);
    }

    // 오른쪽
    if (dir != 2 && y + 1 < M)          // 이전이 오른쪽이 아니면
    {
        dp[x][y][dir] = min(dp[x][y][dir], solve(x + 1, y + 1, 2) + cost[x][y]);
    }

    return dp[x][y][dir];
}

int main(void)
{

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> cost[i][j];

            for (int k = 0; k < 4; k++)
            {
                dp[i][j][k] = 4000;
            }
        }
    }

    int Min = 4000;
    for (int i = 0; i < M; i++)
    {
        // 처음에는 방향이 없기 때문에 dir에 3을 대입 
        Min = min(Min, solve(0, i, 3));
    }

    cout << Min;

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
