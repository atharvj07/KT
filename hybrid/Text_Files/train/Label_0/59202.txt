import java.util.*;

class Main{
    int n,a,b;
    int[] can;

    void solve(){
	Scanner sc = new Scanner(System.in);
	while(true){
	    n = sc.nextInt();
	    a = sc.nextInt();
	    b = sc.nextInt();
	    if(n==0 && a==0 && b==0) break;

	    can = new int[n+1];
	    can[0] = 1;
	    for(int i=0; i<=n; i++){
		if(can[i]==0)continue;
		if(i+a<=n)can[i+a] = 1;
		if(i+b<=n)can[i+b] = 1;
	    }

	    int unableCount = 0;
	    for(int i=1; i<=n; i++){
		if(can[i]==0)unableCount++;
	    }

	    System.out.println(unableCount);
	}
    }

    public static void main(String[] args){
	new Main().solve();
    }
}