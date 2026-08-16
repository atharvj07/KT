import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.FilterInputStream;
import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        ScanReader in = new ScanReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BSortedAdjacentDifferences solver = new BSortedAdjacentDifferences();
        solver.solve(1, in, out);
        out.close();
    }

    static class BSortedAdjacentDifferences {
        public void solve(int testNumber, ScanReader in, PrintWriter out) {
            int t = in.scanInt();
            while (t-- > 0) {
                int n = in.scanInt();
                int arr[] = new int[n];
                for (int i = 0; i < n; i++) arr[i] = in.scanInt();
                int ptr1 = 0;
                int ptr2 = n - 1;
                CodeX.sort(arr);


                ArrayList<Integer> arrayList = new ArrayList<>();
                for (int i = 0; i < n; i++) {
                    if (i % 2 == 0) {
                        arrayList.add(arr[ptr1++]);
                    } else {
                        arrayList.add(arr[ptr2--]);
                    }
                }

                for (int j = n - 1; j >= 0; j--) {
                    out.print(arrayList.get(j) + " ");
                }

                out.println();


            }

        }

    }

    static class ScanReader {
        private byte[] buf = new byte[4 * 1024];
        private int INDEX;
        private BufferedInputStream in;
        private int TOTAL;

        public ScanReader(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }

        private int scan() {
            if (INDEX >= TOTAL) {
                INDEX = 0;
                try {
                    TOTAL = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (TOTAL <= 0) return -1;
            }
            return buf[INDEX++];
        }

        public int scanInt() {
            int I = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    I *= 10;
                    I += n - '0';
                    n = scan();
                }
            }
            return neg * I;
        }

        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }

    }

    static class CodeX {
        public static void sort(int arr[]) {
            merge_sort(arr, 0, arr.length - 1);
        }

        private static void merge_sort(int A[], int start, int end) {
            if (start < end) {
                int mid = (start + end) / 2;
                merge_sort(A, start, mid);
                merge_sort(A, mid + 1, end);
                merge(A, start, mid, end);
            }

        }

        private static void merge(int A[], int start, int mid, int end) {
            int p = start, q = mid + 1;
            int Arr[] = new int[end - start + 1];
            int k = 0;

            for (int i = start; i <= end; i++) {
                if (p > mid)
                    Arr[k++] = A[q++];

                else if (q > end)
                    Arr[k++] = A[p++];

                else if (A[p] < A[q])
                    Arr[k++] = A[p++];

                else
                    Arr[k++] = A[q++];
            }
            for (int i = 0; i < k; i++) {
                A[start++] = Arr[i];
            }

        }

    }
}

