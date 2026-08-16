import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        final int MAXN = 100100;
        final Scanner scanner = new Scanner(System.in);
        final int n = scanner.nextInt();
        int[] u = new int[MAXN];
        int[] ucnt = new int[MAXN];
        Map<Integer, Set<Integer>> m = new HashMap<>();
        for (int i = 0; i < n; i++) {
            u[i] = scanner.nextInt();
            ucnt[u[i]] += 1;
        }
        /*
        if (u[0] == 85787) {
            for (int i = 0; i < MAXN; i++) {
                if (ucnt[i] > 0) {
                    System.out.printf("%d:%d,", i, ucnt[i]);
                }
            }
        }
        */
        for (int i = 0; i < MAXN; i++) {
            if (ucnt[i] > 0) {
                if (!m.containsKey(ucnt[i])) {
                    m.put(ucnt[i], new HashSet<>());
                }
                m.get(ucnt[i]).add(i);
            }
        }
        int ans;
        for (ans = n - 1; ans > 0; ans--) {
            // System.out.printf("ans=%d m=%s\n", ans, m.toString());
            if (m.size() == 1) {
                Integer key = (Integer)m.keySet().toArray()[0];
                if (key == 1 || m.get(key).size() == 1) {
                    break;
                }
            }
            if (m.size() == 2) {
                Object[] keyObjs = m.keySet().toArray();
                Integer[] keys = {(Integer)keyObjs[0], (Integer)keyObjs[1]};
                if (keys[0] > keys[1]) {
                    // let keys[1] bigger than keys[0]
                    keys[0] ^= keys[1];
                    keys[1] ^= keys[0];
                    keys[0] ^= keys[1];
                }
                if (keys[0] == 1 && m.get(keys[0]).size() == 1) {
                    break;
                }
                if (keys[0] + 1 == keys[1] && m.get(keys[1]).size() == 1) {
                    break;
                }
            }
            int curr = u[ans];
            m.get(ucnt[curr]).remove(curr);
            if (m.get(ucnt[curr]).isEmpty()) {
                m.remove(ucnt[curr]);
            }
            ucnt[curr] -= 1;
            if (ucnt[curr] > 0) {
                if (!m.containsKey(ucnt[curr])) {
                    m.put(ucnt[curr], new HashSet<>());
                }
                m.get(ucnt[curr]).add(curr);
            }
        }
        System.out.println(ans + 1);
    }
}