import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;
import java.util.ArrayList;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        E solver = new E();
        solver.solve(1, in, out);
        out.close();
    }

    static class E {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            Set<Integer>[] e = new Set[n];
            for (int i = 0; i < n; i++) {
                e[i] = new HashSet<>();
            }

            for (int i = 0; i < n - 1; i++) {
                int a = in.nextInt();
                int b = in.nextInt();
                e[a].add(b);
                e[b].add(a);
            }

            ArrayList<Integer> deg2 = new ArrayList<>();
            ArrayList<Integer> deg1 = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (e[i].size() == 1) {
                    deg1.add(i);
                }
                if (e[i].size() == 2) {
                    deg2.add(i);
                }
            }

            for (int i = 0; i < deg2.size(); i++) {
                int x = deg2.get(i);
                int y = e[x].iterator().next();
                e[x].remove(y);
                int z = e[x].iterator().next();
                e[x].remove(z);
                e[y].remove(x);
                e[z].remove(x);
                e[y].add(z);
                e[z].add(y);
            }

            if (n == 2 + deg2.size()) {
                out.println(1);
                return;
            }

            int[] neiL = new int[n];
            for (int i = 0; i < n; i++) {
                if (e[i].size() == 0) {
                    continue;
                }
                if (e[i].size() == 1) {
                    int x = e[i].iterator().next();
                    neiL[x] += 1;
                }
            }

            int ans = 0;
            for (int i = 0; i < n; i++) {
                if (neiL[i] > 0) {
                    ans += neiL[i] - 1;
                }
            }
            out.println(ans);

        }

    }
}

