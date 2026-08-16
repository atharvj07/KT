import java.util.*;
public class Main{
    public static void main(String[] args){
	new Main().run();
    }
    Scanner sc = new Scanner(System.in);

    int a, b, c, d, e, f;
    int t1, t2, t3;
    int ans;

    void run(){
	while(sc.hasNext()){
	    a = sc.nextInt();
	    b = sc.nextInt();
	    c = sc.nextInt();
	    d = sc.nextInt();
	    e = sc.nextInt();
	    f = sc.nextInt();
	    if(a==0 && b==0 && c==0 && d==0 && e==0 && f==0) break;
	    
	    t1 = a+d;
	    t2 = b+e;
	    t3 = c+f;
	    ans = 0;

	    for(int i=0; i<3; i++){
		if(t1-i<0 || t2-i<0 || t3-i<0) continue;
		int sum = i + (t1-i)/3 + (t2-i)/3 + (t3-i)/3;
		ans = Math.max(ans, sum);
	    }

	    System.out.println(ans);
	}
    }
}