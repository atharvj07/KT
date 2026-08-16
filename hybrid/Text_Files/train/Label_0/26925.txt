#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
#include <set>

using namespace std;

int field[10][10];
int n;

int bfs(int ss){
	set<int> passed;
	queue<int> q[2];
	int cur=0;
	int nxt=1;
	q[cur].push(ss);
	int cnt=0;
	passed.insert(ss);
	while(q[cur].size()){
		while(q[cur].size()){
			int cs=q[cur].front();
			if(cs==0)return cnt;
			q[cur].pop();
			// csÌóÔ©çÚ®Å«éóÔðñ
			int minx,miny;
			minx=miny=-1;
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					if((cs>>(i*n+j))&1){
						minx=j;
						miny=i;
						break;
					}
				}
				if(minx!=-1)break;
			}
			// EºÌÀWðè
			for(int i=miny;i<n;i++){
				for(int j=minx;j<n;j++){
					// ½]
					int ns=cs;
					for(int k=miny;k<=i;k++){
						for(int l=minx;l<=j;l++){
							if((ns>>(k*n+l))&1)ns&=~(1<<(k*n+l));
							else ns|=(1<<(k*n+l));
						}
					}
					if(passed.find(ns)==passed.end()){
						q[nxt].push(ns);
						passed.insert(ns);
					}
				}
			}
		}
		cnt++;
		swap(cur,nxt);
	}
	return -1;
}

int main(){
	while(cin>>n&&n){
		int ss=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				cin>>field[i][j];
				if(field[i][j])ss|=(1<<(i*n+j));
			}
		}
		int cnt=bfs(ss);
		for(int i=0;i<cnt;i++)cout<<"myon";
		cout<<endl;
	}
	return 0;
}