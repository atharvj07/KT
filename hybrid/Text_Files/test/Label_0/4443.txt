#include <bits/stdc++.h>
using namespace std;


bool is_contain(string T, string s) {
    int idx = 0;
    for (int i = 0; i < T.size() && idx < s.size(); i++) {
        if (T[i] == s[idx]) {
            idx++;
        }
    }
    return (idx == s.size());
}

int main() {
    string S, T; cin >> S >> T;
    string s1, s2;
    for (int i = 0; i < S.size(); i += 2) s1 += S[i];
    for (int i = 1; i < S.size(); i += 2) s2 += S[i];
    
    if (is_contain(T, s1) || is_contain(T, s2)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return (0);
}

