import java.awt.Point;
import java.io.*;
import java.math.BigInteger;
import java.util.*;
import static java.lang.Math.*;

public class BetaRound79_Div1_C implements Runnable {

    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok = new StringTokenizer("");

    public static void main(String[] args) {
        new Thread(null, new BetaRound79_Div1_C(), "", 256 * (1L << 20)).start();
    }

    public void run() {
        try {
            long t1 = System.currentTimeMillis();
            if (System.getProperty("ONLINE_JUDGE") != null) {
                in = new BufferedReader(new InputStreamReader(System.in));
                out = new PrintWriter(System.out);
            } else {
                in = new BufferedReader(new FileReader("input.txt"));
                out = new PrintWriter("output.txt");
            }
            Locale.setDefault(Locale.US);
            solve();
            in.close();
            out.close();
            long t2 = System.currentTimeMillis();
            System.err.println("Time = " + (t2 - t1));
        } catch (Throwable t) {
            t.printStackTrace(System.err);
            System.exit(-1);
        }
    }

    String readString() throws IOException {
        while (!tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    int readInt() throws IOException {
        return Integer.parseInt(readString());
    }

    long readLong() throws IOException {
        return Long.parseLong(readString());
    }

    double readDouble() throws IOException {
        return Double.parseDouble(readString());
    }

    /** http://pastebin.com/j0xdUjDn */
    static class Utils {

        private Utils() {}

        public static void mergeSort(int[] a) {
            mergeSort(a, 0, a.length - 1);
        }

        private static final int MAGIC_VALUE = 50;

        private static void mergeSort(int[] a, int leftIndex, int rightIndex) {
            if (leftIndex < rightIndex) {
                if (rightIndex - leftIndex <= MAGIC_VALUE) {
                    insertionSort(a, leftIndex, rightIndex);
                } else {
                    int middleIndex = (leftIndex + rightIndex) / 2;
                    mergeSort(a, leftIndex, middleIndex);
                    mergeSort(a, middleIndex + 1, rightIndex);
                    merge(a, leftIndex, middleIndex, rightIndex);
                }
            }
        }

        private static void merge(int[] a, int leftIndex, int middleIndex, int rightIndex) {
            int length1 = middleIndex - leftIndex + 1;
            int length2 = rightIndex - middleIndex;
            int[] leftArray = new int[length1];
            int[] rightArray = new int[length2];
            System.arraycopy(a, leftIndex, leftArray, 0, length1);
            System.arraycopy(a, middleIndex + 1, rightArray, 0, length2);
            for (int k = leftIndex, i = 0, j = 0; k <= rightIndex; k++) {
                if (i == length1) {
                    a[k] = rightArray[j++];
                } else if (j == length2) {
                    a[k] = leftArray[i++];
                } else {
                    a[k] = leftArray[i] <= rightArray[j] ? leftArray[i++] : rightArray[j++];
                }
            }
        }

        private static void insertionSort(int[] a, int leftIndex, int rightIndex) {
            for (int i = leftIndex + 1; i <= rightIndex; i++) {
                int current = a[i];
                int j = i - 1;
                while (j >= leftIndex && a[j] > current) {
                    a[j + 1] = a[j];
                    j--;
                }
                a[j + 1] = current;
            }
        }

    }

    // solution

    long ax, ay, bx, by, cx, cy;
    
    void solve() throws IOException {
        ax = readLong();
        ay = readLong();
        bx = readLong();
        by = readLong();
        cx = readLong();
        cy = readLong();
        if (go(ax, ay) || go(ay, -ax) || go(-ax, -ay) || go(-ay, ax)) {
            out.println("YES");
        } else {
            out.println("NO");
        }
    }
    
    boolean go(long ax, long ay) {
        long a = cx, b = cy, c = bx - ax;
        long d = cy, e = -cx, f = by - ay;
        long det = a * e - b * d;
        if (det == 0) {
            if (ax == bx && ay == by) {
                return true;
            } else {
                return false;
            }
        }
        long det1 = c * e - b * f;
        long det2 = a * f - c * d;
        if (det1 % det != 0 || det2 % det != 0) {
            return false;
        }
        return true;
    }

}
