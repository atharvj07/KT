import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Mysterious Dungeons
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int[][] d = {{-1,0},{0,1},{1,0},{0,-1}};
		for(;;){
			int w = sc.nextInt(), h = sc.nextInt();
			if((w|h)==0)break;
			char[][] m = new char[h][];
			int si = 0, sj = 0, gi = 0, gj = 0;
			boolean[] u = new boolean[26];
			for(int i=0;i<h;i++){
				m[i]=sc.next().toCharArray();
				for(int j=0;j<w;j++){
					if(m[i][j]=='@'){
						si = i; sj = j; m[i][j] = '.';
					}
					if(m[i][j]=='<'){
						gi = i; gj = j; m[i][j] = '.';
					}
					if(Character.isUpperCase(m[i][j]))u[m[i][j]-'A']=true;
				}
			}
			for(int i=0;i<h;i++)for(int j=0;j<w;j++)if(Character.isLowerCase(m[i][j])&&!u[m[i][j]-'a'])m[i][j]='.';
			int id = 0;
			int[] b = new int[26];
			for(int i=0;i<26;i++)if(u[i])b[i]=id++;
			boolean[][][] v = new boolean[h][w][256];
			int step = 0, res = -1;
			List<int[]> l = new ArrayList<int[]>();
			l.add(new int[]{si, sj, 0});
			v[si][sj][0] = true;
			while(!l.isEmpty()){
				List<int[]> next = new ArrayList<int[]>();
				for(int[]a:l){
					int i = a[0], j = a[1], s = a[2];
					if(i==gi&&j==gj){
						res = step; next.clear(); break;
					}
					for(int k=0;k<4;k++){
						int ni = i+d[k][0], nj = j+d[k][1], ns = s;
						if(m[ni][nj]=='#')continue;
						if(Character.isUpperCase(m[ni][nj])){
							if(((s>>b[m[ni][nj]-'A'])&1)==0)continue;
						}
						else if(Character.isLowerCase(m[ni][nj])){
							if(((s>>b[m[ni][nj]-'a'])&1)==0)ns+=1<<b[m[ni][nj]-'a'];
							else ns-=1<<b[m[ni][nj]-'a'];
						}
						if(!v[ni][nj][ns]){
							v[ni][nj][ns] = true; next.add(new int[]{ni, nj, ns});
						}
					}
				}
				step++;
				l = next;
			}
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}