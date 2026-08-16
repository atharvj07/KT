#include<iostream>

using namespace std;

int N;

int main() {
    cin >> N;
    long long t = 1, a = 1;
    for (int i = 0; i < N; i++) {
        long long T, A;
        cin >> T >> A;
        long long n = max((t + T - 1) / T, (a + A - 1) / A);
        t = n * T;
        a = n * A;
    }
    cout << a + t << endl;
    return 0;
}