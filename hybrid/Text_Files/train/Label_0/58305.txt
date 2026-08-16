import java.util.*;
import java.io.*;

public class A {
  public static void main(String[] args) {
    new A().run();
  }
  
  public void run() {
    InputReader reader = new InputReader(System.in);
    PrintWriter writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    
    int n = reader.nextInt();
    StringBuilder[] r = new StringBuilder[6];
    r[0] = new StringBuilder("+------------------------+");
    r[1] = new StringBuilder("|#.#.#.#.#.#.#.#.#.#.#.|D|)");
    r[2] = new StringBuilder("|#.#.#.#.#.#.#.#.#.#.#.|.|");
    r[3] = new StringBuilder("|#.......................|");
    r[4] = new StringBuilder("|#.#.#.#.#.#.#.#.#.#.#.|.|)");
    r[5] = new StringBuilder("+------------------------+");
    
    for (int i = 0, currRow = 1, currCol = 1; i < n; i++) {
      r[currRow].setCharAt(currCol, 'O');
      currRow++;
      if (currRow == 3 && currCol != 1) currRow++;
      if (currRow == 5) {
        currRow = 1;
        currCol += 2;
      }
    }
    
    for (int i = 0; i < 6; i++) {
      writer.println(r[i]);
    }
    
    writer.close();
  }
  
  public class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;
    
    public InputReader(InputStream stream) {
      reader = new BufferedReader(new InputStreamReader(stream));
      tokenizer = null;
    }
    
    public boolean hasNext() {
      while (tokenizer == null || !tokenizer.hasMoreTokens()) {
        try {
          String line = reader.readLine();
          if (line == null) {
            return false;
          }
          tokenizer = new StringTokenizer(line);
        } catch (Exception e) { }
      }
      return true;
    }
    
    public String nextLine() {
      hasNext();
      return tokenizer.nextToken("\n\r");
    }
    
    public String next() {
      hasNext();
      return tokenizer.nextToken();
    }
    
    public int nextInt() {
      return Integer.parseInt(next());
    }
    
    public long nextLong() {
      return Long.parseLong(next());
    }
    
    public double nextDouble() {
      return Double.parseDouble(next());
    }
  }
}
