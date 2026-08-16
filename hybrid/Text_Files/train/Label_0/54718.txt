import java.util.Scanner;
 
class Main {
    public static void main(String args[]){
	Scanner sc = new Scanner(System.in);
	int a,p,maxap;
 
	a = sc.nextInt();
	p = sc.nextInt();
 
	maxap = (3*a + p) /2;
 
	System.out.println(maxap);
    }
}