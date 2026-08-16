/**
 * Created by Aminul on 2/18/21.
 */

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;

import static java.lang.Math.min;

public class CF1487E_Set {
    public static void main(String[] args) throws Exception {
        FastReader in = new FastReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int[] sizes = new int[4];
        int[][] costs = new int[4][];

        for (int i = 0; i < 4; i++) {
            sizes[i] = in.nextInt();
            costs[i] = new int[sizes[i]];
        }

        for (int i = 0; i < 4; i++) {
            int n = sizes[i];
            for (int j = 0; j < n; j++) {
                costs[i][j] = in.nextInt();
            }
        }

        HashSet<Integer> graph[][] = new HashSet[3][];
        for (int i = 0; i < graph.length; i++) {
            graph[i] = new HashSet[sizes[i]];
            for (int j = 0; j < graph[i].length; j++) {
                graph[i][j] = new HashSet<>();
            }
        }

        for (int i = 0; i < 3; i++) {
            int m = in.nextInt();
            for (int j = 0; j < m; j++) {
                int from = in.nextInt(), to = in.nextInt();
                graph[i][from - 1].add(to - 1);
            }
        }

        int inf = (int) 1e9;
        Comparator<int[]> comparator = (x, y) -> x[0] == y[0] ? Integer.compare(x[1], y[1]) : Integer.compare(x[0], y[0]);
        TreeSet<int[]> set = null;

        for (int i = 3; i >= 0; i--) {
            int n = sizes[i];

            if (i < 3) {
                for (int j = 0; j < n; j++) {
                    int minCost = inf;
                    for (int[] pair : set) {
                        if (!graph[i][j].contains(pair[1])) {
                            minCost = pair[0];
                            break;
                        }
                    }
                    costs[i][j] += minCost;
                }
            }
            set = new TreeSet<>(comparator);
            for (int j = 0; j < n; j++) {
                set.add(new int[]{min(costs[i][j], inf), j});
            }

        }

        int res = set.first()[0];
        if (res >= inf) {
            res = -1;
        }

        pw.println(res);
        pw.close();
    }


    static void debug(Object... obj) {
        System.err.println(Arrays.deepToString(obj));
    }

    static class FastReader {
        InputStream is;
        private byte[] inbuf = new byte[1024];
        private int lenbuf = 0, ptrbuf = 0;

        public FastReader(InputStream is) {
            this.is = is;
        }

        public int readByte() {
            if (lenbuf == -1) throw new InputMismatchException();
            if (ptrbuf >= lenbuf) {
                ptrbuf = 0;
                try {
                    lenbuf = is.read(inbuf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (lenbuf <= 0) return -1;
            }
            return inbuf[ptrbuf++];
        }

        public int nextInt() {
            int num = 0, b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }
            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + (b - '0');
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }
    }
}