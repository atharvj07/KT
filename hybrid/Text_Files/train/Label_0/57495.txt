import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(in, out);
        out.close();
    }
}


class TaskD {

    private String smallest(String word) {
        if(word.length() % 2 == 1) return word;
        String first = smallest(word.substring(0,word.length() / 2));
        String second = smallest(word.substring(word.length() / 2, word.length()));
        if(first.compareTo(second) <= 0) {
            return first + second;
        } else {
            return second + first;
        }
    }

    void solve(InputReader in, OutputWriter out) {
        String first = in.next();
        String second = in.next();
        if(smallest(first).compareTo(smallest(second)) == 0) {
            out.printLine("YES");
        } else {
            out.printLine("NO");
        }
    }

}
class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;
    public InputReader(InputStream stream) {
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
    public boolean hasNext() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                String line = reader.readLine();
                if ( line == null ) {
                    return false;
                }
                tokenizer = new StringTokenizer(line);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return true;
    }
    public int nextInt() {
        return Integer.parseInt(next());
    }
    public long nextLong() {
        return Long.parseLong(next());
    }
    public double nextDouble() { return Double.parseDouble(next());}
}
class OutputWriter {
    private final PrintWriter writer;
    public OutputWriter(OutputStream outputStream) {
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }
    public OutputWriter(Writer writer) {
        this.writer = new PrintWriter(writer);
    }
    public void print(Object... objects) {
        for (int i = 0; i < objects.length; i++) {
            if ( i != 0 ) {
                writer.print(' ');
            }
            writer.print(objects[i]);
        }
    }
    public void printLine(Object... objects) {
        print(objects);
        writer.println();
    }
    public void close() {
        writer.close();
    }
}