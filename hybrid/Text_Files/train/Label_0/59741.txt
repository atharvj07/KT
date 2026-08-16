import java.util.*;
public class Main{
    public static void main(String[] args){
	new Main().run();
    }
    Scanner sc = new Scanner(System.in);

    double n;
    int a;
    double b;
    boolean d8, d4;
    int[] i, d;

    void run(){
	while(sc.hasNext()){
	    n = sc.nextDouble();
	    if(n<0) break;
	    
	    d8 = true; d4 = true;
	    i = new int[8];
	    d = new int[4];
	    a = (int)n/1;
	    b = n-a;
	    solveI();
	    solveD();

	    if(d8&&d4)
		show();
	    else System.out.println("NA");
	}
    }

    void solveI(){
	if(a > 255){
	    d8 = false;
	    return;
	}
	int s=128;
	for(int k=0; k<i.length; k++){
	    if(a>=s){
		i[k] = 1;
		a -= s;
	    }
	    s /= 2;
	}
	if(a!=0) d8 = false;
    }

    void solveD(){
	double s=0.5;
	for(int k=0; k<d.length; k++){
	    if(b>=s){
		d[k] = 1;
		b -= s;
	    }
	    s /= 2;
	}
	if(b!=0) d8 = false;
    }

    void show(){
	for(int k=0; k<i.length; k++)
	    System.out.print(i[k]);
	System.out.print(".");
	for(int k=0; k<d.length; k++)
	    System.out.print(d[k]);
	System.out.println();
    }
}