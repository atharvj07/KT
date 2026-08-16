import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.util.ArrayList;

public class G {

    static StreamTokenizer st;
    static class Adge {
        int id,dis;
        public Adge(int id, int dis) {
            this.id = id;
            this.dis = dis;
        }
    }
    static ArrayList<Adge>[]ages;
    static int[]color, p, cnt;
    static long[]d0,d;
    static boolean[]in_circle;
    static int cur_root, n, v1, p1;
    static boolean found;
    public static void main(String[] args) throws IOException{
        st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        n = nextInt();
        ages = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) {
            ages[i] = new ArrayList<Adge>();
        }
        for (int i = 1; i <= n; i++) {
            int a = nextInt();
            int b = nextInt();
            int t = nextInt();
            ages[a].add(new Adge(b, t));
            ages[b].add(new Adge(a, t));
        }
        color = new int[n+1];
        p = new int[n+1];
        in_circle = new boolean[n+1];
        dfs(1);
        p[v1] = p1;
        cnt = new int[n+1];
        d0 = new long[n+1];
        for (int i = 1; i <= n; i++) {
            if (in_circle[i]) {
                cur_root = i;
                dfs2(i, 0, 0);
            }
        }
        d = new long[n+1];
        for (int i = 1; i <= n; i++) {
            d[i] = d0[i];
        }
        int[]dis_p = new int[n+1];
        int first = 0, last = 0;
        long length_circle = 0;
        for (int i = 1; i <= n; i++) {
            if (in_circle[i]) {
                first = i;
                for (Adge to : ages[i]) {
                    if (to.id==p[i]) {
                        dis_p[i] = to.dis;
                        length_circle += to.dis;
                        break;
                    }
                }
            }
        }
        long s = 0;
        last = first;
        long cur = 0;
        int cur_cnt = 0;
        boolean f = true;
        for (int i = first; i != first || f; i = p[i]) {
            f = false;
            while (s+dis_p[last] <= length_circle/2) {
                s += dis_p[last];
                last = p[last];
                cur += d0[last]+s*cnt[last];
                cur_cnt += cnt[last];
            }
            d[i] += cur;
            cur -= d0[p[i]]+dis_p[i]*cur_cnt;
            cur_cnt -= cnt[p[i]];
            s -= dis_p[i];
        }
        f = true;
        int[]p_rev = new int[n+1], dis_p_rev = new int[n+1];
        for (int i = first; i != first || f; i = p[i]) {
            f = false;
            p_rev[p[i]] = i;
            dis_p_rev[p[i]] = dis_p[i];
        }
        s = 0;
        last = first;
        cur = 0;
        cur_cnt = 0;
        f = true;
        for (int i = first; i != first || f; i = p_rev[i]) {
            f = false;
            while (s+dis_p_rev[last] < (length_circle % 2==0 ? length_circle/2 : length_circle/2+1)) {
                s += dis_p_rev[last];
                last = p_rev[last];
                cur += d0[last]+s*cnt[last];
                cur_cnt += cnt[last];
            }
            d[i] += cur;
            cur -= d0[p_rev[i]]+dis_p_rev[i]*cur_cnt;
            cur_cnt -= cnt[p_rev[i]];
            s -= dis_p_rev[i];
        }
        for (int i = 1; i <= n; i++) {
            if (in_circle[i])
                dfs3(i, 0);
        }
        for (int i = 1; i <= n; i++) {
            pw.print(d[i]+" ");
        }
        pw.close();
    }
    
    private static void dfs3(int v, int p) {
        for (Adge to : ages[v]) {
            if (to.id==p || in_circle[to.id])
                continue;
            d[to.id] = d[v]+(n-2*cnt[to.id])*to.dis;
            dfs3(to.id, v);
        }
    }

    private static void dfs2(int v, int p, int dis_to_root) {
        d0[cur_root] += dis_to_root;
        for (Adge to : ages[v]) {
            if (to.id==p || in_circle[to.id])
                continue;
            dfs2(to.id, v, dis_to_root+to.dis);
            cnt[v] += cnt[to.id];
        }
        cnt[v]++;
    }

    private static void dfs(int v) {
        color[v] = 1;
        for (Adge to : ages[v]) {
            if (to.id==p[v])
                continue;
            if (color[to.id]==0) {
                p[to.id] = v;
                dfs(to.id);
            }
            else if (color[to.id]==1) {
                int cur = v;
                while (true) {
                    in_circle[cur] = true;
                    if (cur==to.id)
                        break;
                    cur = p[cur];
                }
                v1 = to.id;
                p1 = v;
//              p[to.id] = v;
            }
        }
        color[v] = 2;
    }

    private static int nextInt() throws IOException{
        st.nextToken();
        return (int) st.nval;
    }

}
