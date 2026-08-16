import java.io.*;
import java.util.*;

public class __Solution {

    static final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;

    public static void main(String[] args) {
        new __Solution().run();
    }

    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok;

    void init() throws FileNotFoundException {

        if (ONLINE_JUDGE) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        } else {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        }

        tok = new StringTokenizer("");
    }

    void run() {
        try {
            long timeStart = System.currentTimeMillis();

            init();
            solve();

            out.close();

            long timeEnd = System.currentTimeMillis();
            System.err.println("Time = " + (timeEnd - timeStart));
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }

    String readLine() throws IOException {
        return in.readLine();
    }

    String delimiter = " ";

    String readString() throws IOException {
        while (!tok.hasMoreTokens()) {
            String nextLine = readLine();
            if (null == nextLine) return null;

            tok = new StringTokenizer(nextLine);
        }

        return tok.nextToken(delimiter);
    }

    int readInt() throws IOException {
        return Integer.parseInt(readString());
    }

    long readLong() throws IOException {
        return Long.parseLong(readString());
    }

    void solve() throws IOException {
        int[] input = new int[26];
        int[] output = new int[26];
        boolean[] was = new boolean[26];
        Arrays.fill(input, -1);
        Arrays.fill(output, -1);
        Arrays.fill(was, false);

        int n = readInt();
        for (int i = 0; i < n; i++) {
            char[] string = readString().toCharArray();
            for (int j = 0; j < string.length; j++)
                was[string[j]-'a'] = true;
            for (int j = 0; j < string.length-1; j++) {
                int n1 = string[j]-'a';
                int n2 = string[j+1]-'a';
                if (n2 == n1) {
                    out.println("NO");
                    return;
                }
                if (output[n1] != -1 && output[n1] != n2) {
                    out.println("NO");
                    return;
                }
                output[n1] = n2;
                if (input[n2] != -1 && input[n2] != n1) {
                    out.println("NO");
                    return;
                }
                input[n2] = n1;
            }
        }
        boolean h = true;
        String ans = "";
        for (int i = 0; i < 26; i++) {
            if (was[i] && input[i] == -1) {
                h = false;
                int now = i;
                while (now != -1) {
                    was[now] = false;
                    ans += (char)(((char)now)+'a');
                    now = output[now];
                }
            }
        }
        for (int i = 0; i < 26; i++)
            if (was[i])
            {
                out.println("NO");
                return;
            }
        if (h)
            out.print("NO");
        out.print(ans);
    }
}