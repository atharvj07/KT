#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;
#define N 300000
#define P(x,y) make_pair(x,y)

int n;
multiset<int> s[N];
map<int,int> mp[N];
queue<pii> q;

void ins(int x,int y){
	if (x==y) return;
	++mp[x][y]; ++mp[y][x];
	if (mp[x][y]==2) q.push(P(x,y));
	s[x].insert(y); s[y].insert(x);
}

int main(){
	scanf("%d",&n);
	for (int i=1;i<n*2-1;++i){
		int x,y; scanf("%d%d",&x,&y);
		ins(x,y);
	}
	for (int i=1;i<n;++i){
		while (1){
			if (q.empty()){puts("NO"); return 0;}
			int x=q.front().first,y=q.front().second; q.pop();
			if (!mp[x][y]) continue;
			if (s[x].size()<s[y].size()) swap(x,y);
			for (int i:s[y]){
				mp[y][i]=mp[i][y]=0;
				s[i].erase(s[i].find(y));
				ins(i,x);
			}
			break;
		}
	}
	puts("YES");
	
	return 0;
}
			