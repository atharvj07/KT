import java.util.Scanner;

public class Main {
	static int bord[][];
	static int ans;
	static int mx[]={-1,0,1,0};
	static int my[]={0,-1,0,1};
	static int sx,sy,gx,gy,w,h;

	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
		int i,j;
		while(true){
			w=sc.nextInt();
			h=sc.nextInt();
			if(w+h==0) break;
			bord=new int[h][w];
			ans=-1;
			for(i=0;i<h;i++){
				for(j=0;j<w;j++){
					bord[i][j]=sc.nextInt();
					if(bord[i][j]==2){
						sx=j;
						sy=i;
					}
					if(bord[i][j]==3){
						gx=j;
						gy=i;
					}
				}
			}
			dfs(sx,sy,1);
			System.out.println(ans);
		}
	}//main

	static void dfs(int x,int y,int k){
		int nx,ny,i;
		boolean flag;
		if(10<k) return;
		for(i=0;i<4;i++){
			nx=x+mx[i];
			ny=y+my[i];
			flag=true;
			if(0<=nx && nx<w && 0<=ny && ny<h && bord[ny][nx]!=1){
				if(nx==gx && ny==gy){
					if(ans==-1 || k<ans)
						ans=k;
					return;
				}
				while(true){
					nx=nx+mx[i];
					ny=ny+my[i];
					if(0<=nx && nx<w && 0<=ny && ny<h){
						if(nx==gx && ny==gy){
							if(ans==-1 || k<ans)
								ans=k;
							return;
						}
						if(bord[ny][nx]==1){
							break;
						}
					}
					else{
						flag=false;
						break;
					}
				}
				if(flag){
					bord[ny][nx]=0;
					dfs(nx-mx[i],ny-my[i],k+1);
					bord[ny][nx]=1;
				}
			}
		}
	}

}