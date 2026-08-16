import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.valueOf(reader.readLine());

        boolean[][] compatible = new boolean[count][count];

        for (int i = 0; i < count; ++i) {
            String[] parts = reader.readLine().split(" ");
            for (int j = 0; j < count; ++j) {
                if (Integer.valueOf(parts[j]) == 1) {
                    compatible[i][j] = true;
                }
            }
        }
        long modulo = 1_000_000_007;

        int combinationCount = 1 << count;
        long[] counts = new long[combinationCount];
        counts[0] = 1;

        Map<Integer, List<Integer>> seq = new HashMap<>();
        for (int len = 0; len <= count; ++len) {
            Map<Integer, List<Integer>> newSeq = new HashMap<>();

            for (int ones = 0; ones <= len; ++ones) {
                ArrayList<Integer> list = new ArrayList<>();
                if (ones == 0) {
                    list.add(0);
                } else {
                    if (ones < len) {
                        for (int s : seq.get(ones)) {
                            list.add(s << 1);
                        }
                    }

                    for (int s : seq.get(ones - 1)) {
                        list.add((s << 1) | 1);
                    }
                }


                newSeq.put(ones, list);
            }

            seq = newSeq;
        }

        for (int i = 0; i < count; ++i) {
            for (int j = 0; j < count; ++j) {
                if (compatible[i][j]) {
                    for (int s : seq.get(i)) {
                        if ((s & (1 << j)) == 0) {
                            int newS = s | (1 << j);
                            counts[newS] += counts[s];
                            counts[newS] %= modulo;
                        }
                    }
                }
            }
        }

        System.out.println(counts[combinationCount - 1]);
    }
}
