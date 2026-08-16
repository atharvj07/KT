import java.util.*;

public class Main{
    Main(){
	Scanner sc = new Scanner(System.in);

	while(sc.hasNext()){
	    int r = sc.nextInt(), t, cnt=1, l=0;
	    if(r == 0) break;
	    int[] ary = new int[r+1];
	    
	    for(int i = 0; i < r; i++)
		ary[i] = sc.nextInt();
	    t = sc.nextInt();
	    r--;

	    for(;l <= r; cnt++){
		int v = (l+r)/2;

		if(ary[v] == t) break;
		if(ary[v] < t) l = v+1;
		else r = v-1;

		if(l > r) break;
	    }

	    System.out.println(Integer.toString(cnt));
	}
    }

    public static void main(String[] args){
	new Main();
    }
}