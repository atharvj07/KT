// package Quarantine;

import javafx.util.Pair;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class PaintTheTree {
    static ArrayList<Pair<Integer,Integer>> tree[];
    static boolean visited[];
    static long dp[][];
    static int k;
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int q=Integer.parseInt(br.readLine());
        StringBuilder print=new StringBuilder();
        while(q--!=0){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int n=Integer.parseInt(st.nextToken());
            k=Integer.parseInt(st.nextToken());
            visited=new boolean[n+1];
            tree=new ArrayList[n+1];
            dp=new long[n+1][2];
            for(int i=1;i<=n;i++){
                tree[i]=new ArrayList<>();
            }
            for(int i=1;i<n;i++){
                st=new StringTokenizer(br.readLine());
                int u=Integer.parseInt(st.nextToken());
                int v=Integer.parseInt(st.nextToken());
                int w=Integer.parseInt(st.nextToken());
                tree[u].add(new Pair<>(v,w));
                tree[v].add(new Pair<>(u,w));
            }
            dfs(1);
            print.append(dp[1][0]).append("\n");
        }
        System.out.print(print.toString());
    }
    public static void dfs(int curr){
        visited[curr]=true;
        ArrayList<PaintInfo> paintInfos=new ArrayList<>();
        for(Pair<Integer,Integer> p:tree[curr]){
            int j=p.getKey();
            int w=p.getValue();
            if(!visited[j]){
                dfs(j);
                paintInfos.add(new PaintInfo(w,dp[j][0],dp[j][1]));
            }
        }
        Collections.sort(paintInfos,Collections.reverseOrder());
        int lim0=Math.min(k,paintInfos.size());
        int lim1=Math.min(k-1,paintInfos.size());
        long sum[]=new long[paintInfos.size()+1];
        for(int i=paintInfos.size()-1;i>=0;i--){
            sum[i]=sum[i+1]+paintInfos.get(i).b;
        }
        long temp=0;
        for(int i=0;i<=lim0;i++){
            dp[curr][0]=Math.max(dp[curr][0],sum[i]+temp);
            if(i!=lim0)
            temp+=paintInfos.get(i).a+paintInfos.get(i).c;
        }
        temp=0;
        for(int i=0;i<=lim1;i++){
            dp[curr][1]=Math.max(dp[curr][1],sum[i]+temp);
            if(i!=lim1)
                temp+=paintInfos.get(i).a+paintInfos.get(i).c;
        }
//        System.out.println(curr+" "+dp[curr][0]+" "+dp[curr][1]);
        return;
    }
}

class PaintInfo implements Comparable<PaintInfo>{
    long a,b,c,d;
    public PaintInfo(long a,long b,long c){
        this.a=a;
        this.b=b;
        this.c=c;
        this.d=this.a+this.c-this.b;
    }

    @Override
    public int compareTo(PaintInfo o) {
        return Long.compare(this.d,o.d);
    }
}
