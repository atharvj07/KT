#include "iostream"
#include "climits"
#include "list"
#include "queue"
#include "stack"
#include "set"
#include "functional"
#include "algorithm"
#include "string"
#include "map"
#include "unordered_map"
#include "unordered_set"
#include "iomanip"
#include "cmath"
#include "random"
#include "bitset"
#include "cstdio"
#include "numeric"
#include "cassert"
#include "ctime"

using namespace std;

constexpr long long int MOD = 1000000007;
//constexpr int MOD = 1000000007;
//constexpr int MOD = 998244353;
//constexpr long long int MOD = 998244353;
constexpr long double EPS = 1e-8;

long long int N, M, K, L, R, H, W;
//int N, M, K, L, R, H, W;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M;
	N <<= 1;
	vector<long long int>v(N);
	vector<long long int>w(N);
	for (auto &i : v)cin >> i;
	for (auto &i : w)cin >> i;
	long long int ans = v.front() + v.back();
	set<pair<long long int, int>>in;
	set<pair<long long int, int>>out;
	long long int insum = 0;
	vector<long long int>num(N);
	for (int i = 1; i < N - 1; i++) {
		ans += v[i];
		num[i] = w[i] - v[i];
		if (v[i] < w[i]) {
			in.insert({ num[i],i });
			ans += num[i];
		}
		else {
			out.insert({ -num[i],i });
		}
	}
	while (in.size() && in.begin()->first < 0) {
		int n = in.begin()->second;
		ans -= num[n];
		out.insert({ -in.begin()->first, in.begin()->second });
		in.erase(in.begin());
	}
	while (out.size() && out.begin()->first < 0) {
		int n = out.begin()->second;
		ans += num[n];
		in.insert({ -out.begin()->first, out.begin()->second });
		out.erase(out.begin());
	}
	if (in.size() & 1) {
		if (in.begin()->first > out.begin()->first) {
			in.insert({ -out.begin()->first,out.begin()->second });
			ans += num[out.begin()->second];
			out.erase(out.begin());
		}
		else {
			out.insert({ -in.begin()->first,in.begin()->second });
			ans -= num[in.begin()->second];
			in.erase(in.begin());
		}
	}
	while (M--) {
		cin >> K >> L >> R;
		K--;
		ans -= v[K];
		v[K] = L, w[K] = R;
		if (K == 0 || K == N - 1) {
			ans += v[K];
			cout << ans << endl;
			continue;
		}
		if (in.find({ num[K],K }) != in.end()) {
			ans -= num[K];
			in.erase({ num[K],K });
		}
		else {
			out.erase({ -num[K],K });
		}
		num[K] = w[K] - v[K];
		ans += L;
		if (num[K] > 0) {
			in.insert({ num[K],K });
			ans += num[K];
		}
		else {
			out.insert({ -num[K],K });
		}
		while (in.size() && in.begin()->first < 0) {
			int n = in.begin()->second;
			ans -= num[n];
			out.insert({ -in.begin()->first, in.begin()->second });
			in.erase(in.begin());
		}
		while (out.size() && out.begin()->first < 0) {
			int n = out.begin()->second;
			ans += num[n];
			in.insert({ -out.begin()->first, out.begin()->second });
			out.erase(out.begin());
		}
		if (in.size() & 1) {
			if (in.begin()->first > out.begin()->first) {
				in.insert({ -out.begin()->first,out.begin()->second });
				ans += num[out.begin()->second];
				out.erase(out.begin());
			}
			else {
				out.insert({ -in.begin()->first,in.begin()->second });
				ans -= num[in.begin()->second];
				in.erase(in.begin());
			}
		}
		cout << ans << endl;
	}
}