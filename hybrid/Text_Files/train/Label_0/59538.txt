import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class C159 {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(input.readLine()), n, p, tmp_int;
        String s = input.readLine();;
        int len = s.length(), m = len * k + 1;
        HashMap<Integer, List<Integer>> hash = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < len; i++) {
            tmp_int = s.charAt(i) - 'a';
            if (!hash.containsKey(tmp_int))
                hash.put(tmp_int, new ArrayList<Integer>());
            for (int j = 1; j <= k; j++)
                hash.get(tmp_int).add(i + (j - 1) * len + 1);
        }
        for (List<Integer> x: hash.values())
            Collections.sort(x);
        n = Integer.parseInt(input.readLine());
        for (int i = 0; i < n; i++) {
            String tmp[] = input.readLine().split(" ");
            p = Integer.parseInt(tmp[0]);
            int a = tmp[1].charAt(0) - 'a';
            hash.get(a).remove(p - 1);
        }
        char answer[] = new char[m];
        for (int x: hash.keySet()) {
            for (int y: hash.get(x))
                answer[y - 1] = (char) (x + 'a');
        }
        for (int i = 0; i < m; i++)
            if (answer[i] >= 'a')
                System.out.print(answer[i]);
    }
}
