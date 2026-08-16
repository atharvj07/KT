#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <stdio.h>
using namespace std;
#define int long long
int MOD = 1000000007;
vector<int> sieve_of_eratosthenes(int n) {
	vector<int> primes(n);
	for (int i = 2; i < n; ++i)
		primes[i] = i;
	for (int i = 2; i*i < n; ++i)
		if (primes[i])
			for (int j = i*i; j < n; j += i)
				primes[j] = 0;
	return primes;
}
signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	vector<int> primes = sieve_of_eratosthenes(1000005);
	int N;
	cin >> N;
	vector<int> A(N);
	int res = 0;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	vector<int> B;
	vector<int> C;
	bool f1, f2, f3;
	for (int i = 0; i < N; i++) {
		if (i > 0) {
			f1 = (primes[A[i - 1]] != 0);
		}
		else {
			f1 = false;
		}
		f2 = (primes[A[i]] != 0);
		if (i < N - 1) {
			f3 = (primes[A[i + 1]] != 0);
		}
		else {
			f3 = true;
		}
		if (!f2 && !f3) {
			cout << 0 << endl;
			return 0;
		}
		if (!f1 && !f2) {
			cout << 0 << endl;
			return 0;
		}
		if (f2) {
			if (!f1) {
				B.push_back(A[i]);
				C.push_back(1);
			}
			else if (!f3) {
				B.push_back(A[i]);
				C.push_back(1);
			}
			else {
				B.push_back(A[i]);
				C.push_back(0);
			}

		}
	}
	/*for (int i = 0; i < B.size(); i++) {
		cerr << B[i] << " ";
	}
	cerr << endl;
	for (int i = 0; i < C.size(); i++) {
		cerr << C[i] << " ";
	}
	cerr << endl;*/
	vector<vector<int> > dp((int)B.size() + 1, vector<int>(3, 0));
	dp[0][1] = 1;
	for (int i = 1; i < B.size(); i++) {
		//for (int k = 0; k < 3; k++) {
			if (C[i] == 0) {
				if (i > 0 && B[i] > B[i - 1]) {
					dp[i][1] = dp[i - 1][1];
				}
				if (i <= 1 || B[i] > B[i - 2]) {
					dp[i][1] = (dp[i][1] + dp[i - 1][0]) % MOD;
				}
				dp[i][0] = (dp[i][0] + dp[i - 1][1]) % MOD;
			}
			else {
				if (i > 0 && B[i] > B[i - 1]) {
					dp[i][1] = dp[i - 1][1];
				}
				if (i <= 1 || B[i] > B[i - 2]) {
					dp[i][1] = (dp[i][1] + dp[i - 1][0]) % MOD;
				}
				dp[i][0] = 0;
			}
		//}
	}
	/*for (int i = 0; i < dp.size(); i++) {
		cerr << dp[i][0] << " ";
	}
	cerr << endl;
	for (int i = 0; i < dp.size(); i++) {
		cerr << dp[i][1] << " ";
	}
	cerr << endl;*/
	cout << (dp[B.size() - 1][0] + dp[B.size() - 1][1])%MOD << endl;
}
