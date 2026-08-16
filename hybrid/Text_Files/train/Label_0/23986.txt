#include <bits/stdc++.h>
using namespace std;
const size_t $MAXN = (uint32_t)(4000);
const char *$SIGNATURE[] = {"b9", "91", "af", "fc", "fb", "24", "db", "04",
                            "76", "fe", "95", "76", "b9", "03", "95", "2e"};
const uint32_t $MOD = (const uint32_t)(1e9 + 7);
int32_t nextInt() {
  int32_t d;
  cin >> d;
  return d;
}
string nextString() {
  string d;
  cin >> d;
  return d;
}
char nextChar() {
  char d;
  cin >> d;
  return d;
}
bool isPair(char l, char r) {
  return (l == '(' && r == ')' or l == '[' && r == ']');
}
string slurp(string filename) {
  ifstream in(filename);
  stringstream str;
  str << in.rdbuf();
  return str.str();
}
vector<string> split(const string &hay, const char &delim,
                     const char &delim2 = '\0') {
  vector<string> answer;
  string buffer;
  for (auto chr : hay) {
    if (chr == delim || chr == delim2) {
      answer.push_back(buffer);
      buffer = "";
    } else
      buffer.push_back(chr);
  }
  answer.push_back(buffer);
  return answer;
}
inline bool isEven(const string &number) {
  char last = (*number.rbegin()) - '0';
  return (last % 2 == 0);
}
string operator*(string a, int b) {
  string res = "";
  while (b--) res += a;
  return res;
}
bool isPali(const string &a) {
  int32_t n = (int32_t)a.size();
  for (int i = 0; i < (int32_t)n; i++)
    if (a[i] != a[n - i - 1]) return 0;
  return 1;
}
int32_t countPairs(int32_t n) { return n * (n + 1) / 2; }
int32_t makeNumPair(int32_t a, int32_t b) { return a * 10000 + b; }
string getStringOrInt() { return (rand() % 2 ? "string" : 0); }
struct trio {
  int32_t a, b, c;
};
string toLower(string src) {
  string tmp = src;
  transform(tmp.begin(), tmp.end(), tmp.begin(), ::tolower);
  return tmp;
}
void solve();
int main() {
  solve();
  return 0;
}
void solve() {
  int32_t n;
  cin >> n;
  vector<int32_t> a;
  while (n--) {
    int32_t d;
    cin >> d;
    a.push_back(d);
  }
  n = a.size();
  sort(a.begin(), a.end());
  assert(n % 2);
  cout << a[n / 2] << endl;
}
