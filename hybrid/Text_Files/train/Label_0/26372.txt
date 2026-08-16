#include <bits/stdc++.h>
using namespace std;

#define get(x) scanf("%d",&x)
#define f(i,n) for (int i = 0; i<n;i++)

int main() {
	int n; 
	get(n);
	vector<int> adj[n];
	f(i,n-1) {
		int a,b;
		get(a); get(b);
		adj[--a].push_back(--b); adj[b].push_back(a);
	}
	int d = 0;
	function<int(int,int)> diameter = [&](int v, int p) {
		int best[2];
		best[0]=best[1]=0;
		for (int w : adj[v])
			if (w!=p) {
				int dd = diameter(w,v);				
				if (dd>best[0]) swap(dd,best[0]);
				if (dd>best[1]) swap(dd,best[1]);
				if (dd>best[0]) swap(dd,best[0]);
			}
		d=max(d,1+best[0]+best[1]);
		return 1+max(best[0],best[1]);
	};
	diameter(0,-1);
	if (d < 2 || (d-2)%3)
		cout << "First" << endl;
	else
		cout << "Second" << endl;

	return 0; 
}