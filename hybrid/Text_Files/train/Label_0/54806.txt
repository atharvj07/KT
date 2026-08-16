import java.util.Arrays;
import java.util.Scanner;


public class Main {

	Scanner sc;
	int[][] cards;
	
	int[][] cost;
	
	//i番目からj番目までの山を重ねる時の最小cost
	int dfs(int i,int j){
		if(cost[i][j]!=-1)return cost[i][j];
		
		int res=Integer.MAX_VALUE;
		if(i==j) res=0;
		else{
			for(int k=i;k<j;++k){
				res=Math.min(res, dfs(i,k)+dfs(k+1,j)+cards[i][0]*cards[k][1]*cards[k+1][0]*cards[j][1]);
			}
		}
		return cost[i][j]=res;
	}
	
	int ni(){
		return sc.nextInt();
	}
	
	void io(){
		sc=new Scanner(System.in);
		int n=ni();
		cards=new int[n][2];
		cost=new int[n][n];
		for(int[] e:cost)Arrays.fill(e,-1);
		for(int i=0;i<n;++i){
			for(int j=0;j<2;++j)cards[i][j]=ni();
		}
		System.out.println(dfs(0,n-1));
	}
	
	void debug(Object...os){
		System.err.println(Arrays.deepToString(os));
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Main().io();
	}

}