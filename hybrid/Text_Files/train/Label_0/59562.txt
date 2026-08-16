import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class C {
    static List<Integer>[] a;
    static int[] group;

    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        a = new List[n + 1];
        group = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            a[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(in.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            a[u].add(v);
            a[v].add(u);
        }
        StringBuilder ans = new StringBuilder();
        boolean valid = true;
        for (int i = 1; i <= n; i++) {
            if (group[i] == 0 && !a[i].isEmpty()) {
                if (!dfs(i, 1)) {
                    valid = false;
                    break;
                }
            }
        }
        if (valid) {
            StringBuilder groupOne = new StringBuilder();
            StringBuilder groupTwo = new StringBuilder();
            int k1 = 0, k2 = 0;
            for (int i = 1; i <= n; i++) {
                if (group[i] == 1) {
                    groupOne.append(i).append(" ");
                    k1++;
                } else if (group[i] == 2) {
                    groupTwo.append(i).append(" ");
                    k2++;
                }
            }
            groupOne.deleteCharAt(groupOne.length() - 1);
            groupTwo.deleteCharAt(groupTwo.length() - 1);
            ans.append(k1).append("\n").append(groupOne).append("\n").append(k2).append("\n").append(groupTwo);
        } else {
            ans.append("-1");
        }
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        out.write(ans.toString());
        out.close();
    }

    private static boolean dfs(int i, int grp) {
        if (group[i] != 0) {
            return group[i] == grp;
        }
        group[i] = grp;
        for (int j : a[i]) {
            if (!dfs(j, 3 - grp)) {
                return false;
            }
        }
        return true;
    }
}
