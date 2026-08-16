#include <bits/stdc++.h>
using namespace std;

int main(){
	string str;
	int n;
	cin >> str >> n;
	char x = 'x';
	int f = 0, s = 0;
	int num[20];
	bool used[20];
	for(int i = 0; i < 20; i++) used[i] = false;
	char ope[20];
	for(int i = 0; i < str.size(); i++){
		if(i%2 == 0){
			num[i/2] = str[i]-'0';
		} else{
			ope[i/2] = str[i];
		}
	}
	int t = -1;
	for(int i = 0; i < str.size()/2; i++){
		if(ope[i] == '*'){
			if(t == -1){
				t = num[i]*num[i+1];
				used[i] = true;
				used[i+1] = true;
			} else{
				t *= num[i+1];
				used[i+1] = true;
			}
		} else{
			if(t != -1) f += t;
			t = -1;
		}
	}
	if(t > 0) f += t;
	for(int i = 0; i < (str.size()+1)/2; i++){
		if(!used[i]) f += num[i];
	}
	for(int i = 0; i < str.size(); i++){
		if(i%2 == 0){
			if(x == 'x') s = str[i]-'0';
			if(x == '+') s += str[i]-'0';
			if(x == '*') s *= str[i]-'0';
		} else{
			x = str[i];
		}
	}
	if(s == n){
		if(f == n) cout << "U" << endl;
		else cout << "L" << endl;
	} else{
		if(f == n) cout << "M" << endl;
		else cout << "I" << endl;
	}
}