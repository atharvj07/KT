import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.HashMap;
import java.util.Map;

public class CF199A {
    public static void main(final String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] parts = br.readLine().split("\\s+");
        int[] a = new int[10];
        for (int i = 0; i < parts.length; i++) {
            int val = Integer.parseInt(parts[i]);
            a[val]++;
        }

        Map<String, Integer> map = new HashMap<String, Integer>();

        boolean found = true;
        while (a[1] > 0 && found) {
            found = false;
            if (a[2] > 0) {
                if (a[4] > 0) {
                    int count = Math.min(a[1], Math.min(a[2], a[4]));
                    map.put("1 2 4", count);
                    a[1] -= count;
                    a[2] -= count;
                    a[4] -= count;
                    found = true;
                } else if (a[6] > 0) {
                    int count = Math.min(a[1], Math.min(a[2], a[6]));
                    map.put("1 2 6", count);
                    a[1] -= count;
                    a[2] -= count;
                    a[6] -= count;
                    found = true;
                }
            } else if (a[3] > 0) {
                if (a[6] > 0) {
                    int count = Math.min(a[1], Math.min(a[3], a[6]));
                    map.put("1 3 6", count);
                    a[1] -= count;
                    a[3] -= count;
                    a[6] -= count;
                    found = true;
                }
            }
        }

        for (int i = 0; i < a.length; i++) {
            if (a[i] > 0) {
                System.out.println(-1);
                return;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> m : map.entrySet()) {
            int cnt = m.getValue();
            while (cnt > 0) {
                cnt--;
                sb.append(m.getKey() + "\n");
            }
        }

        System.out.println(sb.toString());

    }

}
