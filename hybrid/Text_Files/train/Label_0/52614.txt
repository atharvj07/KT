import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class sequence {

    /**
     * @param args
     * @throws IOException
     * @throws NumberFormatException
     */
    public static void main(String[] args) throws NumberFormatException,
            IOException {
        BufferedReader str = new BufferedReader(
                new InputStreamReader(System.in));
        int n = Integer.parseInt(str.readLine());
        PrintWriter out = new PrintWriter(System.out);

        int[] arr = new int[3];
        StringTokenizer input = new StringTokenizer(str.readLine());
        for (int i = 0; i < n; i++) {

            int x = Integer.parseInt(input.nextToken());
            arr[(x - 1)]++;

        }
        int max = 0;
        max = Math.max(arr[0], Math.max(arr[1], arr[2]));
        out.println(n - max);
        out.close();

    }

}
