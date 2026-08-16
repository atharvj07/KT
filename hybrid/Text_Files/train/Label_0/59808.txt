import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int m, n=5;
	int[][] a;
	int[] score;

	void run(){
		for(;;){
			m=sc.nextInt();
			if(m==-1){
				break;
			}
			a=new int[n][n];
			for(int j=0; j<n; j++){
				for(int i=0; i<n; i++){
					a[j][i]=sc.nextInt()-1;
				}
			}
			score=new int[n];
			for(int i=0; i<n; i++){
				score[i]=sc.nextInt();
			}
			solve();
		}
	}

	void solve(){
		max=0;
		for(int j=0; j<n; j++){
			for(int i=0; i<n; i++){
				rec(i, j, 0);
			}
		}
		println(max+"");
	}

	int max;

	void rec(int x, int y, int depth){
		if(depth>m){
			return;
		}
		eval();
		int[] dx={0, 0, -1, 1};
		int[] dy={-1, 1, 0, 0};
		for(int i=0; i<4; i++){
			int x2=x+dx[i], y2=y+dy[i];
			if(x2>=0&&x2<n&&y2>=0&&y2<n){
				int t=a[y][x];
				a[y][x]=a[y2][x2];
				a[y2][x2]=t;
				rec(x2, y2, depth+1);
				t=a[y][x];
				a[y][x]=a[y2][x2];
				a[y2][x2]=t;
			}
		}
	}

	void eval(){
		int[][] b=new int[n][n];
		for(int j=0; j<n; j++){
			for(int i=0; i<n; i++){
				b[j][i]=a[j][i];
			}
		}
		int tot=0;
		for(int bonus=1;; bonus++){
			boolean[][] clear=new boolean[n][n];
			for(int y=0; y<n; y++){
				for(int x=0; x<n; x++){
					if(b[y][x]==-1){
						continue;
					}
					if(y+2<n&&b[y][x]==b[y+1][x]&&b[y+1][x]==b[y+2][x]){
						clear[y][x]=clear[y+1][x]=clear[y+2][x]=true;
					}
					if(x+2<n&&b[y][x]==b[y][x+1]&&b[y][x+1]==b[y][x+2]){
						clear[y][x]=clear[y][x+1]=clear[y][x+2]=true;
					}
				}
			}
			int block=0;
			boolean updated=false;
			for(int y=0; y<n; y++){
				for(int x=0; x<n; x++){
					if(clear[y][x]){
						block+=score[b[y][x]];
						b[y][x]=-1;
						updated=true;
					}
				}
			}
			for(int x=0; x<n; x++){
				for(int y=n-1; y>=0; y--){
					if(b[y][x]!=-1){
						for(int j=y+1; j<n&&b[j][x]==-1; j++){
							int t=b[j-1][x];
							b[j-1][x]=b[j][x];
							b[j][x]=t;
						}
					}
				}
			}
			tot+=block*bonus;
			if(!updated){
				break;
			}
		}
		max=max(max, tot);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}