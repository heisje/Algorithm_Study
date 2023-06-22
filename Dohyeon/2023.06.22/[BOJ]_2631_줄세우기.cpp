// [BOJ]_2631_줄세우기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    // 데이터 입력
    int n;
    int answer;
    cin >> n;

    vector<int> children(n);
    for (int i = 0; i < n; i++) {
        cin >> children[i];
    }


    vector<int> dp(n, 1);       // n개를 1로 초기화

    int max_length = 1;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {       // 앞에 있는 값들을 확인
            if (children[j] < children[i]) {    // 순서가 맞다면
                dp[i] = max(dp[i], dp[j] + 1);
                max_length = max(max_length, dp[i]);
            }
        }
    }


    answer = n - max_length;                    // 움직여야 하는 횟수는 원래 길이 - 정렬된 값 수
    cout << answer << endl;

    return 0;

}

