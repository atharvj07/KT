#include<bits/stdc++.h>


using namespace std;

int dp[200][101];
int d, n, days[200], ans = 0;
struct cloth{
  int a, b, c;
};
cloth clothes[200];

int dfs(int day, int point){
  if(day == d)
    return 0;
  if(~dp[day][point])
    return dp[day][point];
  int res = 0;
  for(int i = 0; i < n; i++){
    if(clothes[i].a <= days[day] && days[day] <= clothes[i].b){
      res = max(res, abs(point - clothes[i].c)+ dfs(day + 1, clothes[i].c));
    }
  }
  return dp[day][point] = res;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(0);
  cin >> d >> n;
  for(int i = 0; i < d; i++){
    cin >> days[i];
  }
  for(int i = 0; i < n; i++){
    cin >> clothes[i].a >> clothes[i].b >> clothes[i].c;
  }
  memset(dp, -1, sizeof(dp));
  for(int i = 0; i < n; i++){
    if(clothes[i].a <= days[0] && days[0] <= clothes[i].b){
      ans = max(ans, dfs(1, clothes[i].c));
    }
  }
  cout << ans << "\n";
}