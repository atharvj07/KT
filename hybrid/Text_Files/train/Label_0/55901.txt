import java.util.*;

public class Main {

    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int k = sc.nextInt();

    public static void main(String[] args) {

        new Main().run();

    }

    void run() {
        int[] friendNum = new int[n];
        int[] blockNum = new int[n];

        UnionFind u = new UnionFind(n);

        for (int i=0; i<m; i++) {
            int a = sc.nextInt()-1;
            int b = sc.nextInt()-1;
            u.unite(a, b);
            friendNum[a]++;
            friendNum[b]++;
        }

        for (int i=0; i<k; i++) {
            int a = sc.nextInt()-1;
            int b = sc.nextInt()-1;

            if (u.same(a, b)) {
                blockNum[a]++;
                blockNum[b]++;
            }
        }

        sc.close();

        StringBuilder sb = new StringBuilder();

        for (int i=0; i<n; i++) {
            int ans = u.size(i)-friendNum[i]-blockNum[i]-1;
            sb.append(ans+" ");
        }

        System.out.println(sb.toString());
    }

    class UnionFind {

        int[] parents, sizes;

        UnionFind(int n) {
            parents = new int[n];
            sizes = new int[n];
            for (int i=0; i<n; i++) {
                parents[i] = i;
                sizes[i] = 1;
            }
        }

        public int find(int x) {
            if (x==parents[x]) return x;
            return parents[x] = find(parents[x]);
        }

        public void unite(int x, int y) {
            x = find(x);
            y = find(y);
            if (x==y) return;
            if (sizes[x] < sizes[y]) {
                int tmp = x;
                x = y;
                y = tmp;
            }
            parents[y] = x;
            sizes[x] += sizes[y];
        }

        public boolean same(int x, int y) {
            return find(x) == find(y);
        }

        public int size(int x) {
            return sizes[find(x)];
        }

    }
}
