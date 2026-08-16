// UTPC2010 F. UTF-8

#include <iostream>
#include <vector>
#include <string>
#include <string.h>

using namespace std;

int main(){
	int n;
	string cmp[4] = {"0xxxxxxx", "110yyyyx10xxxxxx", "1110yyyy10yxxxxx10xxxxxx", "11110yyy10yyxxxx10xxxxxx10xxxxxx"};
	long long dp[1001];
	while(cin >> n, n){
		vector<string> vs(n);
		for(int i=0;i<n;i++) cin >> vs[i];
		memset(dp, 0, sizeof(dp));
		dp[0] = 1;
		for(int i=0;i<n;i++){
			string cur;
			for(int j=0;j<4&&i+j<n;j++){
				cur += vs[i+j];
				int mul = 1;
				bool one = false;
				bool zero = true;
				bool seen = false;
				for(int k=0;k<cur.size();k++){
					if(isdigit(cmp[j][k])&&cmp[j][k]!=cur[k]&&cur[k]!='x') mul = 0;
					if(cmp[j][k]=='y'){
						if(cur[k]=='1') one = true;
						if(cur[k]!='0') zero = false;
						if(cur[k]=='x') mul *= 2;
					}
					if(cmp[j][k]=='x'){
						if(j!=0&&!seen){
							if(zero) mul = 0;
							if(!one&&mul>1) mul--;
							seen = true;
						}
						if(cur[k]=='x') mul = (mul*2)%1000000;
					}
				}
				dp[i+j+1] = (dp[i+j+1]+dp[i]*mul)%1000000;
			}
		}
		cout << dp[n] << endl;
	}
}