#include <iostream>
#include <algorithm>
#include <deque>
#include <vector>
#include <utility>
#define pii pair<int,int>
#define F first
#define S second
using namespace std;

const int maxN = 1e5 + 326;
int N, x, last[maxN];
deque<int> vals;
deque<pii> stk;
vector<pii> segs;

int main(){
	cin >> N;
	for(int i = 0; i < N; i++){
		cin >> x;
		if(!vals.size() || vals.back() != x) vals.push_back(x);
	}
	N = vals.size();
	fill(last, last + maxN, -1);
	for(int i = 0; i < N; i++){
		if(~last[vals[i]]) segs.emplace_back(last[vals[i]], i);
		last[vals[i]] = i;
	}
	sort(segs.begin(), segs.end(), [](const pii &a, const pii &b) {
		return a.S == b.S ? a.F < b.F : a.S < b.S;
	});
	for(auto [l, r] : segs){
		//find the answer
		//cout << "going for " << l << ", " << r << endl;
		int tmp;
		if(!stk.size()) tmp = 0;
		else {
			auto p = lower_bound(stk.begin(), stk.end(), pii({l + 1, maxN}));
			if(p != stk.begin()) --p;
			auto x = *p;
			//cout << "found: " << x.F << " " << x.S << endl;
			if(x.F > l + 1) tmp = 0;
			else tmp = x.S;
		}
		tmp++;
		if(!stk.size() || stk.back().S < tmp) stk.emplace_back(r, tmp);
		//cout << "for " << l << " " << r << ", ans = " << tmp << endl;
	}
	int ans = 1;
	for(int i = 1; i < N; i++) ans += (vals[i] != vals[i - 1]);
	ans -= (stk.size() ? stk.back().S : 0);
	cout << ans << endl;
}
