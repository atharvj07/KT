import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.io.StreamTokenizer;
import java.util.HashMap;
import java.io.IOException;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author lebegio
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        StreamTokenizer in = new StreamTokenizer(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        public StreamTokenizer st;

        public void solve(int testNumber, StreamTokenizer st, PrintWriter out) {
            this.st = st;
            int n = nextInt();
            int m = nextInt();
            int[] vert = new int[n];
//        Pair[] arr = new Pair[m];
            int[] rez = new int[n];
            HashMap<Integer, HashSet<Integer>> valz = new HashMap<>();
            for (int i = 0; i < m; i++) {
                Pair p = new Pair(nextInt(), nextInt());
//            arr[i] = p;
                if (!valz.containsKey(p.x)) {
                    valz.put(p.x, new HashSet<Integer>());
                }
                valz.get(p.x).add(p.y);

                if (!valz.containsKey(p.y)) {
                    valz.put(p.y, new HashSet<Integer>());
                }
                valz.get(p.y).add(p.x);

                vert[p.x - 1]++;
                vert[p.y - 1]++;
            }
            //Arrays.sort(arr, mComp);
            for (int i = 0; i < n; i++) {
                if (vert[i] == n - 1) {
                    rez[i] = 2;
                }
            }

            for (int i = 0; i < n; i++) {
                if (rez[i] == 0) {
                    rez[i] = 1;//isOne?1:3;
                    if (valz.get(i + 1) != null)
                        for (Integer key : valz.get(i + 1)) {
                            if (rez[key - 1] != 2) {
                                rez[key - 1] = 1;
                            }
                        }
                    break;
                }
            }

            for (int i = 0; i < n; i++) {
                if (rez[i] == 2) {
                    continue;
                }
                for (int j = 0; j < n; j++) {
                    if (i == j || rez[j] == 2) {
                        continue;
                    }
                    if (rez[i] == rez[j]) {
                        if (valz.get(i + 1) == null || !valz.get(i + 1).contains(j + 1)) {
                            out.println("No");
                            return;
                        }
                    } else {
                        if (valz.get(i + 1) != null && valz.get(i + 1).contains(j + 1)) {
                            out.println("No");
                            return;
                        }
                    }
                }
            }

            out.println("Yes");
            for (int i = 0; i < n; i++) {
                if (rez[i] == 1) out.print("a");
                if (rez[i] == 2) out.print("b");
                if (rez[i] == 0) out.print("c");
            }

        }

        int nextInt() {
            try {
                st.nextToken();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return (int) st.nval;
        }

        public static class Pair {
            public int x = 0;
            public int y = 0;

            public Pair(int xx, int yy) {
                this.x = Math.min(xx, yy);
                this.y = Math.max(xx, yy);
            }

        }

    }
}

