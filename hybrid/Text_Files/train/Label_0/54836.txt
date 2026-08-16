// package codeforces.round.n657;

import java.util.*;

/**
 * @Author: nayix
 * @Date: 7/20/20 10:13 AM
 */
public class ChoosingFlowers {
    static class Flower {
        private long happiness;
        private long continueHappiness;

        public Flower(Scanner in) {
            this.happiness = in.nextLong();
            this.continueHappiness = in.nextLong();
        }

        public long getHappiness() {
            return happiness;
        }

        public long getContinueHappiness() {
            return continueHappiness;
        }
    }

    public long work(int n, int m, List<Flower> flowerList) {
        flowerList.sort(Comparator.comparing(Flower::getHappiness).reversed());
        long ans = 0L;
        long[] sum = new long[m];
        sum[0] = flowerList.get(0).happiness;
        for (int i = 1; i < m; i++) {
            sum[i] = sum[i-1] + flowerList.get(i).happiness;
        }
        for (int i = 0; i < m; i++) {
            Flower flower = flowerList.get(i);
            int l = 0, r = m - 1;
            for ( ; l <= r; ) {
                int mid = (l + r) >> 1;
                if (flowerList.get(mid).happiness >= flower.continueHappiness) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            if (r >= n) {
                ans = Math.max(ans, sum[n-1]);
            } else if (r >= i) {
                ans = Math.max(ans, sum[r] + flower.continueHappiness * (n - r - 1));
            } else if (r < 0) {
                ans = Math.max(ans, flower.happiness + flower.continueHappiness * (n-1));
            } else {
                ans = Math.max(ans, sum[r] + flower.happiness + flower.continueHappiness * (n - r - 2));
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        ChoosingFlowers choosingFlowers = new ChoosingFlowers();
        Scanner in = new Scanner(System.in);
        for (int t = in.nextInt(); t > 0; t--) {
            int n = in.nextInt();
            int m = in.nextInt();
            List<Flower> flowerList = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                flowerList.add(new Flower(in));
            }
            System.out.println(choosingFlowers.work(n, m, flowerList));
        }
        in.close();
    }
}
