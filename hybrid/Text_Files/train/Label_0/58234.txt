
import java.util.*;

import static java.lang.System.*;

class Main {
    public static Scanner sc = new Scanner(in);
    public static Random rand=new Random();


    public void run() {
    	while(true){
    	int n=sc.nextInt();
    	int w=sc.nextInt();
    	if(n==0)return;
    	int[] v=nextIntArray(n);

    	int[] dat=new int[100/w+1];

    	for(int i=0;i<v.length;i++){
    		dat[v[i]/w]++;
    	}

    	int max=0,l=0;
    	for(int i=0;i<dat.length;i++){
    		if(dat[i]>max)max=dat[i];
    		if(dat[i]!=0)l=i;
    	}

    	double res=0;
    	for(int i=0;i<l;i++){
    		res+=(double)dat[i]/max*(l-i)/(l);
    	}
    	res+=0.01;

    	ln(res);
    	}
    }
    public static void main(String[] args) {
        new Main().run();
    }

    public int[] nextIntArray(int n){
        int[] res=new int[n];
        for(int i=0;i<n;i++){
            res[i]=sc.nextInt();
        }
        return res;
    }
    public static void pr(Object o) {
        out.print(o);
    }
    public static void ln(Object o) {
        out.println(o);
    }
    public static void ln() {
        out.println();
    }
}