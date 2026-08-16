import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class Main {

    public static void main(String[] args) throws IOException {
        Pattern space = Pattern.compile(" ");
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        int[] first = space.splitAsStream(stdin.readLine()).mapToInt(Integer::parseInt).toArray();
        int n = first[0];
        int k = first[1];
        long[] a = space.splitAsStream(stdin.readLine()).mapToLong(Long::parseLong).toArray();

        long[] b = new long[n + 1];
        for (int i = 0; i < n; i++) b[i + 1] = a[i] + b[i];

        List<Long> sums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                sums.add(b[j + 1] - b[i]);
            }
        }


        long ans = 0L;
        for (long i = 40L; i >= 0; i--) {
            List<Long> nxts = new ArrayList<>();
            for (long sum : sums) {
                if ((sum & (1L << i)) != 0L) nxts.add(sum);
            }

            if (nxts.size() >= k) {
                ans |= 1L << i;
                sums = nxts;
            }
        }

        System.out.println(ans);
    }
}
