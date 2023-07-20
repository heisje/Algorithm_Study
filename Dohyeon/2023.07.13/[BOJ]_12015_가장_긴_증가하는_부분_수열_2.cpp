// [BOJ]_12015_가장_긴_증가하는_부분_수열_2.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//


/*
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> dp(n, 1);       // n개를 1로 초기화

    int max_length = 1;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {       // 앞에 있는 값들을 확인
            if (arr[j] < arr[i]) {    // 순서가 맞다면
                dp[i] = max(dp[i], dp[j] + 1);
                max_length = max(max_length, dp[i]);
            }
        }
    }

    cout << max_length;

    return 0;

}
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> dp;
    dp.push_back(arr[0]);

    for (int i = 1; i < n; i++) {
        if (arr[i] > dp.back()) {
            dp.push_back(arr[i]);
        }
        else {
            auto it = lower_bound(dp.begin(), dp.end(), arr[i]); // 시작부터 끝까지 돌며 arr[i] 하한선이 나오는 위치 확인
            *it = arr[i];               // 해당위치에 하한선 삽입, 최대 길이를 구하는 것이므로 교체는 상관x, 제일 뒷부분이 바뀌는지만 확인
        }
    }

    cout << dp.size() << endl;

    return 0;
}