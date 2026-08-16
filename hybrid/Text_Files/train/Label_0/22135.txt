#include <iostream>
#include <algorithm>
#include <queue>
#include <string>

using namespace std;

bool check(int turn, string str, int player)
{
  if(turn%3 == 0 && turn%5 == 0){
    return str == "FizzBuzz";
  } else if(turn%3 == 0){
    return str == "Fizz";
  } else if(turn%5 == 0){
    return str == "Buzz";
  }

  return atoi(str.c_str()) == turn;
}

int main()
{
  int n, m;
  string str;

  while(cin>>m>>n && n+m){
    queue<int> players;

    for(int i = 1; i <= m; ++i)
      players.push(i);

    for(int i = 1; i <= n; ++i){
      cin >> str;
      if(players.size() == 1) continue;

      int player = players.front();
      players.pop();

      if(check(i, str, player)){
	players.push(player);
      }
    }

    vector<int> vec;
    while(!players.empty()){
      vec.push_back(players.front());
      players.pop();
    }
    sort(vec.begin(), vec.end());

    for(int i = 0; i < vec.size()-1; ++i)
      cout << vec[i] << " ";
    cout << vec.back() << endl;
  }

  return 0;
}