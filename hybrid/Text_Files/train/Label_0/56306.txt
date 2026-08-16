/*
 * Main.java: 1022: Indian Puzzle
 */

import java.util.*;

public class Main {
  // constant

  static int Error = Integer.MIN_VALUE;

  // inner classes

  static class Box {
    int id;
    char val;

    Box(int id, char val) { this.id = id; this.val = val; }
    char get() { return val; }
    void set(char v) { val = v; }
  }

  // global variables

  static int n;
  static int pos = 0;

  static HashMap<ArrayList<Box>, Integer> expcache;
  static HashMap<ArrayList<Box>, Boolean> eqncache;
  static ArrayList<ArrayList<ArrayList<Box>>> eqnbls;

  static Box[] mtx, blanks;
  static char[] cands;

  static boolean[] used;

  // subroutines

  static int parse_num(ArrayList<Box> exp) {
    if (pos >= exp.size()) return Error;
    if (exp.get(pos).get() == '0') {
      pos++;
      return 0;
    }

    int val = 0;
    boolean exist = false;

    while (pos < exp.size()) {
      char ch = exp.get(pos).get();
      if (ch < '0' ||  ch > '9') break;
      val = 10 * val + (ch - '0');
      pos++;
      exist = true;
    }

    return (exist ? val : Error);
  }

  static int parse_md(ArrayList<Box> exp) {
    int val = parse_num(exp);
    if (val == Error) return Error;

    while (pos < exp.size()) {
      char ch = exp.get(pos).get();
      if (ch != '*' && ch != '/') break;
      pos++;

      int val0 = parse_num(exp);
      if (val0 == Error) return Error;

      if (ch == '*')
        val *= val0;
      else {
        if (val0 == 0 || val % val0 != 0) return Error;
        val /= val0;
      }
    }

    return val;
  }

  static int parse_exp(ArrayList<Box> exp) {
    int val = parse_md(exp);
    if (val == Error) return Error;

    while (pos < exp.size()) {
      char ch = exp.get(pos).get();
      if (ch != '+' && ch != '-') break;
      pos++;

      int val0 = parse_md(exp);
      if (val0 == Error) return Error;

      if (ch == '+')
        val += val0;
      else
        val -= val0;
    }

    return val;
  }

  static int eval_exp(ArrayList<Box> exp) {
    //if (expcache.containsKey(exp)) return expcache.get(exp);

    int val = parse_exp(exp);
    if (pos < exp.size() && exp.get(pos).get() != '=') val = Error;

    //expcache.put(exp, val);
    return val;
  }

  static boolean is_valid_eqn(ArrayList<Box> eqn) {
    //if (eqncache.containsKey(eqn)) return eqncache.get(eqn);

    int eqnum = 0;
    for (Box box: eqn)
      if (box.get() == '=') eqnum++;
    if (eqnum != 1) {
      //eqncache.put(eqn, false);
      return false;
    }

    boolean ok = false;
    pos = 0;

    int val0 = eval_exp(eqn);
    if (val0 != Error) {
      pos++;
      int val1 = eval_exp(eqn);
      if (val1 != Error && val0 == val1) ok = true;
    }

    //eqncache.put(eqn, ok);
    return ok;
  }

  static boolean check_rec(int k) {
    if (k >= n) return true;

    for (int d = 0; d < n; d++) {
      if (used[d]) continue;

      used[d] = true;
      blanks[k].set(cands[d]);
      boolean ok = true;

      for (ArrayList<Box> eqn: eqnbls.get(k)) {
        ok = is_valid_eqn(eqn);
        if (! ok) break;
      }

      if (ok)
        ok = check_rec(k + 1);

      used[d] = false;

      if (ok) return true;
    }

    return false;
  }


  // main
  public static final void main(String[] args) throws Exception {
    Scanner sc = new Scanner(System.in);

    for (;;) {
      int h = sc.nextInt();
      int w = sc.nextInt();
      if (h == 0 && w == 0) break;

      mtx = new Box[h * w];

      for (int y = 0; y < h; y++) {
        String line = sc.next();
        for (int x = 0; x < w; x++) {
          int id = y * w + x;
          mtx[id] = new Box(id, line.charAt(x));
        }
      }

      ArrayList<ArrayList<Box>> eqns = new ArrayList<ArrayList<Box>>();

      for (int y = 0; y < h; y++) {
        int x = 0;
        while (x < w) {
          int x0 = x;
          ArrayList<Box> eqn = new ArrayList<Box>();

          while (x0 < w) {
            Box b = mtx[y * w + x0];
            if (b.get() == '#') break;
            eqn.add(b);
            x0++;
          }

          if (eqn.size() > 1) eqns.add(eqn);
          x = x0 + 1;
        }
      }

      for (int x = 0; x < w; x++) {
        int y = 0;
        while (y < h) {
          int y0 = y;
          ArrayList<Box> eqn = new ArrayList<Box>();

          while (y0 < h) {
            Box b = mtx[y0 * w + x];
            if (b.get() == '#') break;
            eqn.add(b);
            y0++;
          }

          if (eqn.size() > 1) eqns.add(eqn);
          y = y0 + 1;
        }
      }

      n = sc.nextInt();

      blanks = new Box[n];
      int kb = 0;
      for (Box box: mtx)
        if (box.get() == '.') blanks[kb++] = box;

      cands = new char[n];
      for (int i = 0; i < n; i++) {
        String str = sc.next();
        cands[i] = str.charAt(0);
      }

      eqnbls = new ArrayList<ArrayList<ArrayList<Box>>>();
      for (int i = 0; i < n; i++)
        eqnbls.add(new ArrayList<ArrayList<Box>>());

      for (int i = 0; i < eqns.size(); i++) {
        ArrayList<Box> eqn = eqns.get(i);

        Box blb = null;
        for (int j = eqn.size() - 1; j >= 0; j--) {
          blb = eqn.get(j);
          if (blb.get() == '.') break;
        }

        if (blb != null)
          for (int k = 0; k < n; k++)
            if (blb == blanks[k]) {
              eqnbls.get(k).add(eqn);
              break;
            }
      }

      used = new boolean[n];
      Arrays.fill(used, false);

      //expcache = new HashMap<ArrayList<Box>, Integer>();
      //eqncache = new HashMap<ArrayList<Box>, Boolean>();

      boolean ok = check_rec(0);

      System.out.println(ok ? "Yes" : "No");
    }
  }
}