import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.NavigableSet;
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
        TaskF solver = new TaskF();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskF {
        static final int INF = (int) 2e9;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int l = in.nextInt();
            TreeSet<TaskF.Item> itemsByPos = new TreeSet<>(new Comparator<TaskF.Item>() {

                public int compare(TaskF.Item o1, TaskF.Item o2) {
                    return o1.pos - o2.pos;
                }
            });
            TreeSet<TaskF.Item> itemsByVal = new TreeSet<>(new Comparator<TaskF.Item>() {

                public int compare(TaskF.Item o1, TaskF.Item o2) {
                    int z = o1.value - o2.value;
                    if (z == 0) z = o1.pos - o2.pos;
                    return z;
                }
            });
            for (int i = 0; i < n; ++i) {
                TaskF.Item item = new TaskF.Item();
                item.pos = i;
                item.value = in.nextInt();
                item.choicesIfFirst = 1;
                item.choicesIfLast = 1;
                itemsByPos.add(item);
                itemsByVal.add(item);
            }
            long res = n;
            TaskF.Item[] segment = new TaskF.Item[n + 1];
            int[] sumStarts = new int[n + 1];
            TaskF.Item[] newItems = new TaskF.Item[n + 1];

            while (!itemsByVal.isEmpty()) {
                int segmentSize = 0;
                TaskF.Item left = itemsByVal.first();
                NavigableSet<TaskF.Item> after = itemsByPos.tailSet(left, true);
                for (TaskF.Item item : after) {
                    if (item.value != left.value) {
                        break;
                    }
                    segment[segmentSize++] = item;
                }
                for (int i = 0; i < segmentSize; ++i) {
                    TaskF.Item s = segment[i];
                    if (!itemsByVal.remove(s)) throw new RuntimeException();
                    if (!itemsByPos.remove(s)) throw new RuntimeException();
                }
                if (segmentSize < l) {
                    TaskF.Item sentinel = new TaskF.Item();
                    sentinel.pos = left.pos;
                    sentinel.value = INF;
                    itemsByPos.add(sentinel);
                    continue;
                }
                sumStarts[0] = 0;
                for (int i = 0; i < segmentSize; ++i) {
                    sumStarts[i + 1] = sumStarts[i] + segment[i].choicesIfFirst;
                }
                for (int i = l - 1; i < segmentSize; ++i) {
                    long ways = segment[i].choicesIfLast * (long) sumStarts[i + 2 - l];
                    res += ways;
                }
                int newCount = segmentSize / l;
                for (int i = 0; i < newCount; ++i) {
                    newItems[i] = new TaskF.Item();
                    newItems[i].value = left.value + 1;
                    newItems[i].pos = left.pos + i;
                }
                for (int i = 0; i + l <= segmentSize; ++i) {
                    int got = (segmentSize - i) / l;
                    newItems[newCount - got].choicesIfFirst += segment[i].choicesIfFirst;
                }
                for (int i = l - 1; i < segmentSize; ++i) {
                    int got = (i + 1) / l;
                    newItems[got - 1].choicesIfLast += segment[i].choicesIfLast;
                }
                sumStarts[0] = 0;
                for (int i = 0; i < newCount; ++i) {
                    sumStarts[i + 1] = sumStarts[i] + newItems[i].choicesIfFirst;
                }
                for (int i = l - 1; i < newCount; ++i) {
                    long ways = newItems[i].choicesIfLast * (long) sumStarts[i + 2 - l];
                    res -= ways;
                }
                for (int i = 0; i < newCount; ++i) {
                    itemsByVal.add(newItems[i]);
                    itemsByPos.add(newItems[i]);
                }
            }
            out.println(res);
        }

        static class Item {
            int pos;
            int value;
            int choicesIfFirst;
            int choicesIfLast;

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

