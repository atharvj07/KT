import java.io.*;
import java.util.*;

import static java.lang.Math.max;


public class Main {
    BufferedReader br;
    StringTokenizer in;
    PrintWriter pw;
    Random r;
    int INF = (int) (2 * 1e9) + 1;
    long LNF = (long) 1e18;
    long mod = (long) (1e9 + 7);
    int pp = 27;
    // you shall not hack!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    //        /*\
    //       ///          /^\
    //      ///    ~~~~  (___)
    //     ///   ~~~~~~~~  \\__
    //   _/_/_  ~/ .& . \~  \\ \
    //  [____] ~|  (__)  |~/ \\/
    //  /_/\  \~|~~~~~~~~~~  /\\
    //      \   ~~~~~~~~~~ _/ \\
    //       \ _    ~~   _/\   \\
    //      /  |        /   \   \\
    //     |  /        |     \   \\
    //    /  /   ___   |      \
    //   /___|  | __|  |_______\
    //      _|  |   |  |_
    //     |____|   |____|
    //       P.S this is omnipotent Gandalf

    int n;

    class node {
        road a;
        int prior;
        node L;
        node R;

        public node(road aa) {
            a = aa;
            prior = r.nextInt();
            L = null;
            R = null;
        }
    }

    node merge(node a, node b) {
        if (a == null) return b;
        if (b == null) return a;
        if (a.prior > b.prior) {
            a.R = merge(a.R, b);
            return a;
        } else {
            b.L = merge(a, b.L);
            return b;
        }
    }

    pairn split(node c, long bb) {
        if (c == null) return new pairn(null, null);
        if (c.a.t >= bb) {
            pairn p = split(c.L, bb);
            c.L = p.s;
            return new pairn(p.f, c);
        } else {
            pairn p = split(c.R, bb);
            c.R = p.f;
            return new pairn(c, p.s);
        }
    }

    class pairn {
        node f;
        node s;

        public pairn(node ff, node ss) {
            f = ff;
            s = ss;
        }
    }

    ArrayList<road> foreach2(node c) {
        if (c == null) return new ArrayList<>();
        ArrayList<road> l = new ArrayList<>();
        if (c.L != null) l = foreach2(c.L);
        ArrayList<road> r = new ArrayList<>();
        if (c.R != null) r = foreach2(c.R);
        l.add(c.a);
        for (int i = 0; i < r.size(); i++) {
            l.add(r.get(i));
        }
        return l;
    }


    void solve() throws IOException {
        int n = nextInt();
        int m = nextInt();
        int d = nextInt();
        pair f[] = new pair[n];
        pair inf[] = new pair[m];
        pair prefsum[] = new pair[m];
        for (int i = 0; i < n; i++) {
            f[i] = new pair(nextInt(), nextInt());
        }
        for (int i = 0; i < m; i++) {
            inf[i] = new pair(nextInt(), nextInt());
        }
        Arrays.sort(f);
        Arrays.sort(inf);
        for (int i = 0; i < m; i++) {
            if (i > 0) prefsum[i] = new pair(prefsum[i - 1], inf[i]);
            else prefsum[i] = inf[i];
        }
        long ans = 0;
        long sumc = 0;
        long sumw = 0;
        for (int i = 0; i < n; i++) {
            sumc += f[i].c;
            sumw += f[i].w;
            if (sumw > d) break;
            int l = -1;
            int r = m;
            while (l + 1 != r) {
                int mid = (l + r) / 2;
                if (sumw + prefsum[mid].w > d) r = mid;
                else l = mid;
            }
            if (l == -1) break;
            long curans = sumc + prefsum[l].c;
            if (sumw + prefsum[l].w <= d) ans = max(ans, curans);
        }
        pw.print(ans);

    }


    class road {
        int to;
        int t;

        public road(int toto, int tt) {
            to = toto;
            t = tt;
        }
    }
//***************************************

    class pair implements Comparable<pair> {
        long c;
        long w;

        public pair(long ll, long rr) {
            c = ll;
            w = rr;
        }

        public pair(pair a, pair b) {
            c = a.c + b.c;
            w = a.w + b.w;
        }


        @Override
        public int compareTo(pair o) {
            if (c != o.c) return Long.compare(o.c, c);
            return Long.compare(w, o.w);
        }
    }

    String nextToken() throws IOException {
        while (in == null || !in.hasMoreTokens()) {
            in = new StringTokenizer(br.readLine());
        }
        return in.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    public void gener() throws IOException {
        pw = new PrintWriter(new FileWriter("input.txt"));
        int n = r.nextInt(5) + 2;
    }

    public void run() throws IOException {
        r = new Random(5);
//        for (int i = 0; i < 100; i++) {
//            gener();
        br = new BufferedReader(new InputStreamReader(System.in));
        pw = new PrintWriter(new OutputStreamWriter(System.out));
//        br = new BufferedReader(new FileReader("input.txt"));
//        pw = new PrintWriter(new FileWriter("output.txt"));
//        br = new BufferedReader(new FileReader("pixels.in"));
//        pw = new PrintWriter(new FileWriter("pixels.out"));
        solve();
//        pw.print(a);
        pw.close();
//            int b = solve2();
//            if (a != b) break;
//            pw.close();
//        }
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }
}