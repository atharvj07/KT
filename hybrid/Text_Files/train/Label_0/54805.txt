import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

/**
 * Created by eldar on 2/12/16.
 */
public class Main {

    static class BitIndexedTree {
        final int[] data;
        public BitIndexedTree(int n) {
            data = new int[n + 1];
        }

        void increment(int index, int num) {
            while(index < data.length) {
                data[index] += num;
                index = (index | (index - 1)) + 1;
            }
        }

        private int getSum(int r) {
            int ret = 0;
            while(r > 0) {
                ret += data[r];
                r &= r - 1;
            }
            return ret;
        }

        int getSum(int l, int r) {
            if (l > r) return 0;
            return getSum(r) - getSum(l - 1);
        }
    }

    static void update(BitIndexedTree tree, int cap, int day, int num) {
        int cur = tree.getSum(day, day);
        if (cur + num > cap) {
            num = cap - cur;
        }
        tree.increment(day, num);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        String[] s = in.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);
        int a = Integer.parseInt(s[2]);
        int b = Integer.parseInt(s[3]);
        int q = Integer.parseInt(s[4]);

        BitIndexedTree broken = new BitIndexedTree(n);
        BitIndexedTree repaired = new BitIndexedTree(n);
        while(q-- > 0) {
            s = in.readLine().split(" ");
            int type = Integer.parseInt(s[0]);
            if (type == 1) {
                int day = Integer.parseInt(s[1]);
                int num = Integer.parseInt(s[2]);
                update(broken, b, day, num);
                update(repaired, a, day, num);
            } else {
                int repairsStart = Integer.parseInt(s[1]);
                System.out.println(broken.getSum(1, repairsStart - 1) + repaired.getSum(repairsStart + k, n));
            }
        }
    }
}