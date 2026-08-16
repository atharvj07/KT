import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main implements Runnable {
  BufferedReader in;
  PrintWriter out;
  StringTokenizer tok = new StringTokenizer("");

  @Override
  public void run() {
    init();
    solve();
    out.close();
  }

  private void init() {
    in = new BufferedReader(new InputStreamReader(System.in));
    out = new PrintWriter(System.out);
  }

  private String readString() {
    while (!tok.hasMoreTokens()) {
      try {
        tok = new StringTokenizer(in.readLine());
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
    return tok.nextToken();
  }

  private int readInt() {
    return Integer.parseInt(readString());
  }

  public static void main(String[] args) {
    new Thread(new Main()).run();
  }

  private long readLong() {
    return Long.parseLong(readString());
  }

  private void solve() {
    int n = readInt();
    int start = readInt();
    int finish = readInt();
    int add = finish > 0 ? 1 : -1;
    if (finish < 0)
      finish = -finish;
    while (finish > 0) {
      start += add;
      finish--;
      if (start == n + 1)
        start = 1;
      if (start == 0)
        start = n;
    }
    out.print(start);
  }


}
