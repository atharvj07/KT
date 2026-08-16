import java.io.*;
import java.util.*;

public class HillClimbing {
    static class Hill{
        int x;
        long y;
        Hill(int x, long y){
            this.x=x;
            this.y=y;
        }
    }
    static class Climbers{
        int u,v;
        Climbers(int u,int v){
            this.u=u;
            this.v=v;
        }
    }

    public static int [][] tb;
    public static int [] lvl;
    public static int [] q;
    public static Hill[] hills;
    public static Climbers[] climbers;

    public static int LCA(int u, int v){
        if(lvl[u] > lvl[v]){
            int tmp = u;
            u=v;
            v=tmp;
        }
        int d = lvl[v] - lvl[u];

        for(int i = 0; i < 18; i++)if(((d>>i)&1) != 0)
            v = tb[i][v];

        if(u==v)return v;
        for(int i = 17; i >= 0; i--){
            if(tb[i][v] != tb[i][u]){
                u = tb[i][u];
                v = tb[i][v];
            }
        }
        return tb[0][u];
    }

    public static long cross(int i, int j, int k){
        return (hills[j].x-hills[i].x)*(hills[k].y-hills[i].y) - (hills[k].x-hills[i].x)*(hills[j].y-hills[i].y);
    }

    public static void main(String[] args) {
        PrintWriter pw = new PrintWriter(System.out);
        Scanner cin= new Scanner(System.in);
        int n = cin.nextInt();
        tb = new int[18][n];
        lvl = new int[n];
        hills= new Hill[n];

        for(int i = 0; i < n; i++){
            int x = cin.nextInt();
            long y= cin.nextLong();
            hills[i]= new Hill(x,y);
        }
        int m= cin.nextInt();
//        climbers= new Climbers[m];
//        for (int i=0;i<m;i++){
//            int u=cin.nextInt();
//            int v= cin.nextInt();
//            climbers[i]= new Climbers(u,v);
//        }

        q = new int[n];
        q[0] = n-1;
        int sz=1;
        tb[0][n-1]=n-1;

        for(int i = n-2; i >= 0; i--){
            while (sz >= 2){

                int j = q[sz-1];
                int k = q[sz-2];

                if(cross(i,j,k)<= 0)break;
                --sz;
            }
            tb[0][i] = q[sz-1];
            q[sz++] = i;
        }

        for(int i = 1; i < 18; i++)
            for(int j = 0; j < n; j++)
                tb[i][j]=tb[i-1][tb[i-1][j]];

        for(int i = n-2; i >= 0; i--)
            lvl[i] = lvl[tb[0][i]] + 1;

        for(int i=0;i<m;i++){
            int u = cin.nextInt() - 1, v = cin.nextInt() - 1;
            pw.println(LCA(u,v) + 1);
        }
        pw.close();

    }
}
