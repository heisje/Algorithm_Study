#include <iostream>

using namespace std;

const int MAX_N = 2000;

int arr[MAX_N];

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + N);

    int count = 0;
    for (int i = 0; i < N; i++) {
        int target = arr[i];
        int left = 0, right = N - 1;

        while (left < right) {
            if (left == i) {
                left++;
                continue;
            }
            if (right == i) {
                right--;
                continue;
            }

            int sum = arr[left] + arr[right];
            if (sum == target) {
                count++;
                break;
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }
    }

    cout << count << endl;

    return 0;
}



