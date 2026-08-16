import java.io.*;
import java.util.*;

public class Main implements Runnable {

    private void solve() throws IOException {

        int N = nextInt();
        long[] arr = new long[N];
        for(int i = 0; i < N; ++i) {
            arr[i] = nextLong();
        }

        UF uf = new UF(N);

        Arrays.sort(arr);

        long[] pref = new long[N + 1];
        for(int i = 1; i <= N; ++i) {
            pref[i] = arr[i-1];
            pref[i] += pref[i-1];
        }

        for(int i = N - 1; i >= 0; --i) {
            if(arr[i] * 2 >= arr[N-1]) {
                uf.union(i, N - 1);
            } else {
                if(i + 1 < N) {
                    if(2*arr[i] >= arr[i+1]) {
                        uf.union(i, i + 1);
                    }
                }
                long buff = pref[i];
                long stronger = arr[i] + buff;
                if(i + 1 < N) {
                    if(2*stronger >= arr[i+1]) {
                        uf.union(i, i + 1);
                    }
                    if(2 * stronger >= arr[N-1]) {
                        uf.union(i, N - 1);
                    }
                }
            }
        }
        int root = uf.getRoot(N - 1);
        int ans = 0;
        for(int i = 0; i < N; ++i) {
            if(root == uf.getRoot(i)) ++ans;
        }
        writer.println(ans);

    }

    static class UF {
        int[] elem;
        int[] rank;
        int N;

        public UF(int N) {
            this.N = N;
            elem = new int[N];
            rank = new int[N];

            for(int i = 0; i < N; ++i) {
                elem[i] = i;
                rank[i] = 1;
            }
        }

        public int getRoot(int x) {
            if(x == elem[x]) return x;
            else return elem[x] = getRoot(elem[x]);
        }

        public void union(int x,int y) {
            int xRoot = getRoot(x);
            int yRoot = getRoot(y);
            if(xRoot == yRoot) return;

            if(rank[xRoot] > rank[yRoot]) {
                rank[xRoot] += rank[yRoot];
                elem[yRoot] = xRoot;
            } else {
                rank[yRoot] += rank[xRoot];
                elem[xRoot] = yRoot;
            }
        }
    }

    public static void main(String[] args) {
        new Main().run();
    }

    BufferedReader reader;
    //    BufferedReader reader2;
    StringTokenizer tokenizer;
    PrintWriter writer;
    //    BufferedWriter writer;

    public void run() {
        try {
            reader = new BufferedReader(new InputStreamReader(System.in));
//            reader = new BufferedReader(new FileReader("highcard.in"));
            //            reader2 = new BufferedReader(new FileReader("1.in"));
            tokenizer = null;
            writer = new PrintWriter(System.out);
//            writer = new     PrintWriter("output.txt");
//                                                    writer = new BufferedWriter(System.out);
            //                        writer = new BufferedWriter(new OutputStreamWriter(System.out));
            solve();
            reader.close();
            //            reader2.close();
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

    short nextShort() throws IOException {
        return Short.parseShort(nextToken());
    }

    String nextToken() throws IOException {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(reader.readLine());
        }

        return tokenizer.nextToken();
    }

}