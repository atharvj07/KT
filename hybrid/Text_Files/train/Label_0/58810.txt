import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.*;

public class CodeForces {
    private final BufferedReader reader;
    private final PrintWriter writer;
    private StringTokenizer tokenizer;

    private void solve() {
        int n = nextInt();
        int[] l = new int[n];
        int[] r = new int[n];
        int lSum = 0;
        int rSum = 0;
        for (int i = 0; i < n; i++) {
            lSum += l[i] = nextInt();
            rSum += r[i] = nextInt();
        }
        int res = -1;
        int maxD = Math.abs(lSum - rSum);
        for (int i = 0; i < n; i++) {
            if (Math.abs(lSum - l[i] + r[i] - (rSum - r[i] + l[i])) > maxD) {
                maxD = Math.abs(lSum - l[i] + r[i] - (rSum - r[i] + l[i]));
                res = i;
            }
        }
        writer.print(res == -1 ? 0 : res + 1);
    }

    public static void main(String[] args) {
        new CodeForces(System.in, System.out);
    }

    private CodeForces(InputStream inputStream, OutputStream outputStream) {
        this.reader = new BufferedReader(new InputStreamReader(inputStream));
        this.writer = new PrintWriter(outputStream);
        solve();
        writer.close();
    }

    private String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(readLine());
        }
        return tokenizer.nextToken();
    }

    private String readLine() {
        String line;
        try {
            line = reader.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return line;
    }

    private int nextInt() {
        return Integer.parseInt(next());
    }

    private long nextLong() {
        return Long.parseLong(next());
    }

    private double nextDouble() {
        return Double.parseDouble(next());
    }

    public boolean hasNext() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            String line = readLine();
            if (line == null) {
                return false;
            }
            tokenizer = new StringTokenizer(line);
        }
        return true;
    }

    public BigInteger nextBigInteger() {
        return new BigInteger(next());
    }

    public static int upperBinarySearch(int[] array, int start, int finish, int key) {
        int low = 0;
        int high = array.length - 1;
        if (high < 0) return -1;
        while (low < high) {
            int mid = (low + high + 1) >>> 1;
            if (array[mid] <= key) low = mid;
            else high = mid - 1;
        }
        if (array[low] != key) {
            if (array[low] < key) low++;
            low = -(low + 1);
        }
        return low;
    }
}
