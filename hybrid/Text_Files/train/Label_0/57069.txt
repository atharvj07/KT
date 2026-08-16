import java.io.PrintWriter;
import java.util.Scanner;

/**
 * <a href="http://codeforces.ru/problemset/problem/219/A"/>
 *
 * @author pvasilyev
 * @since 07 Jan 2014
 */
public class Problem084 {

    public static void main(String[] args) {
        final Scanner reader = new Scanner(System.in);
        final PrintWriter writer = new PrintWriter(System.out);

        solve(reader, writer);

        reader.close();
        writer.close();
    }

    private static void solve(final Scanner reader, final PrintWriter writer) {
        final int k = reader.nextInt();
        final char[] string = reader.next().toCharArray();
        if (string.length % k != 0) {
            writer.println(-1);
            return;
        }
        int[] counts = new int[26];
        for (int i = 0; i < string.length; i++) {
            counts[string[i]-'a']++;
        }
        if (!accepts(counts, k)) {
            writer.println(-1);
            return;
        }
        final StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < counts.length; i++) {
            final int count = counts[i] / k;
            for (int j = 0; j < count; ++j) {
                stringBuilder.append((char)('a'+i));
            }
        }
        final StringBuilder result = new StringBuilder();
        for (int i = 0; i < k; ++i) {
            result.append(stringBuilder);
        }

        writer.println(result.toString());
    }

    private static boolean accepts(final int[] counts, final int k) {
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] % k != 0) {
                return false;
            }
        }
        return true;
    }

}
