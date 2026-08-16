import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.util.Comparator;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            TreeSet<TaskC.Item> items = new TreeSet<>(new Comparator<TaskC.Item>() {

                public int compare(TaskC.Item o1, TaskC.Item o2) {
                    int z = o2.b - o1.b;
                    if (z == 0) z = o1.pos - o2.pos;
                    return z;
                }
            });
            TaskC.Item[] itemArr = new TaskC.Item[n];
            for (int i = 0; i < n; ++i) {
                itemArr[i] = new TaskC.Item();
                itemArr[i].pos = i;
                itemArr[i].a = in.nextInt();
            }
            for (int i = 0; i < n; ++i) {
                itemArr[i].b = in.nextInt();
                if (itemArr[i].b < itemArr[i].a) {
                    out.println(-1);
                    return;
                }
                if (itemArr[i].b > itemArr[i].a) {
                    items.add(itemArr[i]);
                }
            }
            long ops = 0;
            while (!items.isEmpty()) {
                TaskC.Item item = items.first();
                items.remove(item);
                TaskC.Item prev = itemArr[(item.pos - 1 + n) % n];
                TaskC.Item next = itemArr[(item.pos + 1) % n];
                long step = prev.b + next.b;
                long maxSteps = (item.b - Math.max(item.a, Math.max(prev.b, next.b)) + step - 1) / step;
                if (maxSteps == 0) {
                    out.println(-1);
                    return;
                }
                item.b -= step * maxSteps;
                ops += maxSteps;
                if (item.b < item.a) {
                    out.println(-1);
                    return;
                }
                if (item.b > item.a) {
                    items.add(item);
                }
            }
            out.println(ops);
        }

        static class Item {
            int pos;
            int a;
            int b;

        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
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

    }
}

