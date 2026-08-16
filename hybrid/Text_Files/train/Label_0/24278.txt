#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

template<class T> inline void chmin(T &a, const T &b) { if(a > b) a = b; }

typedef array<int, 2> A;
typedef pair<A, A> E;
typedef unsigned hash_t;

hash_t rolling_hash(const string &s) {
	static constexpr hash_t base = 1000000007;
	hash_t res = 0;
	for(const auto &c : s) {
		res = res * base + c;
	}
	return res;
}
 
string to_str(const vector<string> &state) {
	string res = "";
	for(const auto &s : state) {
		res += s + ":";
	}
	return res;
}
 
unordered_map<hash_t, int> bfs(int limit, const vector<string> &start, const vector<E> &exchanges) {
	unordered_map<hash_t, int> res;
	queue<vector<string>> que;
 
	res.insert({rolling_hash(to_str(start)), 0});
	que.push(start);
 
	while(!que.empty()) {
		vector<string> state = que.front();
		que.pop();
		const int d = res.at(rolling_hash(to_str(state)));
 
		if(d == limit) break;
 
		for(const auto &element : exchanges) {
			const A &pos = element.first;
			const A &dir = element.second;
			const array<string, 2> train{move(state[pos.front()]), move(state[pos.back()])};

			for(int i = 0; i <= 1; ++i) {
				const int from = i;
				const int to = 1 - i;

				const int &p1 = pos[from];
				const int &p2 = pos[to];
				const int &d1 = dir[from];
				const int &d2 = dir[to];
				const string &t1 = train[from];
				const string &t2 = train[to];

				for(int num = 1; num <= t1.size(); ++num) {
					string tmp = (d1 ? t1.substr(0, num) : t1.substr(t1.size() - num));
					if(d1 == d2) reverse(tmp.begin(), tmp.end());
					state[p1] = (d1 ? t1.substr(num) : t1.substr(0, t1.size() - num));
					state[p2] = (d2 ? tmp + t2 : t2 + tmp);
 
					const hash_t h = rolling_hash(to_str(state));
					if(!res.count(h)) {
						res.insert({h, d + 1});
						que.push(state);
					}
				}
			}
 
			state[pos.front()] = move(train.front());
			state[pos.back()] = move(train.back());
		}
	}
 
	return res;
}
 
int main(){
	cin.tie(nullptr);
	ios::sync_with_stdio(false);
 
	for(int x, y; cin >> x >> y && x;) {
		vector<E> exchanges;
		exchanges.reserve(y);
 
		for(int i = 0; i < y; ++i) {
			string a, b;
			cin >> a >> b;
 
			const int p1 = a[0] - '0';
			const int d1 = (a[1] == 'W');
			const int p2 = b[0] - '0';
			const int d2 = (b[1] == 'W');
 
			exchanges.emplace_back(A{p1, p2}, A{d1, d2});
		}
 
		vector<string> lines(x), goal(x);
 
		for(auto &e : lines) {
			cin >> e;
			if(e == "-") e = "";
		}
 
		for(auto &e : goal) {
			cin >> e;
			if(e == "-") e = "";
		}
     
		const auto d1 = bfs(3, lines, exchanges);
		const auto d2 = bfs(2, goal, exchanges);
 
		int ans = 6;
		for(const auto &e1 : d2) {
			if(ans <= e1.second) continue;
 
			if(d1.count(e1.first)) {
				chmin(ans, e1.second + d1.at(e1.first));
			}
		}
 
		cout << ans << endl;
	}
 
	return EXIT_SUCCESS;
}