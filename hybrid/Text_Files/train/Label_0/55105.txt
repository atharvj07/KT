import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class DTask {

    static Scanner in;
    static int[] first = new int[4];
    static int[] second = new int[4];
    static PrintWriter out;
    static int n;

    public static void main(String[] args) throws IOException {
        in = new Scanner(System.in);
        out = new PrintWriter(System.out);
        n = in.nextInt() + 1;
        first = new int[]{0, 0, n, n};
        second = new int[]{0, 0, n, n};
        for (int i = 0; i < first.length; i++) {
            boolean inc = i < 2;
            search(first, i, inc, false);
            if (!inc) {
                first[i] += 1;
            }
        }

        for (int i = 0; i < second.length; i++) {
            boolean inc = i < 2;
            search(second, i, inc, true);
            if (!inc) {
                second[i] += 1;
            }
        }
        String s = "!";
        for (int i = 0; i < 4; i++) {
            s += " " + second[i];
        }
        for (int i = 0; i < 4; i++) {
            s += " " + first[i];
        }
        out.println(s);
        out.flush();
    }

    static void search(int arr[], int i, boolean inc, boolean cond) {
        int start = 0;
        int end = n;
        while (true) {
            if (end - start <= 1) {
                arr[i] = start;
                return;
            }
            int mid = (start + end) / 2;
            arr[i] = mid;
            int n = ask(arr, cond);
            if (n > 0) {
                if (inc) {
                    start = mid;
                } else {
                    end = mid;
                }
            } else {
                if (inc) {
                    end = mid;
                } else {
                    start = mid;
                }
            }
        }
    }

    static int ask(int arr[], boolean cond) {
        if (arr[1] > arr[3] || arr[0] > arr[2]) {
            return 0;
        }
        arr = Arrays.copyOf(arr, 4);
        String q = "";
        q += "?";
        for (int i = 0; i < arr.length; i++) {
            int x = Math.min(arr[i], n - 1);
            x = Math.max(x, 1);
            q += " " + x;
        }
        out.println(q);
        out.flush();
        int x = in.nextInt();
        if (cond) {
            x -= within(arr, first) ? 1 : 0;
        }
        return x;
        /*if (arr[1] > arr[3] || arr[0] > arr[2]) {
            return 0;
        }
        int[] check = new int[]{1, 1, 10, 1};
        int[] check1 = new int[]{5, 5, 5, 10};
        int result = within(arr, check) ? 1 : 0;
        result += within(arr, check1) ? 1 : 0;
        if (cond) {
            result -= within(arr, first) ? 1 : 0;
        }
        return result;*/


    }

    static boolean within(int outer[], int inner[]) {
        return (outer[0] <= inner[0] && outer[1] <= inner[1] && outer[2] >= inner[2] && outer[3] >= inner[3]);
    }

    static class MyInputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public MyInputReader(InputStream stream) {
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

