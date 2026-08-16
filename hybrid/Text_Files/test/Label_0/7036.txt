#include<iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,n) for(int i=0;i<n;i++)

/* 大文字を小文字に変換 */
char tolower(char c) {return (c + 0x20);}
/* 小文字を大文字に変換 */
char toupr(char c) {return (c - 0x20);}

// if('A'<=s[i] && s[i]<='Z') s[i] += 'a'-'A';

/*
string s = "abcdefg"
s.substr(4) "efg"
s.substr(0,3) "abc"
s.substr(2,4) "cdef"
*/

int binarySearch(vector<int> A, int k, int n){
    int left = 0;
    int right = n;
    while(left < right){
        int mid = (left + right) / 2;
        if(A[mid] == k){
            return 1;
        }else if(A[mid] > k){
            right = mid;
        }else{
            left = mid+1;
        }
    }
    return 0;
}

int main()
{
    int n; cin >> n;
    set<int> S;
    rep(i,n){
        int Ai; cin >> Ai;
        S.insert(Ai);
    }
    int q; cin >> q;
    rep(i,q){
        int k; cin >> k;
        if(S.count(k)) cout << 1 << endl;
        else cout << 0 << endl;
    }
}
