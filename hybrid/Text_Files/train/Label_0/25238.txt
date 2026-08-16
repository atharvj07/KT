#include <bits/stdc++.h>
#define mod 1000000007
#define sp ' '
#define intmax 2147483647
#define llmax 9223372036854775807
#define mkp make_pair
typedef long long ll;
using namespace std;

int N, DP[4001][4001], R[2001], B[2001];
string S;


int main() {
	cin >> S;
	N = S.size();
	for (int i = 1; i <= N; ++i) {
		switch (S[i - 1]) {
		case '0':
			R[i] = 2;
			break;
		case '1':
			R[i] = B[i] = 1;
			break;
		case '2':
			B[i] = 2;
			break;
		}
		R[i] += R[i - 1];
		B[i] += B[i - 1];
	}
	DP[0][0] = 1;
	for (int i = 0; i < N * 2; ++i) {
		for (int j = max(0, i - B[min(i, N)]); j <= R[min(i, N)] && j <= i; ++j) {
			if (j + 1 <= R[min(i + 1, N)]) {
				DP[j + 1][i - j] = (DP[j + 1][i - j] + DP[j][i - j]) % 998244353;
			}
			if (i - j + 1 <= B[min(i + 1, N)]) {
				DP[j][i - j + 1] = (DP[j][i - j + 1] + DP[j][i - j]) % 998244353;
			}
		}
	}
	cout << DP[R[N]][B[N]] << endl;
	return 0;
}