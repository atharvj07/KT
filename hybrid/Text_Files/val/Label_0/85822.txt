#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
using namespace std;

string normalize(string s, char c, bool isLeft)
{
    if(c != '#'){
        if(s[0] != '#')
            replace(s.rbegin(), s.rend(), s[0], c);
        if(s[s.size()-1] != '#' && !isLeft)
            replace(s.begin(), s.end(), s[s.size()-1], c);
    }

    s += c;
    if(s[0] == 'A' && s.find('A', 1) == string::npos)
        return "";
    s = s.substr(1);

    char x = 'A';
    map<char, char> m;
    m['#'] = '#';
    for(unsigned i=0; i<s.size(); ++i){
        if(m.find(s[i]) == m.end()){
            m[s[i]] = x;
            ++ x;
        }
        s[i] = m[s[i]];
    }

    return s;
}

int main()
{
    int w, h, s;
    cin >> w >> h >> s;

    map<pair<string, int>, long long> dp;
    dp[make_pair(string(w, '#'), s)] = 1;

    for(int y=0; y<h; ++y){
        for(int x=0; x<w; ++x){
            map<pair<string, int>, long long> next;
            for(map<pair<string, int>, long long>::iterator it=dp.begin(); it!=dp.end(); ++it){
                string s = it->first.first;
                int wall = it->first.second;

                if(wall <= (h-1-y)*w + (w-1-x)){
                    string t = normalize(s, 'Z', x==0);
                    if(t != "")
                        next[make_pair(t, wall)] += it->second;
                }

                if(wall > 0 && !(y == 0 && x == 0) && !(y == h-1 && x == w-1)){
                    string t = normalize(s, '#', x==0);
                    if(t != "")
                        next[make_pair(t, wall-1)] += it->second;
                }
            }
            dp.swap(next);
        }
    }

    long long ret = 0;
    for(map<pair<string, int>, long long>::iterator it=dp.begin(); it!=dp.end(); ++it){
        string s = it->first.first;
        int wall = it->first.second;
        if(s.find('B') == string::npos)
            ret += it->second;
    }
    cout << ret << endl;

    return 0;
}