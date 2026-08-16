import java.io.*;
import java.util.*;

public class Main {

    public static void functi(int v, int[] mas, int[] masC, int cV, int k, int n){
        if(masC[v] != cV)
            mas[0]--;

        for(int i = 0; i < n; i++){
            if(mas[i] == v)
                functi(i, mas, masC, masC[v], k, n);
        }

    }
    public static void main(String[] args) throws IOException {
        FastScanner in = new FastScanner(/*new InputStreamReader(new FileInputStream(new File("dijkstra.in")))); */ System.in);
        FastPrinter out = new FastPrinter(/*new OutputStreamWriter(new FileOutputStream(new File("dijkstra.out")))); */  System.out);
        int n = in.nextInt();
        int[] mas = new int[n+1];
        int k = 0;
        for(int i = 0; i <= n; i++) {
            mas[i] = in.nextInt();
            k += mas[i];
        }

        boolean flag = true;
        boolean flagg = false;
        for(int i = 0; i <= n; i++){
            if(flag == false && mas[i] > 1) {flagg = true; break;}
            if(mas[i] > 1) flag = false;
            else flag = true;
        }

        if(!flagg) System.out.println("perfect");
        else {
            int[] mas2 = new int[k];
            boolean flag2 = false;
            boolean flag3 = false;
            k = 0;
            System.out.println("ambiguous");
            int v = 0;
            for(int i = 0; i <= n; i++) {
                for (int j = 0; j < mas[i]; j++) {
                    System.out.print(v + " ");
                    if (flag2 && mas[i] > 1) {
                        mas2[k++] = v - 1;
                        flag2 = false;
                        flag3 = true;
                    }
                    else {mas2[k++] = v; flag2 = false;}
                }
                v = k;
                if(mas[i] > 1) if(flag3 == false) flag2 = true;
             //   i += mas[i];
            }
            System.out.println();
            for(int i = 0; i < k; i++)
                System.out.print(mas2[i] + " ");
        }
        out.close();
    }
}

class FastPrinter {
    private final PrintWriter writer;

    public FastPrinter(OutputStream outputStream) {
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }

    public FastPrinter(Writer writer) {
        this.writer = new PrintWriter(writer);
    }

    public void close() {
        writer.close();
    }

    public void println(long i) {
        writer.println(i);
    }

    public void println(double d) {
        writer.println(d);
    }

    public void println(String s) {
        writer.println(s);
    }

    public void println(String format, Object... args) {
        println(String.format(format, args));
    }

    public void println() {
        writer.println();
    }

    public void print(long i) {
        writer.print(i);
    }

    public void print(char c) {
        writer.print(c);
    }

    public void print(double d) {
        writer.print(d);
    }

    public void print(String s) {
        writer.print(s);
    }

    public void print(String format, Object... args) {
        print(String.format(format, args));
    }

    public void flush() {
        writer.flush();
    }
}

class FastScanner {

    private BufferedReader reader;
    private StringTokenizer st;
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private SpaceCharFilter filter;

    public FastScanner(InputStream stream) {
        this.reader = new BufferedReader(new InputStreamReader(stream));
        this.st = new StringTokenizer("");
    }

    public FastScanner(InputStreamReader stream) {
        this.reader = new BufferedReader(stream);
        this.st = new StringTokenizer("");
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

    public String next() {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(readLine());
        }
        return st.nextToken();
    }

    public String nextLine() {
        st = new StringTokenizer("");
        return readLine();
    }

    public String tryNextLine() {
        st = new StringTokenizer("");
        return tryReadLine();
    }

    private String readLine() {
        String line = tryReadLine();
        if (line == null) throw new InputMismatchException();
        return line;
    }

    private String tryReadLine() {
        try {
            return reader.readLine();
        } catch (IOException e) {
            throw new InputMismatchException();
        }
    }

    public int[] nextIntArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++)
            array[i] = nextInt();
        return array;
    }

    public int[][] nextIntTable(int rowCount, int columnCount) {
        int[][] table = new int[rowCount][];
        for (int i = 0; i < rowCount; i++)
            table[i] = nextIntArray(columnCount);
        return table;
    }

    public long[] nextLongArray(int size) {
        long[] array = new long[size];
        for (int i = 0; i < size; i++)
            array[i] = nextLong();
        return array;
    }

    public long[][] nextLongTable(int rowCount, int columnCount) {
        long[][] table = new long[rowCount][];
        for (int i = 0; i < rowCount; i++)
            table[i] = nextLongArray(columnCount);
        return table;
    }

    public boolean isSpaceChar(int c) {
        if (filter != null)
            return filter.isSpaceChar(c);
        return isWhitespace(c);
    }

    public static boolean isWhitespace(int c) {
        return c == ' ' || c == '\t' || isEOL(c);
    }

    public static boolean isEOL(int c) {
        return c == '\n' || c == '\r' || c == -1;
    }

    public interface SpaceCharFilter {
        public boolean isSpaceChar(int ch);
    }
}