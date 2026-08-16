#include<iostream>
#include<cstdio>
#include<algorithm>
#include<climits>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<stack>
#include<functional>
using namespace std;

struct Team{
	int n,t;
	bool operator <(const Team &a)const{
		return t<a.t;
	}
};

struct Time{
	int s,m;
};

Team team[1000000];

int main(){
	int N;
	while(cin>>N,N){
		for(int i=0;i<N;i++){
			Time time;
			cin>>team[i].n; team[i].t = 0;
			for(int j=0;j<4;j++){
				cin>>time.m>>time.s; team[i].t += time.m*60+time.s;
			}
		}
		sort(team,team+N);
		printf("%d\n%d\n%d\n",team[0].n,team[1].n,team[N-2].n);
	}
	return 0;
}