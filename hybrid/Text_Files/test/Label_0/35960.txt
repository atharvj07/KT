import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author El Mehdi ASSALI
 */
public class Main {
  public static void main(String[] args) {
    InputStream inputStream = System.in;
    OutputStream outputStream = System.out;
    InputReader in = new InputReader(inputStream);
    PrintWriter out = new PrintWriter(outputStream);
    AConneRAndTheARCMarklandN solver = new AConneRAndTheARCMarklandN();
    solver.solve(1, in, out);
    out.close();
  }

  static class AConneRAndTheARCMarklandN {
    public void solve(int testNumber, InputReader in, PrintWriter out) {
      int t = in.nextInt();
      while (t-- > 0) {
        int n = in.nextInt(), s = in.nextInt(), k = in.nextInt();
        int[] arr = new int[k];
        HashSet<Integer> memo = new HashSet<>();
        for (int i = 0; i < k; i++) {
          arr[i] = in.nextInt();
          memo.add(arr[i]);
        }
        for (int i = 0, l = 0; l < 10000; l++, i++) {
          if (!memo.contains(s - i) && s - i > 0) {
            out.println(i);
            break;
          } else if (!memo.contains(s + i) && s + i <= n) {
            out.println(i);
            break;
          }
        }
      }
    }

  }

  static class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;

    public InputReader(InputStream inputStream) {
      reader = new BufferedReader(new InputStreamReader(inputStream));
    }

    public String next() {
      while (tokenizer == null || !tokenizer.hasMoreTokens()) {
        try {
          tokenizer = new StringTokenizer(reader.readLine());
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
      return tokenizer.nextToken();
    }

    public int nextInt() {
      return Integer.parseInt(next());
    }

  }
}

