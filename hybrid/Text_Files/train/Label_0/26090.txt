#include <set>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int64;

const int MAX_N = int(1e5 + 10);
const int MAX_K = 30;
const int64 INF = int64(2.05e18); //^@ 2^63 ~ 9.2*10^18。本当にこれで大丈夫？

int N, K;
int64 L;
int sa[MAX_N + 1];
int64 comb[MAX_N + MAX_K + 1][MAX_K + 1];

inline int64 multi(const int64 x, const int64 y) {
	return (double(x)*y < INF * 1.3) ? x * y : INF;
}

void init() {
	scanf("%d%d%lld", &N, &K, &L);
	sa[0] = N;
	for (int i = 1; i <= N; ++i) {
		scanf("%d", sa + i);
		--sa[i];
	}
}

void prepareCombination() {
	for (int n = 0; n <= N + K; ++n) {
		comb[n][0] = 1;
		if (n <= K) {
			comb[n][n] = 1;
		}
		for (int k = 1; k <= min(n, K); ++k) {
			if (n - 1 >= k) {
				comb[n][k] = min(INF, comb[n-1][k] + comb[n-1][k-1]);
			}
		}
	}
}

struct State {
	int from, to;
	int64 ways;
	State(){}
	State(int from_, int to_, int64 ways_):
		from(from_), to(to_), ways(ways_)
	{}
};

void solve() {
	prepareCombination();

	//inv[i] := str[k..]は辞書順何番目にくるのか。
	static int inv[MAX_N + 1];
	for (int i = 0; i <= N; ++i) {
		inv[sa[i]] = i;
	}

	//mustInc[i] := sa[i]番目の文字はsa[i-1]番目の文字より大きくなければならないか。
	static bool mustInc[MAX_N + 1];
	int incCount = 0;
	for (int i = 1; i < N; ++i) {
		if (inv[sa[i+1] + 1] < inv[sa[i] + 1]) {
			mustInc[i] = true;
			++incCount;
		}
	}

	//足りない、不可能な場合
	K -= incCount;
	if (K <= 0 || comb[N+K-1][K-1] < L) {
		puts("Impossible");
		return ;
	}

	//fixedAcc[i]: -1ならその文字は未確定。そうでないならaccの累積値がfixedAcc[i]でなくてはならない。
	static int fixedAcc[MAX_N + 1];
	memset(fixedAcc, -1, sizeof(fixedAcc));
	fixedAcc[N] = K - 1;

	//意味のある区間の数。statesに含まれる要素は高々K個。
	vector<State> states;
	states.push_back(State(-1, N, comb[N+K-1][K-1]));
	//setを使ってO(n*(log n + A))で手抜く。
	set<int> fixed;
	fixed.insert(1);
	fixed.insert(-N);

	for (int _ = 0; _ < N; ++_) {
		const int p = inv[_] - 1;
		int key = -1;
		int64 w = 1;
		int prev = -(*fixed.lower_bound(-p));
		int lAcc = prev == -1 ? 0 : fixedAcc[prev];
		for (int i = 0; i < int(states.size()); ++i) {
			if (states[i].from <= p && p <= states[i].to) {
				key = i;
			}
			else {
				w = multi(w, states[i].ways);
			}
		}
		if (key == -1) {
			fixedAcc[p] = lAcc;
			fixed.insert(-p);
			continue;
		}
		const int from = states[key].from, to = states[key].to;
		states.erase(states.begin() + key);
		for (int a = lAcc; ; ++a) {
			int64 leftWay = 1, rightWay = 1;
			int leftFlex  = a - (from >= 0 ? fixedAcc[from]: 0);
			int rightFlex = fixedAcc[to] - a;
			if (leftFlex > 0) {
				leftWay = comb[p-from-1 + leftFlex][leftFlex];
			}
			if (rightFlex > 0) {
				rightWay = comb[to-p-1 + rightFlex][rightFlex];
			}
			int64 newWay = multi(leftWay, rightWay);
			if (multi(newWay, w) >= L) {
				if (leftWay > 1) {
					states.push_back(State(from, p, leftWay));
				}
				if (rightWay > 1) {
					states.push_back(State(p, to, rightWay));
				}
				fixedAcc[p] = a;
				fixed.insert(-p);
				break;
			}
			else {
				L -= newWay * w;
			}
		}
	}

	static char ans[MAX_N + 1];
	int add = 0;
	for (int i = 0; i < N; ++i) {
		if (mustInc[i]) {
			++add;
		}
		ans[sa[i+1]] = char('a' + fixedAcc[i] + add);
	}
	puts(ans);
}

int main() {
	init();
	solve();
	return 0;
}