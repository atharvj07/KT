import java.io.*;
import java.util.stream.Stream;

/**
 * @author madi.sagimbekov
 */
public class C1093A {

    private static BufferedReader in;
    private static BufferedWriter out;

    public static void main(String[] args) throws IOException {
        open();

        int[] arr = readInts();
        int n = arr[0];
        while(n-- > 0) {
            int x = readInt();
            System.out.println(x / 7 + (x % 7 > 0 ? 1 : 0));
        }


        close();
    }

    private static int[] readInts() throws IOException {
        return Stream.of(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    }

    private static int readInt() throws IOException {
        return Integer.parseInt(in.readLine());
    }

    private static long[] readLongs() throws IOException {
        return Stream.of(in.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
    }

    private static long readLong() throws IOException {
        return Long.parseLong(in.readLine());
    }

    private static double[] readDoubles() throws IOException {
        return Stream.of(in.readLine().split(" ")).mapToDouble(Double::parseDouble).toArray();
    }

    private static double readDouble() throws IOException {
        return Double.parseDouble(in.readLine());
    }

    private static String readString() throws IOException {
        return in.readLine();
    }

    private static void open() {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new BufferedWriter(new OutputStreamWriter((System.out)));
    }

    private static void close() throws IOException {
        out.flush();
        out.close();
        in.close();
    }

}
