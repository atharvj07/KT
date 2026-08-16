import java.util.*;

public class Main{
    static int[] p = new int[1130];
    static int pnum;
    static int[][][] dp;

    public static void main(String[] args){
	Scanner sc = new Scanner(System.in);

	calcPrimes();

	int n = sc.nextInt();
	int k = sc.nextInt();

	while(n!=0){

	    dp = new int[1121][15][188];
	    for(int i=0; i<=n; i++)
		for(int j=0; j<=k; j++)
		    for(int l=0; l<188; l++)dp[i][j][l] = -1;
	    System.out.println(solve(n,k,0));

	    n = sc.nextInt();
	    k = sc.nextInt();
	}
    }

    public static int solve(int n, int k, int idx){
	if(n==0 && k==0){return 1;}
	else if(n==0 || k==0){return 0;}
	if(dp[n][k][idx]>=0){return dp[n][k][idx];}
	
	int res = 0;
	for(int i=idx; i<pnum; i++){
	    if(p[i]>n){
		break;
	    }else{
		res += solve(n-p[i],k-1,i+1);
	    }
	}

	return dp[n][k][idx] = res;
    }

    public static void calcPrimes(){
	p[0] = 2;
	pnum = 1;
	for(int i=3; i<=1120; i+=2){
	    boolean add = true;
	    for(int j=0; j<pnum; j++){
		if(p[j]*p[j]>i){break;}
		if(i%p[j]==0){
		    add = false;
		    break;
		}
	    }
	    if(add){p[pnum++] = i;}
	}
    }
}