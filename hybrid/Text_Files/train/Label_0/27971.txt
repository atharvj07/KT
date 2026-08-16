#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define ALL(v) begin(v),end(v)

typedef long long LL;
const LL INF = 1010101010;

struct solver{

	enum nodetype{
		CON, PAR, ADD, MUL
	};

	struct node{
		nodetype tp;
		LL val;
		vector<int> child;
		vector<LL> psum;
	};

	vector<node> nodes;
	LL n;
	const char *p;
	LL ans;
	
	LL solve(int n_, const string &s){
		n = n_;
		ans = 0;
		for(int i = 0; i < 10; ++i){
			int k = newnode(CON);
			nodes[k].val = i;
		}

		p = s.c_str();
		int root = expr();
		dfs(root);
		return ans;
	}

	int newnode(nodetype tp){
		nodes.emplace_back();
		nodes.back().tp = tp;
		return nodes.size() - 1;
	}

	int factor(){
		if(*p == '('){
			++p;
			int e = expr();
			++p;
			int ret = newnode(PAR);
			nodes[ret].val = nodes[e].val;
			nodes[ret].child.push_back(e);
			return ret;
		}
		int k = *p - '0';
		++p;
		if(k < 0 || k > 9){ throw 0; }
		return k;
	}

	int term(){
		int f = factor();
		if(*p != '*'){ return f; }
		int ret = newnode(MUL);
		LL val = nodes[f].val;
		nodes[ret].child.push_back(f);
		nodes[ret].psum.push_back(val);
		while(*p == '*'){
			++p;
			f = factor();
			val = min(val * nodes[f].val, INF);
			nodes[ret].child.push_back(f);
			nodes[ret].psum.push_back(val);
		}
		nodes[ret].val = val;
		return ret;
	}

	int expr(){
		int t = term();
		if(*p != '+'){ return t; }
		int ret = newnode(ADD);
		LL val = nodes[t].val;
		nodes[ret].child.push_back(t);
		nodes[ret].psum.push_back(val);
		while(*p == '+'){
			++p;
			t = term();
			val += nodes[t].val;
			nodes[ret].child.push_back(t);
			nodes[ret].psum.push_back(val);
		}
		nodes[ret].val = min(val, INF);
		return ret;
	}

	void procadd(node &nd, int lt, LL accl){
		if(accl >= n){ return; }
		int sz = nd.psum.size();
		int rt = lower_bound(ALL(nd.psum), n - accl + nd.psum[lt]) - nd.psum.begin();
		if(rt <= lt || rt >= sz){ return; }
		node &rch = nodes[nd.child[rt]];
		if(rch.tp == MUL){
			LL tgt = n - accl - (nd.psum[rt - 1] - nd.psum[lt]);
			int k1 = lower_bound(ALL(rch.psum), tgt) - rch.psum.begin();
			int k2 = upper_bound(ALL(rch.psum), tgt) - rch.psum.begin();
			ans += k2 - k1;
		}
		else if(nd.psum[rt] == n - accl + nd.psum[lt]){
			++ans;
		}
	}

	void dfs(int u){
		node &nd = nodes[u];
		if(nd.val < n){ return; }
		for(int c : nd.child){ dfs(c); }
		int sz = nd.child.size();
		if(nd.tp == ADD){
			for(int lt = 0; lt + 1 < sz; ++lt){
				node &lch = nodes[nd.child[lt]];
				if(lch.tp == MUL){
					LL accl = 1;
					for(int i = lch.child.size(); i--; ){
						accl *= nodes[lch.child[i]].val;
						if(accl >= n){ break; }
						procadd(nd, lt, accl);
					}
				}
				else{
					procadd(nd, lt, nodes[nd.child[lt]].val);
				}
			}
		}
		else if(nd.tp == MUL){
			LL acc = 1;
			int rt = 0;
			int con1 = 0;
			for(int lt = 0; lt < sz; ++lt){
				if(rt <= lt){
					rt = lt;
					con1 = 0;
					acc = 1;
				}
				while(rt < sz){
					if(acc > n){ break; }
					LL v = nodes[nd.child[rt]].val;
					if(v == 1){
						++con1;
					}
	 				else if(acc == n){ break; }
	 				else{
	 					con1 = 0;
						acc *= v;
	 				}
					++rt;
				}
				if(acc == n && rt - lt > 1){
					LL t = min(con1, rt - lt - 2);
					ans += t + 1;
				}
				acc /= nodes[nd.child[lt]].val;
			}
		}
		else{
			if(nd.val == n){ ++ans; }
		}
	}
};

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	string s;
	while(cin >> n >> s){
		LL ans = solver().solve(n, s);
		cout << ans << '\n';
	}
}

