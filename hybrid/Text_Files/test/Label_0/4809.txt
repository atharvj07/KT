#include "bits/stdc++.h"
#include<unordered_map>
#include<unordered_set>
#pragma warning(disable:4996)
using namespace std;
using ld = long double;
template<class T>
using Table = vector<vector<T>>;
const ld eps=1e-9;

//// < "D:\D_Download\Visual Studio 2015\Projects\programing_contest_c++\Debug\a.txt"
int main() {
	while (1) {
		int N; cin >> N;
		if (!N)break;
		vector<int>mys(N),ops(N);
		for (int i = 0; i < N; ++i) {
			cin >> mys[i];
		}
		for (int i = 0; i < N; ++i) {
			cin >>ops[i];
		}
		sort(mys.begin(), mys.end(), greater<int>());
		sort(ops.begin(), ops.end(), greater<int>());
		int ans = -1;
		if (N == 1) {
			
		}
		else if (mys[0] > ops[0]) {
			ans = 1;
		}
		else {
			for (int k = 3; k < N; k += 2) {
				if (mys[k - 1] > ops[k / 2]) {
					ans = k;
					break;
				}
			}
		}
		if (ans == -1) {
			cout << "NA" << endl;
		}
		else {
			cout << ans << endl;
		}
	}
	return 0;
}