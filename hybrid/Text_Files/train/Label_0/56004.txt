import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class CF283D1 {

    private static class Result implements Comparable<Result> {
        Integer s;
        Integer t;

        public Result(final Integer s, final Integer t) {
            this.s = s;
            this.t = t;
        }

        @Override
        public int compareTo(final Result o) {

            if (s.compareTo(o.s) == 0) {
                return t.compareTo(o.t);
            }

            return s.compareTo(o.s);
        }
    }

    public static void main(final String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<Integer> posOnesList = new LinkedList<Integer>();
        List<Integer> posTwosList = new LinkedList<Integer>();
        int[] meetOnes = new int[n];
        int[] meetTwos = new int[n];
        int last = -1;
        for (int i = 0; i < n; i++) {
            int curr = sc.nextInt();
            meetOnes[i] = i > 0 ? meetOnes[i - 1] : 0;
            meetTwos[i] = i > 0 ? meetTwos[i - 1] : 0;
            if (curr == 1) {
                posOnesList.add(i);
                meetOnes[i]++;
            } else {
                posTwosList.add(i);
                meetTwos[i]++;
            }

            if (i == n - 1) {
                last = curr;
            }
        }

        Integer[] posOnes = posOnesList.toArray(new Integer[0]);
        Integer[] posTwos = posTwosList.toArray(new Integer[0]);

        List<Result> results = new LinkedList<Result>();

        for (int t = 1; t <= n; t++) {

            int currPos = -1;
            int onesWins = 0;
            int twosWins = 0;
            while (currPos < n) {
                int metOnes = currPos >= 0 ? meetOnes[currPos] : 0;
                int metTwos = currPos >= 0 ? meetTwos[currPos] : 0;

                int i1 = 3 * n;
                if (metOnes + t - 1 < posOnes.length) {
                    i1 = posOnes[metOnes + t - 1];
                }

                int i2 = 3 * n;
                if (metTwos + t - 1 < posTwos.length) {
                    i2 = posTwos[metTwos + t - 1];
                }

                if (i1 < i2) {
                    currPos = i1;
                    onesWins++;
                } else if (i2 < i1) {
                    currPos = i2;
                    twosWins++;
                } else {
                    break;
                }

            }

            if (currPos == n - 1 && onesWins != twosWins) {
                if (onesWins > twosWins && last == 1) {
                    results.add(new Result(onesWins, t));
                }

                if (twosWins > onesWins && last == 2) {
                    results.add(new Result(twosWins, t));
                }

            }

        }

        Result[] res = results.toArray(new Result[0]);
        Arrays.sort(res);

        StringBuilder sb = new StringBuilder();
        for (Result r : res) {
            if (sb.length() > 0) {
                sb.append("\n");
            }

            sb.append(r.s + " " + r.t);
        }

        System.out.println(res.length);
        if (res.length > 0) {
            System.out.println(sb.toString());
        }

    }
}
