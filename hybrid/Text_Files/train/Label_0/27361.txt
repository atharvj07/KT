#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;
typedef pair<string, int> psi;

void print(vector<vector<psi>> &sl, int fst = 0, int depth = 0) {
    REP (i, 0, sl[fst].size()) {
        REP (j, 0, depth) cout << '.';
        cout << sl[fst][i].first << endl;
        print(sl, sl[fst][i].second, depth + 1);
    }
}

int main () {
    int n;
    cin >> n;
    vector<vector<psi>> slist(n + 1);
    REP (i, 0, n) {
        int k;
        string s;
        cin >> k >> s;
        slist[k].push_back({s, i + 1});
    }
    print(slist);
    return 0;
}