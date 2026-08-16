import java.util.*;
public class Main{
    public static void main(String[] args){
	new Main().run();
    }
    Scanner sc = new Scanner(System.in);
    long n, count;

    void run(){
	while(sc.hasNext()){
	    n = sc.nextLong();
	    count = 0;
	    if(n!=0) solve();
	}
    }

    void solve(){
	while(n!=1){
	    if(n%2==0) n = n/2;
	    else n = n*3+1;
	    count++;
	}
	System.out.println(count);
    }
}