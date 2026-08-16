import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

public class ProblemE {
    static int N;
    static long Y;
    static long ycnt;
    static int[] place;
    static boolean[][] invalidGraph;
    static boolean[][] rules;

    private static long cnt2(int now) {
        int[] parray = new int[N];
        int[] map = new int[N];
        Arrays.fill(map, -1);
        int pidx = 0;
        for (int i = 0 ; i < N ; i++) {
            if (place[i] != -1) {
                map[place[i]] = i;
            } else {
                parray[pidx++] = i;
            }
        }
        
        for (int i = 0 ; i < now ; i++) {
            for (int j = i+1 ; j < now ; j++) {
                int young = -1;
                int old = -1;
                if (map[i] < map[j]) {
                    young = j;
                    old = i;
                } else {
                    old = j;
                    young = i;
                }
                if (invalidGraph[young][old]) {
                    return 0;
                }
            }
        }
        
        // check one : with already placed
        boolean[][] placeable = new boolean[pidx][N];
        for (int i = 0 ; i < pidx ; i++) {
            for (int next = now ; next < N ; next++) {
                placeable[i][next] = true;
                for (int prev = 0 ; prev < now ; prev++) {
                    int young = -1;
                    int old = -1;
                    if (map[prev] < parray[i]) {
                        young = next;
                        old = prev;
                    } else {
                        young = prev;
                        old = next;
                    }
                    if (invalidGraph[young][old]) {
                        placeable[i][next] = false;
                        break;
                    }
                }
            }
        }
        
        int maxptn = 1<<(N-now);
        long[][] dp = new long[pidx+1][maxptn];
        dp[0][0] = 1;
        for (int i = 0 ; i < pidx ; i++) {
            for (int ptn = 0 ; ptn < maxptn ; ptn++) {
                if (dp[i][ptn] <= 0) {
                    continue;
                }
                // next, we'll use parray[i] !
                // then, where to place parray[i] ?
                for (int next = now ; next < N ; next++) {
                    if ((ptn & (1<<(next-now))) >= 1) {
                        continue;
                    }
                
                    if (!placeable[i][next]) {
                        continue;
                    }
                    
                    // check two : with dp placed
                    boolean isok = true;
                    for (int prev = now ; prev < N ; prev++) {
                        if ((ptn & (1<<(prev-now))) >= 1) {
                            int old = prev;
                            int young = next;
                            if (invalidGraph[young][old]) {
                                isok = false;
                                break;
                            }
                        }
                    }
                    
                    if (isok) {
                        int nptn = ptn | (1<<(next-now));
                        dp[i+1][nptn] += dp[i][ptn];
                    }
                }
            }
        }
        return dp[pidx][maxptn-1];
    }
    
    
    private static void dfs(int now) {
        for (int i = 0 ; i < N ; i++) {
            if (place[i] == -1) {
                place[i] = now;
                
                long dcnt = cnt2(now+1);
                if (ycnt + dcnt >= Y) {
                    dfs(now+1);
                    break;
                }
                ycnt += dcnt;
                place[i] = -1;
            }
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader s = new BufferedReader(new InputStreamReader(System.in));
        String[] line = s.readLine().split(" ");
        int n = Integer.valueOf(line[0]);
        long y = Long.valueOf(line[1]) - 2000;
        int m = Integer.valueOf(line[2]);
        
        invalidGraph = new boolean[n][n];
        for (int i = 0 ; i < m ; i++) {
            String[] data = s.readLine().split(" ");
            int senior = Integer.valueOf(data[0])-1;
            int junior = Integer.valueOf(data[1])-1;
            invalidGraph[senior][junior] = true;
        }
        
        N = n;
        Y = y;
        ycnt = 0;
        place = new int[N];
        Arrays.fill(place, -1);
        
        dfs(0);

        if (place[0] == -1) {
            System.out.println("The times have changed");
            return;
        } else {
            int[] map = new int[N];
            for (int i = 0 ; i < n ; i++) {
                map[place[i]] = i;
            }
            StringBuffer b = new StringBuffer();
            for (int i = 0 ; i < n ; i++) {
                b.append(map[i]+1).append(" ");
            }
            System.out.println(b.substring(0, b.length()-1));
        }
    }
}