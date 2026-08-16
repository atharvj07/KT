#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>

using namespace std;

int main(){
	int n;
	string s;
	map< string, vector<int> > m;
	while(cin >> s >> n){
		m[s].push_back(n);
	}
	
	map< string, vector<int> >::iterator it;
	for(it = m.begin(); it != m.end(); it++){
		cout << it->first << endl;
		sort(it->second.begin(), it->second.end());
		for(int i = 0; i < it->second.size(); i++){
			if(i){
				cout << ' ';
			}
			cout << it->second[i];
		}
		cout << endl;
	}
	
	return 0;
}