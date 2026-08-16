#include <bits/stdc++.h>

using namespace std;

int main(){
	int n; cin >> n;
	vector <string> v(n);
	for (int i = 0; i < n; i++){
		cin >> v[i];
	}
	bool rr = false;
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			if (v[i][j] == '#')
				rr = true;
		}
	}
	if(!rr){
		cout << "-1" << endl;
 		return 0;
	}
	
	
	int r = n * 2;
	for (int i = 0; i < n; i++){
		int c = 0;
		bool hst = false;
		for (int j = 0; j < n; j++){
				if (v[j][i] == '#'){
				hst = true;
			}
			if (v[i][j] == '.'){
				c++;
			}
		}
		if (!hst){
			c++;
		}
		for (int j = 0; j < n; j++){
			bool hd = false;
			for (int z = 0; z < n; z++){
				if (v[z][j] == '.')
					hd = true;
			}
			if (hd)
				c++;
		}
		
		r = min(r, c);
		
	}
	
	cout << r << endl;
	
	return 0;
}