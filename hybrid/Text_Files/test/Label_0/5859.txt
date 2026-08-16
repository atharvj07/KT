#include<bits/stdc++.h>
using namespace std;

struct state{
  int fc,kc,wc,fb;
  state(int fc,int kc,int wc,int fb):
    fc(fc), kc(kc), wc(wc), fb(fb) {}
  state(){
    fb = -1;
  }
  bool operator==(const state &st ) const{
    if( fc == st.fc &&
        kc == st.kc &&
        wc == st.wc &&
        fb == st.fb ) return true;
    return false;
  }
  void view(){
    cout << "result: " << endl;
    cout << "F: " << fc <<endl;
    cout << "K: " << kc <<endl;
    cout << "W: " << wc <<endl;
    cout << "action: " << fb << endl;
  }
};

typedef pair<state,state> P;

state better( const state& a, const state& b,int p, bool kf ){  
  if( a.fb < 0 ) return b;
  if( p == 0 ){//turn flog
    if( a.fc != b.fc )
      return a.fc > b.fc ? a : b;
  } else if( p == 1 ){//turn kappa
    if( kf ){ // kappa-seeing
      if( a.fc != b.fc )
        return a.fc < b.fc ? a : b;
    } else {
      // kaeru-seeing
      if( a.kc != b.kc )
        return a.kc > b.kc ? a : b;
    }
  } else {//turn weasel
    if( a.wc != b.wc )
      return a.wc > b.wc ? a : b;
  }
  return a.fb < b.fb ? a : b;
}

int X[13],Y[7];

int cut(int st,int y ){
  int cnt = 0;
  for(int i=0;i<12;i++){
    if( st & (1<<i) ) continue;
    if( cnt == y ) return  st|(1<<i);
    cnt++;
  }
  return -1;
}

int check( int st ){
  for(int i=0;i<12;i++){
    if( st & (1<<i) ) continue;
    return st | (1<<i);   
  }
  return -1;
}

void calc( state& ret,int st,int t,int uc){
  int cnt = 0;
  for(int i=0;i<12;i++){
    if( st & (1<<i) ) continue;
    if( uc==-1 || cnt == uc ) {
      if( t == 0 ) ret.fc+=X[i];
      else if( t == 1 ) ret.kc+=X[i];
      else ret.wc+=X[i];
      break;
    }
    cnt++;
  }
  ret.fb = uc+1;
}

void calc( P& ret, int st, int t, int uc ){
  calc( ret.first, st, t, uc );
  calc( ret.second, st, t, uc );
}

P dp[3][(1<<6)][(1<<12)];

P better( const P& a, const P& b,int t){
  P ret;
  if( t == 1 ){ // Kappa
    ret.first = better(a.first, b.first, t, true );
    ret.second= better(a.second,b.second,t, false );
  } else { // Flog or Weasel
    if( a.second == better(a.second,b.second,t, false ) )
      ret = a;
    else
      ret = b;
  }
  return ret;
}

P solve(int t,int yst,int xst ){// first : Kappa,  second : Flog
  if( dp[t][yst][xst].first.fb >= 0 ) return dp[t][yst][xst];
  P ret;
  if( xst == (1<<12)-1 ) return dp[t][yst][xst] = P( state(0,0,0,0), state(0,0,0,0) );
  
  P tmp = solve( (t+1)%3, yst, check(xst) );
  calc( tmp, xst, t, -1 );
  ret = tmp;
  //ret = better( ret, tmp, t );
  //view()
  if( 0 ) {
    cout << t << " "<< bitset<6>(yst) << " " << bitset<12>(xst) << endl;
    ret.first.view();
    ret.second.view();
  }
  
  
  for(int i=t*2;i<t*2+2;i++){
    if( yst & (1<<i) ) continue;
    int next = cut( xst, Y[i] );
    P tmp;
    if( next == -1 ) continue;
    tmp = solve((t+1)%3, yst|(1<<i), next );
    calc( tmp, xst, t, Y[i] );          
    ret = better( ret, tmp, t );
  }
  //view()
  if( 0 ){
    cout << t << " "<< bitset<6>(yst) << " " << bitset<12>(xst) << endl;
    ret.first.view();
    ret.second.view();
  }
  return dp[t][yst][xst] = ret;
}

int main(){
  for(int i=11;i>-1;i--) cin >> X[i];
  for(int i=0;i<6;i++) {
    cin >> Y[i]; Y[i]--;
  }
  P res = solve(0,0,0);
  cout << res.first.fc << " " << res.first.kc << " "<< res.first.wc << endl;
}