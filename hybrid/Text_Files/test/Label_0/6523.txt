#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,a,b) for(int i = a; i < (int)b; i++)
#define pb push_back
#define mp make_pair
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef long long ll;
const int INF = 1<<28;
const ll MOD = 1000000007;
const int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};

struct order {
	string name;
	char com;
	int price;
	bool operator < (const order &a) const {
		return price < a.price;
	}
};

struct comodity {
	int min, max, sum, cnt;
};

void addCom(map<char, comodity> &m, int v, char name) {
	if(!m.count(name)) {
		comodity c;
		c.min = c.max = c.sum = v;
		c.cnt = 1;
		m[name] = c;
	}
	else {
		m[name].min = min(m[name].min, v);
		m[name].max = max(m[name].max, v);
		m[name].sum += v;
		m[name].cnt++;
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int n;
	while(cin >> n, n) {
		vector<order> buy, sell;
		map<string, pi> ppl;
		map<char, comodity> m;
		REP(i, n) {
			order o; string in;
			cin >> o.name >> in >> o.com >> o.price;
			if(!ppl.count(o.name))
				ppl[o.name] = mp(0,0);
/*
			cout << "-----" << i << endl;
			cout << o.name << ' ' << in << ' ' << o.com << ' ' << o.price << endl;
			cout << "-----BUY" << endl;
			REP(i, buy.size())
				cout << buy[i].name << ' ' << buy[i].com << ' ' << buy[i].price << endl;
			cout << "-----SELL" << endl;
			REP(i, sell.size())
				cout << sell[i].name << ' ' << sell[i].com << ' ' << sell[i].price << endl;
*/
			bool flg = false;
			int v, pnt;
			if(in == "SELL") {
				REP(j, buy.size()) {
					if(o.com == buy[j].com && o.name != buy[j].name && o.price <= buy[j].price) {
						v = (o.price + buy[j].price) / 2;
						addCom(m, v, o.com);
						flg = true;
						pnt = j;
						break;
					}
				}
				if(flg) {
					ppl[buy[pnt].name].first += v;
					ppl[o.name].second += v;
					buy.erase(buy.begin() + pnt);
				}
				else {
					sell.pb(o);
					stable_sort(sell.begin(), sell.end());
				}
			}
			else if(in == "BUY") {
				REP(j, sell.size()) {
					if(o.com == sell[j].com && o.name != sell[j].name && o.price >= sell[j].price) {
						v = (o.price + sell[j].price) / 2;
						addCom(m, v, o.com);
						flg = true;
						pnt = j;
						break;
					}
				}
				if(flg) {
					ppl[o.name].first += v;
					ppl[sell[pnt].name].second += v;
					sell.erase(sell.begin() + pnt);
				}
				else {
					buy.pb(o);
					stable_sort(buy.rbegin(), buy.rend());
				}
			}
		}
		for(auto i : m)
			cout << i.first << ' ' << i.second.min << ' ' << i.second.sum / i.second.cnt << ' ' << i.second.max << endl;
		cout << "--" << endl;
		for(auto i : ppl)
			cout << i.first << ' ' << i.second.first << ' ' << i.second.second << endl;
		cout << "----------" << endl;
	}
	return 0;
}