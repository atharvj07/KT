import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class E implements Runnable {
    private void solve() throws IOException {
        int n = readInt();
        char[] s = readString().toCharArray();
        int left = 1, right = 2 * n, ans = -1;
        List<Integer> stars = new ArrayList<>();
        List<Integer> pacmans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (s[i] == '*') stars.add(i);
            if (s[i] == 'P') pacmans.add(i);
        }
        while (left <= right) {
            int mid = (left + right) / 2;
            if (ok(mid, stars, pacmans)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        if (ans == -1) throw new RuntimeException();
        out.println(ans);
    }

    private boolean ok(int len, List<Integer> stars, List<Integer> pacmans) {
        int si = 0;
        for (int pi = 0; pi < pacmans.size(); pi++) {
            if (si == stars.size()) {
                return true;
            }
            int starPos = stars.get(si);
            int pacmanPos = pacmans.get(pi);

            if (starPos < pacmanPos) {
                int toLeft = pacmanPos - starPos;
                if (toLeft > len) {
                    return false;
                }

                int rem1 = len;
                int si1 = si;
                while (si1 < stars.size() && stars.get(si1) <= pacmanPos) {
                    si1++;
                }
                rem1 -= toLeft * 2;
                if (rem1 < 0) {
                    rem1 = 0;
                }
                while (si1 < stars.size() && stars.get(si1) <= pacmanPos + rem1) {
                    si1++;
                }

                int rem2 = len;
                int si2 = si;
                while (si2 < stars.size() && stars.get(si2) <= pacmanPos) {
                    si2++;
                }
                rem2 -= toLeft;
                if (rem2 < 0) {
                    rem2 = 0;
                }
                while (si2 < stars.size() && stars.get(si2) <= pacmanPos + rem2 / 2) {
                    si2++;
                }

                si = Math.max(si1, si2);
            } else {
                while (si < stars.size() && stars.get(si) <= pacmanPos + len) {
                    si++;
                }
            }
        }

        if (si == stars.size()) {
            return true;
        }
        return false;
    }

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    public static void main(String[] args) {
        new Thread(null, new E(), "", 128 * (1L << 20)).start();
    }

    private static final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
    private BufferedReader reader;
    private StringTokenizer tokenizer;
    private PrintWriter out;

    @Override
    public void run() {
        try {
            if (ONLINE_JUDGE) {
                reader = new BufferedReader(new InputStreamReader(System.in));
                out = new PrintWriter(System.out);
            } else {
                reader = new BufferedReader(new FileReader("input.txt"));
                out = new PrintWriter("output.txt");
            }
            solve();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                // nothing
            }
            out.close();
        }
    }

    private String readString() throws IOException {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(reader.readLine());
        }
        return tokenizer.nextToken();
    }

    @SuppressWarnings("unused")
    private int readInt() throws IOException {
        return Integer.parseInt(readString());
    }

    @SuppressWarnings("unused")
    private long readLong() throws IOException {
        return Long.parseLong(readString());
    }

    @SuppressWarnings("unused")
    private double readDouble() throws IOException {
        return Double.parseDouble(readString());
    }
}