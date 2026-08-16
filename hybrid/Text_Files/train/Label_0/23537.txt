#include <bits/stdc++.h>
#define int long long
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;

int w1, w2, h1, h2, sum;
int hash_a[800][800][13], hash_b[800][13];
int cumo_a[800][800][13], cumo_b[800][13];
char s[800][800],t[800][700];

void make_table(){
  rep(i,h1) rep(j,w1-w2+1) {
    rep(k,w2){
      rep(l,8) hash_a[i][j][(k*8)/64] = hash_a[i][j][(k*8)/64]*2 + ( ((s[i][j+k]>>l)&1)?1:0);
      rep(l,8) cumo_a[i][j][(k*8)/64] = cumo_a[i][j][(k*8)/64]*2 + (s[i][j+k]=='?'?1:0);
    }
  }
  rep(i,h2) {
    rep(j,w2){
      rep(k,8) hash_b[i][(j*8)/64] = hash_b[i][(j*8)/64]*2 + (((t[i][j]>>k)&1)?1:0);
      rep(k,8) cumo_b[i][(j*8)/64] = cumo_b[i][(j*8)/64]*2 + (t[i][j]=='?'?1:0);
    }
  }
}

void count_s(){
  rep(i,h1-h2+1) {
    rep(j,w1-w2+1) {
      rep(k,h2) {
        int p1[13]={} ,p2[13]={} ,flag = 0;
        rep(l,13){
          p1[l] = hash_a[i+k][j][l] ^ hash_b[k][l];
          p2[l] = cumo_a[i+k][j][l] | cumo_b[k][l];
          if( (p1[l] | p2[l]) != p2[l] ) { flag ++; break; }
        }
        if( flag ) break ;
        if( k == h2-1 ) sum++;
      }
    }
  }
}

signed main(){
  cin >> w1 >> h1 >> w2 >> h2;
  rep(i,h1) scanf("%s", s[i]);
  rep(i,h2) scanf("%s", t[i]);
  make_table();
  count_s();
  cout << sum << endl;
}