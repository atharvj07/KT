import java.util.*;
public class Main{
    public static void main(String[] args){
	new Main().run();
    }
    Scanner sc = new Scanner(System.in);

    int t, n, sum;

    void run(){
	while(sc.hasNext()){
	    t = sc.nextInt();
	    if(t==0) break;
	    n = sc.nextInt();
	    sum = 0;

	    for(int i=0; i<n; i++)
		sum += Math.abs(sc.nextInt() - sc.nextInt());
	
	    System.out.println(sum>=t ? "OK" : (t-sum));
	}
    }
}