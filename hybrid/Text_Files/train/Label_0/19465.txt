#include <iostream>
#include <queue>
#include <map>
#include <climits>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
typedef pair<int,int> NODE;
#define pos first
#define depth second

bool info[100][100];

int bfs(int s,int d){
	queue<NODE> Q;
	bool done[100]={false};
	
	Q.push( make_pair(s,0) );
	while( !Q.empty() ){
		/* queueツづ個静ヲツ督ェツづ個ノツーツドツづーツ訪ツ姪「ツ催渉づ敖づ可つオツづowツ陛渉青板づ可禿シツづェツ、ツキツδーツつゥツづァツ偲ヲツづィツ渉慊つュ */
		NODE now = Q.front();
		Q.pop();
		done[now.pos] = true;

		if(now.pos == d){
			return now.depth;
		}

		for(int next=0;next<100;next++){
			if( !done[next] && info[now.pos][next] ){
				Q.push( make_pair(next,now.depth+1) );
			}
		}
	}
	return INT_MAX;
}

int main(){
	int n,r,k,t,p,s,d,v;
	
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> r >> k;
		r--;
		for(int j=0;j<k;j++){
			cin >> t;
			t--;
			info[r][t] = true;
		}
	}	
	
	cin >> p;
	for(int i=0;i<p;i++){
		cin >> s >> d >> v;
		s--;d--;
		if(v > bfs(s,d) )cout << bfs(s,d)+1 << endl;
		else cout << "NA" << endl;
	}
}