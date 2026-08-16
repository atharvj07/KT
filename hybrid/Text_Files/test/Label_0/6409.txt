#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int n;

	cin >> n;

	int A[n];

	for (int i = 0; i < n; i++) {
		A[i] = i + 1;
	}

	do {
		for (int i = 0; i < n; i++) {
			if (i == 0) cout << A[i];
			else cout << " " << A[i];
		}
		cout << endl;
	} while (next_permutation(A, A + n));
}


