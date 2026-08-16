import java.util.*;

public class Main {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            char[] orgChar = sc.next().toCharArray();
            boolean[] org = new boolean[orgChar.length];
            for (int j = 0; j < orgChar.length; j++) {
                org[j] = (orgChar[j] == '1');
            }
            HashMap<Long, Integer> map = new HashMap<>();
            map.put(getNum(org), 0);
            int orgCount = 1;
            for (int j = 1; j < org.length; j++) {
                if (org[org.length - j]) {
                    org[org.length - j] = false;
                    if (!org[org.length - j - 1]) {
                        org[org.length - j - 1] = true;
                    }
                    map.put(getNum(org), orgCount);
                    orgCount++;
                }
            }
            char[] nextChar = sc.next().toCharArray();
            boolean[] next = new boolean[nextChar.length];
            for (int j = 0; j < nextChar.length; j++) {
                next[j] = (nextChar[j] == '1');
            }
            if (map.containsKey(getNum(next))) {
                sb.append(map.get(getNum(next))).append("\n");
                continue;
            }
            int nextCount = 1;
            for (int j = 1; j < next.length; j++) {
                if (next[next.length - j]) {
                    next[next.length - j] = false;
                    if (!next[next.length - j - 1]) {
                        next[next.length - j - 1] = true;
                    }
                    if (map.containsKey(getNum(next))) {
                        sb.append(map.get(getNum(next)) + nextCount).append("\n");
                        break;
                    }
                    nextCount++;
                }
            }
            
        }
        System.out.print(sb);
    }
    
    static long getNum(boolean[] arr) {
        long ans = 0;
        for (boolean b : arr) {
            ans <<= 1;
            if (b) {
                ans++;
            }
        }
        return ans;
    }
}
