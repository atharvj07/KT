#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cctype>
#include <map>
#include <functional>
using namespace std;

typedef vector<int> vint;

int ans;
const char *ptr;
char buf[256];
map<string,int> mp;

size_t cmp(const vint &v1, const vint &v2){
	return v1.size() < v2.size();
}

vint block(bool brace, string defvar = string()){
	vector<vint> freqs;
	map<string,int>::iterator it;
	
	if(!defvar.empty()){
		mp.insert(make_pair(defvar, 1));
	}

	if(brace) ++ptr;
	while(*ptr != '}'){
		if(*ptr == '{'){
			freqs.push_back(block(true));
		}
		else if(*ptr == 'V'){	//VAR
			ptr += 3;
			ans += 3;

			int dif = 0;
			sscanf(ptr, " %[a-z]%n", buf, &dif);
			string varname = buf;
			ptr += dif;

			freqs.push_back(block(false, varname));
		}
		else if(islower(*ptr)){
			sscanf(ptr, "%[a-z]", buf);
			string varname = buf;
			ptr += varname.size();
			++mp[varname];
		}
		else if(!isspace(*ptr++)){
			++ans;
		}
	}
	if(brace){
		++ptr;
		ans += 2;
	}

	vint res;
	if(freqs.size() == 1){
		res.swap(freqs[0]);
	}
	else if(freqs.size() > 1){
		int maxsize = max_element(freqs.begin(), freqs.end(), cmp)->size();
		for(int i = 0; i < maxsize; ++i){
			int s = 0;
			for(int j = 0; j < freqs.size(); ++j){
				if(i < freqs[j].size()){
					s += freqs[j][i];
				}
			}
			res.push_back(s);
		}
	}

	if(!defvar.empty()){
		map<string,int>::iterator it = mp.find(defvar);
		res.push_back(it->second);
		mp.erase(it);
	}
	sort(res.begin(), res.end(), greater<int>());

	return res;
}

int main(){
	string s, lines;
	int n;
	while(cin >> n, n){
		cin.ignore();
		lines = "{";
		for(int i = 0; i < n; ++i){
			getline(cin, s);
			lines += s;
		}
		lines += '}';
		
		ans = -2;
		mp.clear();
		ptr = lines.c_str();
		vint v = block(true);
		
		v.resize(1024, 0);
		vint::iterator it1 = v.begin(), it2;
		for(int i = 1; i <= 9; ++i){
			it2 = it1 + (1 << i);
			ans += accumulate(it1, it2, 0) * i;
			it1 = it2;
		}
		
		cout << ans << '\n';
	}
}