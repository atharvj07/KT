#include "bits/stdc++.h"
using namespace std;

int main() {
	int N, L, R;
	while (cin >> N >> L >> R) {
		if (N == 0) return 0;
		vector<int> A(N);
		for (int i = 0; i < N; i++) cin >> A[i];
		A.push_back(1), N++;
		int ANS = 0;
		for (int i = L; i <= R; i++) {
			for (int j = 0; j < N; j++) {
				if (i % A[j] == 0) {
					if (j % 2 == 0) ANS++;
					break;
				}
			}
		}
		cout << ANS << endl;
	}
}
