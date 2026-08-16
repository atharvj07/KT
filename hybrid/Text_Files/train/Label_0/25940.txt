/*
    Mbak Sana Dong
    Mbak Chaeyoung Dong
    Mbak Eunha Dong
    Mbak Seulgi Dong
    Mbak Wendy Dong
    Stream https://www.youtube.com/watch?v=LmBYPXGqtss
*/
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization ("unroll-loops,O3")
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    int n,m,i,j,k,x,y,ans,curr,temp,q;
    int tc;
    cin >> tc;
    while(tc--) {
        string s;
        cin >> s;
        n = s.length();
        s = " " + s;
        vector<int> cnt(30, 0), vis(30, 0);
        for(i=1;i<=n;i++) {
            cnt[s[i] - 'a']++;
        }

        stack<char> st;

        for(i=1;i<=n;i++) {
            curr = s[i] - 'a';
            if(vis[curr]) {
                cnt[curr]--;
                continue;
            }

            while(!st.empty() && cnt[st.top() - 'a'] > 0 && st.top() < s[i]) {
                vis[st.top() - 'a'] = 0;
                st.pop();
            }

            st.push(s[i]);
            cnt[curr]--;
            vis[curr] = 1;
        }

        string eunha = "";
        while(!st.empty()) {
            eunha += st.top();
            st.pop();
        }

        reverse(eunha.begin(), eunha.end());
        cout << eunha << endl;
    }
    return 0;
}
