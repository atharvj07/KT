#include<bits/stdc++.h>
using namespace std;
const int maxn = 300001;
int m, n, ans;
bool visited[maxn];
vector < int > edge[maxn];
void dfs(int now){
	if(visited[now])return;
	visited[now] = true;
	for(auto &i : edge[now])dfs(i);
}
int main(){
	cin >> n >> m;
	for(int a, b, c, i = 0;i < m;++i){
		cin >> a >> b >> c;
		edge[a].push_back(b);
		edge[b].push_back(a);
	}
	for(int i = 1;i <= n;++i){
		if(!visited[i]){
			++ans;
			dfs(i);
		}
	}
	cout << ans << '\n';
}
