/* attention to typo and overflow */
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;
const int INF=1<<25;
//void io(){ cin.tie(0);ios::sync_with_stdio(false);} //attention to use of endl
/*printf("%.9Lf\n",cf);*/
char output(bool i,bool j){
	if(i==1 && j==0){
		return 'M';
	}
	if(i==0 && j==1){
		return 'L';
	}
	if(i==0 && j==0){
		return 'I';
	}
	if(i==1 && j==1){
		return 'U';
	}
	return 'N';
}

int main(){
	//io();
	string s;
	getline(cin,s);
	//cin.ignore();
	int ans;
	cin>>ans;

	vector <int> plus;
	for(int i=0;i<s.size();i++){
		if(i%2==0){
			if(i!=0 && s[i-1]=='*'){
				plus[plus.size()-1]*=s[i]-'0';
			}else{
				plus.push_back(s[i]-'0');
			}
		}
	}

	int one=0;
	for(int i=0;i<plus.size();i++){
		//cerr<<plus[i]<<endl;
		one+=plus[i];
	}

	int two=s[0]-'0';
	for(int i=1;i<s.size();i++){
		if(i%2==0){
			if(s[i-1]=='+'){
				two+=s[i]-'0';
			}else{
				two*=s[i]-'0';
			}
		}
	}

	//cerr<<ans<<' '<<one<<' '<<two<<endl;

	cout<<output(ans==one,ans==two)<<endl;

	return 0;
}