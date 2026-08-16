#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <array>
#include <cassert>
#include <bitset>
#include <cstdint>
using namespace std;
using LL = long long;

LL M;
string C;
const LL MOD = 1000000007;

int main() {
	cin >> M;
	cin >> C;
	int N = C.size();
	if (N == 1 && M == 0) {
		cout << 0 << endl;
		return 0;
	}
	LL ten = 1;
	LL arr[10] = {};
	for (int i = N - 1; i >= 0; --i) {
		arr[C[i] - '0'] += ten;
		arr[C[i] - '0'] %= MOD;
		ten *= 10;
		ten %= MOD;
	}
	vector<int>per;
	for (int i = 0; i < 10; ++i)per.push_back(i);
	int sent = C[0] - '0';
	do {
		if (per[sent] != 0) {
			LL tmp = 0;
			for (int i = 0; i < 10; ++i) {
				tmp += (arr[i] * per[i]) % MOD;
				tmp %= MOD;
			}
			if (tmp == M) {
				for (char c : C) {
					cout << per[c - '0'];
				}
				cout << endl;
				return 0;
			}
		}
	} while (next_permutation(per.begin(), per.end()));
	cout << -1 << endl;
	return 0;
}
