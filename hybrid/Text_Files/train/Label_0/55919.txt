import java.io.*;
import java.util.*;


public class ProblemD { 
    InputReader in; PrintWriter out;
    class FenwickTree {
        List<Long> tree;
        int n;
        FenwickTree(int len) {
            tree = new ArrayList<Long>(len);
            for (int i = 0; i < len; i++)
                tree.add(0L);
            n = len;
        }
        void inc(int pos, Long el) {
            for (int i = pos; i < n; i = (i | (i + 1)))
                tree.set(i, tree.get(i) + el);
        }
        Long sum (int r) {
            Long result = 0L;
            for (int j = r; j >= 0; j = (j & (j + 1)) - 1)
                result = result + tree.get(j);
            return result;
        }
        Long sum(int l, int r) {
            return sum(r) - sum(l - 1);
        }
    }
    long[][] zg = new long[12][7];
    Long zig(int i, int z) {
        i++;
        int mod = i % (2 * (z - 1));
        if (mod == 0)
            return 2L;
        else if (mod <= z)
            return (long)mod;
        else 
            return (long)2 * z - mod;
    }
    void solve() {
        for (int i = 0; i < 12; i++)
            for (int j = 2; j < 7; j++)
                zg[i][j] = zig(i, j);
        int n = in.nextInt();
        FenwickTree[][] t = new FenwickTree[7][12];
        for (int j = 0; j < 7; j++)
            for (int j2 = 0; j2 < 12; j2++)
                t[j][j2] = new FenwickTree(n + 1);
        for (int i = 0; i < n; i++) {
            long cur = in.nextLong();
            for (int j = 2; j < 7; j++) {
                int j2 = i % (2 * j - 2);
                t[j][j2].inc(i, cur);
            }
        }
        int m = in.nextInt();
        for (int j = 0; j < m; j++) {
            int op = in.nextInt();
            if (op == 2) {
                int left = in.nextInt();
                int right = in.nextInt();
                left--;
                right--;
                int z = in.nextInt();
                long ans = 0;
                for (int z2 = 0; z2 < (2 * z - 2); z2++) {
                    ans += t[z][(z2 + left) % (2 * z - 2)].sum(left, right) * zg[z2][z];
//                  out.println(ans);
                }
                out.println(ans);
            }
            else
            {
                int pos = in.nextInt();
                long zn = in.nextLong();
                pos--;
                for (int z = 2; z < 7; z++) {
                    int z2 = pos % (2 * z - 2);
                    t[z][z2].inc(pos, zn - t[z][z2].sum(pos, pos));
                }
            }
        }
    }
    ProblemD(){
        boolean oj = System.getProperty("ONLINE_JUDGE") != null;
        try {
            if (oj) {
                in = new InputReader(System.in);
                out = new PrintWriter(System.out);
            }
            else {
                Writer w = new FileWriter("output.txt");
                in = new InputReader(new FileReader("input.txt"));
                out = new PrintWriter(w);
            }
        } catch(Exception e) {
            throw new RuntimeException(e);
        }
        solve();
        out.close();
    }
    public static void main(String[] args){
        new ProblemD();
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
        tokenizer = null;
    }
    
    public InputReader(FileReader fr) {
        reader = new BufferedReader(fr);
        tokenizer = null;
    }

    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }
    public int nextInt() {
        return Integer.parseInt(next());
    }
    public long nextLong() {
        return Long.parseLong(next());
    }
    public double nextDouble() {
        return Double.parseDouble(next());
    }

}