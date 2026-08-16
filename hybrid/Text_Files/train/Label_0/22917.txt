#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

const int INF = int(1.05e9); 

class SegMax {
	int N;
	vector<int> maxi;
	inline void doit(int k, int x) {maxi[k] = max(maxi[k], x);}
public:
	SegMax(int n) : N(n == 1 ? 1 : 1<<(32 - __builtin_clz(n - 1))), maxi(2*N, 0) {}
	int query(int k) {
		int ans = 0;
		for (k+=N;k>0;k>>=1) ans = max(ans, maxi[k]);
		return ans;
	}

	void fill(int s, int t, int x) {
		for (int idx;0<s && s+(s&-s)<=t && (idx=(N+s)/(s&-s)); s+=s&-s) doit(idx, x);
		for (int idx;s<t && (idx=(N+t)/(t&-t)-1); t-=t&-t) doit(idx, x);
	}
};

class SegRMQ {
	int N;
	vector<pair<int, bool> > datas;//(mini, uniform)
	inline void update(int k) {
		datas[k].first = min(datas[2*k].first, datas[2*k+1].first);
	}
	inline void prop(int k) {
		if (datas[k].second) {
			datas[2*k] = datas[2*k+1] = datas[k];
			datas[k].second = false;
		}
	}
public:
	SegRMQ(const vector<int>& ns) {
		N = ns.size() == 1 ? 1 : 1<<(32 - __builtin_clz(int(ns.size())-1));
		datas.assign(2*N, make_pair(INF, false));
		for (int i = 0; i < int(ns.size()); ++i) {
			datas[i+N].first = ns[i];
		}
		for (int i = N - 1 ; i > 0; --i) update(i);
	}

	int getMin(int s, int t) {
		int h = N, k = 0, ans = INF;
		for (;h && (s&h)==(t&h) && (k=(k<<1)|bool((s&h)||h==N)) && k<N; h>>=1) prop(k);

		int i=s?(N+s)/(s&-s):k, sk=k;
		for (int sh = h; sh && (sk=(sk<<1)|bool((s&sh)||sh==N)) < i; sh >>= 1) prop(sk);
		for (int idx;0<s && s+(s&-s)<=t && (idx=(N+s)/(s&-s)); s+=s&-s) ans = min(ans, datas[idx].first);;

		int j = s<t?(N+t)/(t&-t)-1:k, tk=k;
		for (int th = h; th && (tk=(tk<<1)|bool((t&th)||th==N)) < j; th >>= 1) prop(tk);
		for (int idx;s<t && (idx=(N+t)/(t&-t)-1); t-=t&-t) ans = min(ans, datas[idx].first);

		return ans;
	}

	void fill(int s, int t, int x) {
		int h = N, k = 0;
		for (;h && (s&h)==(t&h) && (k=(k<<1)|bool((s&h)||h==N)) && k<N; h>>=1) prop(k);

		int i=s?(N+s)/(s&-s):k, sk=k;
		for (int sh = h; sh && (sk=(sk<<1)|bool((s&sh)||sh==N)) < i; sh >>= 1) prop(sk);
		for (int idx;0<s && s+(s&-s)<=t && (idx=(N+s)/(s&-s)); s+=s&-s) datas[idx] = make_pair(x, true);
		for (;(sk>>=1) > k;) update(sk);

		int j = s<t?(N+t)/(t&-t)-1:k, tk=k;
		for (int th = h; th && (tk=(tk<<1)|bool((t&th)||th==N)) < j; th >>= 1) prop(tk);
		for (int idx;s<t && (idx=(N+t)/(t&-t)-1); t-=t&-t) datas[idx] = make_pair(x, true);
		for (;(tk>>=1) > k;) update(tk);

		for (k>>=bool(k>=N); k > 0; k>>=1) update(k);
	}
};

const int MAX_N = int(5e4);
int as[MAX_N], bs[MAX_N], ys[MAX_N], ns[2*MAX_N], ts[MAX_N];

int main() {
	int n; scanf("%d", &n);
	int L = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d%d%d%d", ts+i, as+i, bs+i, ys+i);
		++bs[i];
		ns[L++] = as[i];
		ns[L++] = bs[i];
	}
	sort(ns, ns + L);
	L = unique(ns, ns+L) - ns;
	for (int i = 0; i < n; ++i) {
		as[i] = lower_bound(ns, ns+L, as[i]) - ns;
		bs[i] = lower_bound(ns, ns+L, bs[i]) - ns;
	}

	SegMax seg(L);
	set<int> ids;
	vector<int> xs(L);
	for (int i = 0; i < L; ++i) {
		ids.insert(i);
	}
	for (int i = 0; i < n; ++i) {
		if (ts[i] == 0) {
			seg.fill(as[i], bs[i], ys[i]);
		}
		else {
			for (set<int>::iterator itr = ids.lower_bound(as[i]); itr != ids.end() && *itr < bs[i]; ids.erase(itr++)) {
				xs[*itr] = seg.query(*itr);
			}
		}
	}
	for (set<int>::iterator itr = ids.begin(); itr != ids.end(); ++itr) {
		xs[*itr] = seg.query(*itr);
	}
	SegRMQ rmq(xs);
	for (int i = 0; i < n; ++i) {
		if (ts[i] == 0 && rmq.getMin(as[i], bs[i]) != ys[i]) {
			puts("NO");
			return 0;
		}
		else if (ts[i] == 1) {
			rmq.fill(as[i], bs[i], ys[i]);
		}
	}
	puts("YES");

	return 0;
}