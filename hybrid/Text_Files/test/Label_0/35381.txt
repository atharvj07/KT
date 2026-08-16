import java.util.List;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.AbstractMap;
import java.util.StringTokenizer;
import java.math.BigInteger;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author AlexFetisov
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskD solver = new TaskD();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskD {
    int left, right;

    public void solve(int testNumber, InputReader in, PrintWriter out) {
        int n = in.nextInt();
        int[] a = Utils.readIntArray(in, n);
        Arrays.sort(a);

        List<Integer> seq = new ArrayList<Integer>();
        MultiHashSet<Integer> rest = new MultiHashSet<Integer>();
        seq.add(a[0]);
        for (int i = 1; i < n; ++i) {
            if (a[i] - a[i-1] > 1) {
                out.println("NO");
                return;
            }
            if (a[i] == a[i-1]) {
                rest.add(a[i]);
            } else {
                seq.add(a[i]);
            }
        }
        left = seq.get(0);
        right = seq.get(seq.size()-1);

        if (seq.size() <= 1) {
            if (rest.size() != 0) {
                out.println("NO");
            } else {
                out.println("YES");
            }
            return;
        }

        for (int i = left + 1; i <= right - 1; ++i) {
            if (!rest.containsKey(i)) {
                out.println("NO");
                return;
            } else {
                rest.remove(i);
            }
        }

        if (test(rest)) {
            out.println("YES");
            return;
        }
        out.println("NO");
    }

    private boolean test(MultiHashSet<Integer> rest) {
        for (int i = left; i < right; ++i) {
            int j = i + 1;
            Integer ni = rest.get(i);
            Integer nj = rest.get(j);
            if (ni != null && nj != null) {
                int mi = Math.min(ni, nj);
                ni -= mi;
                nj -= mi;
                rest.removeAll(i);
                rest.removeAll(j);
                if (ni != 0) {
                    rest.add(i, ni);
                }
                if (nj != 0) {
                    rest.add(j, nj);
                }
            }
        }
        return rest.isEmpty();
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer stt;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
    }

    public String nextLine() {
        try {
            return reader.readLine();
        } catch (IOException e) {
            return null;
        }
    }

    public String nextString() {
        while (stt == null || !stt.hasMoreTokens()) {
            stt = new StringTokenizer(nextLine());
        }
        return stt.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(nextString());
    }

}

class Utils {
    public static int[] readIntArray(InputReader in, int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }
        return a;
    }

}

class MultiHashSet<K> {
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        MultiHashSet that = (MultiHashSet) o;

        if (map != null ? !map.equals(that.map) : that.map != null) return false;

        return true;
    }

    public int hashCode() {
        return map != null ? map.hashCode() : 0;
    }

    private final HashMap<K, Integer> map;

    public MultiHashSet() {
        map = new HashMap<K, Integer>();
    }

    public int size() {
        return map.size();
    }

    public boolean isEmpty() {
        return map.isEmpty();
    }

    public boolean containsKey(K key) {
        return map.containsKey(key);
    }

    public Integer get(K key) {
        return map.get(key);
    }

    public int add(K key, int count) {
        Integer value = map.get(key);
        if (value == null) {
            value = 0;
        }
        value += count;
        map.put(key, value);
        return value;
    }

    public int add(K key) {
        return add(key, 1);
    }

    public int remove(K key) {
        Integer value = map.get(key);
        if (value == null) {
            return 0;
        }
        --value;
        if (value == 0) {
            map.remove(key);
        } else {
            map.put(key, value);
        }
        return value;
    }

    public int removeAll(K key) {
        Integer value = map.remove(key);
        if (value == null) {
            return 0;
        }
        return value;
    }

}

