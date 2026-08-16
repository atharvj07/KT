#include<bits/stdc++.h>
using namespace std;

using DB = double;
struct PT {
	int x, y;
	PT (int x = 0, int y = 0) : x(x), y(y) {}
	void in() { scanf("%d%d", &x, &y); }
	bool operator <(const PT &pts) const { return make_pair(x, y) < make_pair(pts.x, pts.y); }
	bool operator ==(const PT &pts) const { return make_pair(x, y) == make_pair(pts.x, pts.y); }
};

DB sqr(int x) { return (DB)x * x; }

DB dis(PT p1, PT p2) {
	return sqrt(sqr(p1.x - p2.x) + sqr(p1.y - p2.y));
}

long long vect(PT p, PT p1, PT p2) {
	return 1LL * (p1.x - p.x) * (p2.y - p.y) - 1LL * (p1.y - p.y) * (p2.x - p.x);
}

long long scal(PT p, PT p1, PT p2) {
	return 1LL * (p1.x - p.x) * (p2.x - p.x) + 1LL * (p1.y - p.y) * (p2.y - p.y);
}

bool check(PT p1, PT p2, PT p3) {
	if (vect(p1, p2, p3) < 0) return 1;
	if (!vect(p1, p2, p3)) return scal(p2, p1, p3) <= 0;
	return 0;
}

vector<PT> pts, cvx;

void convex() {
	sort(pts.begin(), pts.end());
	pts.erase(unique(pts.begin(), pts.end()), pts.end());
	if (pts.size() == 1) {
		cvx.push_back(pts[0]);
		return;
	}
	for (int times = 0; times < 2; times++) {
		for (auto t : pts) {
			while (cvx.size() > 1 && check(cvx[cvx.size() - 2], cvx.back(), t)) cvx.pop_back();
			cvx.push_back(t);
		}
		reverse(pts.begin(), pts.end());
	}
	cvx.pop_back();
}

int getId(PT p) {
	return lower_bound(pts.begin(), pts.end(), p) - pts.begin();
}

vector<PT> getConvex(PT lft, PT cur, PT rht, PT nV) {
	vector<PT> nC;
	int px = getId(lft), cx = getId(cur), rx = getId(rht);
	int now = px;
	while (now != cx) {
		if (!(pts[now] == nV)) {
			while (nC.size() > 1 && check(nC[nC.size() - 2], nC.back(), pts[now])) nC.pop_back();
			nC.push_back(pts[now]);
		}
		if (now < cx) ++now;
		else --now;
	}
	while (now != rx) {
		if (now < rx) ++now;
		else --now;
		if (!(pts[now] == nV)) {
			while (nC.size() > 1 && check(nC[nC.size() - 2], nC.back(), pts[now])) nC.pop_back();
			nC.push_back(pts[now]);
		}
	}
	return nC;
}

vector<DB> profit;
multiset<DB> PM;
DB ans;

void process() {
	int sz = cvx.size();
	for (int i = 0; i < cvx.size(); i++) {
		PT lft = cvx[(i - 1 + sz) % sz], cur = cvx[i], rht = cvx[(i + 1) % sz];
		DB lose = dis(lft, cur) + dis(cur, rht);
		vector<PT> nC = getConvex(lft, cur, rht, PT(1e8, 1e8));
		DB get = 0;
		for (int j = 1; j < nC.size(); j++) get += dis(nC[j - 1], nC[j]);
		profit.push_back(lose - get);
		PM.insert(lose - get);
		nC.push_back(cvx[(i + 2) % sz]);
		for (int j = 1; j < (int)nC.size() - 1; j++) {
			PT _lft = nC[j - 1], _cur = nC[j], _nxt = nC[j + 1];
			DB _lose = dis(_lft, _cur) + dis(_cur, _nxt);
			vector<PT> _nC = getConvex(_lft, _cur, _nxt, cur);
			DB _get = 0;
			for (int k = 1; k < _nC.size(); k++) _get += dis(_nC[k - 1], _nC[k]);
			ans = max(ans, lose - get + _lose - _get);
		}
	}
	for (int i = 0; i < profit.size(); i++) {
		DB l = profit[(i - 1 + sz) % sz], c = profit[i], r = profit[(i + 1) % sz];
		PM.erase(PM.find(l)), PM.erase(PM.find(r)), PM.erase(PM.find(c));
		if (PM.size()) ans = max(ans, c + *(PM.rbegin()));
		else ans = max(ans, c);
		PM.insert(l), PM.insert(r), PM.insert(c);
	}
}

int main() {
	int n; scanf("%d", &n);
	PT p;
	while (n--) p.in(), pts.push_back(p);
	convex();
	process();
	printf("%.10lf\n", ans);
}

