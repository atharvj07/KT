#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int N;
	while(cin>>N&&N){
		map<string,int> anime;
		vector<int> time;
		for(int i=0; i<N; ++i){
			int weekday,start;
			string name;
			cin >> name >> weekday >> start;
			int tmp=60*(start/100)+start%100;
			anime[name]=weekday*60*24+tmp;
			time.push_back(weekday*60*24+tmp);
		}
		int P;
		cin >> P;
		vector<string> fav(P);
		for(int i=0; i<P; ++i){
			cin >> fav[i];
		}
		bool flag=true;
		for(int i=0; i<P; ++i){
			for(int j=0; j<P; ++j){
				if(i!=j&&abs(anime[fav[i]]-anime[fav[j]])<30) flag=false;
			}
		}
		sort(time.begin(),time.end());
		int ans=0,t=0;
		for(int i=0; i<N; ++i){
			bool flag_=true;
			if(t<=time[i]){
				for(int j=0; j<P; ++j){
					if(time[i]!=anime[fav[j]]&&time[i]<anime[fav[j]]&&time[i]+30>anime[fav[j]]){
						flag_=false;
						break;
					}
				}
				if(flag_){
					++ans;
					t=time[i]+30;
				}
			}
		}
		if(!flag) cout << -1 << endl;
		else cout << ans << endl;
	}
	return 0;
}