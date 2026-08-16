import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {//とりあえずbitで最小値求める
		try(Scanner sc = new Scanner(System.in)){
			int n=sc.nextInt();//蔵の数
			double[][] dist=new double[n][n];//蔵間の距離
			double[] d=new double[n];//城からの距離
			int[] v=new int[n];//千両箱の数
			int[] s=new int[n+1];
			double[][] dp=new double[1<<n][n];
			int[][] p=new int[1<<n][n];
			int[] ws=new int[1<<n];
			int INF=1<<28;
			double eps=1e-9;
		
			for(int i=0; i<n; i++) {
				s[i]=sc.nextInt();//蔵番号
				d[i]=sc.nextDouble();//城からの距離
				v[i]=sc.nextInt();//蔵にある千両箱の数
			}
			
			for(int i=0; i<(1<<n); i++) {
				for(int j=0; j<n; j++) {
					ws[i|(1<<j)]=ws[i]+20*v[j];
					if(i!=0)dp[i][j]=INF;
				}
			}
			
			for(int i=0; i<n; i++) {
				for(int j=i+1; j<n; j++) {
					dist[i][j]=Math.abs(d[i]-d[j]);
					dist[j][i]=Math.abs(d[i]-d[j]);
				}
			}
			
			for(int i=0; i<(1<<n); i++) {
				for(int j=0; j<n; j++) {//現在いる頂点j
					//System.out.println("j="+j);
					for(int k=0; k<n; k++) {//次の行き先頂点k
						//System.out.println("k="+k);
						if((1&i>>k)==1) continue;//すでに訪れてるとき
						int nexti = i| (1<<k);//bitごとのOR演算(今まで通ってきた頂点に次の頂点を足せる) 
						//System.out.println("nexti="+nexti);
						double nextd=dp[i][j]+(dist[j][k]*(70.0+ws[i])/2000.0);
						//System.out.println("nextd="+nextd);
						if(nextd+eps<dp[nexti][k]) {
							dp[nexti][k]=nextd;
							p[nexti][k]=j;
						}
					}
				}
			}
			
			int m=0;
			int all=(1<<n)-1;//最後の全部bitたっている状態
			for(int i=0; i<n; i++) {
				//System.out.println(dp[all][i]);
				if(dp[all][i]+eps<dp[all][m]) {
					m=i;//all状態でdp値が一番小さいものを探している→一番最後に訪れたところ
				}
			}
			//int sup=all;
			ArrayList<Integer> list=new ArrayList<Integer>();
			for(int k=m, sup=all; sup!=0;) {//後ろから前へ逆戻りのイメージ
				//System.out.println(i+" "+sup);
				list.add(k);
				int j=p[sup][k];//状態がsupになるkを訪れる前の頂点j
				//System.out.println(j);
				sup&=~(1<<k);//訪問状態から訪問前の状態にしてる
				k=j;
			}
			for(int i=0; i<list.size(); i++) {
				System.out.print(s[list.get(list.size()-1-i)]+(i==list.size()-1?"\n":" "));
			}

		}
	}
}
