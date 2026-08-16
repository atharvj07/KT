#include <cstdio>
#include <cstdint>
#include <cassert>
#include <cctype>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <stdexcept>

struct Dimension: std::vector<int> {
  Dimension(size_t n=0): std::vector<int>(n) {}
  Dimension &operator +=(const Dimension &oth) {
    if (*this != oth) throw std::logic_error("mismatch");
    return *this;
  }
  Dimension &operator -=(const Dimension &oth) {
    if (*this != oth) throw std::logic_error("mismatch");
    return *this;
  }
  Dimension &operator *=(const Dimension &oth) {
    for (size_t i=0; i<size(); ++i)
      (*this)[i] += oth[i];

    return *this;
  }
  Dimension &operator /=(const Dimension &oth) {
    for (size_t i=0; i<size(); ++i)
      (*this)[i] -= oth[i];

    return *this;
  }
};

Dimension parse(
    const std::string &s, size_t &i,
    const std::map<std::string, Dimension> expr, size_t preced=0) {

  const std::vector<std::string> ops={"+-", "*/"};

  if (preced == ops.size()) {
    if (s[i] == '(') {
      Dimension res=parse(s, ++i, expr, 0);
      assert(s[i] == ')');
      ++i;
      return res;
    }
    if (isalpha(s[i])) {
      std::string name(1, s[i]);
      while (++i < s.length() && isalpha(s[i]))
        name += s[i];

      return expr.at(name);
    }
    assert(false);
  }

  Dimension lhs=parse(s, i, expr, preced+1);
  while (i < s.length()) {
    char op=s[i];
    if (!std::count(ops[preced].begin(), ops[preced].end(), op)) break;
    Dimension rhs=parse(s, ++i, expr, preced+1);
    if (op == '+') lhs += rhs;
    if (op == '-') lhs -= rhs;
    if (op == '*') lhs *= rhs;
    if (op == '/') lhs /= rhs;
  }
  return lhs;
}

int testcase_ends() {
  size_t n, m, p;
  scanf("%zu %zu %zu", &n, &m, &p);
  if (n == 0 && m == 0 && p == 0) return 1;

  std::map<std::string, Dimension> stod;
  std::map<Dimension, std::string> dtos;
  for (size_t i=0; i<m; ++i) {
    char buf[32];
    scanf("%s", buf);
    std::string s=buf;
    Dimension d(n);
    for (size_t j=0; j<n; ++j)
      scanf("%d", &d[j]);

    stod[s] = d;
    dtos[d] = s;
  }

  std::string s;
  {
    char buf[128];
    scanf("%s", buf);
    s = buf;
  }

  std::map<std::string, Dimension> expr;
  for (size_t i=0; i<p; ++i) {
    char buf[128];
    scanf("%s", buf);
    std::string lhs=buf;
    scanf("%s", buf);
    std::string rhs=buf;
    expr[lhs] = stod[rhs];
  }

  size_t i=0;
  try {
    Dimension res=parse(s, i, expr);
    printf("%s\n", dtos.at(res).c_str());
  } catch (std::out_of_range &e) {
    printf("undefined\n");
  } catch (std::logic_error &e) {
    printf("error\n");
  }

  return 0;
}
  
int main() {
  while (!testcase_ends()) {}
}

