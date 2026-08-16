#include <bits/stdc++.h>
using namespace std;
int getFldsFromLine(char *line, std::vector<char *> &res,
                    const char *sep = " \t\n\v\f\r");
int main(int argc, char **argv) {
  FILE *infile = stdin;
  char *line;
  line = (char *)calloc(1000000, sizeof(char));
  if (line == NULL) {
    fprintf(stderr, "Couldn't allocate space for '%s'\nBye!\n", "line");
    exit(-1);
  };
  std::vector<char *> flds;
  int numFlds, numCases, caseNum = 0;
  fgets(line, 1000000, infile);
  numFlds = getFldsFromLine(line, flds);
  numCases = atoi(flds[0]);
  int n = atoi(flds[0]), m = atoi(flds[1]);
  vector<string> a, b;
  fgets(line, 1000000, infile);
  numFlds = getFldsFromLine(line, flds);
  for (int i = 0; i < n; ++i) a.push_back(string(flds[i]));
  fgets(line, 1000000, infile);
  numFlds = getFldsFromLine(line, flds);
  for (int i = 0; i < m; ++i) b.push_back(string(flds[i]));
  int numQueries, yr;
  cin >> numQueries;
  for (int i = 0; i < numQueries; ++i) {
    cin >> yr;
    --yr;
    int n1 = yr % n, m1 = yr % m;
    cout << a[n1] << b[m1] << endl;
  }
  return (0);
}
int getFldsFromLine(char *line, std::vector<char *> &res, const char *sep) {
  res.clear();
  char *tok = strtok(line, sep);
  while (tok) {
    res.push_back(tok);
    tok = strtok(0, sep);
  }
  return res.size();
}
