import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.*;

public class Template implements Runnable {

    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok = new StringTokenizer("");

    void init() throws FileNotFoundException {
        try {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        } catch (Exception e) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        }
    }

    String readString() throws IOException {
        while (!tok.hasMoreTokens()) {
            try {
                tok = new StringTokenizer(in.readLine(), " :");
            } catch (Exception e) {
                return null;
            }
        }
        return tok.nextToken();
    }

    int readInt() throws IOException {
        return Integer.parseInt(readString());
    }

    int[] readIntArray(int size) throws IOException {
        int[] res = new int[size];
        for (int i = 0; i < size; i++) {
            res[i] = readInt();
        }
        return res;
    }

    long readLong() throws IOException {
        return Long.parseLong(readString());
    }

    double readDouble() throws IOException {
        return Double.parseDouble(readString());
    }

    <T> List<T>[] createGraphList(int size) {
        List<T>[] list = new List[size];
        for (int i = 0; i < size; i++) {
            list[i] = new ArrayList<>();
        }
        return list;
    }

    public static void main(String[] args) {
        new Thread(null, new Template(), "", 1l * 200 * 1024 * 1024).start();
    }

    long timeBegin, timeEnd;

    void time() {
        timeEnd = System.currentTimeMillis();
        System.err.println("Time = " + (timeEnd - timeBegin));
    }

    long memoryTotal, memoryFree;

    void memory() {
        memoryFree = Runtime.getRuntime().freeMemory();
        System.err.println("Memory = " + ((memoryTotal - memoryFree) >> 10)
                + " KB");
    }

    public void run() {
        try {
            timeBegin = System.currentTimeMillis();
            memoryTotal = Runtime.getRuntime().freeMemory();
            init();
            solve();
            out.close();
            if (System.getProperty("ONLINE_JUDGE") == null) {
                time();
                memory();
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }


    int[] dsu;
    boolean[] left;
    int[][] comp;
    int[] cnt;

    void add(int i, int val) {
        comp[i][cnt[i]++] = val;
    }

    void clearDSU() {
        for (int i = 0; i < dsu.length; i++) {
            dsu[i] = i;
            left[i] = true;
            cnt[i] = 0;
            add(i, i);
        }
    }

    int[] f;
    int[] to;
    int[] w;
    int[] index;
    int[] indexes;

    Random rnd = new Random();

    int cmp(int i, int j) {
        return -w[indexes[i]] + w[indexes[j]];
    }

    private void doSort(int start, int end) {
        if (start >= end)
            return;
        int i = start, j = end;
        int cur = i + rnd.nextInt(j - i);
        while (i < j) {
            while (i < cur && (cmp(i, cur) <= 0)) {
                i++;
            }
            while (j > cur && (cmp(cur, j) <= 0)) {
                j--;
            }
            if (i < j) {
                int temp = indexes[i];
                indexes[i] = indexes[j];
                indexes[j] = temp;
                if (i == cur)
                    cur = j;
                else if (j == cur)
                    cur = i;
            }
        }
        doSort(start, cur);
        doSort(cur + 1, end);
    }

    void solve() throws IOException {
        int n = readInt();
        int m = readInt();
        int q = readInt();

        comp = new int[n][n];
        dsu = new int[n];
        left = new boolean[n];
        cnt = new int[n];

        f = new int[m];
        to = new int[m];
        w = new int[m];
        index = new int[m];

        for (int i = 0; i < m; i++) {
            f[i] = readInt() - 1;
            to[i] = readInt() - 1;
            w[i] = readInt();
            index[i] = i + 1;
        }

        indexes = new int[m];
        for (int i = 0; i < m; i++) indexes[i] = i;
        doSort(0, m - 1);

        while (q-- > 0) {
            int l = readInt();
            int r = readInt();

            clearDSU();
            int answer = -1;
            for (int i = 0; i < m; i++) {
                int ind = indexes[i];
                if (index[ind] < l || index[ind] > r) continue;
                if (dsu[f[ind]] == dsu[to[ind]]) {
                    if (left[f[ind]] == left[to[ind]]) {
                        answer = w[ind];
                        break;
                    }
                } else {
                    int pa = dsu[f[ind]];
                    int pb = dsu[to[ind]];
                    if (cnt[pa] < cnt[pb]) {
                        int t = pa;
                        pa = pb;
                        pb = t;
                    }

                    boolean invert = left[f[ind]] == left[to[ind]];
                    for (int j = 0; j < cnt[pb]; j++) {
                        int x = comp[pb][j];
                        dsu[x] = pa;
                        add(pa, x);
                        if (invert) left[x] ^= true;
                    }
                }
            }
            out.println(answer);
        }


    }

    static final class LongIntHashMap {
        final static class Entry {
            final long key;
            int value;
            Entry next;

            Entry(long key, int value, Entry next) {
                this.key = key;
                this.value = value;
                this.next = next;
            }
        }

        private Entry[] table;
        private int capacity;
        private int threshold;
        private int size;

        public LongIntHashMap() {
            this(16);
        }

        @SuppressWarnings("unchecked")
        public LongIntHashMap(int capacity) {
            this.capacity = capacity;
            this.threshold = capacity * 4 / 3;
            this.table = new Entry[capacity];
        }

        public boolean containsKey(long key) {
            final int index = ((((int) (key >>> 32)) ^ ((int) (key))) & 0x7fffffff) % capacity;

            for (Entry entry = table[index]; entry != null; entry = entry.next) {
                if (entry.key == key) {
                    return true;
                }
            }
            return false;
        }

        public int get(long key) {
            final int index = ((((int) (key >>> 32)) ^ ((int) (key))) & 0x7fffffff) % capacity;
            for (Entry entry = table[index]; entry != null; entry = entry.next) {
                if (entry.key == key) {
                    return entry.value;
                }
            }
            return 0;
        }

        public int put(long key, int value) {
            final int index = ((((int) (key >>> 32)) ^ ((int) (key))) & 0x7fffffff) % capacity;
            final Entry entryOriginal = table[index];
            for (Entry entry = entryOriginal; entry != null; entry = entry.next) {
                if (entry.key == key) {
                    int oldValue = entry.value;
                    entry.value = value;
                    return oldValue;
                }
            }
            table[index] = new Entry(key, value, entryOriginal);
            size++;
            if (size > threshold) {
                setCapacity(2 * capacity);
            }
            return 0;
        }

        public int remove(long key) {
            int index = ((((int) (key >>> 32)) ^ ((int) (key))) & 0x7fffffff) % capacity;
            Entry previous = null;
            Entry entry = table[index];
            while (entry != null) {
                Entry next = entry.next;
                if (entry.key == key) {
                    if (previous == null) {
                        table[index] = next;
                    } else {
                        previous.next = next;
                    }
                    size--;
                    return entry.value;
                }
                previous = entry;
                entry = next;
            }
            return 0;
        }

        long[] getKeys() {
            long[] arr = new long[size()];
            int index = 0;
            for (int i = 0; i < table.length; i++) {
                Entry e = table[i];
                while (e != null) {
                    arr[index++] = e.key;
                    e = e.next;
                }
            }
            return arr;
        }

        public void clear() {
            size = 0;
            Arrays.fill(table, null);
        }

        public int size() {
            return size;
        }

        public void setCapacity(int newCapacity) {
            @SuppressWarnings("unchecked")
            Entry[] newTable = new Entry[newCapacity];
            int length = table.length;
            for (int i = 0; i < length; i++) {
                Entry entry = table[i];
                while (entry != null) {
                    long key = entry.key;
                    int index = ((((int) (key >>> 32)) ^ ((int) (key))) & 0x7fffffff) % newCapacity;

                    Entry originalNext = entry.next;
                    entry.next = newTable[index];
                    newTable[index] = entry;
                    entry = originalNext;
                }
            }
            table = newTable;
            capacity = newCapacity;
            threshold = newCapacity * 4 / 3;
        }

        /**
         * Target load: 0,6
         */
        public void reserveRoom(int entryCount) {
            setCapacity(entryCount * 5 / 3);
        }

    }

}