import java.util.*;
import java.io.*;
import static java.lang.Math.*;
public class C {
    public static long gcd(long a, long b){
        return b==0?a:gcd(b, a%b);
    }
    public static long lcm(long a, long b) {
        return a/gcd(a,b)*b;
    }

    int[][] gcd;
    int[][] lcm;
    List<Integer>[] adj;
    int[] num;
    Set<Integer> v;
    Scanner in = new Scanner(System.in);
    StringBuilder buf = new StringBuilder();
    public C() throws Exception {
        int n = in.nextInt();
        int m = in.nextInt();

        gcd = new int[n][n];
        lcm = new int[n][n];
        adj = new ArrayList[n];
        for (int i=0;i<n;i++)
            adj[i] = new ArrayList();
        
        for (int i=0;i<m;i++) {
            int a = in.nextInt()-1;
            int b = in.nextInt()-1;
            int g = in.nextInt();
            int l = in.nextInt();
            adj[a].add(b);
            adj[b].add(a);
            gcd[a][b] = g;
            gcd[b][a] = g;
            lcm[a][b] = l;
            lcm[b][a] = l;
        }

        boolean valid = true;
        num = new int[n];
        loop:for (int i=0;i<n ;i++) {
            if(num[i]!=0) continue;

            long min = 1;
            int max = 1000000;
            for (int nbr:adj[i]) {
                min = lcm(min, gcd[i][nbr]);
                max = min(max, lcm[i][nbr]);
                if(min>1000000) {
                   valid = false;
                   break loop;
                }
            }

            if(valid){
                int d = (int)min;
                l2:for (int j=d;j<=max ;j+=d) {
                    for (int nbr:adj[i]) {
                        if(lcm[i][nbr]%j!=0) {
                            continue l2;
                        }
                    }
                    num[i] = j;
                    stop = false;
                    v = new HashSet();
                    dfs(i);
                    if(!stop) {
                        break;
                    }
                    for (int k : v) {
                        num[k] = 0 ;
                    }
                }

                if(num[i]==0) {
                    valid = false;
                    break;
                }
                
            }
        }
        if(valid) {
            buf.append("YES\n");
            for (int i=0;i<n ;i++) {
                buf.append(num[i]).append(' ');
            }
        } else {
            buf.append("NO\n");
        }

        System.out.print(buf);
    }

    boolean stop;
    void dfs(int cnt) {
        if(v.contains(cnt))return;
        v.add(cnt);
        for (int nbr:adj[cnt]) {
            if(num[nbr]==0){
                if(lcm[cnt][nbr]%num[cnt]!=0){
                    stop = true;
                    return;
                }
                long t = lcm[cnt][nbr]/num[cnt]*gcd[cnt][nbr];
                if(t>1000000||gcd(num[cnt], t)!=gcd[cnt][nbr]) {
                    stop = true;
                    return;
                }
                num[nbr] = (int)t;
                dfs(nbr);
                if(stop)
                    return;
            } else {
                if(lcm[cnt][nbr]%num[cnt]!=0){
                    stop = true;
                    return;
                }
                long t = lcm[cnt][nbr]/num[cnt]*gcd[cnt][nbr];
                if(t>1000000||gcd(num[cnt], t)!=gcd[cnt][nbr]) {
                    stop = true;
                    return;
                }
            }
        }
        
    }

    public static void main(String[] args) throws Exception {
        new C();
    }
}
