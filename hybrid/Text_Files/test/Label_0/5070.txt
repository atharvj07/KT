#include <algorithm>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cassert>
#include <set>
#include <cstring>

using namespace std;

typedef long long ll;

#define SIZE 100010
#define INF 1000000000
#define mod 1000000007

ll dp[2010][2010];
int posl[26][SIZE], posr[26][SIZE];

int main(){
  char s[2010];
  int n;
  set<int> ss[26], ss_b[26];

  
  
  scanf("%s", s);
  n = strlen(s);

  for(int i=0;i<26;i++){
    for(int j=0;j<=n;j++){
      posl[i][j] = INF;
      posr[i][j] = -INF;
    }
  }
  
  for(int i=0;i<n;i++){
    ss[s[i]-'a'].insert(i);
    ss_b[s[i]-'a'].insert(-i);
    //vec[s[i]-'a'].push_back(i);
    posl[s[i]-'a'][i] = i;
    posr[s[i]-'a'][i] = i;
  }

  for(int k=0;k<26;k++){
    for(int i=0;i<n;i++) posr[k][i+1] = max(posr[k][i], posr[k][i+1]);
    for(int i=n;i>0;i--) posl[k][i-1] = min(posl[k][i], posl[k][i-1]);
  }
  
  for(int i=0;i<26;i++){
    ss[i].insert(INF);
    ss_b[i].insert(INF);
  }

  for(int i=0;i<26;i++){
    int a = *ss[i].begin();
    int b = -*ss_b[i].begin();

    //cerr << a << " " << b << endl;
    
    if(a != b && a != INF && b != -INF){
      dp[a][b]++;
    }
  }

  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      for(int k=0;k<26;k++){
        int nextl = posl[k][i+1]; //*ss[k].lower_bound(i+1);
        int nextr = posr[k][j-1]; //-*ss_b[k].lower_bound(-(j-1));

        //if(i == 0 && j == 6) cerr << " > " << nextl << " " << nextr << endl;
        
        if(nextl < nextr){
          dp[nextl][nextr] = (dp[nextl][nextr] + dp[i][j])%mod;
        }
      }      
    }
  }

  ll ans = 0;
  
  for(int i=0;i<26;i++){
    ans += ss[i].size() >= 2;
  }

  //cerr << ans << endl;
  
  for(int i=0;i<n;i++){
    for(int j=i;j<n;j++){
      //if(dp[i][j]) cerr << i << " " << j << " " << dp[i][j] << endl; 
      ans = (ans + dp[i][j])%mod;

      for(int k=0;k<26;k++){
        if(posl[k][i+1] < j){
          ans = (ans + dp[i][j])%mod;
        }
      }
    }
  }

  printf("%lld\n", ans%mod);
  return 0;
}
 

