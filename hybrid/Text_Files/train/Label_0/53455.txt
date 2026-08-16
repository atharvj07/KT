import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		ArrayList<Integer> x = new ArrayList<Integer>();
		ArrayList<Integer> y = new ArrayList<Integer>();
		ArrayList<Integer> z = new ArrayList<Integer>();
		int[][] in = new int[n][6];
		for(int i=0;i<n;i++){
			for(int j=0;j<6;j++){
				in[i][j] = sc.nextInt();
				if(j%3==0 && !x.contains(in[i][j])) x.add(in[i][j]);
				else if(j%3==1 && !y.contains(in[i][j])) y.add(in[i][j]);
				else if(j%3==2 && !z.contains(in[i][j])) z.add(in[i][j]);
			}
		}
		Collections.sort(x);
		Collections.sort(y);
		Collections.sort(z);
		
		int xc = x.size();
		int yc = y.size();
		int zc = z.size();
		long[][][] cnt = new long[zc][yc][xc];
		
		for(int i=0;i<n;i++){
			int x1 = x.indexOf(in[i][0]);
			int y1 = y.indexOf(in[i][1]);
			int z1 = z.indexOf(in[i][2]);
			int x2 = x.indexOf(in[i][3]);
			int y2 = y.indexOf(in[i][4]);
			int z2 = z.indexOf(in[i][5]);
			for(int a=z1;a<z2;a++){
				for(int b=y1;b<y2;b++){
					for(int c=x1;c<x2;c++){
						cnt[a][b][c]++;
					}
				}
			}
		}
		
		long ans = 0;
		for(int i=0;i<zc-1;i++){
			for(int j=0;j<yc-1;j++){
				for(int s=0;s<xc-1;s++){
					if(cnt[i][j][s]>=k){
						long xx = x.get(s+1)-x.get(s);
						long yy = y.get(j+1)-y.get(j);
						long zz = z.get(i+1)-z.get(i);
						ans += xx*yy*zz;
					}
				}
			}
		}
		System.out.println(ans);
	}	
}